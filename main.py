#!/usr/bin/env python3
"""make.fun entry for news-image-20261123 (Python 3.13, standard library only).

The poster image is the entry.png beside this file; this program copies it
to /output/entry.png. Outside the grader's container, MAKEFUN_OUTPUT_DIR
stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

No network access. Every run writes exactly the same bytes.
"""
import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out_dir / "entry.png")
