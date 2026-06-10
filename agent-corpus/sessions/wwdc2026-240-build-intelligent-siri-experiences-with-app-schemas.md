---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Build Intelligent Siri Experiences With App Schemas
> Neutral research record for Apple WWDC 2026 session 240.

## Entries

- ID: `wwdc2026-240`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/240/
- Apple topics: App Services, AI & Machine Learning
- Platforms: ios, ipados, macos, visionos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Bring your app's content and actions to siri with app intents. model your data using app entities, adopt app schemas to enable powerful system actions, and support natural language interactions powered by apple intelligence. explore how to enable semantic search, perform actions across apps, and create contextual experiences using onscreen awareness and content transfer. find out best practices and testing tools to build fast, reliable siri experiences.

### What Was Announced Or Covered

- Apple groups this session under App Services, AI & Machine Learning; use it as source material for build intelligent siri experiences with app schemas.
- bring your app's content and actions to siri with app intents. model your data using app entities, adopt app schemas to enable powerful system actions, and support natural language interactions powered by apple intelligence. explore how to enable semantic search, perform actions across apps, and create contextual experiences using onscreen awareness and content transfer. find out best practices and testing tools to build fast, reliable siri experiences.
- Chapter coverage includes: Introduction; What's new in Siri; Contributing content with App Entities; Entity resolution and IndexedEntity; Making actions available.
- Transcript-derived capability tags: app intents, apple intelligence, siri, xcode.
- API and framework terms to verify in SDK docs: APIs, AppEntity, AppIntentsTesting, ContactEntity, EntityStringQuery, IndexedEntity, IntentValueQuery, WWDC24.
- Treat this WWDC26 session as the current primary source, then confirm exact API availability against installed SDK docs.

### APIs And Concepts

- AppEntity
- AppIntentsTesting
- ContactEntity
- EntityStringQuery
- IndexedEntity
- IntentValueQuery
- WWDC24
- app intents
- apple intelligence
- siri
- xcode

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/240/4/d46aac11-3990-42cd-bb33-4ce5e958b902/downloads/wwdc2026-240_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/240/4/d46aac11-3990-42cd-bb33-4ce5e958b902/downloads/wwdc2026-240_sd.mp4?dl=1)

### Chapters

- Introduction
- What's new in Siri
- Contributing content with App Entities
- Entity resolution and IndexedEntity
- Making actions available
- Adopting a schema domain in UnicornChat
- Moving content across apps
- Working across apps: onscreen awareness

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
