#!/usr/bin/env python3
"""Generate the one-line entry for The One-Line Laugh bounty."""

from pathlib import Path

ENTRY = "My smart fridge put me on a diet without asking — now the ice cream hides behind the vegetables and judges me in Celsius."

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(ENTRY)}")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
