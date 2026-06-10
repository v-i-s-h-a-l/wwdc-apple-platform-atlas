---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Industry Comparison Sources
> Neutral source map for comparing Apple announcements with industry model/tooling patterns.

## Entries

- Structured outputs: https://platform.openai.com/docs/guides/structured-outputs, https://ai.google.dev/gemini-api/docs/structured-output
- Tool calling: https://platform.openai.com/docs/api-reference/responses/create, https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/overview/, https://ai.google.dev/gemini-api/docs/function-calling
- Local/private inference: https://developer.apple.com/documentation/foundationmodels, https://developer.apple.com/documentation/coreai, https://ml-explore.github.io/mlx/build/html/index.html

## Synthesis

### Structured outputs

Use Apple Generable/Guided Generation for Swift-native app flows; compare against provider JSON Schema when building cross-platform agents.

### Tool calling

Map Apple Tools and App Intents to narrow, typed, confirmable actions; avoid broad command tools unless isolated.

### Local/private inference

Prefer local/PCC routes for user-private context, then provider models when availability, model family, or cross-platform reach dominates.

## Small Observations (Don't Delete)

- This page is intentionally compact in phase 1.
- Future work should add dated structured comparison tables.

<!-- docbot: end -->
