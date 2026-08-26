#!/usr/bin/env python3

"""Count unwanted punctuation tokens in a JSONL file.

Tokens are counted as:
- words/numbers/underscores
- colons
- unwanted punctuation: quotation marks, commas, and curly braces

The script reports the number of unwanted tokens, the total token count,
and the fraction of unwanted tokens.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


TOKEN_RE = re.compile(r'[A-Za-z0-9_]+|:|["{},]')
UNWANTED_RE = re.compile(r'["{},]')


def count_tokens(text: str) -> tuple[int, int]:
    """Return (unwanted_tokens, total_tokens) for the given text."""

    tokens = TOKEN_RE.findall(text)
    unwanted = sum(1 for token in tokens if UNWANTED_RE.fullmatch(token))
    return unwanted, len(tokens)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Count unwanted punctuation tokens in a JSONL file."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default="data.jsonl",
        help="Path to the JSONL file (default: data.jsonl)",
    )
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    total_unwanted = 0
    total_tokens = 0

    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            unwanted, tokens = count_tokens(line)
            total_unwanted += unwanted
            total_tokens += tokens

    fraction = (total_unwanted / total_tokens) if total_tokens else 0.0

    print(f"unwanted_tokens: {total_unwanted}")
    print(f"total_tokens: {total_tokens}")
    print(f"fraction_unwanted: {fraction:.6f}")


if __name__ == "__main__":
    main()