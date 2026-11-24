#!/usr/bin/env python3
"""Dad Joke Showdown v2 — writes one dad joke to /output/entry.txt."""

import os

PART_A = "I told Dad the elevator stopped working. He sighed, 'Well, "
PART_B = "that's just another level of disappointment.'"
LINE = PART_A + PART_B


def main():
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
