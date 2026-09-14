"""
Compare two retrieval methods over FULL module content (courses_md/unit_*.md),
restricted to modules whose token length is < 9,000 (gte tokenizer):

    1. Semantic search   (Bi-Encoder, Alibaba-NLP/gte-large-en-v1.5, 8192-token window)
    2. Cross-encoder     (gte top-N candidates -> jinaai/jina-reranker-v3 -> top-K)

Ground truth: evaluate/final_evaluation_dataset.jsonl (graded 0-3). Entries whose
document_id falls outside the filtered corpus are dropped; queries left with no
relevant doc (score >= --rel_threshold) are skipped so both methods see the same
query set. Metrics: NDCG@K (graded), MRR, Precision@K, Recall@K (binary).

Usage:
    python evaluate/compare_gte_vs_jina.py                       # both methods
    python evaluate/compare_gte_vs_jina.py --methods gte         # bi-encoder only
    python evaluate/compare_gte_vs_jina.py --methods jina --limit 30
    python evaluate/compare_gte_vs_jina.py --stats_only          # just the token filter

Results are exported per query (JSONL, append-mode with resume) so long jina runs
can be interrupted and resumed. Doc embeddings are cached to --cache_dir.
"""

import os
import re
import sys
import json
import glob
import time
import argparse
from collections import defaultdict
from statistics import mean, median

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from calculate_ndcg import ndcg_at_k  # noqa: E402

GTE_MODEL = "Alibaba-NLP/gte-large-en-v1.5"
JINA_MODEL = "jinaai/jina-reranker-v3"


# ------------------------------- corpus ----------------------------------------

def load_modules(courses_md_dir):
    """unit_id(int) -> full markdown text (frontmatter stripped)."""
    modules = {}
    for path in sorted(glob.glob(os.path.join(courses_md_dir, "unit_*.md"))):
        with open(path, encoding="utf-8") as f:
            text = f.read()
        m = re.search(r"^unit_id:\s*(\d+)", text, re.MULTILINE)
        if not m:
            print(f"  ! no unit_id in {os.path.basename(path)}, skipped")
            continue
        unit_id = int(m.group(1))
        # strip the leading --- frontmatter block
        body = re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)
        modules[unit_id] = body.strip()
    return modules


def filter_by_tokens(modules, tokenizer, max_tokens):
    """Return ({unit_id: text} under limit, {unit_id: n_tokens} for all)."""
    counts = {}
    kept = {}
    for uid, text in modules.items():
        n = len(tokenizer(text, add_special_tokens=True,
                          truncation=False, verbose=False)["input_ids"])
        counts[uid] = n
        if n < max_tokens:
            kept[uid] = text
    return kept, counts


# ----------------------------- ground truth ------------------------------------

def load_ground_truth(path, keep_ids, rel_threshold):
    """query -> {doc_id: grade}, restricted to keep_ids; queries with no
    remaining relevant doc are dropped. Returns (gt, n_dropped_queries)."""
    raw = defaultdict(dict)
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            raw[row["query"]][row["document_id"]] = row["relevance_score"]
    gt, dropped = {}, 0
    for q, scores in raw.items():
        filtered = {d: s for d, s in scores.items() if d in keep_ids}
        if any(s >= rel_threshold for s in filtered.values()):
            gt[q] = filtered
        else:
            dropped += 1
    return gt, dropped


# ------------------------------- metrics ---------------------------------------

def per_query_metrics(ranked_ids, gt_scores, k, rel_threshold):
    relevant_ids = {d for d, s in gt_scores.items() if s >= rel_threshold}
    topk = ranked_ids[:k]
    ndcg = ndcg_at_k(ranked_ids, gt_scores, k)
    hits = sum(1 for d in topk if gt_scores.get(d, 0) >= rel_threshold)
    precision = hits / k
    recall = hits / len(relevant_ids) if relevant_ids else None
    rr = 0.0
    for rank, d in enumerate(topk, start=1):
        if gt_scores.get(d, 0) >= rel_threshold:
            rr = 1.0 / rank
            break
    return {"ndcg": ndcg, "mrr": rr, "precision": precision, "recall": recall}


def aggregate(rows):
    out = {}
    for metric in ("ndcg", "mrr", "precision", "recall"):
        vals = [r[metric] for r in rows if r[metric] is not None]
        out[metric] = (mean(vals), median(vals)) if vals else (float("nan"), float("nan"))
    return out


# ------------------------------ retrieval --------------------------------------

def embed_docs(model, doc_ids, doc_texts, doc_tokens, cache_path, mps_token_limit=4096):
    """Embed (or load cached) document embeddings; cache keyed by doc id list.

    Long docs (> mps_token_limit tokens) OOM the MPS shared pool (fp32 attention
    at 8k tokens needs ~4 GiB), so they are embedded on CPU instead.
    """
    if os.path.exists(cache_path):
        data = np.load(cache_path, allow_pickle=False)
        if list(data["ids"]) == doc_ids:
            print(f"  using cached doc embeddings: {cache_path}")
            return data["emb"]
        print("  cache doc-id mismatch, re-embedding")

    embs = [None] * len(doc_ids)
    t0 = time.time()
    short = [i for i, uid in enumerate(doc_ids) if doc_tokens[uid] <= mps_token_limit]
    long_ = [i for i, uid in enumerate(doc_ids) if doc_tokens[uid] > mps_token_limit]

    for n, i in enumerate(short, start=1):
        embs[i] = model.encode([doc_texts[i]], normalize_embeddings=True)[0]
        if n % 25 == 0:
            print(f"  embedded {n}/{len(short)} short docs ({time.time()-t0:.0f}s)")

    if long_:
        if str(model.device).startswith("mps"):
            print(f"  {len(long_)} docs > {mps_token_limit} tokens -> embedding on CPU (MPS OOM workaround)")
            device = model.device
            model.to("cpu")
            for n, i in enumerate(long_, start=1):
                embs[i] = model.encode([doc_texts[i]], normalize_embeddings=True)[0]
                print(f"  long doc {n}/{len(long_)} ({time.time()-t0:.0f}s)")
            model.to(device)
        else:
            # The MPS shared-pool OOM this split avoids doesn't apply on CUDA/CPU;
            # embedding these on-device (GPU on Anvil) is both correct and far faster.
            print(f"  {len(long_)} docs > {mps_token_limit} tokens -> embedding on {model.device} (no MPS workaround needed)")
            for n, i in enumerate(long_, start=1):
                embs[i] = model.encode([doc_texts[i]], normalize_embeddings=True)[0]
                if n % 10 == 0 or n == len(long_):
                    print(f"  long doc {n}/{len(long_)} ({time.time()-t0:.0f}s)")

    emb = np.array(embs, dtype=np.float32)
    np.savez(cache_path, ids=np.array(doc_ids), emb=emb)
    print(f"  doc embeddings cached -> {cache_path} ({time.time()-t0:.0f}s)")
    return emb


def load_export(path):
    """Resume support: query -> ranked ids already computed."""
    done = {}
    if path and os.path.exists(path):
        with open(path) as f:
            for line in f:
                row = json.loads(line)
                done[row["query"]] = row["results"]
    return done


# --------------------------------- main ----------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ground_truth", default=os.path.join(HERE, "final_evaluation_dataset.jsonl"))
    parser.add_argument("--courses_md", default=os.path.join(ROOT, "courses_md"))
    parser.add_argument("--max_tokens", type=int, default=9000)
    parser.add_argument("--k", type=int, default=10)
    parser.add_argument("--candidate_pool", type=int, default=50)
    parser.add_argument("--rel_threshold", type=int, default=1)
    parser.add_argument("--methods", nargs="+", default=["gte", "jina"], choices=["gte", "jina"])
    parser.add_argument("--limit", type=int, default=0, help="first N queries only (0 = all)")
    parser.add_argument("--export_dir", default=os.path.join(ROOT, "run_results_gte_jina"))
    parser.add_argument("--cache_dir", default=os.path.join(ROOT, "run_results_gte_jina"))
    parser.add_argument("--stats_only", action="store_true", help="print token-filter stats and exit")
    args = parser.parse_args()

    # ---- 1. corpus: full module content, token-filtered -----------------------
    print(f"Loading modules from {args.courses_md} ...")
    modules = load_modules(args.courses_md)
    print(f"  {len(modules)} modules loaded")

    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(GTE_MODEL)
    kept, counts = filter_by_tokens(modules, tokenizer, args.max_tokens)
    lens = sorted(counts.values())
    print(f"Token filter (< {args.max_tokens}, {GTE_MODEL} tokenizer):")
    print(f"  kept {len(kept)}/{len(modules)} modules  "
          f"(dropped {len(modules)-len(kept)})")
    print(f"  token length min/median/max: {lens[0]} / {lens[len(lens)//2]} / {lens[-1]}")

    # ---- 2. ground truth restricted to the filtered corpus --------------------
    gt, dropped_q = load_ground_truth(args.ground_truth, set(kept), args.rel_threshold)
    print(f"Ground truth: {len(gt)} usable queries "
          f"({dropped_q} dropped: no relevant doc left after filtering)")
    queries = list(gt.keys())
    if args.limit:
        queries = queries[: args.limit]

    os.makedirs(args.export_dir, exist_ok=True)
    stats = {
        "max_tokens": args.max_tokens,
        "modules_total": len(modules),
        "modules_kept": len(kept),
        "queries_usable": len(gt),
        "queries_dropped": dropped_q,
        "token_counts": counts,
    }
    with open(os.path.join(args.export_dir, "filter_stats.json"), "w") as f:
        json.dump(stats, f, indent=2)
    if args.stats_only:
        return

    doc_ids = sorted(kept)
    doc_texts = [kept[i] for i in doc_ids]

    # ---- 3. gte bi-encoder -----------------------------------------------------
    import torch
    device = "cuda" if torch.cuda.is_available() else ("mps" if torch.backends.mps.is_available() else "cpu")
    from sentence_transformers import SentenceTransformer
    print(f"Loading {GTE_MODEL} on {device} ...")
    gte = SentenceTransformer(GTE_MODEL, trust_remote_code=True, device=device)
    gte.max_seq_length = 8192

    cache_path = os.path.join(args.cache_dir, "gte_doc_embeddings.npz")
    doc_emb = embed_docs(gte, doc_ids, doc_texts, counts, cache_path)

    print(f"Embedding {len(queries)} queries ...")
    q_emb = gte.encode(queries, normalize_embeddings=True, batch_size=32,
                       show_progress_bar=False)
    sims = np.asarray(q_emb) @ doc_emb.T          # cosine (normalized)
    pool = max(args.k, args.candidate_pool)
    top_idx = np.argsort(sims, axis=1)[:, ::-1][:, :pool]
    gte_ranked = {q: [doc_ids[j] for j in top_idx[i]] for i, q in enumerate(queries)}

    summary = {}
    if "gte" in args.methods:
        rows = [per_query_metrics(gte_ranked[q][: args.k], gt[q], args.k, args.rel_threshold)
                for q in queries]
        summary["gte"] = aggregate(rows)
        with open(os.path.join(args.export_dir, "gte_results.jsonl"), "w") as f:
            for q in queries:
                f.write(json.dumps({"query": q, "results": gte_ranked[q][: args.k]}) + "\n")
        print("gte done.")

    # ---- 4. jina cross-encoder over gte candidates -----------------------------
    if "jina" in args.methods:
        export_path = os.path.join(args.export_dir, "jina_results.jsonl")
        done = load_export(export_path)
        todo = [q for q in queries if q not in done]
        print(f"Jina rerank: {len(done)} cached, {len(todo)} to run "
              f"(pool={args.candidate_pool})")
        if todo:
            from transformers import AutoModel
            print(f"Loading {JINA_MODEL} ...")
            jina = AutoModel.from_pretrained(JINA_MODEL, dtype="auto", trust_remote_code=True)
            jina.eval().to(device)
            print(f"jina reranker on device: {device}")
            text_by_id = dict(zip(doc_ids, doc_texts))
            with open(export_path, "a") as f:
                for n, q in enumerate(todo, start=1):
                    cand_ids = gte_ranked[q][: args.candidate_pool]
                    cand_texts = [text_by_id[i] for i in cand_ids]
                    t0 = time.time()
                    ranked = jina.rerank(query=q, documents=cand_texts)
                    ids = [cand_ids[r["index"]] for r in ranked[: args.k]
                           if r.get("index") is not None]
                    done[q] = ids
                    f.write(json.dumps({"query": q, "results": ids}) + "\n")
                    f.flush()
                    print(f"  [{n}/{len(todo)}] {time.time()-t0:.1f}s  {q[:60]!r}")
        rows = [per_query_metrics(done[q], gt[q], args.k, args.rel_threshold)
                for q in queries if q in done]
        summary["jina"] = aggregate(rows)
        summary["jina_n"] = sum(1 for q in queries if q in done)

    # ------------------------------ report --------------------------------------
    print("\n" + "=" * 78)
    print(f"gte-large-en-v1.5 vs jina-reranker-v3  |  K={args.k}  "
          f"|  rel>={args.rel_threshold}  |  pool={args.candidate_pool}  "
          f"|  corpus={len(kept)} modules (<{args.max_tokens} tok)")
    print("=" * 78)
    label = {"gte": f"Semantic (gte-large)", "jina": f"Cross-enc (jina-v3)"}
    header = f"{'Method':<22}" + "".join(f"{m + ' (mn/med)':>20}" for m in ("NDCG@K", "MRR", "P@K", "R@K"))
    print(header)
    print("-" * len(header))
    for method in args.methods:
        if method not in summary:
            continue
        s = summary[method]
        cells = "".join(f"{s[m][0]:>9.4f}/{s[m][1]:<9.4f}" for m in ("ndcg", "mrr", "precision", "recall"))
        n = summary.get("jina_n") if method == "jina" else len(queries)
        print(f"{label[method]:<22}{cells}   (n={n})")
    print("=" * 78)


if __name__ == "__main__":
    main()
