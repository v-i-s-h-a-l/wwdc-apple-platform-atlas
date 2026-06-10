---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Deep Dive Into The Foundation Models Framework
> Neutral research record for Apple WWDC 2025 session 301.

## Entries

- ID: `wwdc2025-301`
- Coverage: `metadata-only`
- Analysis status: `metadata-only`
- Apple video: https://developer.apple.com/videos/play/wwdc2025/301/
- Apple topics: AI & Machine Learning
- Platforms: ios, ipados, macos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Level up with the foundation models framework. learn how guided generation works under the hood, and use guides, regexes, and generation schemas to get custom structured responses. we'll show you how to use tool calling to let the model autonomously access external information and perform actions, for a personalized experience.   to get the most out of this video, we recommend first watching “meet the foundation models framework”.

### What Was Announced Or Covered

- Deep prerequisite for agentic and tool-heavy Foundation Models sessions.
- Covers session context, transcript behavior, generable types, guides, regex constraints, dynamic schemas, and tool calls.
- Apple groups this session under AI & Machine Learning; use it as source material for deep dive into the foundation models framework.
- level up with the foundation models framework. learn how guided generation works under the hood, and use guides, regexes, and generation schemas to get custom structured responses. we'll show you how to use tool calling to let the model autonomously access external information and perform actions, for a personalized experience.   to get the most out of this video, we recommend first watching “meet the foundation models framework”.
- Chapter coverage includes: Introduction; Sessions; Generable; Dynamic schemas; Tool calling.
- Metadata-derived capability tags: foundation model, tool calling.
- Treat this WWDC25 session as prerequisite context for understanding the WWDC26 changes, not as the newest API source.

### APIs And Concepts

- LanguageModelSession
- Generable
- Guide
- DynamicSchemas
- ToolCalls
- foundation model
- tool calling

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2025/301/4/955589c1-ae33-47db-9e86-2b87311dedb5/downloads/wwdc2025-301_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2025/301/4/955589c1-ae33-47db-9e86-2b87311dedb5/downloads/wwdc2025-301_sd.mp4?dl=1)

### Chapters

- Introduction
- Sessions
- Generable
- Dynamic schemas
- Tool calling

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
