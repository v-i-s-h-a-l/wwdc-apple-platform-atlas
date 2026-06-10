---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Validate Your App Intents Adoption With AppIntentsTesting
> Neutral research record for Apple WWDC 2026 session 295.

## Entries

- ID: `wwdc2026-295`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/295/
- Apple topics: AI & Machine Learning
- Platforms: ios, ipados
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Meet appintentstesting, a new framework for validating your app intents through the same infrastructure used by siri, shortcuts, and spotlight. discover how to execute intents, inspect results, and test entities and queries — all without requiring ui automation. find out how to verify integrations like view annotations and spotlight indexing, helping you catch bugs early in your development workflow.

### What Was Announced Or Covered

- AppIntentsTesting validates App Intents through the same infrastructure used by Siri, Shortcuts, and Spotlight.
- Tests can execute intents, inspect results, and validate app entities and entity queries without UI automation.
- The framework covers chained intent flows, test-only intents, Spotlight indexing, and view annotation verification.
- It turns App Intents adoption into normal testable developer workflow instead of manual Siri/Shortcuts smoke testing.
- Apple groups this session under AI & Machine Learning; use it as source material for validate your app intents adoption with appintentstesting.
- meet appintentstesting, a new framework for validating your app intents through the same infrastructure used by siri, shortcuts, and spotlight. discover how to execute intents, inspect results, and test entities and queries — all without requiring ui automation. find out how to verify integrations like view annotations and spotlight indexing, helping you catch bugs early in your development workflow.
- Chapter coverage includes: Introduction; Meet CometCal: your first test; How AppIntentsTesting works; Testing entity queries; Combining multiple intents.
- Transcript-derived capability tags: app intents, siri, swiftui, xcode.

### APIs And Concepts

- AppIntentsTesting
- AppIntent
- AppEntity
- EntityQuery
- Spotlight
- ViewAnnotations
- TestOnlyIntent
- CalendarEntity
- CreateCalendarIntent
- CreateEventIntent
- DEBUG
- EntityStringQuery
- EventDetailView
- EventEntity
- EventEntityQuery
- OpenEventIntent
- SeedSampleEventsIntent
- UpdateEventIntent

### Risks And Constraints

- Intent tests should include entity-query edge cases, chained actions, missing data, and invalid user requests before relying on Siri or Spotlight behavior.
- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.
- UI changes should be checked across light/dark mode, Dynamic Type, keyboard navigation, and platform-specific layout behavior.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/295/4/cdcee6d3-e3e9-4201-b1ef-cd33e2d10e6f/downloads/wwdc2026-295_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/295/4/cdcee6d3-e3e9-4201-b1ef-cd33e2d10e6f/downloads/wwdc2026-295_sd.mp4?dl=1)

### Chapters

- Introduction
- Meet CometCal: your first test
- How AppIntentsTesting works
- Testing entity queries
- Combining multiple intents
- Test-only intents
- Testing Spotlight indexing
- Testing view annotations

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
