---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Code-Along: Make Your App Available To Siri
> Neutral research record for Apple WWDC 2026 session 344.

## Entries

- ID: `wwdc2026-344`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/344/
- Apple topics: App Services, AI & Machine Learning
- Platforms: ios, ipados, macos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Dive deep into an xcode project showing how you can make your app available to siri. learn how to adopt app schemas to let people ask questions about calendar events and take natural language actions like scheduling. discover best practices for making content available in the spotlight semantic index and providing context for on-screen awareness.

### What Was Announced Or Covered

- Apple groups this session under App Services, AI & Machine Learning; use it as source material for code-along: make your app available to siri.
- dive deep into an xcode project showing how you can make your app available to siri. learn how to adopt app schemas to let people ask questions about calendar events and take natural language actions like scheduling. discover best practices for making content available in the spotlight semantic index and providing context for on-screen awareness.
- Chapter coverage includes: Introduction; App Schemas and the plan; Build the CalendarEntity; Build the AttendeeEntity; Build the EventEntity.
- Transcript-derived capability tags: app intents, apple intelligence, siri, swiftdata, swiftui, xcode.
- API and framework terms to verify in SDK docs: AppEntity, AppIntent, AppIntentsTesting, AttendeeEntity, CSSearchableIndex, CalendarEntity, CalendarListView, CalendarModel, DeleteEventIntent, EntityQuery.
- Treat this WWDC26 session as the current primary source, then confirm exact API availability against installed SDK docs.

### APIs And Concepts

- AppEntity
- AppIntent
- AppIntentsTesting
- AttendeeEntity
- CSSearchableIndex
- CalendarEntity
- CalendarListView
- CalendarModel
- DeleteEventIntent
- EntityQuery
- EnumerableEntityQuery
- EventEntity
- EventSnippetView
- IndexedEntity
- OpenEventIntent
- OpenIntent
- ShowsSnippetView
- SwiftData

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.
- UI changes should be checked across light/dark mode, Dynamic Type, keyboard navigation, and platform-specific layout behavior.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/344/4/ee45cb19-e252-41f4-a2e0-e9b59238c7aa/downloads/wwdc2026-344_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/344/4/ee45cb19-e252-41f4-a2e0-e9b59238c7aa/downloads/wwdc2026-344_sd.mp4?dl=1)

### Chapters

- Introduction
- App Schemas and the plan
- Build the CalendarEntity
- Build the AttendeeEntity
- Build the EventEntity
- Open events with OpenIntent
- Onscreen awareness
- Create events with Siri

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
