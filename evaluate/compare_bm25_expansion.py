"""
Experiment 1: does LLM-based query expansion help plain BM25?

For each ground-truth query, an LLM (AnvilGPT gpt-oss:120b) expands it into
4-10 keywords/phrases (synonyms, abbreviation expansions, related concepts) --
BM25 has no notion of synonymy, so this is meant to compensate for that.
The expanded keyword set is joined into one string and run through the SAME
isolated BM25 retriever as compare_retrievers.py, then scored against the
graded ground truth exactly like the other experiments (NDCG@10, MRR, P@10,
R@10), so results sit next to the existing vector/rerank numbers.

Expansions are cached to a checkpoint file (resumable -- write-as-you-go).

Usage:
    python compare_bm25_expansion.py
    python compare_bm25_expansion.py --limit 20        # smoke test
"""
import os
import sys
import json
import argparse
import requests
from statistics import mean, median

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from compare_retrievers import Retrievers, load_ground_truth, per_query_metrics, aggregate

ANVILGPT_URL = "https://anvilgpt.rcac.purdue.edu/api/chat/completions"
EXPANSION_MODEL = "gpt-oss:120b"
CHECKPOINT_PATH = os.path.join(HERE, "bm25_expansion_checkpoint.jsonl")

SYSTEM_PROMPT = """You are a search-query analyst for Cyberfaces, a platform of educational courses and
modules covering topics such as hydrology and watershed science, geospatial data
processing, Python/R programming, climate and environmental data, machine learning,
and FAIR/data-justice practices.

A user has typed a short, possibly vague or colloquial query into the course search
bar. The search backend is BM25 -- plain bag-of-words matching with no understanding
of synonyms, abbreviations, or intent. Your job is to expand the query into the set
of keywords BM25 needs to find what the user actually means.

Given the user's query, output a JSON object with one field, "keywords": an array of
4-10 short keyword strings (single words or short technical phrases, not full
sentences) that include:
- the literal terms in the query
- close synonyms and common alternate phrasings (e.g. "hydrology" -> "water",
  "streamflow", "watershed")
- standard abbreviation expansions relevant to the domain (e.g. "ML" -> "machine
  learning")
- closely related concepts a student in this catalog might mean

Do not include stopwords, punctuation, boolean operators, or exclusion terms -- this
search engine has no way to require, group, or exclude terms; every keyword you
output will simply be added to the match set, so only include terms that should
count IN FAVOR of a match.

Respond with strict JSON only, no other text."""


def load_checkpoint():
    cache = {}
    if os.path.exists(CHECKPOINT_PATH):
        with open(CHECKPOINT_PATH) as f:
            for line in f:
                row = json.loads(line)
                cache[row["query"]] = row["keywords"]
    return cache


def expand_query(query, api_key, retries=3):
    for attempt in range(retries):
        try:
            r = requests.post(ANVILGPT_URL,
                headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
                json={"model": EXPANSION_MODEL, "temperature": 0, "stream": False,
                      "messages": [{"role": "system", "content": SYSTEM_PROMPT},
                                   {"role": "user", "content": query}]},
                timeout=60)
            r.raise_for_status()
            content = json.loads(r.text)["choices"][0]["message"]["content"]
            content = content.strip()
            if content.startswith("```"):
                content = content.strip("`")
                content = content[content.find("{"):]
            keywords = json.loads(content)["keywords"]
            if isinstance(keywords, list) and keywords:
                return [str(k) for k in keywords]
        except Exception as e:
            if attempt == retries - 1:
                print(f"  expansion FAILED for '{query}': {e}")
    return []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ground_truth", default=os.path.join(HERE, "final_evaluation_dataset.jsonl"))
    ap.add_argument("--k", type=int, default=10)
    ap.add_argument("--rel_threshold", type=int, default=1)
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    api_key = os.environ.get("ANVILGPT_API")
    if not api_key:
        sys.exit("ANVILGPT_API env var required")

    gt = load_ground_truth(args.ground_truth)
    queries = list(gt.keys())
    if args.limit:
        queries = queries[: args.limit]
    print(f"{len(queries)} queries")

    cache = load_checkpoint()
    print(f"{len(cache)} expansions already cached")
    ckpt = open(CHECKPOINT_PATH, "a")

    expanded = {}
    for n, q in enumerate(queries, 1):
        if q in cache:
            expanded[q] = cache[q]
        else:
            kws = expand_query(q, api_key)
            expanded[q] = kws
            ckpt.write(json.dumps({"query": q, "keywords": kws}) + "\n")
            ckpt.flush()
        if n % 50 == 0 or n == len(queries):
            print(f"  expansion {n}/{len(queries)}")
    ckpt.close()

    n_failed = sum(1 for kws in expanded.values() if not kws)
    if n_failed:
        print(f"WARNING: {n_failed} queries got no expansion (falling back to original query text)")

    print("Loading BM25 retriever...")
    retrievers = Retrievers(need_reranker=False)

    summary = {}
    for variant in ("original", "expanded"):
        rows = []
        for n, q in enumerate(queries, 1):
            text = q if variant == "original" else (q + " " + " ".join(expanded[q]) if expanded[q] else q)
            ranked = retrievers.search("bm25", text, args.k, candidate_pool=0)
            rows.append(per_query_metrics(ranked, gt[q], args.k, args.rel_threshold))
            if n % 200 == 0:
                print(f"  bm25/{variant}: {n}/{len(queries)}")
        summary[variant] = aggregate(rows)

    print("\n" + "=" * 78)
    print(f"BM25 query-expansion comparison  |  K={args.k}  |  rel>={args.rel_threshold}  |  n={len(queries)}")
    print("=" * 78)
    header = f"{'variant':<22}" + "".join(f"{m + ' (mn/med)':>18}" for m in ("NDCG@K", "MRR", "P@K", "R@K"))
    print(header)
    print("-" * len(header))
    for variant in ("original", "expanded"):
        s = summary[variant]
        cells = "".join(f"{s[m][0]:>8.4f}/{s[m][1]:<8.4f}" for m in ("ndcg", "mrr", "precision", "recall"))
        print(f"{variant:<22}{cells}")
    d = {m: summary["expanded"][m][0] - summary["original"][m][0] for m in ("ndcg", "mrr", "precision", "recall")}
    print(f"{'  delta (expanded-original)':<22}" + "".join(f"{d[m]:>+18.4f}" for m in ("ndcg", "mrr", "precision", "recall")))
    print("=" * 78)

    json.dump({"summary": {k: {m: v[m] for m in v} for k, v in summary.items()}, "n_failed_expansion": n_failed},
              open("bm25_expansion_results.json", "w"), indent=2)
    print("wrote bm25_expansion_results.json")


if __name__ == "__main__":
    main()
