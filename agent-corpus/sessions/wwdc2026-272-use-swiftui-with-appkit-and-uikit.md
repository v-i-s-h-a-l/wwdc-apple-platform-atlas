---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Use SwiftUI With AppKit And UIKit
> Neutral research record for Apple WWDC 2026 session 272.

## Entries

- ID: `wwdc2026-272`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/272/
- Apple topics: App Services, SwiftUI & UI Frameworks
- Platforms: ios, ipados, macos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Discover how to incrementally adopt swiftui in your existing appkit or uikit app. we'll show you how to use the observation framework to automatically update your views, integrate swiftui components into an existing view hierarchy, and bring gesture recognizers into swiftui. we'll also explore how to add complete swiftui scenes to your app without changing your overall architecture.

### What Was Announced Or Covered

- @Observable can modernize NSView/UIKit view updates before a full SwiftUI migration.
- Observation can track reads in draw, layout, and update-layer paths for legacy views.
- SwiftUI Canvas, NSHostingView, NSGestureRecognizerRepresentable, NSHostingMenu, and NSHostingSceneRepresentation support incremental migration.
- Apple groups this session under App Services, SwiftUI & UI Frameworks; use it as source material for use swiftui with appkit and uikit.
- discover how to incrementally adopt swiftui in your existing appkit or uikit app. we'll show you how to use the observation framework to automatically update your views, integrate swiftui components into an existing view hierarchy, and bring gesture recognizers into swiftui. we'll also explore how to add complete swiftui scenes to your app without changing your overall architecture.
- Chapter coverage includes: Introduction; Observation in AppKit; Hosting SwiftUI in AppKit; AppKit gestures in SwiftUI; SwiftUI in the main menu.
- Transcript-derived capability tags: swiftui, xcode.
- API and framework terms to verify in SDK docs: API, APIs, AppKit, ColorModel, HSBColorPicker, IBAction, NSApplicationDelegate, NSGestureRecognizer, NSGestureRecognizerRepresentable, NSHostingMenu.

### APIs And Concepts

- Observable
- NSObservationTrackingEnabled
- UIObservationTrackingEnabled
- NSHostingView
- NSGestureRecognizerRepresentable
- NSHostingMenu
- NSHostingSceneRepresentation
- AppKit
- ColorModel
- HSBColorPicker
- IBAction
- NSApplicationDelegate
- NSGestureRecognizer
- NSMenu
- NSMenuItem
- NSSegmentedControl
- NSSlider
- NSSliderCell

### Risks And Constraints

- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.
- UI changes should be checked across light/dark mode, Dynamic Type, keyboard navigation, and platform-specific layout behavior.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/272/5/e1e4aa9a-cbe2-4f83-9cea-3dcaae19afd6/downloads/wwdc2026-272_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/272/5/e1e4aa9a-cbe2-4f83-9cea-3dcaae19afd6/downloads/wwdc2026-272_sd.mp4?dl=1)

### Chapters

- Introduction
- Observation in AppKit
- Hosting SwiftUI in AppKit
- AppKit gestures in SwiftUI
- SwiftUI in the main menu
- SwiftUI scenes in AppKit
- Next steps

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
