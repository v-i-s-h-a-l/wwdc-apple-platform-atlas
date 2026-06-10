---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# What's New In SwiftUI
> Neutral research record for Apple WWDC 2026 session 269.

## Entries

- ID: `wwdc2026-269`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/269/
- Apple topics: App Services, Design, SwiftUI & UI Frameworks
- Platforms: ios, ipados, macos, tvos, visionos, watchos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Explore the latest additions to swiftui and discover how they can improve your apps. we'll introduce a new document protocol with direct disk access and snapshot-based diffing for building high-performance apps; new apis for reordering content in lists, grids, and sections; and toolbar enhancements including visibility priority and auto-minimizing behavior. we'll also cover expanded presentation apis — including swipe actions on any view — plus asyncimage caching improvements and lazy state initialization for observable types.

### What Was Announced Or Covered

- SwiftUI auto-adopts much of Liquid Glass, but mixed UIKit/SwiftUI apps need extra resizability and presentation review.
- Document APIs add custom creation sources, direct URL access, writable snapshots, and large-document performance improvements.
- Reorderable containers work beyond List, including grids and watchOS; swipe actions expand beyond list rows.
- AsyncImage now honors HTTP caching and supports custom URLRequest or URLSession, while @State is macro-backed with lazy class initialization.
- Apple groups this session under App Services, Design; use it as source material for what’s new in swiftui.
- explore the latest additions to swiftui and discover how they can improve your apps. we'll introduce a new document protocol with direct disk access and snapshot-based diffing for building high-performance apps; new apis for reordering content in lists, grids, and sections; and toolbar enhancements including visibility priority and auto-minimizing behavior. we'll also cover expanded presentation apis — including swipe actions on any view — plus asyncimage caching improvements and lazy state initialization for observable types.
- Chapter coverage includes: Introduction; Refreshed look and feel; Document-based apps; Presentation and interaction; Data flow and performance.
- Transcript-derived capability tags: agent, swiftui, xcode.

### APIs And Concepts

- SwiftUI
- DocumentCreationSource
- FileDocument
- ReferenceFileDocument
- reorderable
- reorderContainer
- AsyncImage
- State
- ContentBuilder
- ReadableDocument
- StickerDocument
- StickerStoreView
- UIKit
- URLCache
- URLRequest
- URLSession
- WWDC26
- WritableDocument

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.
- UI changes should be checked across light/dark mode, Dynamic Type, keyboard navigation, and platform-specific layout behavior.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/269/4/9215cf93-1308-4706-91e8-34d4e40939d1/downloads/wwdc2026-269_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/269/4/9215cf93-1308-4706-91e8-34d4e40939d1/downloads/wwdc2026-269_sd.mp4?dl=1)

### Chapters

- Introduction
- Refreshed look and feel
- Document-based apps
- Presentation and interaction
- Data flow and performance
- Next steps

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
