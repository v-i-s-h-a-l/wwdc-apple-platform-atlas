#!/usr/bin/env python3
"""Validate public repository safety and routing contracts."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md",
    "CONSTITUTION.md",
    "AGENTS.md",
    "llms.txt",
    "llms-full.txt",
    "agent-router.json",
    "index.html",
    "data/session-atlas.json",
    "agent-corpus/AGENT_INDEX.md",
    "agent-corpus/QUESTION_ROUTING.md",
    "agent-corpus/COVERAGE_STATUS.md",
    "agent-corpus/RESEARCH_QUEUE.md",
    "agent-corpus/manifest.json",
    "docs/workflow/RESEARCH_SYSTEM.md",
    "docs/workflow/AGENT_CORPUS_DESIGN.md",
    "docs/workflow/DEEP_RESEARCH_PROTOCOL.md",
    "docs/workflow/SOURCE_POLICY.md",
    "docs/workflow/DAILY_OPERATIONS.md",
    "docs/workflow/PUBLICATION_CHECKLIST.md",
]

JSON_PATHS = [
    "agent-router.json",
    "data/session-atlas.json",
    "agent-corpus/manifest.json",
    "agent-corpus/session-lookup.json",
    "agent-corpus/concept-routes.json",
]

PRIVATE_PATTERNS = [
    r"poc\.turnip",
    r"\bturnip\b",
    r"v-i-s-h-a-l",
    r"/Users/",
    r"Documents/v-i-s-h-a-l",
    r"github/explorations",
    r"127\.0\.0\.1:8787",
    r"127\.0\.0\.1:\d+",
    r"localhost:\d+",
    r"ATLAS_AGENT_COMMAND",
    r"atlas_agent_launcher",
    r"Kimi WebBridge",
    r"private vault",
    r"gho_[A-Za-z0-9_]+",
]

TRANSCRIPT_PATTERNS = [
    r'id="transcript-content"',
    r"WEBVTT",
    r"\.webvtt",
]

SCAN_EXTENSIONS = {".md", ".txt", ".json", ".html", ".py", ".yml", ".yaml"}


def iter_public_files() -> list[Path]:
    files = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if ".git" in rel.parts:
            continue
        if rel.parts[:2] == ("sources", "cache"):
            continue
        if path.suffix.lower() in SCAN_EXTENSIONS:
            files.append(path)
    return files


def check_required(errors: list[str]) -> None:
    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).exists():
            errors.append(f"missing required path: {rel}")


def check_json(errors: list[str]) -> None:
    for rel in JSON_PATHS:
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing JSON path: {rel}")
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as error:  # noqa: BLE001
            errors.append(f"invalid JSON {rel}: {error}")


def check_source_policy(errors: list[str]) -> None:
    forbidden_paths = [
        "legacy-browser.html",
        "sources/apple-source-collection.json",
        "data/wwdc26-browser-data.json",
        "scripts/collect_apple_sources.py",
        "scripts/build_browser_data.py",
        "scripts/generate_browser_html.py",
    ]
    for rel in forbidden_paths:
        if (ROOT / rel).exists():
            errors.append(f"legacy or unsafe public artifact present: {rel}")

    for path in ROOT.rglob("*-transcript.txt"):
        errors.append(f"transcript cache file present: {path.relative_to(ROOT)}")

    atlas_path = ROOT / "data/session-atlas.json"
    if atlas_path.exists():
        atlas = json.loads(atlas_path.read_text(encoding="utf-8"))
        coverage = atlas.get("meta", {}).get("coverage", {})
        if coverage.get("totalSessionCount", 0) < 200:
            errors.append("session atlas has fewer than 200 sessions")
        if coverage.get("transcriptDerivedCount", 0) < 80:
            errors.append("session atlas has fewer than 80 deep-researched sessions")
        review_status = atlas.get("reviewStatus", {})
        if review_status.get("draft") is True:
            errors.append("session atlas reviewStatus still marks artifact as draft")
        for session in atlas.get("sessions", []):
            transcript = session.get("transcript", {})
            if isinstance(transcript, dict) and (transcript.get("text") or transcript.get("segments")):
                errors.append(f"raw transcript data present for {session.get('year')}-{session.get('id')}")


def check_patterns(errors: list[str]) -> None:
    private_regexes = [re.compile(pattern, re.I) for pattern in PRIVATE_PATTERNS]
    transcript_regexes = [re.compile(pattern) for pattern in TRANSCRIPT_PATTERNS]
    for path in iter_public_files():
        rel = path.relative_to(ROOT)
        if rel.as_posix() == "scripts/validate_public_repo.py":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for regex in private_regexes:
            if rel.parts[0] == "scripts" and regex.pattern in {r"127\.0\.0\.1:\d+", r"localhost:\d+"}:
                continue
            if regex.search(text):
                errors.append(f"private pattern {regex.pattern!r} in {rel}")
        if rel.parts[0] != "scripts":
            for regex in transcript_regexes:
                if regex.search(text):
                    errors.append(f"transcript cache marker {regex.pattern!r} in {rel}")


def check_router(errors: list[str]) -> None:
    router = json.loads((ROOT / "agent-router.json").read_text(encoding="utf-8"))
    required_keys = {"schema", "entrypoints", "routes", "features", "topics", "hotConceptRoutes", "lookupFiles"}
    missing = required_keys - set(router)
    if missing:
        errors.append(f"agent-router.json missing keys: {sorted(missing)}")
    if router.get("schema") != "agentic-research-router/v1":
        errors.append("agent-router.json schema mismatch")
    if not router.get("features"):
        errors.append("agent-router.json has no feature routes")
    if "sessionLookup" in router:
        errors.append("agent-router.json must not embed full sessionLookup; use agent-corpus/session-lookup.json")
    if not router.get("hotConceptRoutes"):
        errors.append("agent-router.json has no hot concept routes")


def main() -> int:
    errors: list[str] = []
    check_required(errors)
    check_json(errors)
    check_source_policy(errors)
    if (ROOT / "agent-router.json").exists():
        check_router(errors)
    check_patterns(errors)

    if errors:
        print("Public repo validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Public repo validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
