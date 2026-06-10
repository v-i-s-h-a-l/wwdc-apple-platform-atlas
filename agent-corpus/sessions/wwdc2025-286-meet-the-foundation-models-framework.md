---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Meet The Foundation Models Framework
> Neutral research record for Apple WWDC 2025 session 286.

## Entries

- ID: `wwdc2025-286`
- Coverage: `metadata-only`
- Analysis status: `metadata-only`
- Apple video: https://developer.apple.com/videos/play/wwdc2025/286/
- Apple topics: AI & Machine Learning
- Platforms: ios, ipados, macos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Learn how to tap into the on-device large language model behind apple intelligence! this high-level overview covers everything from guided generation for generating swift data structures and streaming for responsive experiences, to tool calling for integrating data sources and sessions for context management. this session has no prerequisites.

### What Was Announced Or Covered

- Baseline for WWDC26 Foundation Models work: LanguageModelSession, guided generation, streaming, tools, transcripts, availability, and Instruments.
- Watch before WWDC26 Foundation Models, provider integrations, agentic apps, and agentic profiling sessions.
- Apple groups this session under AI & Machine Learning; use it as source material for meet the foundation models framework.
- learn how to tap into the on-device large language model behind apple intelligence! this high-level overview covers everything from guided generation for generating swift data structures and streaming for responsive experiences, to tool calling for integrating data sources and sessions for context management. this session has no prerequisites.
- Chapter coverage includes: Introduction; The model; Guided generation; Snapshot streaming; Tool calling.
- Metadata-derived capability tags: apple intelligence, foundation model, tool calling.
- Treat this WWDC25 session as prerequisite context for understanding the WWDC26 changes, not as the newest API source.

### APIs And Concepts

- FoundationModels
- LanguageModelSession
- Generable
- Guide
- ToolCalling
- Streaming
- apple intelligence
- foundation model
- tool calling

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2025/286/4/6f221dca-f35f-4dad-bfec-0ec0970849bb/downloads/wwdc2025-286_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2025/286/4/6f221dca-f35f-4dad-bfec-0ec0970849bb/downloads/wwdc2025-286_sd.mp4?dl=1)

### Chapters

- Introduction
- The model
- Guided generation
- Snapshot streaming
- Tool calling
- Stateful session
- Developer experience

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
