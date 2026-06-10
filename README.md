# WWDC Apple Platform Atlas

WWDC Apple Platform Atlas is a static, AI-agent-first research corpus for WWDC26 plus relevant WWDC25 Apple platform sessions and documentation.

The primary audience is not a human scrolling a website. The primary audience is an AI agent that needs to answer a focused question with the shortest reliable path to the right topic, session, documentation, and evidence.

This repository is the Apple/WWDC corpus implementation. The reusable protocol, schemas, and corpus-building conventions live in the sibling project `agentic-research-router`.

## Start Here

- `llms.txt`: compact entry point for AI agents.
- `agent-router.json`: machine-readable routing index.
- `agent-corpus/AGENT_INDEX.md`: corpus overview.
- `agent-corpus/QUESTION_ROUTING.md`: how to route common question types.
- `agent-corpus/RESEARCH_QUEUE.md`: deep-research priority map.
- `agent-corpus/COVERAGE_STATUS.md`: what is deeply researched versus metadata-only.
- `index.html`: public human reader for GitHub Pages.

## Corpus Goal

This repository should reduce the cost of research for agents.

An agent asking “what changed in SwiftData at WWDC26?” should not browse the web broadly. It should:

1. Read `llms.txt`.
2. Open `agent-router.json` or `agent-corpus/QUESTION_ROUTING.md`.
3. Route to `agent-corpus/features/swiftdata.md` or the specific session file.
4. Follow Apple source links only when exact API confirmation is needed.

## Corpus Layout

- `agent-corpus/sessions/`: one Markdown record per WWDC session.
- `agent-corpus/topics/`: Apple topic group routing pages.
- `agent-corpus/features/`: feature-level maps such as SwiftData, SwiftUI, Foundation Models, App Intents, Xcode agents, and Evaluations.
- `agent-corpus/docs/`: source documentation indexes.
- `agent-corpus/comparisons/`: comparison material for non-Apple context.
- `data/session-atlas.json`: normalized source data used to generate the corpus and reader.

## Public Reader

`index.html` is the GitHub Pages reader. It is useful for humans, but it is secondary to the agent corpus.

## Source Policy

Full Apple transcript bodies are not stored. Priority transcripts are read ephemerally by the builder and reduced into structured notes. Public artifacts store derived notes, source links, coverage labels, and routing metadata.

## Relationship To The Router Protocol

This corpus follows the Agentic Research Router pattern:

1. Collect official or primary sources.
2. Normalize them into `data/<corpus>.json`.
3. Generate compact routing files, feature pages, source maps, and coverage status.
4. Validate privacy, source policy, link shape, JSON, and token budgets.
5. Publish static artifacts through GitHub Pages.

Corpus-specific source collection, WWDC feature grouping, Apple documentation links, and generated session records live here. Reusable protocol guidance lives in the generic router repository and is mirrored only where this corpus needs local operating instructions.
