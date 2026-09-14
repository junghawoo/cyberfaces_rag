"""
Experiment 2, step 1: fix the hard-negative pooling bias in the ground truth.

final_evaluation_dataset.jsonl was built by hard_negatives_pipeline.py: for each
query, only the top-10 VECTOR-embedding-nearest docs were ever judged (source doc
forced in as the positive, the other ~9 "hard negatives" are whatever else vector
search happened to rank highest). That structurally favors vector-based retrieval:
a doc a cross-encoder or BM25 correctly surfaces but vector search didn't put in
its own top-10 gets scored as irrelevant (0) purely because nobody ever judged it,
not because it's actually wrong.

This script pools in candidates from BM25 and from the reranker too (not just
vector), judges only the NET-NEW (previously-unjudged) doc_ids per query with an
LLM judge, and writes out an expanded ground truth. The original rows are kept
untouched; only new rows are added.

Judge: AnvilGPT gemma4:26b-a4b (fast, no cost, already-provisioned credential --
swapped in for the original pipeline's Gemini judge, which needs a key we don't
have here).

Resumable: checkpoint file written as-you-go; re-running skips already-judged
(query, doc_id) pairs.

Usage:
    python expand_ground_truth_pool.py
    python expand_ground_truth_pool.py --limit 20 --pool_n 5     # smoke test
"""
import os
import sys
import json
import argparse
import time
import requests
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from compare_retrievers import Retrievers, load_ground_truth

ANVILGPT_URL = "https://anvilgpt.rcac.purdue.edu/api/chat/completions"
JUDGE_MODEL = "gemma4:26b-a4b"
CHECKPOINT_PATH = os.path.join(HERE, "pool_expansion_checkpoint.jsonl")

JUDGE_SYSTEM_PROMPT = """You are an expert search evaluator.
Given a user's search query and a retrieved course document, score how relevant the course is to the query.

Score using this exact scale:
3 = Perfect match / Exact intent
2 = Highly relevant / Very useful
1 = Partially relevant / Tangential
0 = Irrelevant / Not what the user wants

Output ONLY a single integer (0, 1, 2, or 3). No explanation."""


def load_docs_by_id(data_jsonl):
    out = {}
    with open(data_jsonl) as f:
        for line in f:
            line = line.strip()
            if line:
                d = json.loads(line)
                out[d["id"]] = d
    return out


def load_checkpoint():
    done = set()
    rows = []
    if os.path.exists(CHECKPOINT_PATH):
        with open(CHECKPOINT_PATH) as f:
            for line in f:
                row = json.loads(line)
                done.add((row["query"], row["document_id"]))
                rows.append(row)
    return done, rows


def judge(query, title, description, api_key, retries=3):
    user_msg = f'Query: "{query}"\n\nCourse Title: "{title}"\nCourse Description: "{description}"'
    for attempt in range(retries):
        try:
            r = requests.post(ANVILGPT_URL,
                headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
                json={"model": JUDGE_MODEL, "temperature": 0, "stream": False,
                      "messages": [{"role": "system", "content": JUDGE_SYSTEM_PROMPT},
                                   {"role": "user", "content": user_msg}]},
                timeout=45)
            r.raise_for_status()
            content = json.loads(r.text)["choices"][0]["message"]["content"].strip()
            score = int("".join(c for c in content if c.isdigit())[:1] or -1)
            if score in (0, 1, 2, 3):
                return score
        except Exception as e:
            if attempt == retries - 1:
                print(f"    judge FAILED: {e}")
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ground_truth", default=os.path.join(HERE, "final_evaluation_dataset.jsonl"))
    ap.add_argument("--data_jsonl", default=os.path.join(os.path.dirname(HERE), "data.jsonl"))
    ap.add_argument("--out", default=os.path.join(HERE, "final_evaluation_dataset_pooled.jsonl"))
    ap.add_argument("--pool_n", type=int, default=10, help="top-N to pull from BM25 and from the reranker each")
    ap.add_argument("--candidate_pool", type=int, default=50, help="vector candidates fetched before reranking")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    api_key = os.environ.get("ANVILGPT_API")
    if not api_key:
        sys.exit("ANVILGPT_API env var required")

    gt = load_ground_truth(args.ground_truth)
    queries = list(gt.keys())
    if args.limit:
        queries = queries[: args.limit]
    print(f"{len(queries)} queries, ground truth has {sum(len(v) for v in gt.values())} existing judged rows")

    docs_by_id = load_docs_by_id(args.data_jsonl)

    print("Loading retrievers (BM25 + vector + reranker)...")
    retrievers = Retrievers(need_reranker=True)

    done_pairs, new_rows = load_checkpoint()
    if done_pairs:
        print(f"Resuming: {len(done_pairs)} (query, doc_id) pairs already judged")
    ckpt = open(CHECKPOINT_PATH, "a")

    n_missing_doc = n_judged = n_skipped_existing = 0
    t0 = time.time()
    for n, q in enumerate(queries, 1):
        existing_ids = set(gt[q].keys())
        bm25_ids = set(retrievers.search("bm25", q, args.pool_n, candidate_pool=0))
        rerank_ids = set(retrievers.search("rerank", q, args.pool_n, candidate_pool=args.candidate_pool))
        candidates = (bm25_ids | rerank_ids) - existing_ids

        for doc_id in candidates:
            if (q, doc_id) in done_pairs:
                n_skipped_existing += 1
                continue
            doc = docs_by_id.get(doc_id)
            if doc is None:
                n_missing_doc += 1
                continue
            score = judge(q, doc.get("title", ""), doc.get("description", "") or "", api_key)
            if score is None:
                continue
            row = {"query": q, "document_id": doc_id, "relevance_score": score, "source": "llm_judge_pool_gemma"}
            ckpt.write(json.dumps(row) + "\n")
            ckpt.flush()
            done_pairs.add((q, doc_id))
            new_rows.append(row)
            n_judged += 1

        if n % 20 == 0 or n == len(queries):
            elapsed = time.time() - t0
            print(f"  [{n}/{len(queries)}] elapsed={elapsed:.0f}s new_judged={n_judged}", flush=True)

    ckpt.close()
    print(f"\nnew rows judged: {n_judged}  |  missing-from-corpus candidates skipped: {n_missing_doc}")

    # write combined output: all original rows + all new rows
    with open(args.out, "w") as f:
        with open(args.ground_truth) as orig:
            for line in orig:
                f.write(line if line.endswith("\n") else line + "\n")
        for row in new_rows:
            f.write(json.dumps(row) + "\n")
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
