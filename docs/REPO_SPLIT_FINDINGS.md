# Repository Split Findings

The original repository contained both the reusable routing protocol and this Apple platform corpus. They were split so agents can route faster and maintainers can evolve each part independently.

## Finding 1: Apple Questions Need Apple-Specific Routes

Questions about SwiftUI, SwiftData, Foundation Models, App Intents, Xcode agents, or Apple documentation should land in this repository, not in the generic protocol repo.

## Finding 2: Protocol Questions Need Domain-Neutral Docs

Questions about how to build a new corpus, define schemas, validate source policy, or publish static router artifacts should land in the generic protocol repo.

## Finding 3: Corpus Operations Are Source-Specific

This atlas needs Apple-specific refresh logic, Apple documentation checks, WWDC session grouping, coverage labels, and public reader behavior. Those concerns do not belong in the generic protocol.

## Finding 4: The Public Reader Is Secondary

The public reader is useful for inspection, but the primary surface is still the agent-readable corpus: `llms.txt`, `agent-router.json`, and `agent-corpus/`.

## Resulting Direction

- Keep this repository focused on Apple platform research.
- Keep the sibling protocol repository focused on reusable schemas and workflow.
- Use issues to track deep-research promotion, route quality, source freshness, and UI improvements.
- Keep all docs provider-agnostic.
