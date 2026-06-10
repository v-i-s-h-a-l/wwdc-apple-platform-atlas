---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Dive Into Lazy Stacks And Scrolling With SwiftUI
> Neutral research record for Apple WWDC 2026 session 321.

## Entries

- ID: `wwdc2026-321`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/321/
- Apple topics: Design, SwiftUI & UI Frameworks
- Platforms: ios, ipados, macos, tvos, visionos, watchos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Discover the inner workings of lazy stacks in swiftui. we'll explore how lazyvstack and lazyhstack estimate sizes, lazily load subviews, and prefetch content to deliver smooth scrolling experiences. we'll also cover advanced performance optimizations, state management best practices, and tips for precise programmatic scrolling. to get the most out of this session, we recommend basic familiarity with swiftui layout using stacks.

### What Was Announced Or Covered

- Lazy stacks estimate sizes and resolve subviews in ways that affect scroll accuracy and programmatic scrolling.
- Filter data before view construction instead of conditionally hiding rows inside lazy content.
- Environment changes can trigger offscreen body work; cache-backed observable loaders can cooperate better with internal prefetching.
- Avoid post-appearance size changes that move offscreen scroll targets.
- Apple groups this session under Design, SwiftUI & UI Frameworks; use it as source material for dive into lazy stacks and scrolling with swiftui.
- discover the inner workings of lazy stacks in swiftui. we'll explore how lazyvstack and lazyhstack estimate sizes, lazily load subviews, and prefetch content to deliver smooth scrolling experiences. we'll also cover advanced performance optimizations, state management best practices, and tips for precise programmatic scrolling. to get the most out of this session, we recommend basic familiarity with swiftui layout using stacks.
- Chapter coverage includes: Introduction; Layout; Subview loading; Prefetching; Programmatic scrolling.
- Transcript-derived capability tags: evaluation, swiftdata, swiftui.

### APIs And Concepts

- LazyVStack
- LazyHStack
- ScrollView
- scrollTransition
- Prefetching
- ContentUnavailableView
- ContentView
- ProgressView
- StepView
- SwiftData
- VStack
- evaluation
- swiftui

### Risks And Constraints

- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.
- UI changes should be checked across light/dark mode, Dynamic Type, keyboard navigation, and platform-specific layout behavior.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/321/5/78830752-d07d-4d89-aeab-94405c084de9/downloads/wwdc2026-321_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/321/5/78830752-d07d-4d89-aeab-94405c084de9/downloads/wwdc2026-321_sd.mp4?dl=1)

### Chapters

- Introduction
- Layout
- Subview loading
- Prefetching
- Programmatic scrolling
- Next steps

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
