#!/usr/bin/env python3
"""Build an explicit GitHub Pages artifact allowlist."""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_site"

ALLOWLIST = [
    "index.html",
    "session-atlas.html",
    "llms.txt",
    "llms-full.txt",
    "agent-router.json",
    "README.md",
    "CONSTITUTION.md",
    "AGENTS.md",
    "agent-corpus",
    "data/session-atlas.json",
    "docs/workflow",
    "templates/research-project.md",
]


def copy_item(rel: str) -> None:
    source = ROOT / rel
    target = OUT / rel
    if not source.exists():
        raise FileNotFoundError(rel)
    if source.is_dir():
        shutil.copytree(source, target, dirs_exist_ok=True)
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    for rel in ALLOWLIST:
        copy_item(rel)
    print(f"Built {OUT}")


if __name__ == "__main__":
    main()
