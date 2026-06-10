---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# What's New In Swiftdata
> Neutral research record for Apple WWDC 2026 session 274.

## Entries

- ID: `wwdc2026-274`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/274/
- Apple topics: Swift, SwiftUI & UI Frameworks, App Services
- Platforms: ios, ipados, macos, tvos, visionos, watchos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Discover the latest enhancements to swiftdata. we'll show you how to persist custom and third-party types using codable, and group fetched data into sections in your swiftui app. we'll also explore how to observe data store changes anywhere else using modelresultsobserver and historyobserver, giving you the flexibility to drive powerful state objects, integrate with delegate-based architectures, and react precisely to model updates.

### What Was Announced Or Covered

- @Query gains sectioning through sectionBy.
- SwiftData can store custom or third-party Codable types when they cannot become @Model types.
- ResultsObserver, ModelResultsObserver, HistoryObserver, and ModelContext.fetchHistory support non-SwiftUI observation and persistent-history workflows.
- Apple groups this session under Swift, SwiftUI & UI Frameworks; use it as source material for what’s new in swiftdata.
- discover the latest enhancements to swiftdata. we'll show you how to persist custom and third-party types using codable, and group fetched data into sections in your swiftui app. we'll also explore how to observe data store changes anywhere else using modelresultsobserver and historyobserver, giving you the flexibility to drive powerful state objects, integrate with delegate-based architectures, and react precisely to model updates.
- Chapter coverage includes: Introduction; Sectioning your fetches; Using custom types; Observing data stores with ResultsObserver; Observing history with HistoryObserver.
- Transcript-derived capability tags: swiftdata, swiftui.
- API and framework terms to verify in SDK docs: API, APIs, MKMapItem, MapKit, SceneKit, SwiftData, TripListView.

### APIs And Concepts

- SwiftData
- Query
- sectionBy
- Codable
- ResultsObserver
- ModelResultsObserver
- HistoryObserver
- ModelContext
- MKMapItem
- MapKit
- SceneKit
- TripListView
- swiftui

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- UI changes should be checked across light/dark mode, Dynamic Type, keyboard navigation, and platform-specific layout behavior.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/274/4/87fb1efb-9956-414e-8c99-f2579fe86da2/downloads/wwdc2026-274_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/274/4/87fb1efb-9956-414e-8c99-f2579fe86da2/downloads/wwdc2026-274_sd.mp4?dl=1)

### Chapters

- Introduction
- Sectioning your fetches
- Using custom types
- Observing data stores with ResultsObserver
- Observing history with HistoryObserver
- Next steps

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
