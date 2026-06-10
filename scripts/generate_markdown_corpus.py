#!/usr/bin/env python3
"""Generate a neutral Markdown research corpus from the WWDC Session Atlas."""

from __future__ import annotations

import json
import re
import shutil
from collections import defaultdict
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "session-atlas.json"
OUT = ROOT / "agent-corpus"


FEATURES: list[tuple[str, str, list[str]]] = [
    ("foundation-models", "Foundation Models", ["foundation model", "foundationmodels", "language model", "pcc", "private cloud compute"]),
    ("core-ai", "Core AI", ["core ai", "coreai", "aimodel", "custom model"]),
    ("app-intents-siri", "App Intents And Siri", ["app intents", "appintent", "siri", "shortcuts", "core spotlight", "spotlight"]),
    ("xcode-agents", "Xcode Agents And Developer Workflow", ["xcode agents", "agents in xcode", "coding intelligence", "device hub", "xcode cloud", "swift testing", "appintentstesting", "instruments", "metrickit", "devicectl"]),
    ("swiftui-ui-frameworks", "SwiftUI And UI Frameworks", ["swiftui", "uikit", "appkit", "textkit", "widgetkit", "activitykit"]),
    ("swiftdata", "SwiftData", ["swiftdata", "modelcontext", "query", "fetchdescriptor"]),
    ("evaluations", "Evaluations", ["evaluation", "evaluations", "judge", "hill-climbing"]),
    ("agentic-security", "Agentic Security", ["security", "privacy", "prompt injection", "confirmation", "tool calling"]),
    ("visual-intelligence", "Visual Intelligence And Image Understanding", ["visual intelligence", "image understanding", "vision", "image playground"]),
    ("mlx-local-models", "MLX And Local Models", ["mlx", "local agentic ai", "apple silicon"]),
    ("performance-observability", "Performance And Observability", ["instruments", "metrickit", "top functions", "performance", "profile"]),
    ("accessibility", "Accessibility", ["accessibility", "dynamic type", "assistive", "custom controls"]),
]

NOISY_TERMS = {
    "API",
    "APIs",
    "CPU",
    "GPU",
    "HTML",
    "HTTP",
    "IDs",
    "JSON",
    "PNG",
    "PRO",
    "URL",
    "URLs",
}


def load() -> dict[str, Any]:
    return json.loads(DATA.read_text(encoding="utf-8"))


def slug(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "untitled"


def title_case(value: str) -> str:
    replacements = {
        "ai": "AI",
        "ios": "iOS",
        "ipados": "iPadOS",
        "macos": "macOS",
        "tvos": "tvOS",
        "watchos": "watchOS",
        "visionos": "visionOS",
        "swiftui": "SwiftUI",
        "uikit": "UIKit",
        "appkit": "AppKit",
        "xcode": "Xcode",
        "wwdc": "WWDC",
        "mlx": "MLX",
        "llm": "LLM",
        "appintentstesting": "AppIntentsTesting",
        "grpc": "gRPC",
        "css": "CSS",
        "html": "HTML",
    }
    words = []
    for word in re.split(r"(\W+)", value):
        key = word.lower()
        words.append(replacements.get(key, word[:1].upper() + word[1:] if word else word))
    title = "".join(words)
    title = re.sub(r"([A-Za-z])['’]S\b", r"\1's", title)
    title = title.replace(" Fm ", " FM ")
    title = title.replace(" Cli", " CLI")
    title = title.replace(" Sdk", " SDK")
    title = title.replace(" Api", " API")
    title = title.replace(" Apis", " APIs")
    title = title.replace(" Llm", " LLM")
    return title


def sentence_case(value: str) -> str:
    value = md_escape(value)
    return value[:1].upper() + value[1:] if value else value


def md_escape(value: Any) -> str:
    return str(value or "").replace("\n", " ").strip()


def bullets(items: list[Any], limit: int = 8) -> str:
    clean_items = [md_escape(item) for item in items if md_escape(item)]
    if not clean_items:
        return "- None recorded in this corpus phase."
    return "\n".join(f"- {item}" for item in clean_items[:limit])


def clean_terms(items: list[str], limit: int = 28) -> list[str]:
    terms = []
    seen = set()
    for item in items:
        term = md_escape(item)
        if not term or term in NOISY_TERMS or len(term) < 3:
            continue
        key = term.lower()
        if key not in seen:
            terms.append(term)
            seen.add(key)
    return terms[:limit]


def links(items: list[dict[str, str]], limit: int = 10) -> str:
    clean_items = [item for item in items if item.get("url") and item.get("title")]
    if not clean_items:
        return "- None recorded in this corpus phase."
    return "\n".join(f"- [{md_escape(item['title'])}]({item['url']})" for item in clean_items[:limit])


def frontmatter(doc_type: str = "reference", max_words: int = 1600) -> str:
    return f"""---
type: {doc_type}
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: {max_words}
---
"""


def write_doc(path: Path, title: str, summary: str, entries: str, synthesis: str, observations: str, max_words: int = 1600) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    body = f"""{frontmatter(max_words=max_words)}
# {title}
> {summary}

## Entries

{entries.strip()}

## Synthesis

{synthesis.strip()}

## Small Observations (Don't Delete)

{observations.strip()}

<!-- docbot: end -->
"""
    path.write_text(body, encoding="utf-8")


def coverage(session: dict[str, Any]) -> str:
    return "deep-researched" if session.get("analysisStatus") == "transcript-derived" else "metadata-only"


def session_file_name(session: dict[str, Any]) -> str:
    return f"wwdc{session['year']}-{session['id']}-{slug(session['title'])}.md"


def session_path(session: dict[str, Any]) -> str:
    return f"sessions/{session_file_name(session)}"


def session_haystack(session: dict[str, Any]) -> str:
    fields = [
        session.get("title", ""),
        session.get("description", ""),
        " ".join(session.get("topics", [])),
        " ".join(session.get("keywords", [])),
        " ".join(session.get("apiTerms", [])),
        " ".join(session.get("capabilityTerms", [])),
        " ".join(session.get("highlights", [])),
    ]
    return " ".join(fields).lower()


def matched_sessions(sessions: list[dict[str, Any]], terms: list[str]) -> list[dict[str, Any]]:
    subset = [session for session in sessions if any(term in session_haystack(session) for term in terms)]
    return sorted(subset, key=lambda s: (s["year"] != "2026", coverage(s) != "deep-researched", s["title"]))


def write_session(session: dict[str, Any]) -> None:
    title = title_case(session["title"])
    cov = coverage(session)
    entries = f"""- ID: `wwdc{session['year']}-{session['id']}`
- Coverage: `{cov}`
- Analysis status: `{session.get('analysisStatus', 'unknown')}`
- Apple video: {session.get('url', '')}
- Apple topics: {", ".join(session.get("topics", [])) or "None recorded"}
- Platforms: {", ".join(session.get("platforms", [])) or "None recorded"}
- Transcript characters stored: `{session.get("transcriptStats", {}).get("storedCharacters", 0)}`
"""
    synthesis = f"""### One-Line Answer

{sentence_case(session.get("description") or "No Apple description was captured for this session.")}

### What Was Announced Or Covered

{bullets(session.get("highlights", []), 8)}

### APIs And Concepts

{bullets(clean_terms([*session.get("apiTerms", []), *session.get("capabilityTerms", [])], 18), 18)}

### Risks And Constraints

{bullets(session.get("risksAndConstraints", []), 6)}

### Related Apple Resources

{links(session.get("resources", []), 8)}

### Chapters

{bullets(session.get("chapterTopics", []) or [c.get("title", "") for c in session.get("chapters", [])], 10)}
"""
    observations = f"""- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims."""
    write_doc(OUT / session_path(session), title, f"Neutral research record for Apple WWDC {session['year']} session {session['id']}.", entries, synthesis, observations)


def write_topic(topic: str, sessions: list[dict[str, Any]]) -> str:
    path = f"topics/{slug(topic)}.md"
    deep = sum(1 for session in sessions if coverage(session) == "deep-researched")
    entries = "\n".join(
        f"- [{session['year']} {session['id']} - {title_case(session['title'])}](../{session_path(session)}) - `{coverage(session)}`"
        for session in sessions[:80]
    )
    api_terms = clean_terms(sorted({term for session in sessions for term in session.get("apiTerms", [])}), 40)
    synthesis = f"""### Coverage

- Sessions indexed: `{len(sessions)}`
- Deep researched: `{deep}`
- Metadata-only: `{len(sessions) - deep}`

### Recurring APIs And Concepts

{bullets(api_terms, 25)}

### Strongest Evidence Sessions

{bullets([f"{session['year']} {session['id']} - {title_case(session['title'])}" for session in sessions if coverage(session) == "deep-researched"], 12)}
"""
    observations = "- Use session files for video-level evidence.\n- Use feature files for cross-topic claims.\n- Coverage counts describe research depth, not Apple importance."
    write_doc(OUT / path, topic, f"Topic-level routing page for {topic}.", entries or "- No sessions recorded.", synthesis, observations)
    return path


def write_feature(feature_id: str, label: str, sessions: list[dict[str, Any]]) -> str:
    path = f"features/{feature_id}.md"
    deep = [s for s in sessions if coverage(s) == "deep-researched"]
    entries = "\n".join(
        f"- [{session['year']} {session['id']} - {title_case(session['title'])}](../{session_path(session)}) - `{coverage(session)}`"
        for session in sessions[:60]
    )
    claims = []
    for session in deep[:8]:
        for highlight in session.get("highlights", [])[:2]:
            if highlight.startswith("Apple groups this session under"):
                continue
            claims.append(f"{sentence_case(highlight)} Source: WWDC {session['year']} session {session['id']}.")
    synthesis = f"""### What This Page Can Answer

- Whether this feature area appears in the indexed WWDC corpus.
- Which sessions and Apple documentation links are relevant.
- Which claims are backed by deep-researched session notes versus metadata-only indexing.

### Evidence-Backed Claims

{bullets(claims, 12)}

### Related APIs And Concepts

{bullets(clean_terms(sorted({term for session in sessions for term in [*session.get("apiTerms", []), *session.get("capabilityTerms", [])]}), 28), 28)}
"""
    observations = "- This is a neutral feature page, not a recommendation to adopt the feature.\n- Prefer deep-researched sessions for strong answers.\n- Verify beta SDK names before turning research into code."
    write_doc(OUT / path, label, f"Feature-level research page for {label}.", entries or "- No matching sessions recorded.", synthesis, observations, max_words=2400)
    return path


def write_root_docs(data: dict[str, Any], topic_paths: dict[str, str], feature_paths: dict[str, str]) -> None:
    coverage_meta = data["meta"]["coverage"]
    entries = f"""- Public reader: `../index.html`
- Machine-readable atlas: `../data/session-atlas.json`
- Sessions: `{len(data['sessions'])}`
- WWDC26 sessions: `{coverage_meta['wwdc26SessionCount']}`
- Relevant WWDC25 context sessions: `{coverage_meta['wwdc25RelevantSessionCount']}`
- Deep-researched sessions: `{coverage_meta['transcriptDerivedCount']}`
- Topic pages: `{len(topic_paths)}`
- Feature pages: `{len(feature_paths)}`
"""
    synthesis = """### How To Use This Corpus

- Start with `QUESTION_ROUTING.md` for question type routing.
- Use `COVERAGE_STATUS.md` before trusting an answer as deeply researched.
- Use `sessions/` for video-specific evidence.
- Use `topics/` for Apple grouping and broad area questions.
- Use `features/` for "was this announced" and "what changed" questions.
- Use `manifest.json` for retrieval systems that prefer structured indexes.
- Use `RESEARCH_QUEUE.md` to understand promoted sessions and remaining metadata-only work.
"""
    observations = "- This corpus intentionally avoids prompts and execution checklists.\n- It stores derived notes only, not full transcript text.\n- The public HTML and private corpus serve different audiences."
    write_doc(OUT / "AGENT_INDEX.md", "WWDC Research Corpus Index", "Top-level map for the neutral WWDC research corpus.", entries, synthesis, observations)

    routing_entries = """- "Was this announced?" -> Check `features/`, then the linked session files.
- "What changed in a framework?" -> Check `topics/`, then relevant `features/`.
- "Which video should I watch?" -> Check the matching topic page and prefer deep-researched sessions.
- "What documentation is linked?" -> Check `docs/apple-documentation.md` and the session resource sections.
- "Can I trust this answer?" -> Check `COVERAGE_STATUS.md` and each file's coverage field.

### Common Focused Questions

- "What changed in SwiftData?" -> `features/swiftdata.md`, then `sessions/wwdc2026-274-what-s-new-in-swiftdata.md`.
- "Where is AppIntentsTesting covered?" -> `sessions/wwdc2026-295-validate-your-app-intents-adoption-with-appintentstesting.md`.
- "How do Xcode agents work?" -> `features/xcode-agents.md`, then `sessions/wwdc2026-259-xcode-agents-and-you.md`.
- "What is new in SwiftUI?" -> `features/swiftui-ui-frameworks.md`, then `sessions/wwdc2026-269-what-s-new-in-swiftui.md`.
- "How should prompt injection be handled?" -> `features/agentic-security.md`, then `sessions/wwdc2026-347-secure-your-app-mitigate-risks-to-agentic-features.md`.
- "How does local MLX agent work?" -> `features/mlx-local-models.md`, then `sessions/wwdc2026-232-run-local-agentic-ai-on-the-mac-using-mlx.md`.
- "Where is Private Cloud Compute covered?" -> `features/foundation-models.md`, then `sessions/wwdc2026-319-build-with-the-new-apple-foundation-model-on-private-cloud-compute.md`.
- "How do evaluations work?" -> `features/evaluations.md`, then `sessions/wwdc2026-298-meet-the-evaluations-framework.md`.
"""
    routing_synthesis = """### Routing Principle

Answer from the narrowest file that fits the question. Use a session file for video-specific questions, a feature file for capability questions, and a topic file for framework-level summaries. When a page is metadata-only, state that deeper review is needed before making strong claims.
"""
    write_doc(OUT / "QUESTION_ROUTING.md", "Question Routing", "Neutral routing guide for finding the right WWDC research file.", routing_entries, routing_synthesis, "- Routing is descriptive, not an agent workflow.\n- Prefer source-linked claims over broad synthesis.")

    deep_sessions = [s for s in data["sessions"] if coverage(s) == "deep-researched"]
    metadata_sessions = [s for s in data["sessions"] if coverage(s) == "metadata-only"]
    status_entries = f"""- Deep-researched sessions: `{len(deep_sessions)}`
- Metadata-only sessions: `{len(metadata_sessions)}`
- Stored transcript characters: `0`
- Deep-researched examples:
{bullets([f"{s['year']} {s['id']} - {title_case(s['title'])}" for s in deep_sessions], 20)}
"""
    status_synthesis = f"""### Metadata-Only Boundary

Metadata-only sessions are useful for discovery and routing, but they should not be treated as complete research notes. There are `{len(metadata_sessions)}` metadata-only sessions in this phase.

### Deep-Research Boundary

Deep-researched sessions were selected because they were high-value for AI, developer tools, SwiftUI/UI frameworks, App Intents, safety, testing, performance, accessibility, and platform workflows.
"""
    write_doc(OUT / "COVERAGE_STATUS.md", "Coverage Status", "Research-depth map for the corpus.", status_entries, status_synthesis, "- Coverage is a confidence signal, not a quality score.\n- Future phases should promote important metadata-only sessions after deeper review.")

    queued = sorted(
        [s for s in data["sessions"] if s.get("researchPriority")],
        key=lambda s: (s.get("researchPriority", "P9"), s.get("researchWave", ""), s["year"] != "2026", s["title"]),
    )
    remaining = sorted(
        [s for s in data["sessions"] if coverage(s) == "metadata-only" and not s.get("researchPriority")],
        key=lambda s: (s["year"] != "2026", s.get("topics", [""])[0] if s.get("topics") else "", s["title"]),
    )
    queued_entries = "\n".join(
        f"- `{session.get('researchPriority')}` {session.get('researchWave')}: "
        f"[{session['year']} {session['id']} - {title_case(session['title'])}]({session_path(session)}) "
        f"- `{coverage(session)}` - {md_escape(session.get('researchReason'))}"
        for session in queued
    )
    queue_synthesis = f"""### Promotion Model

Queued sessions are not an execution checklist. They are a research-depth map for deciding which metadata-only records should be promoted next and why. A promoted session should have transcript-derived notes, linked Apple resources, risks/constraints, API terms, and agent-facing implications.

### Current Wave Summary

- Queued/promoted sessions with explicit priority: `{len(queued)}`
- Remaining metadata-only sessions without explicit queue metadata: `{len(remaining)}`
- P0 sessions: `{sum(1 for session in queued if session.get('researchPriority') == 'P0')}`
- P1 sessions: `{sum(1 for session in queued if session.get('researchPriority') == 'P1')}`
- P2 sessions: `{sum(1 for session in queued if session.get('researchPriority') == 'P2')}`

### Remaining Metadata-Only Examples

{bullets([f"{s['year']} {s['id']} - {title_case(s['title'])}" for s in remaining], 30)}
"""
    queue_observations = "- Priority describes research sequencing, not Apple feature importance.\n- Keep the queue neutral and evidence-oriented.\n- Add queue metadata in the atlas builder before regenerating this file."
    write_doc(OUT / "RESEARCH_QUEUE.md", "Research Queue", "Prioritized map for promoting WWDC sessions from metadata-only to deep-researched coverage.", queued_entries or "- No queued sessions recorded.", queue_synthesis, queue_observations, max_words=4200)


def write_docs_and_comparisons(data: dict[str, Any]) -> None:
    doc_entries = "\n".join(f"- [{name}]({url})" for name, url in sorted(data.get("documentationIndex", {}).items()))
    doc_synthesis = "### Use\n\nUse these documentation links to verify SDK names, availability, and exact API signatures before turning research notes into code."
    write_doc(OUT / "docs/apple-documentation.md", "Apple Documentation Index", "Apple documentation links referenced by the WWDC corpus.", doc_entries or "- No documentation links recorded.", doc_synthesis, "- Documentation pages can change during beta season.\n- Prefer installed SDK docs for final API signatures.")

    comparison_entries = "\n".join(
        f"- {item['area']}: " + ", ".join(item.get("sources", []))
        for item in data.get("industryComparisons", [])
    )
    comparison_synthesis = "\n\n".join(
        f"### {item['area']}\n\n{item.get('agentUse', '')}"
        for item in data.get("industryComparisons", [])
    )
    write_doc(OUT / "comparisons/industry-comparison.md", "Industry Comparison Sources", "Neutral source map for comparing Apple announcements with industry model/tooling patterns.", comparison_entries or "- No comparison sources recorded.", comparison_synthesis or "No synthesis recorded.", "- This page is intentionally compact in phase 1.\n- Future work should add dated structured comparison tables.")


def build_manifest(data: dict[str, Any], topic_paths: dict[str, str], feature_paths: dict[str, str]) -> None:
    manifest = {
        "generatedAt": "2026-06-10",
        "corpusType": "neutral-research-corpus",
        "publicReader": "../index.html",
        "sourceData": "../data/session-atlas.json",
        "coverage": data["meta"]["coverage"],
        "indexes": {
            "agentIndex": "AGENT_INDEX.md",
            "questionRouting": "QUESTION_ROUTING.md",
            "coverageStatus": "COVERAGE_STATUS.md",
            "researchQueue": "RESEARCH_QUEUE.md",
            "documentation": "docs/apple-documentation.md",
            "industryComparison": "comparisons/industry-comparison.md",
        },
        "topics": [{"title": topic, "path": path} for topic, path in sorted(topic_paths.items())],
        "features": [{"id": feature_id, "title": title, "path": feature_paths[feature_id]} for feature_id, title, _ in FEATURES],
        "sessions": [
            {
                "id": f"wwdc{session['year']}-{session['id']}",
                "year": session["year"],
                "title": title_case(session["title"]),
                "coverage": coverage(session),
                "researchPriority": session.get("researchPriority"),
                "researchWave": session.get("researchWave"),
                "path": session_path(session),
                "url": session.get("url", ""),
                "topics": session.get("topics", []),
            }
            for session in data["sessions"]
        ],
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> None:
    data = load()
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    sessions = data["sessions"]
    for session in sessions:
        write_session(session)

    by_topic: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for session in sessions:
        for topic in session.get("topics", []) or ["Uncategorized"]:
            by_topic[topic].append(session)
    topic_paths = {topic: write_topic(topic, sorted(items, key=lambda s: (s["year"] != "2026", s["title"]))) for topic, items in sorted(by_topic.items())}

    feature_paths = {}
    for feature_id, label, terms in FEATURES:
        feature_paths[feature_id] = write_feature(feature_id, label, matched_sessions(sessions, terms))

    write_docs_and_comparisons(data)
    write_root_docs(data, topic_paths, feature_paths)
    build_manifest(data, topic_paths, feature_paths)
    print(json.dumps({"corpus": str(OUT), "sessions": len(sessions), "topics": len(topic_paths), "features": len(feature_paths)}, indent=2))


if __name__ == "__main__":
    main()
