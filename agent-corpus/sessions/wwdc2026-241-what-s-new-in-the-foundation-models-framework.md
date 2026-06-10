---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# What's New In The Foundation Models Framework
> Neutral research record for Apple WWDC 2026 session 241.

## Entries

- ID: `wwdc2026-241`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/241/
- Apple topics: AI & Machine Learning
- Platforms: ios, ipados, macos, tvos, visionos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Explore what's new in the foundation models framework. learn how to access private cloud compute, integrate third-party and open source models, and work with vision capabilities. discover context management apis, built-in semantic search, and powerful primitives for creating agentic experiences in your apps.

### What Was Announced Or Covered

- Apple groups this session under AI & Machine Learning; use it as source material for what’s new in the foundation models framework.
- explore what's new in the foundation models framework. learn how to access private cloud compute, integrate third-party and open source models, and work with vision capabilities. discover context management apis, built-in semantic search, and powerful primitives for creating agentic experiences in your apps.
- Chapter coverage includes: Introduction; New on-device model; Vision: image understanding; Private Cloud Compute; Model abstraction layer.
- Transcript-derived capability tags: agent, apple intelligence, core spotlight, evaluation, foundation model, mlx, privacy, tool calling, vision, xcode.
- API and framework terms to verify in SDK docs: API, APIs, BarcodeReaderTool, CGImage, CLI, CoreAILanguageModel, DynamicProfile, GPU, LLM, LLMs.
- Treat this WWDC26 session as the current primary source, then confirm exact API availability against installed SDK docs.

### APIs And Concepts

- BarcodeReaderTool
- CGImage
- CLI
- CoreAILanguageModel
- DynamicProfile
- LLM
- LLMs
- LanguageModel
- LanguageModelSession
- MLX
- MLXLanguageModel
- NSImage
- OAuth
- OCRTool
- PCC
- PrivateCloudComputeLanguageModel
- RAG
- SDK

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Privacy and security claims should be tied to Apple documentation, entitlement checks, and data-boundary decisions in the app design.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/241/6/900558cb-1997-490a-9aac-2461b209e578/downloads/wwdc2026-241_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/241/6/900558cb-1997-490a-9aac-2461b209e578/downloads/wwdc2026-241_sd.mp4?dl=1)

### Chapters

- Introduction
- New on-device model
- Vision: image understanding
- Private Cloud Compute
- Model abstraction layer
- Partner model integrations
- System tools: Vision and Spotlight
- Dynamic Profiles for agentic apps

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
