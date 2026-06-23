import json
import os
from dotenv import load_dotenv
from google import genai

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-2.5-pro"


def generate_synthetic_queries(course_title, course_description):
    """
    Calls Gemini to generate 3 realistic search queries for a given course.
    Returns a list of query strings, or [] on failure.
    """
    prompt = f"""You are an expert at understanding user search intent.
Below is a course title and description. Generate 3 realistic, slightly messy search queries
that a student might type into a search bar when looking for exactly this course.

Course Title: {course_title}
Course Description: {course_description}

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


def build_ground_truth_dataset(jsonl_file_path, output_csv_path):
    ground_truth_table = []

    with open(jsonl_file_path, "r") as file:
        documents = [json.loads(line) for line in file]

    for doc in documents[:]:
        doc_id = doc.get("id")
        title = doc.get("title")
        description = doc.get("description")

        print(f"Generating queries for: {title}...")

        synthetic_queries = generate_synthetic_queries(title, description)

        for query in synthetic_queries:
            ground_truth_table.append({
                "query": query,
                "document_id": doc_id,
                "relevance_score": 3,
                "source_llm": MODEL,
            })

    with open(output_csv_path, "w") as out_file:
        for row in ground_truth_table:
            out_file.write(json.dumps(row) + "\n")

    print(f"Successfully generated {len(ground_truth_table)} ground-truth pairs!")


build_ground_truth_dataset("../data.jsonl", "ground_truth_queries.jsonl")
