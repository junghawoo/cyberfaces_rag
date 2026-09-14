"""
Experiment 3: mimic SmartSearch's actual hybrid retrieval before reranking.

Experiment 2's "rerank" method only ever reranked vector-sourced candidates.
Production's combine_advance_reranking() instead unions BM25-top-N and
vector-top-N (deduped, semantic-first) before reranking -- a materially
different (larger, more diverse) candidate pool. This script reuses the exact
production functions combine_advance_reranking() calls -- get_courses() for
the vector leg, get_courses_from_keywords() for the BM25 leg, via a minimal
request shim -- then replicates its union/dedup logic exactly, then reranks
with jina-reranker-v3. No LLM query rewrite (isolated, matching how
Experiments 1 and 2 were run, for direct comparability).

Compares three methods on the SAME (original) ground truth used by
Experiment 1: BM25 only, Vector only, and BM25+Vector -> Jina rerank.

Usage:
    python compare_hybrid_rerank.py
    python compare_hybrid_rerank.py --limit 20 --candidate_pool 24
"""
import os
import sys
import json
import argparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "app"))
sys.path.insert(0, HERE)

import main as app_main  # noqa: E402  (production app module, for its retrieval functions)
from compare_retrievers import Retrievers, load_ground_truth, per_query_metrics, aggregate  # noqa: E402


class _FakeState:
    def __init__(self, stemmer, bm25_obj, docs):
        self.stemmer = stemmer
        self.bm25_obj = bm25_obj
        self.docs = docs


class _FakeApp:
    def __init__(self, state):
        self.state = state


class _FakeRequest:
    def __init__(self, state):
        self.app = _FakeApp(state)


def hybrid_rerank_search(retrievers, fake_request, query, k, candidate_pool):
    """Mirrors combine_advance_reranking() exactly, minus the LLM query rewrite."""
    semantic_docs, _ = app_main.get_courses(query, retrievers.vectordb, num_retrieval=candidate_pool)
    keyword_docs, _ = app_main.get_courses_from_keywords(query, fake_request, num_retrieval=candidate_pool)

    seen = set()
    combined_docs = list(semantic_docs)
    for doc in semantic_docs:
        seen.add(doc.metadata["id"])
    for doc in keyword_docs:
        if doc.metadata["id"] not in seen:
            combined_docs.append(doc)
            seen.add(doc.metadata["id"])

    documents = [doc.page_content for doc in combined_docs]
    ranked = retrievers.reranker.rerank(query=query, documents=documents)
    out = []
    for r in ranked[:k]:
        idx = r.get("index")
        if idx is None:
            continue
        out.append(combined_docs[idx].metadata["id"])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ground_truth", default=os.path.join(HERE, "final_evaluation_dataset.jsonl"))
    ap.add_argument("--k", type=int, default=10)
    ap.add_argument("--candidate_pool", type=int, default=24,
                     help="top-N pulled from EACH of BM25/vector before dedup+rerank "
                          "(matches production's num_retrieval=24)")
    ap.add_argument("--rel_threshold", type=int, default=1)
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    gt = load_ground_truth(args.ground_truth)
    queries = list(gt.keys())
    if args.limit:
        queries = queries[: args.limit]
    print(f"{len(queries)} queries")

    retrievers = Retrievers(need_reranker=True)
    fake_request = _FakeRequest(_FakeState(retrievers.stemmer, retrievers.bm25_index, retrievers.docs))

    summary = {}
    for method in ("bm25", "vector", "hybrid_rerank"):
        rows = []
        for n, q in enumerate(queries, 1):
            if method == "hybrid_rerank":
                ranked = hybrid_rerank_search(retrievers, fake_request, q, args.k, args.candidate_pool)
            else:
                ranked = retrievers.search(method, q, args.k, candidate_pool=0)
            rows.append(per_query_metrics(ranked, gt[q], args.k, args.rel_threshold))
            if n % 100 == 0:
                print(f"  {method}: {n}/{len(queries)}")
        summary[method] = aggregate(rows)

    print("\n" + "=" * 86)
    print(f"SmartSearch-mimic comparison (Exp 3)  |  K={args.k}  |  rel>={args.rel_threshold}  "
          f"|  candidate_pool={args.candidate_pool} per retriever  |  n={len(queries)}")
    print("=" * 86)
    label = {"bm25": "BM25 only", "vector": "Vector only", "hybrid_rerank": "BM25+Vector -> Jina rerank"}
    header = f"{'Method':<28}" + "".join(f"{m + ' (mn/med)':>15}" for m in ("NDCG@K", "MRR", "P@K", "R@K"))
    print(header)
    print("-" * len(header))
    for method in ("bm25", "vector", "hybrid_rerank"):
        s = summary[method]
        cells = "".join(f"{s[m][0]:>7.4f}/{s[m][1]:<7.4f}" for m in ("ndcg", "mrr", "precision", "recall"))
        print(f"{label[method]:<28}{cells}")
    print("=" * 86)

    json.dump({m: dict(summary[m]) for m in summary}, open("hybrid_rerank_results.json", "w"), indent=2)
    print("wrote hybrid_rerank_results.json")


if __name__ == "__main__":
    main()
