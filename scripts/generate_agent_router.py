#!/usr/bin/env python3
"""Generate compact AI-agent routing entry points."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "data" / "session-atlas.json"
MANIFEST = ROOT / "agent-corpus" / "manifest.json"

HOT_CONCEPT_ALIASES = {
    "appintentstesting": ["appintentstesting", "app intents testing", "validate app intents"],
    "plan-mode": ["plan mode", "/plan", "planning in xcode agents"],
    "prompt-injection": ["prompt injection", "indirect prompt injection", "agentic security"],
    "spotlight-search-tool": ["spotlightsearchtool", "spotlight search tool", "llm search", "core spotlight"],
    "languagemodelsession": ["languagemodelsession", "language model session", "foundation models session"],
    "string-catalogs": ["string catalogs", "stringcatalogs", "translation in xcode"],
    "swiftdata-query-sectioning": ["sectionby", "sectioned query", "swiftdata query", "swiftdata sectioning"],
    "private-cloud-compute": ["private cloud compute", "pcc", "server model"],
    "mlx-local-agents": ["local agentic ai", "mlx local", "opencode", "local mlx agents"],
    "device-hub": ["device hub", "devicectl", "simulators and devices"],
    "swift-testing": ["swift testing", "#expect", "#require", "migrate to swift testing"],
    "xcode-cloud": ["xcode cloud", "testflight distribution", "cloud workflows"],
    "foundation-models-tools": ["tool calling", "foundation models tools", "agentic app experiences"],
    "evaluations": ["evaluations framework", "hill-climbing", "agentic evaluations"],
    "metric-kit": ["metrickit", "metric kit", "state reporting", "statereporting"],
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def short_title(value: str, limit: int = 90) -> str:
    value = " ".join(str(value).split())
    return value if len(value) <= limit else value[: limit - 1].rstrip() + "…"


def corpus_path(path: str) -> str:
    return path if path.startswith("agent-corpus/") else f"agent-corpus/{path}"


def session_score(session: dict[str, Any], aliases: list[str]) -> int:
    haystack = " ".join(
        [
            session.get("title", ""),
            " ".join(session.get("topics", [])),
            " ".join(session.get("apiTerms", [])),
            " ".join(session.get("capabilityTerms", [])),
            " ".join(session.get("highlights", [])),
            " ".join(session.get("agentNotes", [])),
            session.get("description", ""),
        ]
    ).lower()
    score = 0
    for alias in aliases:
        if alias.lower() in haystack:
            score += 3 if " " in alias else 2
    if session.get("analysisStatus") == "transcript-derived":
        score += 2
    if session.get("curatedOverlay"):
        score += 1
    return score


def route_item(session: dict[str, Any], lookup: dict[str, Any]) -> dict[str, Any]:
    sid = f"wwdc{session['year']}-{session['id']}"
    item = lookup[sid]
    return {
        "id": sid,
        "title": item["title"],
        "path": item["path"],
        "coverage": item["coverage"],
        "url": item["url"],
    }


def build_hot_concept_routes(atlas: dict[str, Any], lookup: dict[str, Any]) -> dict[str, Any]:
    routes = {}
    for concept, aliases in HOT_CONCEPT_ALIASES.items():
        scored = [
            (session_score(session, aliases), session)
            for session in atlas["sessions"]
        ]
        matches = [session for score, session in sorted(scored, key=lambda item: (-item[0], item[1]["year"] != "2026", item[1]["title"])) if score > 0]
        routes[concept] = {
            "aliases": aliases,
            "best": [route_item(session, lookup) for session in matches[:3]],
        }
    return routes


def build_full_concept_routes(atlas: dict[str, Any], lookup: dict[str, Any]) -> dict[str, Any]:
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for session in atlas["sessions"]:
        sid = f"wwdc{session['year']}-{session['id']}"
        if sid not in lookup:
            continue
        terms = [
            *session.get("apiTerms", []),
            *session.get("capabilityTerms", []),
            *session.get("keywords", []),
        ]
        for term in terms:
            key = str(term).strip().lower()
            if len(key) < 3 or key in {"api", "apis", "wwdc", "apple"}:
                continue
            buckets[key].append(route_item(session, lookup))
    return {
        key: {
            "best": sorted(items, key=lambda item: (item["coverage"] != "deep-researched", item["title"]))[:5]
        }
        for key, items in sorted(buckets.items())
    }


def build_router(atlas: dict[str, Any], manifest: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    sessions = manifest["sessions"]
    features = manifest["features"]
    topics = manifest["topics"]

    by_topic = {item["title"]: item for item in topics}

    session_lookup = {
        item["id"]: {
            "title": item["title"],
            "coverage": item["coverage"],
            "path": corpus_path(item["path"]),
            "url": item["url"],
            "topics": item.get("topics", []),
            "researchPriority": item.get("researchPriority"),
            "researchWave": item.get("researchWave"),
        }
        for item in sessions
    }

    routes = {
        "feature-question": {
            "when": "The user asks whether a capability exists, what changed, or which sessions/docs are relevant.",
            "start": "agent-corpus/features/",
            "fallback": "agent-corpus/QUESTION_ROUTING.md",
        },
        "session-question": {
            "when": "The user asks about a specific WWDC video, session ID, or title.",
            "start": "agent-corpus/sessions/",
            "fallback": "agent-corpus/manifest.json",
        },
        "topic-question": {
            "when": "The user asks about an Apple topic group or broad area.",
            "start": "agent-corpus/topics/",
            "fallback": "agent-corpus/AGENT_INDEX.md",
        },
        "confidence-question": {
            "when": "The answer needs confidence, coverage, or whether deeper review happened.",
            "start": "agent-corpus/COVERAGE_STATUS.md",
            "fallback": "agent-corpus/RESEARCH_QUEUE.md",
        },
        "exact-api-question": {
            "when": "The user needs exact SDK symbols, signatures, or availability.",
            "start": "agent-corpus/docs/apple-documentation.md",
            "fallback": "Follow Apple documentation links from the relevant feature/session file.",
        },
    }

    topic_sessions: dict[str, list[str]] = defaultdict(list)
    for session in sessions:
        for topic in session.get("topics", []):
            topic_sessions[topic].append(session["id"])

    return {
        "schema": "agentic-research-router/v1",
        "corpus": "wwdc-apple-platform-research",
        "generatedFrom": {
            "atlas": "data/session-atlas.json",
            "manifest": "agent-corpus/manifest.json",
        },
        "entrypoints": {
            "llms": "llms.txt",
            "agentIndex": "agent-corpus/AGENT_INDEX.md",
            "questionRouting": "agent-corpus/QUESTION_ROUTING.md",
            "coverageStatus": "agent-corpus/COVERAGE_STATUS.md",
            "researchQueue": "agent-corpus/RESEARCH_QUEUE.md",
            "publicReader": "index.html",
        },
        "coverage": atlas["meta"]["coverage"],
        "routes": routes,
        "features": {
            item["id"]: {
                "title": item["title"],
                "path": corpus_path(item["path"]),
            }
            for item in features
        },
        "topics": {
            title: {
                "path": corpus_path(item["path"]),
                "sessionIds": topic_sessions.get(title, [])[:40],
            }
            for title, item in by_topic.items()
        },
        "prioritySessions": {
            sid: session
            for sid, session in session_lookup.items()
            if session.get("researchPriority")
        },
        "lookupFiles": {
            "fullSessionLookup": "agent-corpus/session-lookup.json",
            "fullConceptRoutes": "agent-corpus/concept-routes.json",
            "manifest": "agent-corpus/manifest.json",
        },
        "hotConceptRoutes": build_hot_concept_routes(atlas, session_lookup),
        "recommendedAgentPath": [
            "Read llms.txt.",
            "Use direct routes in llms.txt when they match.",
            "Use agent-router.json for ambiguous routing or hot concept aliases.",
            "Open the narrow feature/topic/session page.",
            "Check coverage before making strong claims.",
            "Follow Apple source links for exact API details.",
        ],
    }, session_lookup, build_full_concept_routes(atlas, session_lookup)


def write_llms(router: dict[str, Any]) -> None:
    coverage = router["coverage"]
    feature_lines = [
        f"- [{item['title']}]({item['path']}): feature route"
        for item in router["features"].values()
    ]
    topic_lines = [
        f"- [{title}]({item['path']}): topic route"
        for title, item in sorted(router["topics"].items())
    ]
    priority_lines = [
        f"- [{session['title']}]({session['path']}): {session.get('researchPriority')} / {session.get('researchWave')}"
        for session in router["prioritySessions"].values()
    ][:30]

    text = f"""# Agentic Research Router

> Static AI-agent-first research router for Apple WWDC platform research.

Use this file as the smallest entry point. Do not load the full corpus first.

## Routing Contract

1. For capability questions, use the direct Feature Routes below first.
2. For video-specific questions, open `agent-corpus/sessions/`.
3. For broad Apple topic questions, open `agent-corpus/topics/`.
4. For confidence, open `agent-corpus/COVERAGE_STATUS.md`.
5. For research gaps, open `agent-corpus/RESEARCH_QUEUE.md`.
6. For ambiguous concept/API questions, open `agent-router.json` and use `hotConceptRoutes`.
7. For exact API signatures, follow Apple documentation links from the relevant page.

## Coverage

- Sessions: `{coverage['totalSessionCount']}`
- WWDC26 sessions: `{coverage['wwdc26SessionCount']}`
- WWDC25 context sessions: `{coverage['wwdc25RelevantSessionCount']}`
- Deep-researched sessions: `{coverage['transcriptDerivedCount']}`
- Full transcript text stored: `0`

## Core Files

- [Machine router](agent-router.json): compact JSON routing graph and hot concept aliases.
- [Full session lookup](agent-corpus/session-lookup.json): complete session ID/title/path lookup.
- [Full concept routes](agent-corpus/concept-routes.json): larger concept-to-session lookup.
- [Agent index](agent-corpus/AGENT_INDEX.md): corpus overview.
- [Question routing](agent-corpus/QUESTION_ROUTING.md): natural-language routing.
- [Coverage status](agent-corpus/COVERAGE_STATUS.md): confidence boundaries.
- [Research queue](agent-corpus/RESEARCH_QUEUE.md): promoted and remaining work.
- [Public reader](index.html): human-facing reader.

## Feature Routes

{chr(10).join(feature_lines)}

## Topic Routes

{chr(10).join(topic_lines)}

## Priority Deep-Research Routes

{chr(10).join(priority_lines)}

## Source Policy

Full transcripts are not stored. The builder reads priority transcripts ephemerally and writes derived notes, source URLs, coverage labels, and routing metadata.
"""
    (ROOT / "llms.txt").write_text(text, encoding="utf-8")


def write_llms_full(router: dict[str, Any]) -> None:
    lines = [
        "# Agentic Research Router Full Context",
        "",
        "This compact file is for agents that want one fetch before routing into the corpus.",
        "",
        "## Recommended Path",
        "",
    ]
    lines.extend(f"- {step}" for step in router["recommendedAgentPath"])
    lines.extend(["", "## Features", ""])
    lines.extend(f"- {feature_id}: {item['title']} -> {item['path']}" for feature_id, item in router["features"].items())
    lines.extend(["", "## Priority Sessions", ""])
    for sid, session in router["prioritySessions"].items():
        lines.append(
            f"- {sid}: {short_title(session['title'])} -> {session['path']} "
            f"({session.get('researchPriority')}, {session.get('researchWave')}, {session['coverage']})"
        )
    lines.extend(["", "## Coverage", "", json.dumps(router["coverage"], indent=2)])
    (ROOT / "llms-full.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    atlas = load_json(ATLAS)
    manifest = load_json(MANIFEST)
    router, session_lookup, concept_routes = build_router(atlas, manifest)
    (ROOT / "agent-router.json").write_text(json.dumps(router, indent=2, ensure_ascii=False), encoding="utf-8")
    (ROOT / "agent-corpus" / "session-lookup.json").write_text(json.dumps(session_lookup, indent=2, ensure_ascii=False), encoding="utf-8")
    (ROOT / "agent-corpus" / "concept-routes.json").write_text(json.dumps(concept_routes, indent=2, ensure_ascii=False), encoding="utf-8")
    write_llms(router)
    write_llms_full(router)
    print(json.dumps({"router": "agent-router.json", "sessions": router["coverage"]["totalSessionCount"]}, indent=2))


if __name__ == "__main__":
    main()
