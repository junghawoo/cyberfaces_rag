"""
Extract readable course resources (PDF, PPTX, DOCX, notebooks, etc.) into one
structured Markdown file per course unit.

Source of truth for FILES is the on-disk courses directory:
    courses/<unit_id>/<asset_id>/<filename>   (or courses/<unit_id>/<filename>)
Metadata (unit title/description/objectives, asset names, levels, links) comes
from the MySQL dump (dump.sql).

Output: courses_md/unit_<id>__<slug>.md
"""

import os, re, io, json, sys, subprocess
from collections import defaultdict

DUMP   = "/Users/shubham/Downloads/cyberfaces-dump-dev/dump.sql"
COURSES = "/Users/shubham/Desktop/RCAC/cyberfaces_rag/courses"
OUTDIR  = "/Users/shubham/Desktop/RCAC/cyberfaces_rag/courses_md"

READABLE = {"pdf", "pptx", "ppt", "docx", "doc", "ipynb", "md", "txt", "csv", "vtt", "xlsx", "pages"}
MEDIA    = {"png", "jpg", "jpeg", "gif", "svg", "mp4", "mov", "zip", "cmf", "ds_store"}
MAX_CHARS = 400_000  # per-resource safety cap


# --------------------------- robust MySQL dump parser ------------------------

def parse_insert(table, sql):
    """Return list of rows (each a list of Python values) for `INSERT INTO table`.
    Handles MySQL backslash escaping and quoted strings containing commas/parens."""
    m = re.search(r"INSERT INTO `%s` VALUES\s*(.*?);\s*\n" % re.escape(table), sql, re.S)
    if not m:
        return []
    s = m.group(1)
    rows, i, n = [], 0, len(s)
    while i < n:
        if s[i] != "(":
            i += 1
            continue
        # parse one tuple starting at "("
        i += 1
        vals, cur, in_str = [], [], False
        while i < n:
            c = s[i]
            if in_str:
                if c == "\\" and i + 1 < n:          # backslash escape
                    nxt = s[i + 1]
                    cur.append({"n": "\n", "t": "\t", "r": "\r", "0": "\0"}.get(nxt, nxt))
                    i += 2
                    continue
                if c == "'":
                    if i + 1 < n and s[i + 1] == "'":  # '' -> literal '
                        cur.append("'"); i += 2; continue
                    in_str = False; i += 1; continue
                cur.append(c); i += 1; continue
            else:
                if c == "'":
                    in_str = True; i += 1; continue
                if c == ",":
                    vals.append("".join(cur).strip()); cur = []; i += 1; continue
                if c == ")":
                    vals.append("".join(cur).strip()); i += 1; break
                cur.append(c); i += 1; continue
        # normalize raw (unquoted) NULLs
        rows.append([None if v == "NULL" else v for v in vals])
        # skip to next tuple
        while i < n and s[i] not in "(":
            i += 1
    return rows


def cols_of(table, sql):
    m = re.search(r"CREATE TABLE `%s` \((.*?)\) ENGINE" % re.escape(table), sql, re.S)
    return [c.split("`")[1] for c in m.group(1).split("\n") if c.strip().startswith("`")]


def load_db():
    sql = open(DUMP, encoding="utf-8", errors="replace").read()
    def as_dicts(table):
        cols = cols_of(table, sql)
        return [dict(zip(cols, r)) for r in parse_insert(table, sql)]
    units  = {u["id"]: u for u in as_dicts("course_units")}
    assets = {a["id"]: a for a in as_dicts("course_assets")}
    levels = {l["id"]: l for l in as_dicts("course_levels")}
    return units, assets, levels


# ------------------------------- extractors ----------------------------------

def extract_pdf(path):
    import fitz
    doc = fitz.open(path)
    out = [page.get_text().strip() for page in doc]
    doc.close()
    return "\n\n".join(t for t in out if t)

def extract_pptx(path):
    from pptx import Presentation
    prs = Presentation(path)
    chunks = []
    for i, slide in enumerate(prs.slides, 1):
        parts = []
        for shape in slide.shapes:
            if shape.has_text_frame and shape.text_frame.text.strip():
                parts.append(shape.text_frame.text.strip())
            if shape.has_table:
                for row in shape.table.rows:
                    parts.append(" | ".join(c.text for c in row.cells))
        if slide.has_notes_slide and slide.notes_slide.notes_text_frame:
            note = slide.notes_slide.notes_text_frame.text.strip()
            if note:
                parts.append("[Speaker notes] " + note)
        if parts:
            chunks.append(f"### Slide {i}\n" + "\n".join(parts))
    return "\n\n".join(chunks)

def extract_docx(path):
    import docx
    d = docx.Document(path)
    parts = [p.text for p in d.paragraphs if p.text.strip()]
    for t in d.tables:
        for row in t.rows:
            parts.append(" | ".join(c.text for c in row.cells))
    return "\n".join(parts)

def extract_ipynb(path):
    nb = json.load(open(path, encoding="utf-8", errors="replace"))
    out = []
    for cell in nb.get("cells", []):
        src = "".join(cell.get("source", []))
        if not src.strip():
            continue
        if cell.get("cell_type") == "code":
            out.append("```python\n" + src + "\n```")
        else:
            out.append(src)
    return "\n\n".join(out)

def extract_xlsx(path):
    import openpyxl
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    out = []
    for ws in wb.worksheets:
        out.append(f"### Sheet: {ws.title}")
        for row in ws.iter_rows(values_only=True):
            cells = [str(c) for c in row if c is not None]
            if cells:
                out.append(" | ".join(cells))
    wb.close()
    return "\n".join(out)

def extract_textutil(path):
    """macOS built-in converter for legacy .doc / .pages."""
    try:
        r = subprocess.run(["textutil", "-convert", "txt", "-stdout", path],
                           capture_output=True, timeout=60)
        return r.stdout.decode("utf-8", "replace").strip()
    except Exception as e:
        return f"[textutil failed: {e}]"

def extract_plain(path):
    return open(path, encoding="utf-8", errors="replace").read()

def extract(path, ext):
    try:
        if ext == "pdf":   return extract_pdf(path)
        if ext == "pptx":  return extract_pptx(path)
        if ext == "docx":  return extract_docx(path)
        if ext == "ipynb": return extract_ipynb(path)
        if ext == "xlsx":  return extract_xlsx(path)
        if ext in ("doc", "pages"): return extract_textutil(path)
        if ext in ("md", "txt", "csv", "vtt"): return extract_plain(path)
    except Exception as e:
        return f"[extraction error: {type(e).__name__}: {e}]"
    return "[unsupported]"


# --------------------------------- build -------------------------------------

def slugify(s):
    s = (s or "unit").lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60] or "unit"

def fm_escape(s):
    return (s or "").replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").strip()

def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    units, assets, levels = load_db()
    os.makedirs(OUTDIR, exist_ok=True)

    # walk disk -> group files by unit_id
    by_unit = defaultdict(list)   # unit_id -> [(asset_id, filename, path, ext)]
    for root, _, files in os.walk(COURSES):
        for fn in files:
            if fn == ".DS_Store":
                continue
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, COURSES).split(os.sep)
            unit_id = rel[0]
            asset_id = rel[1] if len(rel) == 3 and rel[1].isdigit() else None
            ext = fn.rsplit(".", 1)[-1].lower() if "." in fn else ""
            by_unit[unit_id].append((asset_id, fn, path, ext))

    unit_ids = sorted(by_unit, key=lambda x: int(x) if x.isdigit() else 1e9)
    if limit:
        unit_ids = unit_ids[:limit]

    stats = defaultdict(int)
    written = 0
    for uid in unit_ids:
        u = units.get(uid, {})
        title = u.get("title") or f"Unit {uid}"
        slug = u.get("slug") or slugify(title)
        level = levels.get(u.get("level_id"), {}).get("title", "")
        objectives = u.get("objectives")
        try:
            obj_list = json.loads(objectives) if objectives and objectives.startswith("[") else []
        except Exception:
            obj_list = []

        lines = []
        # front matter
        lines.append("---")
        lines.append(f'title: "{fm_escape(title)}"')
        lines.append(f"unit_id: {uid}")
        if u.get("course_id"): lines.append(f"course_id: {u['course_id']}")
        if level: lines.append(f'level: "{fm_escape(level)}"')
        if u.get("slug"): lines.append(f"slug: {u['slug']}")
        if u.get("is_course"): lines.append(f"is_course: {u['is_course']}")
        if obj_list:
            lines.append("objectives:")
            for o in obj_list:
                lines.append(f'  - "{fm_escape(o)}"')
        lines.append("---\n")

        lines.append(f"# {title}\n")
        if u.get("description"):
            lines.append(f"**Description:** {u['description'].strip()}\n")
        if u.get("markdown_content"):
            lines.append("## Module content\n")
            lines.append(u["markdown_content"].strip() + "\n")

        # resources present on disk
        resources = sorted(by_unit[uid], key=lambda x: (x[3] not in READABLE, x[1].lower()))
        readable = [r for r in resources if r[3] in READABLE]
        media    = [r for r in resources if r[3] in MEDIA]
        other    = [r for r in resources if r[3] not in READABLE and r[3] not in MEDIA]

        if readable:
            lines.append("## Extracted resources\n")
        for asset_id, fn, path, ext in readable:
            a = assets.get(asset_id, {})
            aname = a.get("name") or fn
            atype = a.get("type") or ext
            lines.append(f"### {aname}")
            lines.append(f"*Source file:* `{fn}`  ·  *type:* {atype}\n")
            text = extract(path, ext) or ""
            if len(text) > MAX_CHARS:
                text = text[:MAX_CHARS] + f"\n\n[...truncated at {MAX_CHARS} chars...]"
            stats[ext] += 1
            lines.append(text.strip() if text.strip() else "_[no extractable text]_")
            lines.append("")

        # linked (remote) resources for this unit, from DB (no fetching)
        links = [a for a in assets.values()
                 if a.get("unit_id") == uid and (a.get("url") or "").startswith("http")]
        if links:
            lines.append("## Linked resources (external URLs)\n")
            for a in sorted(links, key=lambda x: x.get("name") or ""):
                lines.append(f"- **{a.get('name','')}** ({a.get('type','')}): {a['url']}")
            lines.append("")

        if media or other:
            lines.append("## Non-text files (not extracted)\n")
            for _, fn, _, ext in media + other:
                lines.append(f"- `{fn}` ({ext})")
            lines.append("")

        out_path = os.path.join(OUTDIR, f"unit_{uid}__{slug}.md")
        open(out_path, "w", encoding="utf-8").write("\n".join(lines))
        written += 1
        if written % 20 == 0:
            print(f"  {written}/{len(unit_ids)} units written")

    print(f"\nDONE: wrote {written} unit markdown files to {OUTDIR}")
    print("Extracted files by type:", dict(sorted(stats.items(), key=lambda x: -x[1])))

if __name__ == "__main__":
    main()
