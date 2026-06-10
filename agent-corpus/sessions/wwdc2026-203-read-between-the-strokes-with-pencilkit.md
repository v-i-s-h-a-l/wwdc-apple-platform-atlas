---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Read Between The Strokes With Pencilkit
> Neutral research record for Apple WWDC 2026 session 203.

## Entries

- ID: `wwdc2026-203`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/203/
- Apple topics: SwiftUI & UI Frameworks, App Services
- Platforms: ios, ipados, macos, visionos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Unlock handwriting recognition in your apps using the same powerful technology behind apple apps like freeform and notes. discover how to use handwriting recognition across a wide range of alphabets and languages, and explore new capabilities for integrating pencilkit into a wider variety of apps.

### What Was Announced Or Covered

- PencilKit remains the low-latency drawing core, while PaperKit builds on it.
- Handwriting recognition can power indexing, find, and text extraction.
- iOS 27 improves model access, stable identity, selection changes, stroke slicing, masks, path conversion, and Metal-backed rendering.
- Apple groups this session under SwiftUI & UI Frameworks, App Services; use it as source material for read between the strokes with pencilkit.
- unlock handwriting recognition in your apps using the same powerful technology behind apple apps like freeform and notes. discover how to use handwriting recognition across a wide range of alphabets and languages, and explore new capabilities for integrating pencilkit into a wider variety of apps.
- Chapter coverage includes: Introduction; Handwriting recognition; Path conversion; Improved model access; Stroke slicing.
- Transcript-derived capability tags: accessibility, vision.
- API and framework terms to verify in SDK docs: API, APIs, PKCanvasView, PKDrawing, PKStroke, PKStrokePath, PKStrokePaths, PKStrokeRecognizer, PaperKit, PencilKit.

### APIs And Concepts

- PencilKit
- PKCanvasView
- PKDrawing
- PKStroke
- PKStrokePath
- PKStrokeRecognizer
- UIFindInteraction
- PKStrokePaths
- PaperKit
- UIFindInteractionDelegate
- UUID
- WWDC20
- WWDC25
- WWDC26
- accessibility
- vision

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.
- UI changes should be checked across light/dark mode, Dynamic Type, keyboard navigation, and platform-specific layout behavior.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/203/4/eb979cd5-af5b-4091-87ec-4839e8d131b9/downloads/wwdc2026-203_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/203/4/eb979cd5-af5b-4091-87ec-4839e8d131b9/downloads/wwdc2026-203_sd.mp4?dl=1)

### Chapters

- Introduction
- Handwriting recognition
- Path conversion
- Improved model access
- Stroke slicing
- Next steps

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
