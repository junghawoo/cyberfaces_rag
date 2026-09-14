#!/usr/bin/env python3
"""
Backfill missing descriptions in summaries/*.md using AnvilGPT (gpt-oss:120b).

- Targets ONLY kept modules whose summary .md still contains the
  "_No description provided._" placeholder (so re-runs fill remaining/failed ones).
- Grounds generation on the module title + its parent-course chain (no lesson
  text exists in the data, so this is an INFERRED description, labeled as such).
- Writes each .md as soon as its description returns -> partial progress is safe.
- Does NOT touch data.jsonl / the search corpus.
"""
import json, os, re, socket, sys, glob
import requests

DATA_FILE = "./data.jsonl"
OUT_DIR   = "./summaries"
PLACEHOLDER = "_No description provided._"
LABEL     = "_AI-generated (inferred from title — not authoritative catalog copy):_"
API_URL   = "https://anvilgpt.rcac.purdue.edu/api/chat/completions"
MODEL     = "gpt-oss:120b"
TIMEOUT   = 45
RETRIES   = 2

socket.setdefaulttimeout(TIMEOUT)

SYS_PROMPT = (
    "You are an academic curriculum assistant for the CyberFaCES cyber-training "
    "platform (topics: FAIR data, climate/water science, geospatial data processing, "
    "hydrology, HPC, Python, machine learning). Given a training module's title and "
    "its course context, write a concise 1-2 sentence description of what the module "
    "likely covers. Be factual and general; do NOT invent specific tools, datasets, "
    "numbers, or claims not implied by the title. Output only the description text."
)

def parent_chain(d, by_id):
    chain, seen = [], set()
    pid = d.get("parent_id")
    while pid and pid not in seen:
        seen.add(pid)
        p = by_id.get(pid)
        if not p:
            break
        chain.append(p.get("title") or "")
        pid = p.get("parent_id")
    return chain

def context_str(d, by_id):
    parts = [f"Module title: {d.get('title')}"]
    chain = parent_chain(d, by_id)
    if chain:
        parts.append("Part of: " + " > ".join(chain))
    if d.get("level_id"):
        parts.append(f"Level: {d['level_id']}")
    return "\n".join(parts)

def generate(api_key, context):
    body = {"model": MODEL, "temperature": 0, "stream": False,
            "messages": [{"role": "system", "content": SYS_PROMPT},
                         {"role": "user", "content": context}]}
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    last = None
    for attempt in range(RETRIES + 1):
        try:
            r = requests.post(API_URL, headers=headers, json=body, timeout=TIMEOUT)
            r.raise_for_status()
            txt = json.loads(r.text)["choices"][0]["message"]["content"].strip()
            txt = re.sub(r"\s+", " ", txt).strip().strip('"')
            if txt:
                return txt
        except Exception as e:
            last = e
    raise RuntimeError(f"generation failed after {RETRIES+1} tries: {last}")

def md_path_for(mid):
    hits = glob.glob(os.path.join(OUT_DIR, f"{mid:03d}-*.md"))
    return hits[0] if hits else None

def main():
    api = os.environ.get("ANVILGPT_API")
    if not api:
        sys.exit("ANVILGPT_API env var required")

    rows = [json.loads(l) for l in open(DATA_FILE, encoding="utf-8") if l.strip()]
    by_id = {d["id"]: d for d in rows}

    # find summary files still holding the placeholder
    targets = []
    for path in sorted(glob.glob(os.path.join(OUT_DIR, "*.md"))):
        if os.path.basename(path) == "INDEX.md":
            continue
        with open(path, encoding="utf-8") as fh:
            if PLACEHOLDER in fh.read():
                m = re.match(r"(\d+)-", os.path.basename(path))
                if m:
                    targets.append((int(m.group(1)), path))

    print(f"modules needing a description: {len(targets)}")
    done = fail = 0
    for i, (mid, path) in enumerate(targets, 1):
        d = by_id.get(mid)
        if not d:
            continue
        try:
            desc = generate(api, context_str(d, by_id))
        except Exception as e:
            fail += 1
            print(f"[{i}/{len(targets)}] id {mid} FAILED: {e}")
            continue
        with open(path, encoding="utf-8") as fh:
            content = fh.read()
        content = content.replace(PLACEHOLDER, f"{LABEL}\n\n{desc}")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
        done += 1
        if i % 10 == 0 or i == len(targets):
            print(f"[{i}/{len(targets)}] done={done} fail={fail}  (last id {mid})")

    print(f"\nfinished: {done} written, {fail} failed, {len(targets)-done-fail} skipped")
    if fail:
        print("re-run this script to retry only the failed ones (idempotent).")

if __name__ == "__main__":
    main()
