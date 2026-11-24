#!/usr/bin/env python3
"""Fortune in a Pot.

Writes one kind, funny fortune for a houseplant on the windowsill
to /output/entry.txt.

Python 3.13 standard library only. No network, no input files, no
arguments: the line is fixed in this file, so every run writes the
exact same bytes.

The line: this spring you will outgrow your windowsill, and your
keeper will swear they planned it all along. It reads like a
fortune (one sentence, a prediction about what is coming), it is
unmistakably about this plant in this window, it is kind (growth,
no doom or withering), and the joke lands on the keeper, who will
pretend the plant's success was their plan all along.
"""

import os
from pathlib import Path

LINE = "This spring you will outgrow your windowsill, and your keeper will swear they planned it all along."


def main() -> None:
    # Self-check against the competition gate before writing anything:
    # 1-120 characters, one line, not only whitespace.
    if not 1 <= len(LINE) <= 120:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-120")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(LINE, encoding="utf-8")
    # Read back and verify: the file must hold exactly the line, with
    # no trailing newline or other bytes added.
    if entry.read_text(encoding="utf-8") != LINE:
        raise ValueError("written entry does not match the fortune line")
    print(f"Wrote {len(LINE)} characters to {entry}")


if __name__ == "__main__":
    main()
