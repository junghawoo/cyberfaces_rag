#!/usr/bin/env python3
"""
Generate one summary markdown per REAL/ACTIVE course module from data.jsonl.

"Real/active" = not deleted (deleted_at is null), published (state == 1), and
not obvious test/placeholder junk (title heuristics). One file per surviving
row is written to ./summaries/<id>-<slug>.md, plus an INDEX.md.
"""
import json, os, re, html

DATA_FILE = "./data.jsonl"
OUT_DIR   = "./summaries"

# ---- junk / placeholder detection -----------------------------------------
JUNK_EXACT = {
    "demo", "trial", "abcd", "module", "cvdf", "df", "xzfg", "xgfg", "fhdjhfd",
    "ffffff", "dgshdgsh", "sdfdas", "wgerw", "dsfadsfds", "fgddgfs", "sdfdas",
    "my module", "my cool module", "new test module", "demo curriculum",
    "reference links", "hidden module test", "share your success story",
    "life is how you hike it",
}
_TEST_RE = re.compile(r"\btest\b", re.I)          # any standalone "test"

def is_junk(title: str) -> bool:
    t = (title or "").strip().lower()
    if not t:
        return True
    if t in JUNK_EXACT:
        return True
    if _TEST_RE.search(t):                          # test / test2 / cert test / luke test ...
        return True
    # short gibberish token with no vowels (xzfg, wgerw, fgddgfs, ...)
    if len(t) <= 9 and " " not in t and not re.search(r"[aeiou]", t):
        return True
    return False

def is_real_active(d: dict) -> bool:
    if d.get("deleted_at"):        # soft-deleted
        return False
    if d.get("state") != 1:        # unpublished / hidden
        return False
    if is_junk(d.get("title")):
        return False
    return True

# ---- text helpers ----------------------------------------------------------
_TAG = re.compile(r"<[^>]+>")
def clean_html(s: str) -> str:
    if not s:
        return ""
    s = html.unescape(s)
    s = _TAG.sub("", s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()

def parse_objectives(raw):
    if not raw:
        return []
    try:
        objs = json.loads(raw)
        return [o for o in objs if isinstance(o, str) and o.strip()]
    except Exception:
        return []

def kind(d: dict) -> str:
    if d.get("is_workshop"): return "Workshop"
    if d.get("is_course"):   return "Course"
    return "Module / Unit"

# ---- main ------------------------------------------------------------------
def main():
    rows = []
    with open(DATA_FILE, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))

    by_id = {d["id"]: d for d in rows}
    kept = [d for d in rows if is_real_active(d)]

    os.makedirs(OUT_DIR, exist_ok=True)
    index_lines = [
        "# CyberFaCES Module Summaries",
        "",
        f"{len(kept)} real/active modules (of {len(rows)} total rows). "
        "One markdown file per module in this directory.",
        "",
        "| id | title | type | description? |",
        "|----|-------|------|-------------|",
    ]

    written = 0
    for d in sorted(kept, key=lambda x: x["id"]):
        mid   = d["id"]
        title = (d.get("title") or "").strip()
        slug  = (d.get("slug") or "module").strip("-") or "module"
        desc  = clean_html(d.get("description"))
        objs  = parse_objectives(d.get("objectives"))
        parent = by_id.get(d.get("parent_id"))
        parent_title = parent.get("title") if parent else None

        md = [f"# {title}", ""]
        meta = [
            f"- **ID:** {mid}",
            f"- **Type:** {kind(d)}",
            f"- **Slug:** `{slug}`",
        ]
        if d.get("course_id"):
            meta.append(f"- **Course group (course_id):** {d['course_id']}")
        if parent_title:
            meta.append(f"- **Parent:** {parent_title} (id {d['parent_id']})")
        if d.get("level_id"):
            meta.append(f"- **Level:** {d['level_id']}")
        if d.get("length"):
            meta.append(f"- **Length:** {d['length']} min")
        meta.append(f"- **Created:** {d.get('created_at','?')}  ·  **Updated:** {d.get('updated_at','?')}")
        md += meta + [""]

        md.append("## Description")
        md.append(desc if desc else "_No description provided._")
        md.append("")

        if objs:
            md.append("## Objectives")
            md += [f"- {o}" for o in objs]
            md.append("")

        fname = f"{mid:03d}-{slug}.md"
        with open(os.path.join(OUT_DIR, fname), "w", encoding="utf-8") as fh:
            fh.write("\n".join(md).rstrip() + "\n")
        written += 1

        has_desc = "yes" if desc else "—"
        safe_title = title.replace("|", "\\|")
        index_lines.append(f"| {mid} | [{safe_title}]({fname}) | {kind(d)} | {has_desc} |")

    with open(os.path.join(OUT_DIR, "INDEX.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(index_lines) + "\n")

    print(f"total rows:       {len(rows)}")
    print(f"kept (real):      {len(kept)}")
    print(f"dropped (junk):   {len(rows)-len(kept)}")
    print(f"files written:    {written} module .md + INDEX.md -> {OUT_DIR}/")

if __name__ == "__main__":
    main()
