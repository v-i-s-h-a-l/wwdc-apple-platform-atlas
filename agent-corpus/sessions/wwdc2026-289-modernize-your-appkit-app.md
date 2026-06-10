---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Modernize Your AppKit App
> Neutral research record for Apple WWDC 2026 session 289.

## Entries

- ID: `wwdc2026-289`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/289/
- Apple topics: SwiftUI & UI Frameworks
- Platforms: macos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Bring your appkit app up to date with modern macos conventions. dive into handling input with control events and gesture recognizers, moving beyond traditional tracking loops. enhance keyboard navigation in your app, implement graceful state restoration after restarts, and take advantage of new corner concentricity apis that let your interface blend seamlessly with the macos aesthetic.

### What Was Announced Or Covered

- AppKit modernization favors gesture recognizers, control events, and view APIs over mouseDown tracking loops.
- macOS 27 adds custom text selection APIs for standard text behavior in any view.
- Keyboard navigation, status items, graceful termination, state restoration, Liquid Glass, corner configuration, and concentricity need explicit review.
- Apple groups this session under SwiftUI & UI Frameworks; use it as source material for modernize your appkit app.
- bring your appkit app up to date with modern macos conventions. dive into handling input with control events and gesture recognizers, moving beyond traditional tracking loops. enhance keyboard navigation in your app, implement graceful state restoration after restarts, and take advantage of new corner concentricity apis that let your interface blend seamlessly with the macos aesthetic.
- Chapter coverage includes: Introduction; Modern input; Modern event handling with gesture recognizers; Selection, context menus, and drag and drop; Text selection in custom views.
- Transcript-derived capability tags: accessibility, swiftui.
- API and framework terms to verify in SDK docs: API, APIs, AppKit, ExpandedInterfaceSession, NSBrowser, NSButton, NSCollectionView, NSCollectionViewItem, NSControlEvents, NSOutlineView.

### APIs And Concepts

- AppKit
- GestureRecognizers
- TextSelection
- StateRestoration
- cornerConfiguration
- Concentricity
- ExpandedInterfaceSession
- NSBrowser
- NSButton
- NSCollectionView
- NSCollectionViewItem
- NSControlEvents
- NSOutlineView
- NSOutlineViewDelegate
- NSResponder
- NSResponders
- NSScrollEdgeEffectStyle
- NSStatusItem

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- UI changes should be checked across light/dark mode, Dynamic Type, keyboard navigation, and platform-specific layout behavior.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/289/5/6a2a7cfa-56a1-4cbb-ae54-1f229e1708ae/downloads/wwdc2026-289_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/289/5/6a2a7cfa-56a1-4cbb-ae54-1f229e1708ae/downloads/wwdc2026-289_sd.mp4?dl=1)

### Chapters

- Introduction
- Modern input
- Modern event handling with gesture recognizers
- Selection, context menus, and drag and drop
- Text selection in custom views
- Control events and gesture recognizers
- Keyboard navigation and status items
- Continuity across launches

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
