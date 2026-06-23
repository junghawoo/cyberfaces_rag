"""
Calculate NDCG@k against final_evaluation_dataset.jsonl.

Expected search results JSONL format (one line per query):
    {"query": "python basics", "results": [101, 45, 22, 78, 33, 12, 5, 99, 200, 150]}

Where "results" is an ordered list of document IDs ranked by your retriever (best first).

Usage:
    python calculate_ndcg.py --results my_retriever_results.jsonl
    python calculate_ndcg.py --results my_retriever_results.jsonl --k 10 --ground_truth final_evaluation_dataset.jsonl
"""

import json
import math
import argparse
from collections import defaultdict


def load_ground_truth(path):
    """
    Returns dict: query -> {doc_id -> relevance_score}
    """
    gt = defaultdict(dict)
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            gt[row["query"]][row["document_id"]] = row["relevance_score"]
    return gt


def load_results(path):
    """
    Returns dict: query -> [doc_id, doc_id, ...]  (ranked, best first)
    """
    results = {}
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            results[row["query"]] = row["results"]
    return results


def dcg(relevances, k):
    return sum(
        rel / math.log2(rank + 2)  # rank is 0-indexed, so log2(rank+2)
        for rank, rel in enumerate(relevances[:k])
    )


def ndcg_at_k(ranked_doc_ids, ground_truth_scores, k):
    """
    ranked_doc_ids: ordered list of doc IDs from retriever
    ground_truth_scores: dict {doc_id -> relevance_score}
    """
    relevances = [ground_truth_scores.get(doc_id, 0) for doc_id in ranked_doc_ids]

    ideal_relevances = sorted(ground_truth_scores.values(), reverse=True)

    actual_dcg = dcg(relevances, k)
    ideal_dcg = dcg(ideal_relevances, k)

    if ideal_dcg == 0:
        return 0.0
    return actual_dcg / ideal_dcg


def evaluate(ground_truth_path, results_path, k=10):
    gt = load_ground_truth(ground_truth_path)
    results = load_results(results_path)

    scores = []
    skipped = 0

    for query, ranked_ids in results.items():
        if query not in gt:
            skipped += 1
            continue
        score = ndcg_at_k(ranked_ids, gt[query], k)
        scores.append((query, score))

    if not scores:
        print("No matching queries found between results and ground truth.")
        return

    ndcg_scores = [s for _, s in scores]
    mean_ndcg = sum(ndcg_scores) / len(ndcg_scores)

    print(f"Results file:      {results_path}")
    print(f"Ground truth file: {ground_truth_path}")
    print(f"k:                 {k}")
    print(f"Queries evaluated: {len(scores)}")
    if skipped:
        print(f"Queries skipped (not in ground truth): {skipped}")
    print(f"")
    print(f"NDCG@{k}:  {mean_ndcg:.4f}")

    # Score distribution
    buckets = {"1.0": 0, "0.8-1.0": 0, "0.6-0.8": 0, "0.4-0.6": 0, "<0.4": 0}
    for s in ndcg_scores:
        if s == 1.0:
            buckets["1.0"] += 1
        elif s >= 0.8:
            buckets["0.8-1.0"] += 1
        elif s >= 0.6:
            buckets["0.6-0.8"] += 1
        elif s >= 0.4:
            buckets["0.4-0.6"] += 1
        else:
            buckets["<0.4"] += 1

    print(f"\nScore distribution:")
    for label, count in buckets.items():
        bar = "#" * (count * 40 // len(scores))
        print(f"  {label:>10}  {bar} {count}")

    # Bottom 10 worst queries
    worst = sorted(scores, key=lambda x: x[1])[:10]
    print(f"\nBottom 10 queries by NDCG@{k}:")
    for query, score in worst:
        print(f"  {score:.4f}  '{query}'")

    return mean_ndcg


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", required=True, help="Path to retriever results JSONL")
    parser.add_argument("--ground_truth", default="final_evaluation_dataset.jsonl")
    parser.add_argument("--k", type=int, default=10)
    args = parser.parse_args()

    evaluate(args.ground_truth, args.results, k=args.k)
