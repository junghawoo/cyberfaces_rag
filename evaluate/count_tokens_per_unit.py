#!/usr/bin/env python3

"""Count tokens per unit in evaluate/courses_md/*.md.

Tokenizes each unit's markdown body (YAML frontmatter excluded) with the
Alibaba-NLP/gte-large-en-v1.5 tokenizer and reports per-unit token counts
plus overall statistics.
"""

from __future__ import annotations

import argparse
import re
import statistics
from pathlib import Path

from transformers import AutoTokenizer

MODEL_NAME = "Alibaba-NLP/gte-large-en-v1.5"
FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
UNIT_ID_RE = re.compile(r"^unit_id:\s*(\d+)", re.MULTILINE)
FILENAME_UNIT_RE = re.compile(r"unit_(\d+)__")


def extract_unit_id(text: str, path: Path) -> int:
    match = UNIT_ID_RE.search(text)
    if match:
        return int(match.group(1))
    match = FILENAME_UNIT_RE.search(path.name)
    if match:
        return int(match.group(1))
    raise ValueError(f"Could not determine unit id for {path}")


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


def print_histogram(token_counts: list[int], bin_size: int) -> None:
    max_count = max(token_counts)
    num_bins = max_count // bin_size + 1
    bins = [0] * num_bins
    for token_count in token_counts:
        bins[token_count // bin_size] += 1

    max_bin_count = max(bins)
    scale = 50 / max_bin_count if max_bin_count > 50 else 1

    print()
    print(f"histogram (bin size = {bin_size} tokens):")
    for i, bin_count in enumerate(bins):
        if bin_count == 0:
            continue
        low = i * bin_size
        high = low + bin_size - 1
        bar = "#" * max(1, round(bin_count * scale))
        print(f"{low:>7}-{high:<7} {bin_count:>4}  {bar}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Count tokens per unit in evaluate/courses_md/*.md."
    )
    parser.add_argument(
        "courses_dir",
        nargs="?",
        default=Path(__file__).parent / "courses_md",
        type=Path,
        help="Directory containing unit markdown files (default: evaluate/courses_md)",
    )
    parser.add_argument(
        "--bin-size",
        type=int,
        default=500,
        choices=(500, 1000),
        help="Histogram bin size in tokens (default: 500)",
    )
    args = parser.parse_args()

    paths = sorted(args.courses_dir.glob("*.md"))
    if not paths:
        raise FileNotFoundError(f"No markdown files found in {args.courses_dir}")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)

    counts: list[tuple[int, int]] = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        unit_id = extract_unit_id(text, path)
        body = strip_frontmatter(text)
        token_count = len(tokenizer.encode(body))
        counts.append((unit_id, token_count))

    counts.sort()

    print(f"{'unit_id':>10}  {'tokens':>10}")
    for unit_id, token_count in counts:
        print(f"{unit_id:>10}  {token_count:>10}")

    token_counts = [c for _, c in counts]
    print()
    print(f"units: {len(token_counts)}")
    print(f"total_tokens: {sum(token_counts)}")
    print(f"average_tokens: {statistics.mean(token_counts):.2f}")
    print(f"median_tokens: {statistics.median(token_counts):.2f}")
    print(f"min_tokens: {min(token_counts)}")
    print(f"max_tokens: {max(token_counts)}")

    print_histogram(token_counts, args.bin_size)


if __name__ == "__main__":
    main()
