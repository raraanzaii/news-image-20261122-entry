#!/usr/bin/env python3
"""Entry program for make.fun's news-image-20261122 bounty.

The entry image is the front page in entry.png beside this file: "The Sunday
World", a one-image summary of Sunday 22 November 2026 built from that day's
wires (see README.md and build_image.py for how it was made and checked).
This program copies that image to /output/entry.png, byte for byte, so both
grader runs produce identical output. Standard library only, no network.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    # The gate reads exactly the bytes in the file and wants a whole image:
    # fail loudly rather than leave a truncated copy behind.
    if target.read_bytes() != SOURCE.read_bytes():
        raise SystemExit("copy verification failed: output differs from entry.png")


if __name__ == "__main__":
    main()
