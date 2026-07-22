"""
Compare three retrieval methods on the graded ground-truth set:

    1. Keyword Search   (BM25)
    2. Vector Search    (Bi-Encoder, all-mpnet-base-v2)
    3. Vector + Rerank  (Vector top-N candidates -> Jina cross-encoder -> top-K)

For every query we get the ordered top-K document IDs, look up their graded
relevance (0-3) in the ground truth (unseen docs -> 0), and compute:

    NDCG@K, MRR, Precision@K, Recall@K

then report the mean and median of each metric per method.

Each method is run in ISOLATION (no hybrid fusion, no LLM query rewriting) so the
numbers reflect the raw retriever, matching the standard IR evaluation protocol.

Usage:
    python evaluate/compare_retrievers.py
    python evaluate/compare_retrievers.py --k 10 --candidate_pool 50 --rel_threshold 1
    python evaluate/compare_retrievers.py --methods bm25 vector            # skip the reranker
    python evaluate/compare_retrievers.py --limit 25                       # quick smoke test
    python evaluate/compare_retrievers.py --export_dir ./run_results       # dump per-method results.jsonl

Notes:
  * The reranker loaded is whatever app/main.py:load_rerankers() configures
    (currently jinaai/jina-reranker-v3).
  * NDCG uses the full graded scale (0-3). MRR / Precision / Recall are binary and
    treat a document as relevant when its graded score >= --rel_threshold.
"""

import os
import sys
import json
import argparse
from collections import defaultdict
from statistics import mean, median

import numpy as np

# --- Make app/ importable and point its relative data paths at the repo root,
#     regardless of the directory this script is launched from. ---
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
os.environ.setdefault("DATA_FILE_PATH", os.path.join(ROOT, "data.jsonl"))
os.environ.setdefault("CHROMADB_PATH", os.path.join(ROOT, "chromaDB"))
os.environ.setdefault("DATA_FILE2_PATH", os.path.join(ROOT, "course_unit_map.jsonl"))
sys.path.insert(0, os.path.join(ROOT, "app"))
sys.path.insert(0, HERE)

import main as app_main          # noqa: E402  (the FastAPI app module; imported for its loaders)
from calculate_ndcg import ndcg_at_k  # noqa: E402  (reuse the exact same NDCG math)


# ----------------------------- ground truth -----------------------------------

def load_ground_truth(path):
    """query_text -> {document_id(int) -> relevance_score(int)}"""
    gt = defaultdict(dict)
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            gt[row["query"]][row["document_id"]] = row["relevance_score"]
    return gt


# --------------------------- retrieval methods ---------------------------------

class Retrievers:
    """Holds the loaded resources and exposes one isolated method per retriever."""

    def __init__(self, need_reranker):
        print("Loading vector DB + documents...")
        self.vectordb, self.docs = app_main.load_vectorDB_docs()
        print("Loading BM25 index...")
        self.bm25_index, self.stemmer = app_main.load_keyword_docs(self.docs)
        self.reranker = None
        if need_reranker:
            print("Loading reranker (this can be a large download / slow on CPU)...")
            _, self.reranker = app_main.load_rerankers()

    def search(self, method, query, k, candidate_pool):
        if method == "bm25":
            return self.bm25_search(query, k)
        if method == "vector":
            return self.vector_search(query, k)
        if method == "rerank":
            return self.rerank_search(query, k, candidate_pool)
        raise ValueError(f"unknown method: {method}")

    def bm25_search(self, query, k):
        tokens = app_main.deep_clean_query(query, self.stemmer)
        scores = self.bm25_index.get_scores(tokens)
        order = np.argsort(scores)[::-1][:k]
        return [self.docs[i].metadata["id"] for i in order]

    def vector_search(self, query, k):
        results = self.vectordb.similarity_search(query, k=k)
        return [d.metadata["id"] for d in results]

    def rerank_search(self, query, k, candidate_pool):
        # 1. Get a candidate pool from vector search, 2. resort with the cross-encoder.
        candidates = self.vectordb.similarity_search(query, k=candidate_pool)
        documents = [d.page_content for d in candidates]
        ranked = self.reranker.rerank(query=query, documents=documents)
        out = []
        for r in ranked[:k]:
            # jina rerank returns dicts carrying the original candidate index.
            idx = r.get("index")
            if idx is None:
                continue
            out.append(candidates[idx].metadata["id"])
        return out


# ------------------------------- metrics ---------------------------------------

def per_query_metrics(ranked_ids, gt_scores, k, rel_threshold):
    """Return dict of metric -> value for one query."""
    relevant_ids = {doc_id for doc_id, s in gt_scores.items() if s >= rel_threshold}
    topk = ranked_ids[:k]

    # NDCG@k uses the full graded relevance.
    ndcg = ndcg_at_k(ranked_ids, gt_scores, k)

    # Precision@k / Recall@k use the binary threshold.
    hits = sum(1 for d in topk if gt_scores.get(d, 0) >= rel_threshold)
    precision = hits / k
    recall = hits / len(relevant_ids) if relevant_ids else None  # None -> exclude from mean

    # MRR: reciprocal rank of the first relevant doc in the returned list.
    rr = 0.0
    for rank, d in enumerate(topk, start=1):
        if gt_scores.get(d, 0) >= rel_threshold:
            rr = 1.0 / rank
            break

    return {"ndcg": ndcg, "mrr": rr, "precision": precision, "recall": recall}


def aggregate(rows):
    """rows: list of per-query metric dicts -> {metric: (mean, median)}"""
    out = {}
    for metric in ("ndcg", "mrr", "precision", "recall"):
        vals = [r[metric] for r in rows if r[metric] is not None]
        out[metric] = (mean(vals), median(vals)) if vals else (float("nan"), float("nan"))
    return out


# --------------------------------- main ----------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ground_truth", default=os.path.join(HERE, "final_evaluation_dataset.jsonl"))
    parser.add_argument("--k", type=int, default=10)
    parser.add_argument("--candidate_pool", type=int, default=50,
                        help="Vector candidates fetched before reranking")
    parser.add_argument("--rel_threshold", type=int, default=1,
                        help="Graded score >= this counts as relevant for MRR/Precision/Recall")
    parser.add_argument("--methods", nargs="+", default=["bm25", "vector", "rerank"],
                        choices=["bm25", "vector", "rerank"])
    parser.add_argument("--limit", type=int, default=0, help="Evaluate only first N queries (0 = all)")
    parser.add_argument("--export_dir", default=None, help="If set, write <method>_results.jsonl here")
    args = parser.parse_args()

    gt = load_ground_truth(args.ground_truth)
    queries = list(gt.keys())
    if args.limit:
        queries = queries[: args.limit]

    retrievers = Retrievers(need_reranker=("rerank" in args.methods))

    if args.export_dir:
        os.makedirs(args.export_dir, exist_ok=True)

    summary = {}
    for method in args.methods:
        print(f"\nRunning method: {method}  ({len(queries)} queries)")
        rows = []
        exported = []
        for n, query in enumerate(queries, start=1):
            ranked = retrievers.search(method, query, args.k, args.candidate_pool)
            rows.append(per_query_metrics(ranked, gt[query], args.k, args.rel_threshold))
            if args.export_dir:
                exported.append({"query": query, "results": ranked})
            if n % 50 == 0:
                print(f"  {n}/{len(queries)}")

        summary[method] = aggregate(rows)

        if args.export_dir:
            out_path = os.path.join(args.export_dir, f"{method}_results.jsonl")
            with open(out_path, "w") as f:
                for row in exported:
                    f.write(json.dumps(row) + "\n")
            print(f"  wrote {out_path}")

    # ------------------------------ report ------------------------------------
    print("\n" + "=" * 78)
    print(f"Retrieval comparison  |  K={args.k}  |  rel_threshold>={args.rel_threshold}  "
          f"|  candidate_pool={args.candidate_pool}  |  queries={len(queries)}")
    print("=" * 78)
    label = {"bm25": "BM25 (keyword)", "vector": "Vector (MPNet)", "rerank": "Vector+Jina rerank"}
    header = f"{'Method':<22}" + "".join(f"{m + ' (mn/med)':>20}" for m in ("NDCG@K", "MRR", "P@K", "R@K"))
    print(header)
    print("-" * len(header))
    for method in args.methods:
        s = summary[method]
        cells = "".join(f"{s[m][0]:>9.4f}/{s[m][1]:<9.4f}" for m in ("ndcg", "mrr", "precision", "recall"))
        print(f"{label[method]:<22}{cells}")
    print("=" * 78)


if __name__ == "__main__":
    main()
