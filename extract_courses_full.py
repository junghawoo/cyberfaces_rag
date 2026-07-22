"""
COMPREHENSIVE course extraction — one Markdown file per unit, pulling from
*every* resource type:

  LOCAL   : pdf, pptx, docx/doc, ipynb (source + outputs), md, txt, csv, vtt, xlsx, pages
  DB      : unit metadata, inline `type=text` HTML assets, quiz questions + choices
  REMOTE  : web pages (HTML->text), GitHub notebooks/readmes, remote PDFs (Springer/
            Dropbox/Google), YouTube transcripts
  OCR     : scanned PDFs (no text layer) and images (png/jpg) via tesseract

Network fetches and OCR are cached under courses_md/.cache/ so reruns are cheap and
partial progress survives failures.
"""

import os, re, io, json, sys, time, hashlib, subprocess
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import extract_courses as base   # reuse DB parser + local extractors

DUMP    = base.DUMP
COURSES = base.COURSES
OUTDIR  = base.OUTDIR
CACHE   = os.path.join(OUTDIR, ".cache")
MAX_CHARS = base.MAX_CHARS
FETCH_TIMEOUT = 25
HEADERS = {"User-Agent": "Mozilla/5.0 (course-extractor; research)"}

SKIP_HOSTS = ("questionpro.com", "qualtrics.com")  # surveys: no readable content


# --------------------------------- cache -------------------------------------

def cache_get(key):
    p = os.path.join(CACHE, hashlib.sha1(key.encode()).hexdigest() + ".txt")
    return open(p, encoding="utf-8").read() if os.path.exists(p) else None

def cache_put(key, val):
    os.makedirs(CACHE, exist_ok=True)
    p = os.path.join(CACHE, hashlib.sha1(key.encode()).hexdigest() + ".txt")
    open(p, "w", encoding="utf-8").write(val or "")


# --------------------------- notebook w/ outputs -----------------------------

def ipynb_from_obj(nb):
    out = []
    for cell in nb.get("cells", []):
        src = "".join(cell.get("source", []))
        if cell.get("cell_type") == "code":
            if src.strip():
                out.append("```python\n" + src + "\n```")
            for o in cell.get("outputs", []):
                if o.get("output_type") == "stream":
                    out.append("_output:_\n```\n" + "".join(o.get("text", [])).strip() + "\n```")
                elif o.get("output_type") in ("execute_result", "display_data"):
                    txt = o.get("data", {}).get("text/plain")
                    if txt:
                        out.append("_result:_\n```\n" + "".join(txt).strip() + "\n```")
        elif src.strip():
            out.append(src)
    return "\n\n".join(out)

def extract_ipynb_full(path):
    return ipynb_from_obj(json.load(open(path, encoding="utf-8", errors="replace")))


# --------------------------------- OCR ---------------------------------------

_TESS = None
def have_tesseract():
    global _TESS
    if _TESS is None:
        from shutil import which
        _TESS = which("tesseract") is not None
    return _TESS

def ocr_image_path(path):
    if not have_tesseract():
        return ""
    key = "ocr:" + path + ":" + str(os.path.getmtime(path))
    c = cache_get(key)
    if c is not None:
        return c
    try:
        import pytesseract
        from PIL import Image
        txt = pytesseract.image_to_string(Image.open(path)).strip()
    except Exception as e:
        txt = f"[OCR error: {e}]"
    cache_put(key, txt)
    return txt

def ocr_pdf(path):
    if not have_tesseract():
        return ""
    key = "ocrpdf:" + path + ":" + str(os.path.getmtime(path))
    c = cache_get(key)
    if c is not None:
        return c
    try:
        import fitz, pytesseract
        from PIL import Image
        doc = fitz.open(path)
        pages = []
        for pg in doc:
            pix = pg.get_pixmap(dpi=200)
            img = Image.open(io.BytesIO(pix.tobytes("png")))
            pages.append(pytesseract.image_to_string(img).strip())
        doc.close()
        txt = "\n\n".join(p for p in pages if p)
    except Exception as e:
        txt = f"[OCR error: {e}]"
    cache_put(key, txt)
    return txt


# ------------------------------- remote fetch --------------------------------

def http_get(url):
    import requests
    return requests.get(url, headers=HEADERS, timeout=FETCH_TIMEOUT, allow_redirects=True)

def html_to_text(html):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "lxml")
    for t in soup(["script", "style", "noscript", "nav", "footer", "header", "svg"]):
        t.decompose()
    title = soup.title.get_text(strip=True) if soup.title else ""
    text = re.sub(r"\n{3,}", "\n\n", soup.get_text("\n", strip=True))
    return (f"# {title}\n\n" if title else "") + text

def youtube_id(url):
    m = re.search(r"(?:v=|youtu\.be/|/embed/)([A-Za-z0-9_-]{11})", url)
    return m.group(1) if m else None

def fetch_youtube(url):
    vid = youtube_id(url)
    if not vid:
        return "[no video id]"
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        try:                       # v1.x API
            api = YouTubeTranscriptApi()
            snippets = api.fetch(vid)
            parts = [s.text for s in snippets]
        except Exception:          # older static API
            parts = [d["text"] for d in YouTubeTranscriptApi.get_transcript(vid)]
        return f"[YouTube transcript {vid}]\n" + " ".join(parts)
    except Exception as e:
        return f"[transcript unavailable: {type(e).__name__}]"

def github_raw_candidates(url):
    u = url.rstrip("/")
    if "/blob/" in u:
        return [u.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")]
    m = re.match(r"https?://github\.com/([^/]+)/([^/]+)(?:/(.*))?$", u)
    if not m:
        return []
    user, repo, rest = m.group(1), m.group(2), m.group(3)
    if rest:  # a path inside the repo, branch unknown -> try HEAD/main/master
        return [f"https://raw.githubusercontent.com/{user}/{repo}/{b}/{rest}"
                for b in ("HEAD", "main", "master")]
    # repo root -> try READMEs
    return [f"https://raw.githubusercontent.com/{user}/{repo}/{b}/README{ext}"
            for b in ("HEAD", "main", "master") for ext in (".md", ".rst", ".txt")]

def fetch_github(url):
    for cand in github_raw_candidates(url):
        try:
            r = http_get(cand)
            if r.status_code == 200 and r.content:
                if cand.endswith(".ipynb"):
                    try:
                        return ipynb_from_obj(r.json())
                    except Exception:
                        return r.text[:MAX_CHARS]
                return r.text[:MAX_CHARS]
        except Exception:
            continue
    return "[github: could not resolve raw content]"

def fetch_remote_pdf(url):
    try:
        import fitz
        r = http_get(url)
        if r.status_code != 200 or not r.content:
            return f"[fetch failed: HTTP {r.status_code}]"
        doc = fitz.open(stream=r.content, filetype="pdf")
        txt = "\n\n".join(p.get_text().strip() for p in doc)
        doc.close()
        return txt or "[remote pdf: no text layer]"
    except Exception as e:
        return f"[remote pdf error: {type(e).__name__}: {e}]"

def fetch_remote(url):
    """Dispatch a remote URL to the right fetcher. Cached."""
    if any(h in url for h in SKIP_HOSTS):
        return "[survey link — skipped]"
    c = cache_get("fetch:" + url)
    if c is not None:
        return c
    try:
        low = url.lower()
        if "youtube.com" in low or "youtu.be" in low:
            res = fetch_youtube(url)
        elif "github.com" in low:
            res = fetch_github(url)
        elif "dropbox.com" in low:
            dl = url.replace("dl=0", "dl=1")
            dl = dl + ("&dl=1" if "?" in dl and "dl=1" not in dl else ("?dl=1" if "?" not in dl else ""))
            res = fetch_remote_pdf(dl) if low.endswith(".pdf") or "pdf" in low else _fetch_generic(dl)
        elif low.endswith(".pdf"):
            res = fetch_remote_pdf(url)
        else:
            res = _fetch_generic(url)
    except Exception as e:
        res = f"[fetch error: {type(e).__name__}: {e}]"
    res = (res or "").strip()
    if len(res) > MAX_CHARS:
        res = res[:MAX_CHARS] + "\n\n[...truncated...]"
    cache_put("fetch:" + url, res)
    return res

def _fetch_generic(url):
    r = http_get(url)
    if r.status_code != 200:
        return f"[fetch failed: HTTP {r.status_code}]"
    ctype = r.headers.get("content-type", "").lower()
    if "pdf" in ctype:
        return fetch_remote_pdf(url)
    if "html" in ctype or "text" in ctype:
        return html_to_text(r.text)
    return f"[unhandled content-type: {ctype}]"


# --------------------------------- build -------------------------------------

def local_extract(path, ext):
    if ext == "ipynb":
        try:
            return extract_ipynb_full(path)
        except Exception as e:
            return f"[extraction error: {e}]"
    if ext in ("png", "jpg", "jpeg"):
        return ocr_image_path(path)
    txt = base.extract(path, ext)
    if ext == "pdf" and (not txt or len(txt.strip()) < 40):   # scanned -> OCR
        ocr = ocr_pdf(path)
        if ocr and not ocr.startswith("[OCR error"):
            txt = "[OCR]\n" + ocr
    return txt


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    units, assets, levels = base.load_db()
    sql = open(DUMP, encoding="utf-8", errors="replace").read()
    questions = [dict(zip(base.cols_of("course_questions", sql), r))
                 for r in base.parse_insert("course_questions", sql)]
    choices = [dict(zip(base.cols_of("course_question_choices", sql), r))
               for r in base.parse_insert("course_question_choices", sql)]
    # questions link to an asset (type=quiz); map through asset -> unit_id
    q_by_unit = defaultdict(list)
    for q in questions:
        a = assets.get(q.get("asset_id"))
        if a:
            q_by_unit[a.get("unit_id")].append(q)
    ch_by_q = defaultdict(list)
    for c in choices:
        ch_by_q[c.get("question_id")].append(c)

    os.makedirs(OUTDIR, exist_ok=True)

    # index local files by unit
    by_unit = defaultdict(list)
    for root, _, files in os.walk(COURSES):
        for fn in files:
            if fn == ".DS_Store":
                continue
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, COURSES).split(os.sep)
            uid = rel[0]
            aid = rel[1] if len(rel) == 3 and rel[1].isdigit() else None
            ext = fn.rsplit(".", 1)[-1].lower() if "." in fn else ""
            by_unit[uid].append((aid, fn, path, ext))

    # ---- PRE-PASS: fetch all remote URLs concurrently (cached) ----
    remote_urls = sorted({a["url"] for a in assets.values()
                          if (a.get("url") or "").startswith("http")})
    todo = [u for u in remote_urls if cache_get("fetch:" + u) is None]
    print(f"Remote URLs: {len(remote_urls)} total, {len(todo)} to fetch...")
    done = 0
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(fetch_remote, u): u for u in todo}
        for f in as_completed(futs):
            done += 1
            if done % 25 == 0:
                print(f"  fetched {done}/{len(todo)}")
    print("Remote fetch pass complete.")

    all_units = sorted(set(list(by_unit) + [u for u in units]),
                       key=lambda x: int(x) if str(x).isdigit() else 1e9)
    if limit:
        all_units = [u for u in all_units if u in by_unit][:limit]

    stats = defaultdict(int)
    written = 0
    for uid in all_units:
        u = units.get(uid, {})
        title = u.get("title") or f"Unit {uid}"
        slug = u.get("slug") or base.slugify(title)
        level = levels.get(u.get("level_id"), {}).get("title", "")
        try:
            obj_list = json.loads(u.get("objectives")) if (u.get("objectives") or "").startswith("[") else []
        except Exception:
            obj_list = []

        L = []
        L.append("---")
        L.append(f'title: "{base.fm_escape(title)}"')
        L.append(f"unit_id: {uid}")
        if u.get("course_id"): L.append(f"course_id: {u['course_id']}")
        if level: L.append(f'level: "{base.fm_escape(level)}"')
        if u.get("slug"): L.append(f"slug: {u['slug']}")
        if u.get("is_course"): L.append(f"is_course: {u['is_course']}")
        if obj_list:
            L.append("objectives:")
            for o in obj_list:
                L.append(f'  - "{base.fm_escape(o)}"')
        L.append("---\n")
        L.append(f"# {title}\n")
        if u.get("description"):
            L.append(f"**Description:** {u['description'].strip()}\n")
        if u.get("markdown_content"):
            L.append("## Module content\n")
            L.append(u["markdown_content"].strip() + "\n")

        # DB inline text assets
        text_assets = [a for a in assets.values()
                       if a.get("unit_id") == uid and a.get("type") == "text" and a.get("content")]
        if text_assets:
            L.append("## Text content\n")
            for a in text_assets:
                L.append(f"### {a.get('name','Text')}")
                try:
                    L.append(html_to_text(a["content"]) if "<" in a["content"] else a["content"])
                except Exception:
                    L.append(a["content"])
                L.append("")

        # Quiz
        uqs = q_by_unit.get(uid, [])
        if uqs:
            L.append("## Quiz\n")
            for q in uqs:
                qt = q.get("name") or q.get("content") or ""
                L.append(f"- **Q:** {re.sub('<[^>]+>','',qt).strip()}")
                for c in ch_by_q.get(q.get("id"), []):
                    ct = re.sub("<[^>]+>", "", c.get("label") or "").strip()
                    mark = " ✓" if str(c.get("is_answer")) in ("1", "true", "True") else ""
                    if ct:
                        L.append(f"    - {ct}{mark}")
            L.append("")

        # Local files
        resources = sorted(by_unit.get(uid, []), key=lambda x: (x[3] not in base.READABLE, x[1].lower()))
        readable = [r for r in resources if r[3] in base.READABLE]
        images   = [r for r in resources if r[3] in ("png", "jpg", "jpeg")]
        other_media = [r for r in resources if r[3] in base.MEDIA and r[3] not in ("png","jpg","jpeg")]

        if readable:
            L.append("## Extracted resources (local files)\n")
        for aid, fn, path, ext in readable:
            a = assets.get(aid, {})
            L.append(f"### {a.get('name') or fn}")
            L.append(f"*Source file:* `{fn}`  ·  *type:* {a.get('type') or ext}\n")
            txt = (local_extract(path, ext) or "").strip()
            if len(txt) > MAX_CHARS:
                txt = txt[:MAX_CHARS] + "\n\n[...truncated...]"
            stats[ext] += 1
            L.append(txt if txt else "_[no extractable text]_")
            L.append("")

        # OCR of images
        ocr_imgs = []
        for aid, fn, path, ext in images:
            t = ocr_image_path(path).strip()
            if t and not t.startswith("[OCR") and len(t) > 15:
                ocr_imgs.append((fn, t))
        if ocr_imgs:
            L.append("## Image text (OCR)\n")
            for fn, t in ocr_imgs:
                stats["ocr_img"] += 1
                L.append(f"### `{fn}`")
                L.append(t)
                L.append("")

        # Remote resources (from cache)
        links = [a for a in assets.values()
                 if a.get("unit_id") == uid and (a.get("url") or "").startswith("http")]
        if links:
            L.append("## Fetched resources (external URLs)\n")
            for a in sorted(links, key=lambda x: x.get("name") or ""):
                url = a["url"]
                L.append(f"### {a.get('name','')} ({a.get('type','')})")
                L.append(f"*URL:* {url}\n")
                content = cache_get("fetch:" + url) or fetch_remote(url)
                if content and not content.startswith("["):
                    stats["remote_ok"] += 1
                L.append(content.strip() if content else "_[no content]_")
                L.append("")

        if other_media:
            L.append("## Non-text files (not extracted)\n")
            for _, fn, _, ext in other_media:
                L.append(f"- `{fn}` ({ext})")
            L.append("")

        open(os.path.join(OUTDIR, f"unit_{uid}__{slug}.md"), "w", encoding="utf-8").write("\n".join(L))
        written += 1
        if written % 20 == 0:
            print(f"  {written}/{len(all_units)} units written")

    print(f"\nDONE: {written} md files -> {OUTDIR}")
    print("Stats:", dict(sorted(stats.items(), key=lambda x: -x[1])))

if __name__ == "__main__":
    main()
