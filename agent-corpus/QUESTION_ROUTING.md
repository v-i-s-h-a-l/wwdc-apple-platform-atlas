---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Question Routing
> Neutral routing guide for finding the right WWDC research file.

## Entries

- "Was this announced?" -> Check `features/`, then the linked session files.
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

## Synthesis

### Routing Principle

Answer from the narrowest file that fits the question. Use a session file for video-specific questions, a feature file for capability questions, and a topic file for framework-level summaries. When a page is metadata-only, state that deeper review is needed before making strong claims.

## Small Observations (Don't Delete)

- Routing is descriptive, not an agent workflow.
- Prefer source-linked claims over broad synthesis.

<!-- docbot: end -->
