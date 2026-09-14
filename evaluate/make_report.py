"""
Generate a Word (.docx) summary of the retrieval-method comparison experiment.

    python evaluate/make_report.py            # writes evaluate/retrieval_comparison_report.docx
    # note: the published copy of this report now lives in docs_archive/
"""
import os
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "retrieval_comparison_report.docx")

ACCENT = RGBColor(0x1F, 0x4E, 0x79)   # dark blue
MUTED = RGBColor(0x60, 0x60, 0x60)

doc = Document()

# ---- base styles ----
normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.font.size = Pt(11)


def heading(text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = ACCENT
    return h


def bullet(text, bold_prefix=None):
    p = doc.add_paragraph(style="List Bullet")
    if bold_prefix:
        r = p.add_run(bold_prefix)
        r.bold = True
        p.add_run(text)
    else:
        p.add_run(text)
    return p


def make_table(headers, rows, bold_row=None, caption=None):
    if caption:
        cap = doc.add_paragraph()
        r = cap.add_run(caption)
        r.italic = True
        r.font.size = Pt(9)
        r.font.color.rgb = MUTED
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = "Light Grid Accent 1"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = ""
        run = hdr[i].paragraphs[0].add_run(h)
        run.bold = True
        run.font.size = Pt(10)
    for ri, row in enumerate(rows):
        cells = table.add_row().cells
        for i, val in enumerate(row):
            cells[i].text = ""
            run = cells[i].paragraphs[0].add_run(str(val))
            run.font.size = Pt(10)
            if bold_row is not None and ri == bold_row:
                run.bold = True
    doc.add_paragraph()
    return table


# ============================== TITLE ==============================
title = doc.add_heading("Retrieval Method Comparison: BM25 vs. Vector Search vs. Cross-Encoder Reranking", level=0)
for run in title.runs:
    run.font.color.rgb = ACCENT
sub = doc.add_paragraph()
sr = sub.add_run("Evaluation of three retrieval pipelines for the Cyberfaces course-search corpus")
sr.italic = True
sr.font.color.rgb = MUTED
meta = doc.add_paragraph()
mr = meta.add_run("Date: 2026-06-24    |    Corpus: 336 documents    |    Ground truth: 996 graded queries")
mr.font.size = Pt(9)
mr.font.color.rgb = MUTED

# ============================== SUMMARY ==============================
heading("Executive Summary", 1)
doc.add_paragraph(
    "We compared three retrieval methods on a graded relevance benchmark using NDCG@10, MRR, "
    "Precision@10, and Recall@10. Vector (bi-encoder) search was the strongest method on every "
    "metric. Adding a cross-encoder reranking stage (Jina reranker v3) on top of the vector "
    "candidates did not help — it measurably degraded ranking quality. BM25 keyword search "
    "was the weakest of the three."
)
bullet(" Vector (MPNet) ranks best — NDCG@10 ≈ 0.87 on the full 996-query set.",
       bold_prefix="Winner:")
bullet(" Reranking the vector top-50 with Jina v3 lowered NDCG@10 from 0.852 to 0.796 (same 30 queries), "
       "demoting relevant documents out of the top 10.", bold_prefix="Surprising result:")
bullet(" Vector  >  Vector + Jina rerank  >  BM25, consistent across the sample and the full set.",
       bold_prefix="Overall ordering:")

# ============================== METHODS ==============================
heading("Experimental Setup", 1)

heading("Methods evaluated", 2)
bullet(" BM25 over the document corpus (Porter-stemmed, stopword-filtered, query-length normalized).",
       bold_prefix="1. Keyword search (BM25):")
bullet(" Bi-encoder dense retrieval with sentence-transformers/all-mpnet-base-v2 embeddings, "
       "cosine similarity, served from a Chroma vector store.", bold_prefix="2. Vector search (MPNet):")
bullet(" Retrieve the top 50 candidates by vector search, then resort them with the "
       "jinaai/jina-reranker-v3 cross-encoder and keep the top 10.",
       bold_prefix="3. Vector + Cross-Encoder rerank:")

heading("Protocol", 2)
doc.add_paragraph(
    "Each method was run in isolation (no hybrid score fusion, no LLM query rewriting). For every "
    "query we took the ordered top-10 document IDs, looked up their graded relevance in the ground "
    "truth (documents not labeled for a query are scored 0), and computed the metrics per query, then "
    "averaged across queries."
)
bullet(" NDCG@10 (graded 0–3, the primary metric), MRR, Precision@10, Recall@10. "
       "Precision/Recall/MRR treat a document as relevant when its graded score ≥ 1.",
       bold_prefix="Metrics:")
bullet(" 996 graded queries over 336 documents (final_evaluation_dataset.jsonl), relevance scored 0–3.",
       bold_prefix="Ground truth:")
bullet(" K = 10; reranker candidate pool = 50.", bold_prefix="Parameters:")

# ============================== RESULTS ==============================
heading("Results", 1)

heading("Full evaluation set (996 queries) — BM25 vs. Vector", 2)
make_table(
    ["Method", "NDCG@10", "MRR", "P@10", "R@10"],
    [
        ["BM25 (keyword)", "0.680", "0.872", "0.400", "0.625"],
        ["Vector (MPNet)", "0.868", "0.965", "0.587", "0.884"],
    ],
    bold_row=1,
    caption="Table 1. Mean metrics over all 996 queries. Vector wins on every metric.",
)
doc.add_paragraph(
    "Vector search dominates BM25: +0.19 NDCG@10, ~1.5× the precision, and it captures ~88% of "
    "relevant documents in the top 10 versus BM25's ~63%."
)

heading("Three-way comparison (30-query sample, including Jina reranker)", 2)
doc.add_paragraph(
    "Because jina-reranker-v3 ran CPU-bound on the local machine at ~6–10 minutes per query "
    "(full 996-query reranking would take ~100+ hours), the cross-encoder was evaluated on a 30-query "
    "sample. BM25 and Vector were run on the same 30 queries for a fair head-to-head."
)
make_table(
    ["Method", "NDCG@10 (mean/med)", "MRR", "P@10", "R@10"],
    [
        ["BM25 (keyword)", "0.648 / 0.650", "0.919", "0.447", "0.582"],
        ["Vector (MPNet)", "0.852 / 0.900", "0.978", "0.670", "0.872"],
        ["Vector + Jina rerank", "0.796 / 0.796", "0.956", "0.533", "0.713"],
    ],
    bold_row=1,
    caption="Table 2. Mean metrics over the same 30 queries (NDCG also shows median). Vector is best; reranking hurts.",
)

heading("Key finding: reranking degrades quality on this corpus", 2)
doc.add_paragraph(
    "Adding the Jina cross-encoder reduced NDCG@10 from 0.852 (vector) to 0.796, with parallel drops "
    "in precision (0.670 → 0.533) and recall (0.872 → 0.713). Because the reranker only reorders "
    "documents already retrieved by vector search (its top-50 candidate pool), the relevant documents "
    "are present in the pool — the reranker is actively pushing them below rank 10. On this domain, "
    "the bi-encoder's ordering is better than the cross-encoder's."
)

# ============================== INTERPRETATION ==============================
heading("Interpretation", 1)
bullet(" For the typical query NDCG@10 reaches ~0.90 (median > mean), with a minority of hard "
       "queries pulling the mean down.", bold_prefix="Vector ordering is near-ideal:")
bullet(" The cross-encoder's relevance judgments disagree with the graded labels for this course "
       "corpus and demote correct results.", bold_prefix="Reranker mis-ranks:")
bullet(" MRR is high for all methods (0.87–0.98) — the first hit is almost always relevant — "
       "so MRR discriminates weakly here; NDCG/Precision/Recall are the informative metrics.",
       bold_prefix="MRR saturates:")

# ============================== CAVEATS ==============================
heading("Caveats and Limitations", 1)
bullet(" The reranker comparison uses 30 queries; the result is directional and should be confirmed at "
       "larger scale (e.g., on GPU hardware).", bold_prefix="Sample size:")
bullet(" The reranker was run on the raw query. The production pipeline adds an instruction prefix and an "
       "LLM query rewrite, which may change reranker behavior and was not tested here.",
       bold_prefix="Isolated configuration:")
bullet(" Ground-truth labels were generated in part from vector/BM25 retrieval candidates "
       "(LLM-judge / perfect-match sources), which may modestly favor the vector ranking.",
       bold_prefix="Label provenance:")
bullet(" jina-reranker-v3 fell back to CPU on Apple Silicon (~6–10 min/query). On a GPU the full "
       "996-query reranking is feasible.", bold_prefix="Hardware:")

# ============================== NEXT STEPS ==============================
heading("Recommended Next Steps", 1)
bullet(" Re-run the full 996-query reranking on GPU (Anvil) to confirm the “reranking hurts” "
       "finding at scale.")
bullet(" Test the reranker with the production instruction prefix + query rewrite to see whether that "
       "is what makes it useful in deployment.")
bullet(" Evaluate additional cutoffs (NDCG@5, NDCG@20) and a higher relevance threshold (≥2) for "
       "precision/recall.")
bullet(" Ship vector (MPNet) search as the default retriever pending the GPU-scale reranker confirmation.")

# ============================== APPENDIX ==============================
heading("Appendix: Reproducibility", 1)
bullet(" evaluate/compare_retrievers.py (computes NDCG@K / MRR / P@K / R@K for the three methods).",
       bold_prefix="Harness:")
bullet(" evaluate/final_evaluation_dataset.jsonl (996 queries, graded 0–3).",
       bold_prefix="Ground truth:")
bullet(" conda env cyberfaces-eval (Python 3.11); model weights cached locally.",
       bold_prefix="Environment:")
p = doc.add_paragraph(style="List Bullet")
p.add_run("Command: ").bold = True
c = p.add_run("python evaluate/compare_retrievers.py --limit 30 --export_dir ./run_results_sample30")
c.font.name = "Consolas"
c.font.size = Pt(9)

doc.save(OUT)
print(f"Wrote {OUT}")
