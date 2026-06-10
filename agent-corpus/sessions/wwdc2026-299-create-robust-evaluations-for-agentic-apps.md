---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Create Robust Evaluations For Agentic Apps
> Neutral research record for Apple WWDC 2026 session 299.

## Entries

- ID: `wwdc2026-299`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/299/
- Apple topics: AI & Machine Learning
- Platforms: ios, ipados, macos, visionos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Learn how to leverage advanced features of the evaluations framework to build robust evaluations for your app. explore evaluating flows with tool calling and dynamic conditions, and how to define what correct behavior means for your use case. discover how to generate synthetic data, use judges effectively, and validate your datasets for reliable results.

### What Was Announced Or Covered

- Apple groups this session under AI & Machine Learning; use it as source material for create robust evaluations for agentic apps.
- learn how to leverage advanced features of the evaluations framework to build robust evaluations for your app. explore evaluating flows with tool calling and dynamic conditions, and how to define what correct behavior means for your use case. discover how to generate synthetic data, use judges effectively, and validate your datasets for reliable results.
- Chapter coverage includes: Introduction; The dataset problem in BookTracker; Generating synthetic data with makeSamples; Customizing generation with SampleGenerator; Sampling strategies.
- Transcript-derived capability tags: agent, evaluation, foundation model, tool calling, vision, xcode.
- API and framework terms to verify in SDK docs: API, APIs, LanguageModelSession, PrivateCloudComputeLanguageModel, SearchBooksTool.
- Treat this WWDC26 session as the current primary source, then confirm exact API availability against installed SDK docs.

### APIs And Concepts

- LanguageModelSession
- PrivateCloudComputeLanguageModel
- SearchBooksTool
- agent
- evaluation
- foundation model
- tool calling
- vision
- xcode

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/299/4/ef9fbc06-fc78-4896-9848-0f0fe2e75fb9/downloads/wwdc2026-299_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/299/4/ef9fbc06-fc78-4896-9848-0f0fe2e75fb9/downloads/wwdc2026-299_sd.mp4?dl=1)

### Chapters

- Introduction
- The dataset problem in BookTracker
- Generating synthetic data with makeSamples
- Customizing generation with SampleGenerator
- Sampling strategies
- Validating synthetic samples
- Comparing evaluation results
- Tool calling and tool evaluations

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
