---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Debug And Profile Agentic App Experiences With Instruments
> Neutral research record for Apple WWDC 2026 session 243.

## Entries

- ID: `wwdc2026-243`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/243/
- Apple topics: AI & Machine Learning
- Platforms: ios, ipados, macos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Explore the enhanced foundationmodels instrument in xcode to inspect behavior and optimize the performance of agentic flows. learn how to inspect prompts, analyze latency, and trace control flow in advanced use cases that leverage multiple languagemodelsessions and profiles.

### What Was Announced Or Covered

- Foundation Models apps need observability because outputs are probabilistic and multi-model pipelines can hide slow or failing steps.
- The Foundation Models Instruments template shows instructions, prompts, responses, errors, sessions, requests, inferences, and tool calls.
- Important metrics include time-to-first-token, tokens-per-second, total latency, prompt size, model configuration, and streaming behavior.
- Traces may contain sensitive prompt data, so collection and sharing need privacy discipline.
- Apple groups this session under AI & Machine Learning; use it as source material for debug and profile agentic app experiences with instruments.
- explore the enhanced foundationmodels instrument in xcode to inspect behavior and optimize the performance of agentic flows. learn how to inspect prompts, analyze latency, and trace control flow in advanced use cases that leverage multiple languagemodelsessions and profiles.
- Chapter coverage includes: Introduction; LLM app development mindset; Inspect and diagnose an agentic experience; Recording a trace with Instruments; Navigating the Instruments UI.
- Transcript-derived capability tags: agent, evaluation, foundation model, instruments, xcode.

### APIs And Concepts

- FoundationModels
- Instruments
- TimeToFirstToken
- TokensPerSecond
- ToolCalls
- GenerateCraftIdeaTool
- GenerateCraftIdeasTool
- LLM
- LLMs
- SwitchToTutorialModeTool
- agent
- evaluation
- foundation model
- xcode

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Privacy and security claims should be tied to Apple documentation, entitlement checks, and data-boundary decisions in the app design.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/243/4/127c397a-8124-4f3d-ad18-ac2a1d275803/downloads/wwdc2026-243_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/243/4/127c397a-8124-4f3d-ad18-ac2a1d275803/downloads/wwdc2026-243_sd.mp4?dl=1)

### Chapters

- Introduction
- LLM app development mindset
- Inspect and diagnose an agentic experience
- Recording a trace with Instruments
- Navigating the Instruments UI
- Performance metrics
- Next steps

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
