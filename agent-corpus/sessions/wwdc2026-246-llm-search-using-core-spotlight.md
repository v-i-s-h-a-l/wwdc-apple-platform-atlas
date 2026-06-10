---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# LLM Search Using Core Spotlight
> Neutral research record for Apple WWDC 2026 session 246.

## Entries

- ID: `wwdc2026-246`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/246/
- Apple topics: AI & Machine Learning
- Platforms: ios, ipados, macos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Level up basic search into a retrieval-augmented system using spotlightsearchtool and languagemodelsession. explore core spotlight integration, delegate-based hydration patterns, and how metadata quality impacts your search results. learn how to use custom pipelinestages for tasks like sentiment analysis. discover best practices for indexing and building flexible, context-rich search experiences in your app.

### What Was Announced Or Covered

- Apple groups this session under AI & Machine Learning; use it as source material for llm search using core spotlight.
- level up basic search into a retrieval-augmented system using spotlightsearchtool and languagemodelsession. explore core spotlight integration, delegate-based hydration patterns, and how metadata quality impacts your search results. learn how to use custom pipelinestages for tasks like sentiment analysis. discover best practices for indexing and building flexible, context-rich search experiences in your app.
- Chapter coverage includes: Introduction; Grounding answers with Spotlight tool-calling; Configure and add SpotlightSearchTool; Displaying results and partial replies; Provide full items with an index delegate.
- Transcript-derived capability tags: agent, apple intelligence, core spotlight, evaluation, foundation model, tool calling, vision, xcode.
- API and framework terms to verify in SDK docs: APIs, CSSearchableIndex, CSSearchableItem, GuidanceProfile, HTML, JSON, LLM, LanguageModelSession, SpotlightSearchTool, SystemLanguageModel.
- Treat this WWDC26 session as the current primary source, then confirm exact API availability against installed SDK docs.

### APIs And Concepts

- CSSearchableIndex
- CSSearchableItem
- GuidanceProfile
- LLM
- LanguageModelSession
- SpotlightSearchTool
- SystemLanguageModel
- agent
- apple intelligence
- core spotlight
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

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/246/4/b390ab9d-d231-4cf5-9d1b-e4270ef5012b/downloads/wwdc2026-246_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/246/4/b390ab9d-d231-4cf5-9d1b-e4270ef5012b/downloads/wwdc2026-246_sd.mp4?dl=1)

### Chapters

- Introduction
- Grounding answers with Spotlight tool-calling
- Configure and add SpotlightSearchTool
- Displaying results and partial replies
- Provide full items with an index delegate
- Customizing with guidance profiles
- Reference resolution with a contact resolver
- Custom pipeline stages

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
