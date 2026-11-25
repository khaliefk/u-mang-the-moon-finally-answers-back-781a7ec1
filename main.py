#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun one-liner entry.

Writes a single line, the Moon replying at last to the wishes, howls
and late-night promises of everyone staring up at it, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Standard library only; no network, no secrets, no input files.
"""

import os

MAX_CHARS = 240

ENTRY = (
    "Four billion years of wishes, howls, and promises you'll change, "
    "and your best one is still 'please let him text back.' "
    "I move oceans. I can't move on from your ex for you."
)

if not 1 <= len(ENTRY) <= MAX_CHARS:
    raise ValueError(f"ENTRY must be 1-{MAX_CHARS} characters, got {len(ENTRY)}")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
