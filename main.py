#!/usr/bin/env python3
"""The Printer Apology -- make.fun entry.

Writes one apology line from an office printer (1-120 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Python 3.13, standard library only,
deterministic: the same line on every run.
"""

import os

ENTRY = (
    "I'm sorry I jammed on the last page. You fed me cheap paper, "
    "swore in three languages, then asked for colour anyway."
)


def main() -> None:
    # Self-check against the sealed gate: 1-120 chars, one line.
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY, "no leading/trailing whitespace"
    assert "\n" not in ENTRY, "must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
