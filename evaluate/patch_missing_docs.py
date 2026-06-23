"""
One-off script to add the 3 docs that were missed because semantic search
never returned them in any query's top-10.
"""
import json

MISSING_IDS = {247, 303, 305}

# Collect queries generated from the missing docs
missing_rows = []
with open("ground_truth_queries.jsonl") as f:
    for line in f:
        row = json.loads(line)
        if row["document_id"] in MISSING_IDS:
            missing_rows.append({
                "query": row["query"],
                "document_id": row["document_id"],
                "relevance_score": 3,
                "source": "perfect_match_forced",
            })

print(f"Adding {len(missing_rows)} rows for doc IDs {MISSING_IDS}")

# Append to both output and checkpoint
for path in ("final_evaluation_dataset.jsonl", "hard_negatives_checkpoint.jsonl"):
    with open(path, "a") as f:
        for row in missing_rows:
            f.write(json.dumps(row) + "\n")

print("Done.")
