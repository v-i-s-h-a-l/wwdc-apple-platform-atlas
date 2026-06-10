---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Unwrap Paperkit
> Neutral research record for Apple WWDC 2026 session 372.

## Entries

- ID: `wwdc2026-372`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/372/
- Apple topics: SwiftUI & UI Frameworks, App Services
- Platforms: ios, ipados, macos, visionos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Craft a canvas-based application with paperkit. explore the new data model apis that let you access, create, and modify markup elements. learn how to add custom controls and annotations, and discover best practices for integrating these features into your app to build a fully featured creative canvas.

### What Was Announced Or Covered

- PaperKit is Apple’s canvas and markup layer for Notes-style experiences.
- New data model APIs expose markup subelements, support programmatic creation and modification, and allow read-only template elements.
- Adornments provide non-persisted custom controls that track zoom and scroll, and images can be placed into the canvas.
- Apple groups this session under SwiftUI & UI Frameworks, App Services; use it as source material for unwrap paperkit.
- craft a canvas-based application with paperkit. explore the new data model apis that let you access, create, and modify markup elements. learn how to add custom controls and annotations, and discover best practices for integrating these features into your app to build a fully featured creative canvas.
- Chapter coverage includes: Introduction; Data model; Elements; Adornments; Next steps.
- Transcript-derived capability tags: speech, vision.
- API and framework terms to verify in SDK docs: APIs, PDF, PaperKit, PencilKit.

### APIs And Concepts

- PaperKit
- PaperMarkup
- Adornments
- MarkupElements
- PDF
- PencilKit
- speech
- vision

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/372/4/012a7de6-cf54-420f-aaf7-02ea568485bf/downloads/wwdc2026-372_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/372/4/012a7de6-cf54-420f-aaf7-02ea568485bf/downloads/wwdc2026-372_sd.mp4?dl=1)

### Chapters

- Introduction
- Data model
- Elements
- Adornments
- Next steps

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
