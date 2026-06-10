---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Build Agentic App Experiences With The Foundation Models Framework
> Neutral research record for Apple WWDC 2026 session 242.

## Entries

- ID: `wwdc2026-242`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/242/
- Apple topics: AI & Machine Learning
- Platforms: ios, ipados, macos, visionos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Learn how to take your intelligence features further with foundation models framework primitives for dynamic context and agentic workflows. we'll walk through engineering shared context, setting up privacy boundaries, and managing key value caching. discover how to orchestrate smooth handoffs between local and server models.

### What Was Announced Or Covered

- Apple groups this session under AI & Machine Learning; use it as source material for build agentic app experiences with the foundation models framework.
- learn how to take your intelligence features further with foundation models framework primitives for dynamic context and agentic workflows. we'll walk through engineering shared context, setting up privacy boundaries, and managing key value caching. discover how to orchestrate smooth handoffs between local and server models.
- Chapter coverage includes: Introduction; The example app and agents; Declaring a dynamic profile; Dynamic instructions; Configuring models per phase.
- Transcript-derived capability tags: agent, evaluation, foundation model, instruments, privacy, tool calling, xcode.
- API and framework terms to verify in SDK docs: API, APIs, DynamicProfile, LanguageModel, LanguageModelSession, LanguageModelsSession, PCC, PCCLanguageModel, PrivateCloudComputeLanguageModel, SystemLanguageModel.
- Treat this WWDC26 session as the current primary source, then confirm exact API availability against installed SDK docs.

### APIs And Concepts

- DynamicProfile
- LanguageModel
- LanguageModelSession
- LanguageModelsSession
- PCC
- PCCLanguageModel
- PrivateCloudComputeLanguageModel
- SystemLanguageModel
- agent
- evaluation
- foundation model
- instruments
- privacy
- tool calling
- xcode

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Privacy and security claims should be tied to Apple documentation, entitlement checks, and data-boundary decisions in the app design.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/242/4/7f05515d-be1a-43a0-9962-a1f77f115666/downloads/wwdc2026-242_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/242/4/7f05515d-be1a-43a0-9962-a1f77f115666/downloads/wwdc2026-242_sd.mp4?dl=1)

### Chapters

- Introduction
- The example app and agents
- Declaring a dynamic profile
- Dynamic instructions
- Configuring models per phase
- Transcript management and history transforms
- Custom modifiers
- Lifecycle modifiers and session properties

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
