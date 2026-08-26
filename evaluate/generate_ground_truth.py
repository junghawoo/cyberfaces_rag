import glob
import json
import os
import re
from dotenv import load_dotenv
from google import genai
import yaml

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-2.5-pro"

SUMMARIES_DIR = os.path.join(os.path.dirname(__file__), "summaries")

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


def parse_summary_md(path):
    """
    Splits a unit_{id}__*.md file into its YAML frontmatter (dict) and
    markdown body (str, stripped). Returns ({}, full_content) if the file
    has no frontmatter block.
    """
    with open(path, "r") as f:
        content = f.read()

    match = FRONTMATTER_RE.match(content)
    if not match:
        return {}, content.strip()

    frontmatter_raw, body = match.groups()
    frontmatter = yaml.safe_load(frontmatter_raw) or {}
    return frontmatter, body.strip()


def generate_synthetic_queries(course_title, course_summary):
    """
    Calls Gemini to generate 3 realistic search queries for a given course.
    Returns a list of query strings, or [] on failure.
    """
    prompt = f"""You are an expert at understanding user search intent.
Below is a course title and a detailed summary of its content (derived from the
course's attached PDFs and Jupyter notebooks). Generate 3 realistic, slightly messy
search queries that a student might type into a search bar when looking for exactly
this course.

Course Title: {course_title}
Course Summary: {course_summary}

Output strictly as a JSON list of strings. Example: ["python basics", "how to code for beginners", "intro python module"]
Output ONLY the JSON list, no additional text."""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
    )
    raw_output = response.text.strip()

    # Strip markdown code fences if present
    if raw_output.startswith("```"):
        raw_output = raw_output.split("```")[1]
        if raw_output.startswith("json"):
            raw_output = raw_output[4:]
        raw_output = raw_output.strip()

    try:
        queries = json.loads(raw_output)
        if isinstance(queries, list):
            return queries
    except json.JSONDecodeError:
        pass
    return []


def build_ground_truth_dataset(summaries_dir, corpus_jsonl_path, output_jsonl_path):
    with open(corpus_jsonl_path, "r") as file:
        corpus_by_id = {doc["id"]: doc for doc in (json.loads(line) for line in file)}

    ground_truth_table = []
    summary_paths = sorted(glob.glob(os.path.join(summaries_dir, "unit_*.md")))

    for path in summary_paths:
        frontmatter, body = parse_summary_md(path)
        doc_id = frontmatter.get("unit_id")
        if doc_id is None:
            print(f"Skipping {path}: no unit_id in frontmatter")
            continue

        corpus_doc = corpus_by_id.get(doc_id)
        title = frontmatter.get("title") or (corpus_doc or {}).get("title")

        # Some units have no attached PDFs/notebooks, so their summary body is
        # empty (frontmatter + heading only) — fall back to data.jsonl's
        # short description for those.
        summary = body
        if not summary and corpus_doc:
            summary = corpus_doc.get("description") or ""

        if not summary:
            print(f"Skipping {title!r} (id={doc_id}): no content available")
            continue

        print(f"Generating queries for: {title} (id={doc_id})...")

        synthetic_queries = generate_synthetic_queries(title, summary)

        for query in synthetic_queries:
            ground_truth_table.append({
                "query": query,
                "document_id": doc_id,
                "relevance_score": 3,
                "source_llm": MODEL,
            })

    with open(output_jsonl_path, "w") as out_file:
        for row in ground_truth_table:
            out_file.write(json.dumps(row) + "\n")

    print(f"Successfully generated {len(ground_truth_table)} ground-truth pairs!")


if __name__ == "__main__":
    build_ground_truth_dataset(SUMMARIES_DIR, "../data.jsonl", "ground_truth_queries.jsonl")
