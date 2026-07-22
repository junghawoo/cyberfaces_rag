"""
Old-vs-new query comparison over the SUMMARIES corpus (summaries/*.md).

Retrievers built fresh over summary documents:
  * BM25 (same nltk stem/stopword pipeline as the app)
  * gte-large-en-v1.5 bi-encoder (cosine)

Both query variants (old = ground-truth phrasing, new = rewrite from
query_comparison.xlsx) are scored against the same graded judgments.

Usage:
    python evaluate/compare_rewrites_summaries.py
"""

import os
import re
import sys
import json
import glob
import argparse
from collections import defaultdict

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from calculate_ndcg import ndcg_at_k
from compare_retrievers import per_query_metrics, aggregate

GTE_MODEL = "Alibaba-NLP/gte-large-en-v1.5"


def load_summaries(d):
    docs = {}
    for p in sorted(glob.glob(os.path.join(d, "unit_*.md"))):
        text = open(p, encoding="utf-8").read()
        m = re.match(r"unit_(\d+)__", os.path.basename(p))
        body = re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)
        docs[int(m.group(1))] = body.strip()
    return docs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ground_truth", default=os.path.join(HERE, "final_evaluation_dataset.jsonl"))
    parser.add_argument("--mapping", default=os.path.join(ROOT, "query_comparison.xlsx"))
    parser.add_argument("--summaries", default=os.path.join(ROOT, "summaries"))
    parser.add_argument("--k", type=int, default=10)
    parser.add_argument("--rel_threshold", type=int, default=1)
    parser.add_argument("--export_dir", default=os.path.join(ROOT, "run_results_query_rewrites"))
    args = parser.parse_args()

    docs = load_summaries(args.summaries)
    doc_ids = sorted(docs)
    texts = [docs[i] for i in doc_ids]
    print(f"{len(docs)} summary docs loaded")

    # ground truth restricted to retrievable docs; keep queries with >=1 relevant doc
    raw = defaultdict(dict)
    with open(args.ground_truth) as f:
        for line in f:
            r = json.loads(line)
            raw[r["query"]][r["document_id"]] = r["relevance_score"]
    gt = {}
    for q, scores in raw.items():
        filt = {d: s for d, s in scores.items() if d in docs}
        if any(s >= args.rel_threshold for s in filt.values()):
            gt[q] = filt

    df = pd.read_excel(args.mapping)
    mapping = {}
    for _, row in df.iterrows():
        mapping.setdefault(str(row["old_query"]), str(row["new_query"]))
    queries = [q for q in gt if q in mapping]
    print(f"{len(queries)} usable queries (of {len(raw)} in GT)")

    # ---------------- BM25 ----------------
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem import PorterStemmer
    from nltk.tokenize import word_tokenize
    from rank_bm25 import BM25Okapi
    for pkg in ("punkt", "punkt_tab", "stopwords"):
        try:
            nltk.download(pkg, quiet=True)
        except Exception:
            pass
    stemmer = PorterStemmer()
    stop = set(stopwords.words("english"))

    def tok(text):
        return [stemmer.stem(w) for w in word_tokenize(text.lower())
                if w.isalnum() and w not in stop]

    bm25 = BM25Okapi([tok(t) for t in texts])

    def bm25_search(qtext, k):
        scores = bm25.get_scores(tok(qtext))
        order = np.argsort(scores)[::-1][:k]
        return [doc_ids[i] for i in order]

    # ---------------- gte ----------------
    import torch
    from sentence_transformers import SentenceTransformer
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"Loading {GTE_MODEL} on {device} ...")
    gte = SentenceTransformer(GTE_MODEL, trust_remote_code=True, device=device)
    gte.max_seq_length = 8192

    print("Embedding summary docs ...")
    demb = gte.encode(texts, normalize_embeddings=True, batch_size=1, show_progress_bar=False)

    def batch_gte(qtexts, k):
        qemb = gte.encode(qtexts, normalize_embeddings=True, batch_size=32, show_progress_bar=False)
        sims = np.asarray(qemb) @ np.asarray(demb).T
        idx = np.argsort(sims, axis=1)[:, ::-1][:, :k]
        return [[doc_ids[j] for j in row] for row in idx]

    # ---------------- evaluate ----------------
    os.makedirs(args.export_dir, exist_ok=True)
    summary = {}
    for variant in ("old", "new"):
        qtexts = [q if variant == "old" else mapping[q] for q in queries]

        rows = [per_query_metrics(bm25_search(t, args.k), gt[q], args.k, args.rel_threshold)
                for q, t in zip(queries, qtexts)]
        summary[("bm25", variant)] = aggregate(rows)

        ranked_all = batch_gte(qtexts, args.k)
        rows = [per_query_metrics(r, gt[q], args.k, args.rel_threshold)
                for q, r in zip(queries, ranked_all)]
        summary[("gte", variant)] = aggregate(rows)
        with open(os.path.join(args.export_dir, f"summaries_gte_{variant}_results.jsonl"), "w") as f:
            for q, t, r in zip(queries, qtexts, ranked_all):
                f.write(json.dumps({"query": q, "query_used": t, "results": r}) + "\n")
        print(f"{variant} queries done")

    print("\n" + "=" * 86)
    print(f"Rewrite comparison over SUMMARIES corpus  |  K={args.k}  |  n={len(queries)}")
    print("=" * 86)
    header = f"{'Method / queries':<26}" + "".join(f"{m + ' (mn/med)':>15}" for m in ("NDCG@K", "MRR", "P@K", "R@K"))
    print(header)
    print("-" * len(header))
    for method in ("bm25", "gte"):
        for variant in ("old", "new"):
            s = summary[(method, variant)]
            cells = "".join(f"{s[m][0]:>7.4f}/{s[m][1]:<7.4f}" for m in ("ndcg", "mrr", "precision", "recall"))
            print(f"{method + ' / ' + variant + ' queries':<26}{cells}")
        d = {m: summary[(method, 'new')][m][0] - summary[(method, 'old')][m][0]
             for m in ("ndcg", "mrr", "precision", "recall")}
        print(f"{'  delta (new - old)':<26}" +
              "".join(f"{d[m]:>+15.4f}" for m in ("ndcg", "mrr", "precision", "recall")))
    print("=" * 86)


if __name__ == "__main__":
    main()
