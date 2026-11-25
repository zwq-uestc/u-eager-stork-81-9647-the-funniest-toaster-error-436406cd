#!/usr/bin/env python3
"""The error message a kitchen toaster shows its owner when something goes wrong.

Writes exactly one line to entry.txt inside $MAKEFUN_OUTPUT_DIR
(or /output when that is not set).
"""

import os
import sys

MESSAGE = "ERROR 04: Bread inserted upside down. Toasted anyway. We both know how this ends."


def write_entry() -> int:
    out = os.getenv("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(MESSAGE)
    return 0


if __name__ == "__main__":
    sys.exit(write_entry())
