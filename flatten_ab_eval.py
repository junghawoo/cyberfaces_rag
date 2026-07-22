#!/usr/bin/env python3
"""
flatten_ab_eval.py  --  A/B test: does flattening the document text (removing
structural symbols like the "|" separator, HTML tags, entities) change the
classification accuracy of the rerankers?

It reproduces the repo's *exact* Fixed-Pool / MCC evaluation logic from
app/main.py, but builds each document's text TWO ways:

  current  :  title + "|" + description          (what app/main.py does today)
  flat     :  prose(title) + ". " + prose(description)   (HTML stripped,
              entities unescaped, structural symbols removed, whitespace
              collapsed -- the "prose translation layer" idea)

For every method it prints mean/median Balanced Accuracy and MCC for both text
variants so you can see the delta.

Run from the repo root (needs the same data files + models as the app):

    pip install sentence-transformers rank-bm25 nltk numpy pandas
    # cross-encoder "base" path needs NO API key:
    python flatten_ab_eval.py --methods RRF CrossEncoder_base
    # to also test the deployed jina-v3 + AnvilGPT query-expansion path:
    export ANVILGPT_API=...   # your key
    python flatten_ab_eval.py --methods RRF CrossEncoder_base CrossEncoder_advance

Notes
-----
* HuggingFace + the AnvilGPT API must be reachable from wherever you run this.
* CrossEncoder_base uses cross-encoder/ms-marco-MiniLM-L-6-v2 with NO query
  expansion -> deterministic-ish and no API needed. It is a faithful proxy for
  the "does the text format matter to a cross-encoder" question.
* CrossEncoder_advance mirrors combine_advance_reranking(): LLM query expansion
  (prompt 3) + instruction + jina-reranker-v3. This is the path that produced
  analysis/CrossEncoder.json (eval threshold -0.1).
"""

import argparse, json, os, re, html, copy, sys
import numpy as np

# ----------------------------------------------------------------------------
# config (matches app/main.py)
# ----------------------------------------------------------------------------
NUM_RETRIEVAL    = 24
KEYWORD_THRESHOLD = 1.25      # normalized BM25 cutoff
SEMANTIC_CUTOFF   = 0.45      # semantic relevance cutoff
EMBED_MODEL       = "sentence-transformers/all-mpnet-base-v2"
BASE_CE_MODEL     = "cross-encoder/ms-marco-MiniLM-L-6-v2"
ADV_CE_MODEL      = "jinaai/jina-reranker-v3"
DATA_FILE         = "./data.jsonl"
MAP_FILE          = "./course_unit_map.jsonl"
EVAL_FILE         = "./gemini_generate_dataset_updateByHuman.jsonl"
CE_EVAL_THRESHOLD = -0.1      # threshold used for CrossEncoder in /evaluate

# ----------------------------------------------------------------------------
# the flattening / prose-translation layer  (the thing under test)
# ----------------------------------------------------------------------------
_TAG   = re.compile(r"<[^>]+>")          # html tags
_STRUCT = re.compile(r"[{}\[\]|\"<>]")   # structural symbols incl. the "|" join
_WS    = re.compile(r"\s+")

def flatten_text(s: str, drop_commas: bool = False) -> str:
    """Strip structural syntax and return clean prose.

    drop_commas=True literally removes commas too (the most aggressive reading
    of 'remove symbols such as { and ,'). Off by default because in-prose
    commas carry meaning and usually help, not hurt, a cross-encoder.
    """
    if not s:
        return ""
    s = html.unescape(s)        # &amp; -> &  , &nbsp; -> space, etc.
    s = _TAG.sub(" ", s)        # remove HTML tags
    s = _STRUCT.sub(" ", s)     # remove { } [ ] | " < >
    if drop_commas:
        s = s.replace(",", " ")
    s = _WS.sub(" ", s).strip()
    return s

def build_text(title, desc, variant, drop_commas=False):
    title = title or ""
    desc  = desc or ""
    if variant == "current":
        # exactly what load_vectorDB_docs() does today
        return (title + "|" + desc) if desc else title
    elif variant == "flat":
        t, d = flatten_text(title, drop_commas), flatten_text(desc, drop_commas)
        return (t + ". " + d).strip(". ").strip() if d else t
    elif variant == "labeled":
        # explicit field labels, e.g. "title: <title> description: <desc>"
        return (f"title: {title} description: {desc}") if desc else (f"title: {title}")
    raise ValueError(variant)

# ----------------------------------------------------------------------------
# lexical preprocessing  (copied verbatim from app/main.py)
# ----------------------------------------------------------------------------
import nltk
for pkg in ("punkt", "punkt_tab", "stopwords"):
    try: nltk.download(pkg, quiet=True)
    except Exception: pass
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

def deep_clean_query(query, stemmer):
    stop_words = set(stopwords.words("english"))
    query = query.replace("-", "").replace("/", " ")
    tokens = word_tokenize(query.lower())
    tech = re.compile(r"^[a-z0-9+#]+$")
    return [stemmer.stem(w) for w in tokens
            if (w.isalpha() or tech.match(w)) and w not in stop_words]

# ----------------------------------------------------------------------------
# metrics  (copied verbatim from app/main.py)
# ----------------------------------------------------------------------------
def calculate_mcc(tp, tn, fp, fn):
    num = (tp * tn) - (fp * fn)
    d1, d2, d3, d4 = tp+fp, tp+fn, tn+fp, tn+fn
    if 0 in (d1, d2, d3, d4): return 0.0
    return num / np.sqrt(d1*d2*d3*d4)

def calculate_fixed_pool(retrieved_items, expected_ids, threshold):
    expected = set(expected_ids)
    split = next((i for i, x in enumerate(retrieved_items) if x["score"] < threshold),
                 len(retrieved_items))
    above = {it["id"] for it in retrieved_items[:split]}
    below = {it["id"] for it in retrieved_items[split:]}
    tp = len(above & expected); fp = len(above - expected)
    fn = len(below & expected); tn = len(below - expected)
    retrieved_ids = {it["id"] for it in retrieved_items}
    fn += len(expected - retrieved_ids)            # missing from pool
    mcc = calculate_mcc(tp, tn, fp, fn)
    spec = tn/(tn+fp) if (tn+fp) else 0
    rec  = tp/(tp+fn) if (tp+fn) else 0
    return {"tp":tp,"fp":fp,"tn":tn,"fn":fn,"specificity":spec,"recall":rec,
            "mcc":mcc,"balanced_accu":(spec+rec)/2}

# ----------------------------------------------------------------------------
# corpus / index for one text variant
# ----------------------------------------------------------------------------
class Index:
    def __init__(self, docs, variant, embedder, drop_commas=False):
        from rank_bm25 import BM25Okapi
        self.ids    = [d["id"] for d in docs]
        self.texts  = [build_text(d.get("title"), d.get("description"), variant, drop_commas)
                       for d in docs]
        self.id2text = dict(zip(self.ids, self.texts))
        self.stemmer = PorterStemmer()
        self.bm25 = BM25Okapi([deep_clean_query(t, self.stemmer) for t in self.texts])
        # normalized embeddings -> cosine == dot product (Chroma uses cosine)
        self.emb = embedder.encode(self.texts, normalize_embeddings=True,
                                   show_progress_bar=False)
        self.embedder = embedder

    def semantic(self, query, k=NUM_RETRIEVAL):
        q = self.embedder.encode([query], normalize_embeddings=True)[0]
        sims = self.emb @ q                      # cosine similarity
        order = np.argsort(sims)[::-1][:k]
        return [(self.ids[i], float(sims[i])) for i in order]

    def lexical(self, query, k=NUM_RETRIEVAL):
        bq = deep_clean_query(query, self.stemmer)
        scores = self.bm25.get_scores(bq)
        order = np.argsort(scores)[::-1][:k]
        n = max(len(bq), 1)
        return [(self.ids[i], float(scores[i]/n)) for i in order]   # length-normalized

def cut_threshold(ranked, thr):
    out = ranked
    for i, (_id, sc) in enumerate(ranked):
        if sc <= thr:
            out = ranked[:i]; break
    return out

# ----------------------------------------------------------------------------
# the methods  (mirror app/main.py)
# ----------------------------------------------------------------------------
def eval_rrf(idx, query, expected):
    sem  = idx.semantic(query); kw = idx.lexical(query)
    psem = cut_threshold(sem, SEMANTIC_CUTOFF)
    pkw  = cut_threshold(kw, KEYWORD_THRESHOLD)
    above = {i for i,_ in psem} | {i for i,_ in pkw}
    retrieved = {i for i,_ in sem} | {i for i,_ in kw}
    below = retrieved - above
    exp = set(expected)
    tp=len(above&exp); fp=len(above-exp); fn=len(below&exp); tn=len(below-exp)
    fn += len(exp - retrieved)
    spec = tn/(tn+fp) if (tn+fp) else 0; rec = tp/(tp+fn) if (tp+fn) else 0
    return {"tp":tp,"fp":fp,"tn":tn,"fn":fn,"specificity":spec,"recall":rec,
            "mcc":calculate_mcc(tp,tn,fp,fn),"balanced_accu":(spec+rec)/2}

def _combined_pool(idx, query):
    sem = idx.semantic(query); kw = idx.lexical(query)
    seen, pool = set(), []
    for i,_ in sem: pool.append(i); seen.add(i)
    for i,_ in kw:
        if i not in seen: pool.append(i); seen.add(i)
    return pool

def eval_cross_base(idx, query, expected, ce):
    pool = _combined_pool(idx, query)
    pairs = [[query, idx.id2text[i]] for i in pool]
    scores = ce.predict(pairs)
    ranked = sorted(zip(scores, pool), key=lambda x: x[0], reverse=True)
    items = [{"id":i, "score":float(s)} for s,i in ranked]
    return calculate_fixed_pool(items, expected, CE_EVAL_THRESHOLD)

def eval_cross_advance(idx, query, expected, adv, api_key):
    q = rewrite_query_with_llm(query, api_key)
    instr = ("Given a course description, identify all documents that provide "
             "relevant information, even if they use different terminology or "
             "they are sub-topics. ")
    qi = f"instruction: {instr}\nquery: {q}"
    pool = _combined_pool(idx, query)
    docs = [idx.id2text[i] for i in pool]
    res = adv.rerank(query=qi, documents=docs)
    # jina rerank() returns results sorted by score, each carrying an "index"
    # back into `docs`/`pool`; map score -> id via that index (do NOT zip with
    # pool positionally, since res is reordered).
    items = [{"id": pool[r["index"]], "score": float(r["relevance_score"])} for r in res]
    items.sort(key=lambda x: x["score"], reverse=True)
    return calculate_fixed_pool(items, expected, CE_EVAL_THRESHOLD)

def rewrite_query_with_llm(question, api_key):
    import requests
    prompt = ("### Role\nYou are an Academic Curriculum Designer. Transform casual "
              "queries into a professional 1-3 sentence course description. Provide "
              "only the rewritten description.")
    r = requests.post("https://anvilgpt.rcac.purdue.edu/api/chat/completions",
        headers={"Authorization":f"Bearer {api_key}","Content-Type":"application/json"},
        json={"model":"gpt-oss:120b","temperature":0,"stream":False,
              "messages":[{"role":"system","content":prompt},
                          {"role":"user","content":question}]})
    return json.loads(r.text)["choices"][0]["message"]["content"]

# ----------------------------------------------------------------------------
# driver
# ----------------------------------------------------------------------------
def load_docs():
    docs = []
    for ln in open(DATA_FILE, encoding="utf-8"):
        ln = ln.strip()
        if ln: docs.append(json.loads(ln))
    return docs

def load_eval():
    qm = {}
    for ln in open(EVAL_FILE, encoding="utf-8"):
        ln = ln.strip()
        if not ln: continue
        d = json.loads(ln)
        qm[d["query_id"]] = {"text": d["user_query"], "expected": set(d["expected_ids"])}
    return qm

def aggregate(rows):
    a = lambda k: np.array([r[k] for r in rows], float)
    return {"mean_bAcc":a("balanced_accu").mean(), "median_bAcc":np.median(a("balanced_accu")),
            "mean_MCC":a("mcc").mean(),  "median_MCC":np.median(a("mcc")),
            "FP":int(a("fp").sum()), "TP":int(a("tp").sum()),
            "FN":int(a("fn").sum()), "TN":int(a("tn").sum())}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--methods", nargs="+",
                    default=["RRF","CrossEncoder_base"],
                    help="RRF | CrossEncoder_base | CrossEncoder_advance")
    ap.add_argument("--drop-commas", action="store_true",
                    help="also strip commas in the flat variant (aggressive)")
    args = ap.parse_args()

    from sentence_transformers import SentenceTransformer, CrossEncoder
    print(f"loading embedder {EMBED_MODEL} ...")
    embedder = SentenceTransformer(EMBED_MODEL)

    docs = load_docs(); qm = load_eval()
    print(f"{len(docs)} docs, {len(qm)} eval queries")

    print("building indices (current + flat + labeled) ...")
    idx_cur     = Index(docs, "current", embedder, args.drop_commas)
    idx_flat    = Index(docs, "flat",    embedder, args.drop_commas)
    idx_labeled = Index(docs, "labeled", embedder, args.drop_commas)
    VARIANTS = (("current", idx_cur), ("flat", idx_flat), ("labeled", idx_labeled))

    ce = adv = api = None
    if "CrossEncoder_base" in args.methods:
        print(f"loading base cross-encoder {BASE_CE_MODEL} ...")
        ce = CrossEncoder(BASE_CE_MODEL)
    if "CrossEncoder_advance" in args.methods:
        from transformers import AutoModel
        api = os.environ.get("ANVILGPT_API")
        if not api: sys.exit("ANVILGPT_API env var required for CrossEncoder_advance")
        print(f"loading advanced reranker {ADV_CE_MODEL} ...")
        adv = AutoModel.from_pretrained(ADV_CE_MODEL, trust_remote_code=True).eval()

    results = {}
    for method in args.methods:
        for variant, idx in VARIANTS:
            rows = []
            for qid, info in qm.items():
                if method == "RRF":
                    rows.append(eval_rrf(idx, info["text"], info["expected"]))
                elif method == "CrossEncoder_base":
                    rows.append(eval_cross_base(idx, info["text"], info["expected"], ce))
                elif method == "CrossEncoder_advance":
                    rows.append(eval_cross_advance(idx, info["text"], info["expected"], adv, api))
            results[(method, variant)] = aggregate(rows)

    # report
    print("\n" + "="*78)
    print(f"{'method':22} {'variant':8} {'bAcc(mean/med)':18} {'MCC(mean/med)':18} {'FP':>5}")
    print("-"*78)
    for method in args.methods:
        for variant, _ in VARIANTS:
            r = results[(method,variant)]
            print(f"{method:22} {variant:8} "
                  f"{r['mean_bAcc']:.3f}/{r['median_bAcc']:.3f}      "
                  f"{r['mean_MCC']:.3f}/{r['median_MCC']:.3f}      {r['FP']:>5}")
        c = results[(method,'current')]
        for variant, _ in VARIANTS:
            if variant == "current": continue
            v = results[(method,variant)]
            print(f"{('  -> delta ('+variant+'-current)'):30} "
                  f"bAcc {v['mean_bAcc']-c['mean_bAcc']:+.3f}   "
                  f"MCC {v['mean_MCC']-c['mean_MCC']:+.3f}   FP {v['FP']-c['FP']:+d}")
        print()

    json.dump({f"{m}|{v}":r for (m,v),r in results.items()},
              open("flatten_ab_results.json","w"), indent=2)
    print("wrote flatten_ab_results.json")

if __name__ == "__main__":
    main()
