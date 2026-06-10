---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Enhance Raw Image Processing With Core Image
> Neutral research record for Apple WWDC 2026 session 305.

## Entries

- ID: `wwdc2026-305`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/305/
- Apple topics: Photos & Camera
- Platforms: ios, ipados, macos, visionos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Harness the power of version 9 of the core image raw processing apis to dramatically improve image quality in your apps, with improved sharpness and more defined color, while using the apple neural engine for optimal performance. take advantage of the cirawfilter api to let your users edit raw photos by changing exposure, noise reduction, sharpness, contrast and more. and explore new ciimageprocessor apis that optimize performance by giving you precise control over tile sizing and buffer management.

### What Was Announced Or Covered

- Core Image improvements for RAW processing matter for pro camera, photo editing, and computational imaging workflows.
- The session connects image pipeline quality with performance and user-visible editing capabilities.
- Use it as deterministic imaging context alongside generative Image Playground or model-assisted photo features.
- Apple groups this session under Photos & Camera; use it as source material for enhance raw image processing with core image.
- harness the power of version 9 of the core image raw processing apis to dramatically improve image quality in your apps, with improved sharpness and more defined color, while using the apple neural engine for optimal performance. take advantage of the cirawfilter api to let your users edit raw photos by changing exposure, noise reduction, sharpness, contrast and more. and explore new ciimageprocessor apis that optimize performance by giving you precise control over tile sizing and buffer management.
- Chapter coverage includes: Introduction; How Core Image supports RAW; The evolution of RAW support; RAW 9 overview; RAW 9 quality improvements.
- Transcript-derived capability tags: swiftui, vision.
- API and framework terms to verify in SDK docs: API, APIs, CIContext, CIImageProcessor, CIImageProcessorOutput, CIKernels, CIRAWFilter, CVPixelBuffer, DNG, EDR.

### APIs And Concepts

- CoreImage
- RAW
- CIRAWFilter
- ImageProcessing
- Camera
- CIContext
- CIImageProcessor
- CIImageProcessorOutput
- CIKernels
- CVPixelBuffer
- DNG
- EDR
- HEIF
- HEIFs
- III
- ISO
- JPEG
- JPEGs

### Risks And Constraints

- RAW pipeline changes need quality, color, performance, and memory checks on representative assets.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.
- UI changes should be checked across light/dark mode, Dynamic Type, keyboard navigation, and platform-specific layout behavior.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/305/5/d8d5f3ce-0ff1-45a3-a630-436743477c62/downloads/wwdc2026-305_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/305/5/d8d5f3ce-0ff1-45a3-a630-436743477c62/downloads/wwdc2026-305_sd.mp4?dl=1)

### Chapters

- Introduction
- How Core Image supports RAW
- The evolution of RAW support
- RAW 9 overview
- RAW 9 quality improvements
- Enable and edit RAW 9 with CIRAWFilter API
- RAW 9 performance overview
- Interactive editing

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
