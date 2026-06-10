---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Prepare Your tvOS Apps For Dynamic Type
> Neutral research record for Apple WWDC 2026 session 221.

## Entries

- ID: `wwdc2026-221`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/221/
- Apple topics: Audio & Video, Accessibility & Inclusion
- Platforms: tvos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Dynamic type empowers people to comfortably read and interact with your app by letting them choose the text size that works best for them. you'll learn how to get your app ready for dynamic type on tvos through practical techniques for implementing font scaling and adapting your layouts for larger content. you'll also discover how to optimize your media-focused interfaces like grids and carousels, ensuring a great experience for everyone who relies on different text sizes.

### What Was Announced Or Covered

- Dynamic Type on tvOS brings large-screen accessibility constraints into focus for apps that historically used fixed text sizes.
- The session helps adapt layouts, focus behavior, and media-oriented screens for variable text without clipping or occlusion.
- It broadens the corpus accessibility model beyond phone, tablet, and desktop assumptions.
- Apple groups this session under Audio & Video, Accessibility & Inclusion; use it as source material for prepare your tvos apps for dynamic type.
- dynamic type empowers people to comfortably read and interact with your app by letting them choose the text size that works best for them. you'll learn how to get your app ready for dynamic type on tvos through practical techniques for implementing font scaling and adapting your layouts for larger content. you'll also discover how to optimize your media-focused interfaces like grids and carousels, ensuring a great experience for everyone who relies on different text sizes.
- Chapter coverage includes: Introduction; Identify common issues; Adapt your layout.
- Transcript-derived capability tags: accessibility, swiftui.
- API and framework terms to verify in SDK docs: HStack, HStackLayout, UIKit, UIStackView, UITraitPreferredContentSizeCategory, VStack, VStackLayout, XXXL.

### APIs And Concepts

- DynamicType
- tvOS
- Accessibility
- FocusEngine
- HStack
- HStackLayout
- UIKit
- UIStackView
- UITraitPreferredContentSizeCategory
- VStack
- VStackLayout
- XXXL
- swiftui

### Risks And Constraints

- Generated tvOS screens should be checked under large accessibility text sizes and focus navigation, not only default typography.
- UI changes should be checked across light/dark mode, Dynamic Type, keyboard navigation, and platform-specific layout behavior.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/221/5/ada10ebd-34f8-4f57-92b5-4b3cd6281267/downloads/wwdc2026-221_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/221/5/ada10ebd-34f8-4f57-92b5-4b3cd6281267/downloads/wwdc2026-221_sd.mp4?dl=1)

### Chapters

- Introduction
- Identify common issues
- Adapt your layout

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
