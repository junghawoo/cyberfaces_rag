# Smart Search Engine for the CyberFaCES platform

Smart Search is a two-stage course search engine for CyberFaCES, and the
implementation behind the US-RSE 2026 paper *"A Generalized Methodology for
Evaluating AI-Integrated Research Software."*

**Stage 1 — retrieval.** Semantic (dense) search and BM25 keyword search run in
parallel, each returning its top 24 candidates, each pre-filterable by a
calibrated threshold (semantic > `0.45`, normalized BM25 > `1.25`).

**Stage 2 — reranking.** One of three strategies reorders the candidates:
conditional RRF (reciprocal rank fusion, `k=60` — **the deployed default**), a
cross-encoder, or LLM scoring.

The repository also contains the retrieval-evaluation research that tested
whether stage 2 is worth its cost. It is not: across nine experiments, plain
semantic search beats every reranking configuration tried. See
[The research question](#the-research-question) below.

---

## Quick start

```bash
docker compose up --build
```

When the container is up you will see:

```
cyberface-rag  | INFO:     Application startup complete.
cyberface-rag  | INFO:     Uvicorn running on http://0.0.0.0:8000
```

Open `http://localhost:8000/docs`, pick an endpoint, click **Try it out**, fill
in the query, and **Execute**.

The advanced cross-encoder and LLM paths call Purdue's AnvilGPT and need
`ANVILGPT_API` set. The other endpoints run without it.

## API endpoints

| Endpoint | Description | Needs `ANVILGPT_API` |
|---|---|---|
| `POST /search_semantic` | Semantic search only | |
| `POST /search_lexical` | BM25 keyword search only | |
| `POST /search_RRF` | Hybrid + **conditional** RRF (threshold-filtered; `keyword_threshold` in `app/main.py`) | |
| `POST /search_RRF_all_candidates` | Hybrid + RRF over the unfiltered union | |
| `POST /search_RRF_unit2course` | Conditional RRF + unit-to-course logic (a matched unit also returns its parent course) | |
| `POST /search_reranking_base` | Hybrid + `ms-marco-MiniLM-L-6-v2` cross-encoder | yes (query expansion) |
| `POST /search_reranking_advance` | Hybrid + `jina-reranker-v3` cross-encoder | yes (query expansion) |
| `POST /search_llm_scores` | Hybrid + LLM scoring (`gpt-oss:120b`) | yes |
| `POST /evaluate` | Fixed-Pool evaluation over the 35-query labeled set | depends on method |

Deployed configuration: **conditional RRF + unit-to-course**.

## Repository layout

```
app/main.py                       FastAPI app: retrieval + all reranking paths
analysis/                         per-query results for each reranker
prompts/                          query-expansion prompts, cross-encoder instructions
evaluate/                         evaluation harnesses (see Experiments below)
evaluate/k8s/                     one Kubernetes Job manifest per experiment
evaluate/k8s/run_logs_2026-09-09/ captured stdout of the full reproduction run
docs_archive/                     superseded .docx write-ups, kept for provenance
courses_md/                       full module markdown, 346 files (Exp 2)
summaries/                        module summaries, 346 files (Exp 3)
curated_summaries_35q/            curated summaries, 239 files (Exps 4-6)
data.jsonl                        course descriptions from the CyberFaCES database
course_unit_map.jsonl             unit-to-course mapping
flatten_ab_eval.py, ndcg_eval.py  top-level evaluation harnesses
```

---

## The research question

**Does reranking beat plain retrieval?** Nine experiments asked it from
different angles. The answer is consistently no.

| # | Question | Answer key | Headline |
|---|---|---|---|
| 1 | BM25 vs. vector vs. vector+rerank | 1,035q | Vector alone wins; reranking costs 0.033 NDCG@10 |
| 2 | Does full document text change it? | 996q | Reranking still loses once both rows are scored alike |
| 3 | Does rewriting the query help? | 996q | No — rewrites score worse against the original intent |
| 4 | Does text formatting matter? | 35q | Barely; RRF is unmoved by text style |
| 5 | Do curated summaries help? | 35q | No — hurt RRF substantially, mixed elsewhere |
| 6 | Does it hold on a 30× larger set? | 1,035q | RRF and the reranker come out nearly tied |
| 7 | Can an LLM teach BM25 synonyms? | 1,035q | **Yes** — improved all four metrics |
| 8 | Was the answer key biased toward vector? | 1,035q | No — de-biasing it didn't change the winner |
| 9 | Does the reranker do better on its real pool? | 1,035q | No — still below vector alone |

### Results on the shared 1,035-query key

All directly comparable — same answer key, same corpus, same scorer:

| Method | NDCG@10 | Source |
|---|---|---|
| BM25 only | 0.4159 | Exps 1, 7, 9 (three independent jobs agree to 4 d.p.) |
| BM25 + AI query expansion | 0.4469 | Exp 7 |
| Vector → jina rerank (pool 50) | 0.4905 | Exp 1 |
| BM25 ∪ vector → jina rerank (pool 24) | 0.5065 | Exp 9 |
| **Vector only** | **0.5241** | Exp 9 (Exp 1: 0.5235) |

Reranking the *union* pool beats reranking the *vector-only* pool — the BM25 leg
gives the reranker material the vector pool lacks — but neither catches plain
vector search. On the de-biased pooled key (Exp 8) the gap is wider still:
vector 0.5665 vs. vector+rerank 0.5185.

### Why the rerankers underperform

Micro-averaged over the 35-query labeled set:

| Method | micro-P | micro-R | predicted-pos/query | total FP | mean MCC |
|---|---|---|---|---|---|
| CrossEncoder (jina-v3 + QE) | 0.33 | 0.85 | ~18 of ~39 | 430 | 0.36 |
| LLM scoring (`gpt-oss:120b`) | 0.39 | 0.95 | ~17 | 369 | 0.45 |
| RRF @ 1.25 | 0.65 | 0.85 | ~9 of ~40 | 114 | 0.68 |

**The failure is precision, not recall.** Recall matches RRF; the cross-encoder
simply admits about twice as many candidates, so false positives explode and MCC
collapses. It is a *gating* problem.

Root causes, ranked by impact, with locations in `app/main.py`:

1. **No upstream filtering before reranking.** `combine_advance_reranking`
   (~L702) and `combine_reranking` (~L661) call the *no-threshold* `get_courses`
   (~L240) and `get_courses_from_keywords` (~L441), so the full ~39-candidate
   union is reranked and gated by a single final cutoff. RRF instead pre-filters
   via `get_courses_with_threshold` (~L256) and
   `get_courses_with_threshold_from_keywords` (~L464) inside `combine_manual_rrf`
   (~L556). **This is the dominant cause** — and the one every experiment below
   keeps pointing back to.
2. **Recall-maximizing instruction plus query expansion.** The instruction at
   ~L719 ("identify all documents … even if … sub-topics") and
   `rewrite_query_with_llm` (~L135) broaden matching until precision collapses.
3. **Uncalibrated, inconsistent threshold.** Evaluation uses `-0.1`
   (`my_search_function`, ~L999) while `/search_reranking_advance` serves `-0.3`
   (~L856). Cross-encoder scores aren't comparable across queries, so one global
   cutoff cannot gate reliably.
4. **Base model out of domain.** `ms-marco-MiniLM-L-6-v2` (~L620) is web-search
   trained and weak on cyber-training acronyms (I-GUIDE, Anvil S3).
5. **Document text format.** `page_content = title + "|" + description`
   (`load_vectorDB_docs`, ~L351) — tested in Experiment 4 and found not to matter.
6. **Stochasticity (secondary).** Query expansion and the cross-encoder are
   nondeterministic; RRF is deterministic, cheaper and scalable.

Verified against `data.jsonl` (336 rows): the loader takes only `.description`,
so no raw JSON braces reach the models — **0** descriptions contain `{`, 3
contain `<p>`, 2 contain HTML entities. The only pervasive structural symbol is
the injected `|`. Experiment 4 confirmed the prediction that removing it changes
nothing material.

### Recommendations

1. **Filter the candidate pool before reranking** — mirror
   `combine_manual_rrf`'s pre-filtering inside `combine_advance_reranking`.
   Highest leverage, best evidenced, still not implemented.
2. **Ship AI query expansion for the keyword path** — Experiment 7 is the only
   change tested here that improved every metric.
3. **Calibrate the decision threshold** *after* (1), and align the eval (`-0.1`)
   and served (`-0.3`) values.
4. **Do not pursue curated summary text** — negative to neutral under two
   metrics and two corpus states.
5. **Fix the GPU placement bug in production's `load_rerankers()`** — see
   [Known defects](#known-defects).

---

## Running the experiments

Every experiment runs as an **isolated one-off Kubernetes Job** in the
`cyberfaces-dev` namespace on Purdue's Anvil cluster — never inside the live
`cyberfaces-rag` Deployment. An early attempt to run in the serving pod hit an
OOM kill (exit 137) inside its 4Gi limit; the Jobs get their own memory and GPU
budget, so production is never at risk.

### Prerequisites

- **Nothing to fetch — the course content ships with the repository.** All three
  corpora the experiments read are tracked, so a fresh clone can run every
  experiment with no extra setup:

  | Directory | Files | Needed by |
  |---|---|---|
  | `courses_md/` | 346 | Exp 2 (uploaded into the running pod) |
  | `summaries/` | 346 | Exp 3 (`unit_N__slug.md`) |
  | `curated_summaries_35q/` | 239 | Exps 4, 5, 6 (`NNN-slug.md`) |

  Verify after cloning:

  ```sh
  ls courses_md/*.md       | wc -l   # 346
  ls summaries             | wc -l   # 346
  ls curated_summaries_35q | wc -l   # 239
  ```

  Note that `summaries/` and `curated_summaries_35q/` are *different* corpora
  with different naming schemes and no overlapping files — see D2 in
  [Known defects](#known-defects).

  Two things are deliberately **not** tracked: `courses/` (2.1 GB of raw source
  attachments — `courses_md/` is generated from it by
  `extract_courses_full.py`), and `courses_md/.cache/` (regenerable OCR and
  network cache). Neither is needed to run anything.
- A kubeconfig with an `anvil` context pointing at `cyberfaces-dev`
  (`kubectl --context=anvil …` throughout).
- Secret `cyberfaces-rag-secrets` providing `ANVILGPT_API`.
- Secret `cyberfaces-hf-token` providing `token` — needed by the `gte` Jobs once
  HuggingFace starts rate-limiting anonymous downloads. A free read token works:
  ```sh
  printf '%s' "hf_xxx..." > /tmp/.hf_token   # never pass a token as a CLI arg
  kubectl --context=anvil create secret generic cyberfaces-hf-token \
    -n cyberfaces-dev --from-file=token=/tmp/.hf_token
  shred -u /tmp/.hf_token
  ```
- All Jobs tolerate the `hub.jupyter.org/dedicated=gpu` and `gpu=h100` taints and
  request `nvidia.com/gpu: 1`. MIG slices are usually full cluster-wide;
  scheduling onto a full H100 node is the reliable path. Expect Jobs to run
  **one at a time** — during the last full run all 9 GPU-capable nodes reported
  `Insufficient nvidia.com/gpu` throughout.

### Manifests

| Manifest | Exp | Script | Answer key |
|---|---|---|---|
| `exp1-job.yaml` | 1 | `compare_retrievers.py` | 1,035q |
| `gte-jina-job.yaml` | 2 (reranked) | `compare_gte_vs_jina.py` | 996q |
| `gte-baseline-job.yaml` | 2 (semantic) | `compare_gte_vs_jina.py` | 996q |
| `exp3-job.yaml` | 3 | `compare_query_rewrites.py`, `compare_rewrites_summaries.py` | 996q |
| `flatten-ab-job.yaml` | 4, 5 | `flatten_ab_eval.py` | 35q |
| `ndcg-job.yaml` | 6 | `ndcg_eval.py` | 1,035q |
| `bm25-expansion-job.yaml` | 7 | `compare_bm25_expansion.py` | 1,035q |
| `hn-pool-job.yaml` | 8 | `expand_ground_truth_pool.py` + `compare_retrievers.py` | 1,035q |
| `hybrid-rerank-job.yaml` | 9 | `compare_hybrid_rerank.py` | 1,035q |
| `db-check-job.yaml` | — | inline (diagnostic: confirms the 29-missing-doc gap) | — |

Each manifest's trailing YAML-comment block holds the exact
`kubectl create configmap … --dry-run=client -o yaml | kubectl apply -f -`
commands to regenerate its ConfigMaps, plus experiment-specific notes. **Those
commands are the source of truth** — always regenerate from the repo rather than
restoring an exported snapshot. An earlier export of the live ConfigMaps was
deliberately left out of version control: it captured the pre-D2
`flatten_ab_eval.py`, with `SUMMARY_DIR = "./summaries"`, so applying it would
silently reintroduce that defect.

### Rules learned the hard way

- **Pull results out of `kubectl logs` before assuming you're done.**
  `kubectl logs` works on a completed pod; **`kubectl cp` and `kubectl exec` do
  not.** Anything written only to the container filesystem is unrecoverable once
  the pod terminates.
- **`ttlSecondsAfterFinished: 86400`** on every Job (1h on the diagnostic). Two
  early runs were lost to the Kubernetes default of 1 hour deleting the pod, and
  its logs, before anyone checked back.
- **Experiment 8 deliberately chains pooling and comparison into one command.**
  The 22,124-row pooled answer key lives only on the pod's filesystem and dies
  with it. Do not split them into separate Jobs — this was learned twice.
- **Experiment 2 needs a manual upload.** `courses_md/` is too large for a
  ConfigMap, so the Job prints `WAITING_FOR_UPLOAD` and blocks:
  ```sh
  tar czf /tmp/courses_md.tar.gz -C . courses_md
  kubectl --context=anvil apply -f evaluate/k8s/gte-jina-job.yaml
  POD=$(kubectl --context=anvil get pods -n cyberfaces-dev -l app=cyberfaces-gte-jina \
         --sort-by=.metadata.creationTimestamp -o jsonpath='{.items[-1:].metadata.name}')
  kubectl --context=anvil cp /tmp/courses_md.tar.gz cyberfaces-dev/"$POD":/work/courses_md.tar.gz
  kubectl --context=anvil exec -n cyberfaces-dev "$POD" -- touch /work/READY
  ```
- **`kubectl apply` fails on the large binary ConfigMaps** (`cyberfaces-hn-data`,
  `cyberfaces-exp3-data`) — the payload exceeds apply's 256KiB
  last-applied-configuration annotation. Use `kubectl replace` or plain
  `kubectl create`.

### The two answer keys are not interchangeable

There are two graded ground-truth sets, and **they are not nested**:

| File | Queries | Rows | Judged docs | Missing from corpus |
|---|---|---|---|---|
| `evaluate/final_evaluation_dataset.jsonl` | 996 | 10,024 | 336 (max id 342) | 0 |
| `final_evaluation_dataset_1035q.jsonl` | 1,035 | 10,428 | 346 (max id 367) | 29 |

They share only **17 query strings** — 979 are unique to the first, 1,018 to the
second. They are two independently generated query sets, not one grown over
time. **No metric transfers between them**: BM25 scores 0.680 on the 996-query
key and 0.4159 on the 1,035-query key, and that difference is the key, not the
retriever. Always check which key a number belongs to before comparing it to
another.

---

## Reproduction run, 2026-09-09 → 09-10

All nine experiments were re-run on Anvil and checked against the archived
write-ups. **All nine reproduce, and no underlying data has drifted** — the
course catalog and both ground-truth sets are unchanged, every deterministic
figure landed on its documented value, and each apparent divergence traced to an
identified cause rather than to the data.

Captured stdout for every Job is in `evaluate/k8s/run_logs_2026-09-09/`. The
audit write-up, with full per-experiment comparison tables, is the
**Cyberfaces Reproduction Audit** artifact.

Highlights:

- Experiments 4 and 5: all eight deterministic rows matched **exactly**,
  including every false-alarm count. LLM-driven rows within run-to-run noise.
- Experiment 6: RRF 0.441 / 0.463, 995 scored and 40 excluded — exact.
- Experiment 7: 0.4159 → 0.4469, expansion improving all four metrics.
- Experiment 8: pooling reproduced to the row — 10,428 existing + 11,696 new =
  22,124.
- Experiment 9: all three methods within 0.001.
- Experiment 1's BM25 row matched Experiment 9's to four decimals — an
  independent check that neither the corpus nor the key has moved.

### Known defects

Five defects were found. They are in the recorded configuration, scoring and
labels — **not** in the measurements. Two are fixed; three change what published
rows mean and are still open.

| | Defect | Status |
|---|---|---|
| D1 | `bm25-expansion-job.yaml`'s regen comment named the 996-query set, but Experiments 7–9 use the 1,035-query set. Following it silently swaps the answer key under all three. | **fixed** — comment corrected, ConfigMap verified byte-identical |
| D2 | The summaries ConfigMap was mounted at `/app/summaries` while `flatten_ab_eval.py` reads `./curated_summaries_35q`; the regen comment pointed at `summaries/`, a *different* 346-file corpus. | **fixed** — mount paths and comment corrected |
| D3 | The `gte` scripts restrict the answer key to documents surviving their corpus filter. Experiment 2's two rows were scored **differently from each other**, which is what produced its "reranking wins" result. | **open** |
| D4 | The artifact describes the two keys as one set grown over time. They share 17 queries. | **open** |
| D5 | `compare_retrievers.py` prints `Vector (MPNet)` while `app/main.py:359` embeds with `gte-large-en-v1.5`. | **open** |

**D3 is the consequential one.** Experiment 2 is written up as the single case
where reranking helped (NDCG@10 0.567 → 0.623). Its reranked row reproduces
exactly *with* the restriction; its semantic row only reproduces *without* it.
Scored consistently, on the same GPU, corpus, key and code path:

| Method | NDCG@10 | MRR | P@10 | R@10 |
|---|---|---|---|---|
| Semantic (gte-large) | **0.6346** | 0.8087 | 0.3307 | 0.6220 |
| → + jina-v3 rerank | **0.6227** | 0.8131 | 0.2902 | 0.5613 |

Reranking loses on NDCG@10, precision and recall. **Experiment 2 is not an
exception to the pattern — it agrees with the other eight.** The archived
reports' synthesis sections, and the recommendation to give the reranker more
text, both rest on the mixed comparison.

Experiment 3's summaries rows carry the same mismatch but survive it: both were
scored unrestricted, so the comparison between them stays internally consistent
and only the absolute values shift. Its conclusion holds under both conventions,
both embedding models and both corpora.

### Open follow-ups

- Correct or annotate the archived write-ups for D3, D4 and D5.
- Fix the label in `compare_retrievers.py` (D5).
- Fix `compare_rewrites_summaries.py:108`, which selects
  `"mps" if available else "cpu"` and never checks CUDA — it cost Experiment 3
  6h04m against Experiment 1's 91s. The same bug was already found and fixed
  twice in sibling scripts.
- Fix the same GPU-placement bug in production's `load_rerankers()`, which
  loads `jina-reranker-v3` with no `.to("cuda")`. The live
  `/search_reranking_advance` endpoint may be reranking on CPU.
- Resolve the eval-set provenance gap: 29 document IDs referenced by the
  1,035-query key exist in no source checked. 14 have recoverable content via
  the file-extraction pipeline; 15 remain stubs.

---

## Provenance

`docs_archive/` holds the superseded write-ups, kept because they are the
original record of the numbers this README's reproduction section cites:

- `SmartSearch_Full_Investigation_Report.docx` — Experiments 4–6 plus the
  infrastructure debugging and corpus-recovery investigation
- `SmartSearch_Reranker_Evaluation.docx` — Experiments 4–5 in detail
- `retrieval_comparison_report.docx` — the original Experiment 1 (996-query key,
  MPNet embeddings, 30-query reranker sample), regenerated by
  `evaluate/make_report.py`

Where those documents and this README disagree, this README reflects the
reproduction run and the archived documents reflect what was originally
published. The differences are catalogued in [Known defects](#known-defects).
