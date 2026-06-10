---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Meet Core AI
> Neutral research record for Apple WWDC 2026 session 324.

## Entries

- ID: `wwdc2026-324`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/324/
- Apple topics: AI & Machine Learning
- Platforms: ios, ipados, macos, watchos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Discover core ai, apple's new framework for on-device ai model deployment. tour the ecosystem, from python libraries for converting, authoring, and optimizing models, to a swift api for simple plug-and-play inference and advanced use cases with strict latency and memory requirements. explore the new core ai models repository with ready-to-run examples for popular architectures. see how deep xcode integration, including ahead-of-time model compilation, streamlines the workflow so you can deliver smarter, more responsive app experiences.

### What Was Announced Or Covered

- Apple groups this session under AI & Machine Learning; use it as source material for meet core ai.
- discover core ai, apple's new framework for on-device ai model deployment. tour the ecosystem, from python libraries for converting, authoring, and optimizing models, to a swift api for simple plug-and-play inference and advanced use cases with strict latency and memory requirements. explore the new core ai models repository with ready-to-run examples for popular architectures. see how deep xcode integration, including ahead-of-time model compilation, streamlines the workflow so you can deliver smarter, more responsive app experiences.
- Chapter coverage includes: Introduction; What is Core AI; Model conversion; App integration; Profiling with Instruments.
- Transcript-derived capability tags: agent, apple intelligence, core ai, foundation model, instruments, vision, xcode.
- API and framework terms to verify in SDK docs: AIModel, AIModelCache, API, APIs, CPU, GPU, LLM, MutableView, NDArray, NDArrays.
- Treat this WWDC26 session as the current primary source, then confirm exact API availability against installed SDK docs.

### APIs And Concepts

- AIModel
- AIModelCache
- LLM
- MutableView
- NDArray
- NDArrays
- agent
- apple intelligence
- core ai
- foundation model
- instruments
- vision
- xcode

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/324/4/3b67b624-4060-495f-9ba7-659805ee6b88/downloads/wwdc2026-324_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/324/4/3b67b624-4060-495f-9ba7-659805ee6b88/downloads/wwdc2026-324_sd.mp4?dl=1)

### Chapters

- Introduction
- What is Core AI
- Model conversion
- App integration
- Profiling with Instruments
- Optimizing performance
- Additional features
- Specialization

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
