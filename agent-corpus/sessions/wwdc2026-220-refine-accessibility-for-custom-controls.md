---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Refine Accessibility For Custom Controls
> Neutral research record for Apple WWDC 2026 session 220.

## Entries

- ID: `wwdc2026-220`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/220/
- Apple topics: SwiftUI & UI Frameworks, Accessibility & Inclusion
- Platforms: ios, ipados, macos, tvos, visionos, watchos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Unlock the full potential of your app's interactive elements by making them accessible to everyone. we'll break down how people understand and use controls with voiceover and other assistive technologies, exploring a variety of input methods like actions, the passthrough gesture, and direct touch. join us for an in-depth exploration of several example controls as we refine and elevate the accessibility experience in each one.

### What Was Announced Or Covered

- Custom controls need label, value, hint, activation point, announcements, and current state through accessibilityValue.
- Custom actions provide non-gesture alternatives; direct interaction and passthrough gestures are reserved for controls that need native gestures.
- Complex visual controls require semantic bounds and a deliberate assistive interaction model.
- Apple groups this session under SwiftUI & UI Frameworks, Accessibility & Inclusion; use it as source material for refine accessibility for custom controls.
- unlock the full potential of your app's interactive elements by making them accessible to everyone. we'll break down how people understand and use controls with voiceover and other assistive technologies, exploring a variety of input methods like actions, the passthrough gesture, and direct touch. join us for an in-depth exploration of several example controls as we refine and elevate the accessibility experience in each one.
- Chapter coverage includes: Introduction; Guiding principles; Complex controls.
- Transcript-derived capability tags: accessibility, speech, swiftui, vision.
- API and framework terms to verify in SDK docs: API, CoffeeDispenserView.

### APIs And Concepts

- Accessibility
- accessibilityValue
- CustomActions
- ActivationPoint
- DirectTouch
- CoffeeDispenserView
- speech
- swiftui
- vision

### Risks And Constraints

- UI changes should be checked across light/dark mode, Dynamic Type, keyboard navigation, and platform-specific layout behavior.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/220/4/945f8d34-8427-4476-ae75-34edc4a9c3f9/downloads/wwdc2026-220_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/220/4/945f8d34-8427-4476-ae75-34edc4a9c3f9/downloads/wwdc2026-220_sd.mp4?dl=1)

### Chapters

- Introduction
- Guiding principles
- Complex controls

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
