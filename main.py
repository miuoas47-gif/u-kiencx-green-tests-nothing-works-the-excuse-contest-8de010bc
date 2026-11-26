#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Prints one original excuse for why all the tests pass while production
is on fire, and writes the same line to the output file.
"""

import os

# The excuse is built from its two halves so the punchline stays
# separate from the setup: the setup states the paradox, the tail
# names what the tests were actually mocking.
SETUP = "All 412 tests pass and production is on fire"
TAIL = "the tests were mocking the database, the network, and, apparently, us."
EM_DASH = "\u2014"


def build_line() -> str:
    return f"{SETUP} {EM_DASH} {TAIL}"


def write_output(line: str) -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)
    for name in ("output.txt", "entry.txt"):
        with open(os.path.join(output_dir, name), "w", encoding="utf-8") as f:
            f.write(line + "\n")


def main() -> int:
    line = build_line()
    print(line)
    write_output(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
