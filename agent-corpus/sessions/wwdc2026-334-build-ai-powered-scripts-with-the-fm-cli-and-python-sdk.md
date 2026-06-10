---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Build AI-Powered Scripts With The FM CLI And Python SDK
> Neutral research record for Apple WWDC 2026 session 334.

## Entries

- ID: `wwdc2026-334`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/334/
- Apple topics: AI & Machine Learning
- Platforms: macos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Explore all the new ways to leverage apple foundation models on macos. the foundation models sdk for python lets you integrate with popular tooling and evaluation packages in the python ecosystem. find out how to use the brand new fm command introduced in macos 27 to streamline scripting, automate model workflows, and accelerate your development process.

### What Was Announced Or Covered

- Apple groups this session under AI & Machine Learning; use it as source material for build ai-powered scripts with the fm cli and python sdk.
- explore all the new ways to leverage apple foundation models on macos. the foundation models sdk for python lets you integrate with popular tooling and evaluation packages in the python ecosystem. find out how to use the brand new fm command introduced in macos 27 to streamline scripting, automate model workflows, and accelerate your development process.
- Chapter coverage includes: Introduction; Introducing the fm CLI and Python SDK; Command line tool; fm respond and structured output; Automating file management with fm.
- Transcript-derived capability tags: agent, evaluation, foundation model, structured output, tool calling, xcode.
- API and framework terms to verify in SDK docs: API, APIs, GitHub, JSON, LanguageModelSession, SDK, WWDC25.
- Treat this WWDC26 session as the current primary source, then confirm exact API availability against installed SDK docs.

### APIs And Concepts

- GitHub
- LanguageModelSession
- SDK
- WWDC25
- agent
- evaluation
- foundation model
- structured output
- tool calling
- xcode

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Privacy and security claims should be tied to Apple documentation, entitlement checks, and data-boundary decisions in the app design.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/334/4/65b71eea-f323-4f86-9096-889b6da91bdd/downloads/wwdc2026-334_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/334/4/65b71eea-f323-4f86-9096-889b6da91bdd/downloads/wwdc2026-334_sd.mp4?dl=1)

### Chapters

- Introduction
- Introducing the fm CLI and Python SDK
- Command line tool
- fm respond and structured output
- Automating file management with fm
- Python SDK
- Prompting, tool calling and guided generation
- Building an evaluation pipeline in Python

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
