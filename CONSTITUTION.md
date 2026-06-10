# WWDC Apple Platform Atlas Constitution

This repository exists to make Apple platform and WWDC research cheaper and more reliable for AI agents.

## Primary User

The primary user is an AI agent operating under context, latency, and tool-call constraints. Humans should be able to inspect the output, but human browsing is not the main optimization target.

## Core Promise

Given a focused question, the repository should route an agent to the smallest useful set of files and source links.

Examples:

- “What was new in SwiftData at WWDC26?”
- “Which Apple session covers AppIntentsTesting?”
- “How should I verify agentic Siri integrations?”
- “Where did Apple discuss local MLX agents?”
- “What sessions are still metadata-only?”

## Non-Negotiables

- Agent-first routing beats visual polish.
- Source links must be preserved.
- Coverage status must be explicit.
- Full transcript text must not be stored.
- Public artifacts must not contain local paths, private project names, or helper ports.
- Generated files should be reproducible from normalized data.
- Human summaries must not hide confidence boundaries.

## Agent Routing Principles

1. Start with the smallest entry point.
2. Prefer structured indexes over prose.
3. Prefer feature pages for capability questions.
4. Prefer session pages for video-specific claims.
5. Prefer source documentation for exact API signatures.
6. Prefer coverage status before making strong claims.
7. State when a session is metadata-only.

## Token Budget Principles

- Root files should be compact.
- Every page should have a stable title, summary, entries, synthesis, and observations.
- Avoid duplicate long prose across pages.
- Use IDs, slugs, topic labels, and coverage fields consistently.
- Let agents retrieve narrow files instead of loading the whole corpus.

## Bigger Vision

This is a static Apple platform research corpus built with the Agentic Research Router pattern.

The larger version of the corpus can route agents through:

- WWDC videos
- Apple documentation sets
- framework release notes
- SDK migration notes
- App Store and distribution guidance
- Apple Intelligence and Foundation Models references
- safety and privacy references

The output should remain static, inspectable, forkable, and easy to host.
