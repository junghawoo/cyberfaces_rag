#!/usr/bin/env python3
"""
ndcg_eval.py -- NDCG@10 for RRF and CrossEncoder_advance, both using the
"summary" text variant, against the graded-relevance eval set
final_evaluation_dataset.jsonl (query, document_id, relevance_score 0-3;
~10 judged docs per query).

Unlike flatten_ab_eval.py's Fixed-Pool method (binary expected_ids, TP/FP/FN/TN
classification), this needs an actual ranked top-10 list per query:

  RRF                : reproduces app/main.py's manual_rrf() -- classic
                        Reciprocal Rank Fusion (k=60) over the two
                        threshold-filtered candidate lists (semantic > 0.45,
                        BM25 > 1.25), same as the deployed /search_RRF path.
  CrossEncoder_advance: reuses eval_cross_advance()'s scoring (LLM query
                        rewrite + jina-reranker-v3 over the unfiltered
                        candidate union), sorted, top 10.

Corpus gap handling: 29 of the eval set's judged document_ids don't exist in
this corpus (confirmed directly against the live production DB -- not a sync
lag, the content genuinely isn't there). Per query, judged docs missing from
the corpus are dropped from BOTH the actual ranking and the ideal (IDCG)
ranking before scoring, so no method is penalized for a corpus gap outside
its control. Queries left with zero corpus-present judged docs are excluded
from the aggregate and counted separately.

Run from the repo root (same deps as flatten_ab_eval.py, plus the eval file):

    export ANVILGPT_API=...
    python ndcg_eval.py
"""
import json, math, os, sys, time
import numpy as np

import flatten_ab_eval as fab

NEW_EVAL_FILE = os.environ.get("NDCG_EVAL_FILE", "./final_evaluation_dataset.jsonl")
EXTRA_DOCS_FILE = os.environ.get("NDCG_EXTRA_DOCS_FILE", "")
VARIANT = os.environ.get("NDCG_VARIANT", "summary")
EMBED_MODEL_OVERRIDE = os.environ.get("NDCG_EMBED_MODEL", "")
RRF_K = 60


def load_extra_docs(path):
    """Synthetic doc entries recovered from a sibling repo's courses_md/*.md
    extraction (real lesson content for IDs missing from data.jsonl/the live
    DB) -- see conversation notes. Same {id, title, description} shape as
    load_docs()'s rows."""
    if not path:
        return []
    docs = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                docs.append(json.loads(line))
    return docs


def load_graded_eval(path):
    """query -> {document_id: relevance_score}, deduped (max score wins)."""
    by_query = {}
    opener = __import__("gzip").open if path.endswith(".gz") else open
    with opener(path, "rt", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            g = by_query.setdefault(d["query"], {})
            g[d["document_id"]] = max(g.get(d["document_id"], 0), d["relevance_score"])
    return by_query


def rrf_rank(idx, query, topn=10):
    """Classic RRF fusion (k=60) over threshold-filtered semantic + BM25
    candidate lists -- mirrors app/main.py's manual_rrf()/combine_manual_rrf()."""
    sem = fab.cut_threshold(idx.semantic(query), fab.SEMANTIC_CUTOFF)
    kw  = fab.cut_threshold(idx.lexical(query),  fab.KEYWORD_THRESHOLD)
    rrf_scores = {}
    for ranked_list in (sem, kw):
        for rank, (doc_id, _) in enumerate(ranked_list, 1):
            rrf_scores[doc_id] = rrf_scores.get(doc_id, 0.0) + 1.0 / (RRF_K + rank)
    ranked = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)
    return [doc_id for doc_id, _ in ranked[:topn]]


def cross_advance_rank(idx, query, adv, api_key, topn=10):
    q = fab.rewrite_query_with_llm(query, api_key)
    instr = ("Given a course description, identify all documents that provide "
              "relevant information, even if they use different terminology or "
              "they are sub-topics. ")
    qi = f"instruction: {instr}\nquery: {q}"
    pool = fab._combined_pool(idx, query)
    docs = [idx.id2text[i] for i in pool]
    res = adv.rerank(query=qi, documents=docs)
    items = [(pool[r["index"]], float(r["relevance_score"])) for r in res]
    items.sort(key=lambda x: x[1], reverse=True)
    return [doc_id for doc_id, _ in items[:topn]]


def dcg(relevances):
    return sum(rel / math.log2(pos + 1) for pos, rel in enumerate(relevances, 1))


def ndcg_at_10(ranked_ids, graded, corpus_ids):
    """Returns NDCG@10, or None if this query has no corpus-present judged doc."""
    g = {doc_id: rel for doc_id, rel in graded.items() if doc_id in corpus_ids}
    if not g:
        return None
    ideal = sorted(g.values(), reverse=True)[:10]
    idcg = dcg(ideal)
    if idcg == 0:
        return None
    actual = [g.get(doc_id, 0) for doc_id in ranked_ids[:10]]
    return dcg(actual) / idcg


def main():
    api = os.environ.get("ANVILGPT_API")
    if not api:
        sys.exit("ANVILGPT_API env var required for CrossEncoder_advance")

    from sentence_transformers import SentenceTransformer
    import torch
    from transformers import AutoModel

    embed_model_name = EMBED_MODEL_OVERRIDE or fab.EMBED_MODEL
    is_gte = "gte" in embed_model_name.lower()
    embed_device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"loading embedder {embed_model_name} (trust_remote_code={is_gte}, device={embed_device}) ...")
    embedder = SentenceTransformer(embed_model_name, trust_remote_code=is_gte, device=embed_device)
    if is_gte:
        embedder.max_seq_length = 8192

    docs = fab.load_docs()
    summaries = fab.load_summaries()

    extra_docs = load_extra_docs(EXTRA_DOCS_FILE)
    if extra_docs:
        docs = docs + extra_docs
        for d in extra_docs:
            summaries[d["id"]] = fab.flatten_text(f"{d['title']}. {d['description']}")
        print(f"extra docs (recovered content, IDs missing elsewhere): {len(extra_docs)} "
              f"({sorted(d['id'] for d in extra_docs)})")

    n_missing = sum(1 for d in docs if d["id"] not in summaries)
    print(f"{len(docs)} docs, variant={VARIANT}, summary: {len(summaries)} curated, "
          f"{n_missing} fall back to current text")
    idx = fab.Index(docs, VARIANT, embedder, summaries=summaries)
    corpus_ids = set(idx.ids)

    print(f"loading advanced reranker {fab.ADV_CE_MODEL} ...")
    adv_device = "cuda" if torch.cuda.is_available() else "cpu"
    adv = AutoModel.from_pretrained(fab.ADV_CE_MODEL, trust_remote_code=True).eval().to(adv_device)
    print(f"advanced reranker on device: {adv_device}")

    print(f"loading eval set {NEW_EVAL_FILE} ...")
    graded = load_graded_eval(NEW_EVAL_FILE)
    queries = list(graded.items())
    limit = int(os.environ.get("NDCG_LIMIT", "0"))
    if limit:
        queries = queries[:limit]
    print(f"{len(queries)} unique queries" + (f" (limited to {limit})" if limit else ""))

    rrf_scores, adv_scores = [], []
    rrf_excluded = adv_excluded = 0
    rrf_errors = adv_errors = 0
    t0 = time.time()
    for n, (query, g) in enumerate(queries, 1):
        try:
            rrf_ids = rrf_rank(idx, query)
            s = ndcg_at_10(rrf_ids, g, corpus_ids)
            if s is not None:
                rrf_scores.append(s)
            else:
                rrf_excluded += 1
        except Exception as e:
            rrf_errors += 1
            print(f"  RRF error on query {n} ({query!r}): {e}", flush=True)

        try:
            adv_ids = cross_advance_rank(idx, query, adv, api)
            s = ndcg_at_10(adv_ids, g, corpus_ids)
            if s is not None:
                adv_scores.append(s)
            else:
                adv_excluded += 1
        except Exception as e:
            adv_errors += 1
            print(f"  CrossEncoder_advance error on query {n} ({query!r}): {e}", flush=True)

        if n % 20 == 0 or n == len(queries):
            elapsed = time.time() - t0
            print(f"  [{n}/{len(queries)}] elapsed={elapsed:.0f}s "
                  f"rrf_mean={np.mean(rrf_scores):.3f} adv_mean={np.mean(adv_scores):.3f} "
                  f"rrf_errors={rrf_errors} adv_errors={adv_errors}",
                  flush=True)
            write_results(rrf_scores, rrf_excluded, rrf_errors,
                           adv_scores, adv_excluded, adv_errors,
                           f"ndcg_results_{VARIANT}_partial.json", n, len(queries))

    print("\n" + "=" * 70)
    print(f"{'method':22} {'n_scored':>9} {'n_excluded':>11} {'n_errors':>9} {'NDCG@10 mean/median':>22}")
    print("-" * 70)
    for name, scores, excl, err in ((f"RRF ({VARIANT})", rrf_scores, rrf_excluded, rrf_errors),
                                     (f"CrossEncoder_advance ({VARIANT})", adv_scores, adv_excluded, adv_errors)):
        arr = np.array(scores)
        print(f"{name:22} {len(scores):9d} {excl:11d} {err:9d} "
              f"{arr.mean():.3f} / {np.median(arr):.3f}")

    write_results(rrf_scores, rrf_excluded, rrf_errors,
                   adv_scores, adv_excluded, adv_errors,
                   f"ndcg_results_{VARIANT}.json", len(queries), len(queries))
    print(f"wrote ndcg_results_{VARIANT}.json")


def write_results(rrf_scores, rrf_excluded, rrf_errors,
                   adv_scores, adv_excluded, adv_errors,
                   path, n_done, n_total):
    def summarize(scores, excluded, errors):
        arr = np.array(scores)
        return {"scores": scores, "excluded": excluded, "errors": errors,
                "mean": float(arr.mean()) if len(arr) else None,
                "median": float(np.median(arr)) if len(arr) else None}
    json.dump({
        "progress": f"{n_done}/{n_total}",
        "rrf_summary": summarize(rrf_scores, rrf_excluded, rrf_errors),
        "cross_advance_summary": summarize(adv_scores, adv_excluded, adv_errors),
    }, open(path, "w"), indent=2)


if __name__ == "__main__":
    main()
