# CLAUDE.md

Project context for Claude Code. This repo (`cyberfaces_rag`, branch
**local-test**) is a two-stage course search engine — hybrid retrieval
(semantic + BM25) followed by reranking (conditional RRF / cross-encoder / LLM).
Main app: `app/main.py`. It implements the US-RSE 2026 paper in the repo.

## Active work

Investigating why the **cross-encoder and LLM rerankers classify poorly** vs
conditional RRF. Full diagnosis, root causes, the fix plan, the nine retrieval
experiments, how to run them as Jobs on Anvil, and the known defects are all in
**`README.md`** — read that first.

TL;DR: the rerankers' recall is fine but precision/specificity is poor (they
over-admit). Highest-leverage fix is structural — filter the candidate pool
*before* reranking and calibrate the decision threshold — not a model swap.

## Key facts

- Constants: `num_retrieval=24`, `keyword_threshold=1.25` (norm. BM25),
  semantic cutoff `0.45`. Deployed config = conditional RRF + unit-to-course.
- Eval: `/evaluate` endpoint, "Fixed-Pool" method scored by MCC + balanced
  accuracy over `gemini_generate_dataset_updateByHuman.jsonl` (35 queries).
  Per-query results live in `analysis/*.json`.
- Advanced reranker + LLM paths require `ANVILGPT_API` (Purdue AnvilGPT).
- Run the full eval where models + API are reachable (local with GPU, or the
  Anvil pod). HuggingFace + AnvilGPT are not reachable from sandboxes.
