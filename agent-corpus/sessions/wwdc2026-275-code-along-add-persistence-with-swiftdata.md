---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Code-Along: Add Persistence With Swiftdata
> Neutral research record for Apple WWDC 2026 session 275.

## Entries

- ID: `wwdc2026-275`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/275/
- Apple topics: Swift, SwiftUI & UI Frameworks, App Services
- Platforms: ios, ipados, macos, tvos, visionos, watchos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Experience swiftdata in action as we add persistence to an existing app. we'll show you how to define your data models and seamlessly integrate persistent data with swiftui. you'll also learn foundational skills for managing your app's state using this expressive, declarative api.

### What Was Announced Or Covered

- The code-along identifies transient SwiftUI state worth persisting, converts observable types to @Model, and attaches schema with modelContainer.
- It uses Codable custom values, relationships, @Query, FetchDescriptor, SortDescriptor, and dynamic query initialization.
- The implementation handles search, recent views, errors, and date-edited side effects.
- Apple groups this session under Swift, SwiftUI & UI Frameworks; use it as source material for code-along: add persistence with swiftdata.
- experience swiftdata in action as we add persistence to an existing app. we'll show you how to define your data models and seamlessly integrate persistent data with swiftui. you'll also learn foundational skills for managing your app's state using this expressive, declarative api.
- Chapter coverage includes: Introduction; Identify relevant state; Define your schemas; Define model relationships; Update the view layer.
- Transcript-derived capability tags: swiftdata, swiftui.
- API and framework terms to verify in SDK docs: ActivityItemView, ContentUnavailableView, GoalsView, IDs, RAM, RecentTripsPageView, SearchResultsListView, SwiftData, TripCollectionView, TripDetailView.

### APIs And Concepts

- Model
- modelContainer
- Query
- FetchDescriptor
- SortDescriptor
- SwiftData
- ActivityItemView
- ContentUnavailableView
- GoalsView
- RAM
- RecentTripsPageView
- SearchResultsListView
- TripCollectionView
- TripDetailView
- TripEditModel
- swiftui

### Risks And Constraints

- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.
- UI changes should be checked across light/dark mode, Dynamic Type, keyboard navigation, and platform-specific layout behavior.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/275/4/7c64f887-3c3c-4bdf-8472-72d6b96f8e3d/downloads/wwdc2026-275_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/275/4/7c64f887-3c3c-4bdf-8472-72d6b96f8e3d/downloads/wwdc2026-275_sd.mp4?dl=1)

### Chapters

- Introduction
- Identify relevant state
- Define your schemas
- Define model relationships
- Update the view layer
- Next steps

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
