---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Integrate On-Device AI Models Into Your App Using Core AI
> Neutral research record for Apple WWDC 2026 session 326.

## Entries

- ID: `wwdc2026-326`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/326/
- Apple topics: AI & Machine Learning
- Platforms: ios, ipados, macos, watchos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Discover a curated collection of popular open-source models — including qwen, mistral, sam3, and more — optimized for apple silicon using the new core ai framework. learn how to download, run, and benchmark models on your mac, and integrate them into your app with just a few lines of code. explore a new workflow for model compilation and on-device specialization to speed up first-time model load. find out how to profile and optimize runtime performance with core ai tools in xcode.

### What Was Announced Or Covered

- Apple groups this session under AI & Machine Learning; use it as source material for integrate on-device ai models into your app using core ai.
- discover a curated collection of popular open-source models — including qwen, mistral, sam3, and more — optimized for apple silicon using the new core ai framework. learn how to download, run, and benchmark models on your mac, and integrate them into your app with just a few lines of code. explore a new workflow for model compilation and on-device specialization to speed up first-time model load. find out how to profile and optimize runtime performance with core ai tools in xcode.
- Chapter coverage includes: Introduction; App concept: camera-based vocab learning; Model discovery; Getting models with the Core AI models repository; Integration.
- Transcript-derived capability tags: agent, core ai, foundation model, instruments, structured output, vision, xcode.
- API and framework terms to verify in SDK docs: API, APIs, CoreAILanguageModel, GitHub, LanguageModelSession, SAM, SAM3, URL.
- Treat this WWDC26 session as the current primary source, then confirm exact API availability against installed SDK docs.

### APIs And Concepts

- CoreAILanguageModel
- GitHub
- LanguageModelSession
- SAM
- SAM3
- agent
- core ai
- foundation model
- instruments
- structured output
- vision
- xcode

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/326/5/7ff038e2-12cb-4b92-9f49-1d051db7ce5d/downloads/wwdc2026-326_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/326/5/7ff038e2-12cb-4b92-9f49-1d051db7ce5d/downloads/wwdc2026-326_sd.mp4?dl=1)

### Chapters

- Introduction
- App concept: camera-based vocab learning
- Model discovery
- Getting models with the Core AI models repository
- Integration
- Writing the Swift integration code
- Diagnosing model specialization latency
- Deployment

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
