---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Bring An LLM Provider To The Foundation Models Framework
> Neutral research record for Apple WWDC 2026 session 339.

## Entries

- ID: `wwdc2026-339`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/339/
- Apple topics: AI & Machine Learning
- Platforms: ios, ipados, macos, visionos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Extend the foundation models framework by implementing a languagemodelexecutor for new models. explore how to interface with the languagemodelsession's transcript, manage session state effectively, and optimize kv cache utilization. find out how to support custom segment types and unlock advanced capabilities for your generative ai features.

### What Was Announced Or Covered

- Apple groups this session under AI & Machine Learning; use it as source material for bring an llm provider to the foundation models framework.
- extend the foundation models framework by implementing a languagemodelexecutor for new models. explore how to interface with the languagemodelsession's transcript, manage session state effectively, and optimize kv cache utilization. find out how to support custom segment types and unlock advanced capabilities for your generative ai features.
- Chapter coverage includes: Introduction; Packaging; Protocol; Authentication; Customization.
- Transcript-derived capability tags: agent, apple intelligence, core ai, foundation model, mlx, privacy, structured output, vision, xcode.
- API and framework terms to verify in SDK docs: ANE, API, EXECutor, EXECutors, IDs, LLM, LanguageModel, LanguageModelSession, MLX, PCC.
- Treat this WWDC26 session as the current primary source, then confirm exact API availability against installed SDK docs.

### APIs And Concepts

- ANE
- EXECutor
- EXECutors
- LLM
- LanguageModel
- LanguageModelSession
- MLX
- PCC
- agent
- apple intelligence
- core ai
- foundation model
- privacy
- structured output
- vision
- xcode

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Privacy and security claims should be tied to Apple documentation, entitlement checks, and data-boundary decisions in the app design.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/339/4/334f1ee9-4263-4c86-9b10-632f0f2edab1/downloads/wwdc2026-339_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/339/4/334f1ee9-4263-4c86-9b10-632f0f2edab1/downloads/wwdc2026-339_sd.mp4?dl=1)

### Chapters

- Introduction
- Packaging
- Protocol
- Authentication
- Customization
- Next steps

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
