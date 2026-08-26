import csv
import json
import collections


def load_queries(path):
    """Returns {document_id: [query1, query2, query3]} preserving file order."""
    grouped = collections.defaultdict(list)
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            grouped[row["document_id"]].append(row["query"])
    return grouped


def main():
    old = load_queries("ground_truth_queries-old.jsonl")
    new = load_queries("ground_truth_queries.jsonl")

    all_doc_ids = sorted(set(old) | set(new))

    with open("query_comparison.csv", "w", newline="") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["document_id", "old_query", "new_query"])

        for doc_id in all_doc_ids:
            old_queries = old.get(doc_id, [])
            new_queries = new.get(doc_id, [])
            row_count = max(len(old_queries), len(new_queries))

            for i in range(row_count):
                old_q = old_queries[i] if i < len(old_queries) else ""
                new_q = new_queries[i] if i < len(new_queries) else ""
                writer.writerow([doc_id, old_q, new_q])


if __name__ == "__main__":
    main()
