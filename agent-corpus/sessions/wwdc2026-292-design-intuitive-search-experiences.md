---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Design Intuitive Search Experiences
> Neutral research record for Apple WWDC 2026 session 292.

## Entries

- ID: `wwdc2026-292`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/292/
- Apple topics: Essentials, Design
- Platforms: ios, ipados, macos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Explore new patterns and best practices when implementing search in your app. discover how search plays a key role in helping people find and navigate content, and find out how to integrate search across different navigation models and apple platforms.

### What Was Announced Or Covered

- Search design guidance covers search field behavior, placement patterns, navigation models, platform differences, and best practices.
- Search is positioned as both content discovery and navigation, not just filtering text in a list.
- The session helps decide when search belongs globally, within a tab/sidebar, inside content, or across platform-specific surfaces.
- Apple groups this session under Essentials, Design; use it as source material for design intuitive search experiences.
- explore new patterns and best practices when implementing search in your app. discover how search plays a key role in helping people find and navigate content, and find out how to integrate search across different navigation models and apple platforms.
- Chapter coverage includes: Introduction; Search field; Patterns and placement; Best practices; Next steps.
- Treat this WWDC26 session as the current primary source, then confirm exact API availability against installed SDK docs.

### APIs And Concepts

- Search
- SearchField
- Navigation
- InformationArchitecture

### Risks And Constraints

- Search UI should define scope, empty states, ranking, query persistence, keyboard behavior, and accessibility before implementation.
- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/292/5/05adbfdf-d9ba-4a6d-8d2f-f43593907f55/downloads/wwdc2026-292_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/292/5/05adbfdf-d9ba-4a6d-8d2f-f43593907f55/downloads/wwdc2026-292_sd.mp4?dl=1)

### Chapters

- Introduction
- Search field
- Patterns and placement
- Best practices
- Next steps

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
