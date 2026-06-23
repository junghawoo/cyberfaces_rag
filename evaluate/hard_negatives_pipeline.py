import json
import os
import time
import numpy as np
from sentence_transformers import SentenceTransformer, util
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import ServerError, ClientError

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-2.5-flash"

retriever_model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

CHECKPOINT_PATH = "hard_negatives_checkpoint.jsonl"


def llm_consensus_judge(query, doc_title, doc_description, retries=5):
    """
    Calls Gemini Flash (no thinking) to judge relevance of a doc to a query.
    Returns an integer score 0-3. Retries on transient 503 errors.
    """
    prompt = f"""You are an expert search evaluator.
Given a user's search query and a retrieved course document, score how relevant the course is to the query.

Query: "{query}"

Course Title: "{doc_title}"
Course Description: "{doc_description}"

Score using this exact scale:
3 = Perfect match / Exact intent
2 = Highly relevant / Very useful
1 = Partially relevant / Tangential
0 = Irrelevant / Not what the user wants

Output ONLY a single integer (0, 1, 2, or 3). No explanation."""

    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(thinking_budget=0)
                ),
            )
            raw_score = response.text.strip()
            score = int(raw_score)
            if score in (0, 1, 2, 3):
                return score
        except ClientError as e:
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                print(f"\nDaily quota exhausted. Progress is saved — re-run after the quota resets.\n{e}")
                raise SystemExit(1)
            raise
        except ServerError as e:
            if attempt < retries - 1:
                wait = 2 ** attempt  # 1s, 2s, 4s, 8s, 16s
                print(f"  503 error, retrying in {wait}s... (attempt {attempt+1}/{retries})")
                time.sleep(wait)
            else:
                print(f"  Failed after {retries} attempts: {e}")
        except (ValueError, AttributeError):
            pass
    return 0


def load_checkpoint():
    """Returns a set of (query, document_id) pairs already processed."""
    done = set()
    if os.path.exists(CHECKPOINT_PATH):
        with open(CHECKPOINT_PATH, "r") as f:
            for line in f:
                row = json.loads(line)
                done.add((row["query"], str(row["document_id"])))
    return done


def build_hard_negatives_dataset(corpus_jsonl, synthetic_queries_jsonl, output_ground_truth_jsonl, top_k=10):
    print("Loading corpus...")
    corpus = []
    with open(corpus_jsonl, "r") as f:
        for line in f:
            corpus.append(json.loads(line))

    print(f"Embedding {len(corpus)} documents with all-mpnet-base-v2...")
    corpus_texts = [f"{doc.get('title', '')} {doc.get('description', '')}" for doc in corpus]
    corpus_embeddings = retriever_model.encode(corpus_texts, convert_to_tensor=True, show_progress_bar=True)

    print("Loading synthetic queries...")
    queries = []
    with open(synthetic_queries_jsonl, "r") as f:
        for line in f:
            queries.append(json.loads(line))

    unique_queries = list({q["query"]: q for q in queries}.values())

    # Resume from checkpoint
    done_pairs = load_checkpoint()
    if done_pairs:
        print(f"Resuming — {len(done_pairs)} pairs already done.")

    checkpoint_file = open(CHECKPOINT_PATH, "a")
    output_file = open(output_ground_truth_jsonl, "a")

    try:
        print(f"Retrieving and judging top-{top_k} docs per query ({len(unique_queries)} queries)...")
        for idx, item in enumerate(unique_queries):
            query_text = item["query"]
            print(f"[{idx+1}/{len(unique_queries)}] '{query_text}'")

            query_embedding = retriever_model.encode(query_text, convert_to_tensor=True)
            search_results = util.semantic_search(query_embedding, corpus_embeddings, top_k=top_k)[0]
            retrieved_ids = {corpus[r["corpus_id"]]["id"] for r in search_results}

            # Always include the source doc as a perfect match, even if outside top-k
            source_doc_id = item.get("document_id")
            if source_doc_id not in retrieved_ids:
                if (query_text, str(source_doc_id)) not in done_pairs:
                    source_doc = next((d for d in corpus if d["id"] == source_doc_id), None)
                    if source_doc:
                        row = {
                            "query": query_text,
                            "document_id": source_doc_id,
                            "relevance_score": 3,
                            "source": "perfect_match_forced",
                        }
                        checkpoint_file.write(json.dumps(row) + "\n")
                        checkpoint_file.flush()
                        output_file.write(json.dumps(row) + "\n")
                        output_file.flush()

            for result in search_results:
                retrieved_doc = corpus[result["corpus_id"]]
                doc_id = retrieved_doc["id"]

                if (query_text, str(doc_id)) in done_pairs:
                    continue

                if doc_id == source_doc_id:
                    score = 3
                    source = "perfect_match"
                else:
                    score = llm_consensus_judge(
                        query=query_text,
                        doc_title=retrieved_doc["title"],
                        doc_description=retrieved_doc["description"],
                    )
                    time.sleep(0.1)
                    source = "llm_judge"

                row = {
                    "query": query_text,
                    "document_id": doc_id,
                    "relevance_score": score,
                    "source": source,
                }
                checkpoint_file.write(json.dumps(row) + "\n")
                checkpoint_file.flush()
                output_file.write(json.dumps(row) + "\n")
                output_file.flush()
    finally:
        checkpoint_file.close()
        output_file.close()

    print(f"Done! Results saved to {output_ground_truth_jsonl}")


build_hard_negatives_dataset(
    corpus_jsonl="../data.jsonl",
    synthetic_queries_jsonl="ground_truth_queries.jsonl",
    output_ground_truth_jsonl="final_evaluation_dataset.jsonl",
)
