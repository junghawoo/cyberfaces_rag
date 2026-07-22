"""
Old-vs-new query comparison on the graded ground-truth set.

query_comparison.xlsx maps each ground-truth query (old_query) to a rewritten
form (new_query). Both forms are run through the same retrievers (BM25, Vector)
and scored against the SAME graded relevance judgments (which are keyed by the
old query), so the delta isolates the effect of the rewrite.

Usage:
    python evaluate/compare_query_rewrites.py
    python evaluate/compare_query_rewrites.py --methods vector --limit 50
"""

import os
import sys
import json
import argparse
from statistics import mean, median

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import pandas as pd

from compare_retrievers import Retrievers, load_ground_truth, per_query_metrics, aggregate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ground_truth", default=os.path.join(HERE, "final_evaluation_dataset.jsonl"))
    parser.add_argument("--mapping", default=os.path.join(ROOT, "query_comparison.xlsx"))
    parser.add_argument("--k", type=int, default=10)
    parser.add_argument("--rel_threshold", type=int, default=1)
    parser.add_argument("--methods", nargs="+", default=["bm25", "vector"], choices=["bm25", "vector"])
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--export_dir", default=os.path.join(ROOT, "run_results_query_rewrites"))
    args = parser.parse_args()

    gt = load_ground_truth(args.ground_truth)

    df = pd.read_excel(args.mapping)
    mapping = {}
    collisions = 0
    for _, row in df.iterrows():
        old, new = str(row["old_query"]), str(row["new_query"])
        if old in mapping and mapping[old] != new:
            collisions += 1
            continue
        mapping[old] = new

    queries = [q for q in gt if q in mapping]
    skipped = len(gt) - len(queries)
    if args.limit:
        queries = queries[: args.limit]
    print(f"{len(queries)} queries with a rewrite  |  {skipped} GT queries without mapping  "
          f"|  {collisions} ambiguous rows ignored")

    retrievers = Retrievers(need_reranker=False)
    os.makedirs(args.export_dir, exist_ok=True)

    summary = {}
    for method in args.methods:
        for variant in ("old", "new"):
            rows, exported = [], []
            for n, q in enumerate(queries, start=1):
                text = q if variant == "old" else mapping[q]
                ranked = retrievers.search(method, text, args.k, candidate_pool=0)
                rows.append(per_query_metrics(ranked, gt[q], args.k, args.rel_threshold))
                exported.append({"query": q, "query_used": text, "results": ranked})
                if n % 200 == 0:
                    print(f"  {method}/{variant}: {n}/{len(queries)}")
            summary[(method, variant)] = aggregate(rows)
            out = os.path.join(args.export_dir, f"{method}_{variant}_results.jsonl")
            with open(out, "w") as f:
                for row in exported:
                    f.write(json.dumps(row) + "\n")
            print(f"{method}/{variant} done -> {out}")

    print("\n" + "=" * 86)
    print(f"Query rewrite comparison  |  K={args.k}  |  rel>={args.rel_threshold}  |  n={len(queries)}")
    print("=" * 86)
    header = f"{'Method / queries':<26}" + "".join(f"{m + ' (mn/med)':>15}" for m in ("NDCG@K", "MRR", "P@K", "R@K"))
    print(header)
    print("-" * len(header))
    for method in args.methods:
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
