---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Discover Generated Subtitles And Subtitle Styles
> Neutral research record for Apple WWDC 2026 session 256.

## Entries

- ID: `wwdc2026-256`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/256/
- Apple topics: Accessibility & Inclusion, Audio & Video
- Platforms: ios, ipados, macos, tvos, visionos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Make your video content more accessible with generated subtitles — a powerful new feature that can transcribe spoken audio or translate subtitles from another language, using on-device models. explore caption style preview, which lets people customize and preview subtitle styles during playback, and dive into implementation details for avkit, avplayerlayer, and the media accessibility framework.

### What Was Announced Or Covered

- Generated subtitles and subtitle styles combine accessibility, media quality, localization, and playback presentation.
- Apps should consider subtitle generation, styling, readability, and user preference behavior together.
- This session is relevant for video, education, social, and immersive media workflows.
- Apple groups this session under Accessibility & Inclusion, Audio & Video; use it as source material for discover generated subtitles and subtitle styles.
- make your video content more accessible with generated subtitles — a powerful new feature that can transcribe spoken audio or translate subtitles from another language, using on-device models. explore caption style preview, which lets people customize and preview subtitle styles during playback, and dive into implementation details for avkit, avplayerlayer, and the media accessibility framework.
- Chapter coverage includes: Introduction; Media authoring; Subtitle generation methods; Availability and support; Presenting subtitles in your app.
- Transcript-derived capability tags: accessibility, speech, vision.
- API and framework terms to verify in SDK docs: API, AVCaptionRenderer, AVFoundation, AVLegibleMediaOptionsMenuController, AVPlayerLayer, AVPlayerView, AVPlayerViewController, HTTP, IDs.

### APIs And Concepts

- Subtitles
- GeneratedSubtitles
- AVFoundation
- Accessibility
- Localization
- AVCaptionRenderer
- AVLegibleMediaOptionsMenuController
- AVPlayerLayer
- AVPlayerView
- AVPlayerViewController
- speech
- vision

### Risks And Constraints

- Generated subtitle workflows need review for accuracy, language coverage, timing, styling contrast, and user correction paths.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- UI changes should be checked across light/dark mode, Dynamic Type, keyboard navigation, and platform-specific layout behavior.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/256/4/d28efb5e-5550-468d-b1d1-caec51ce55e6/downloads/wwdc2026-256_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/256/4/d28efb5e-5550-468d-b1d1-caec51ce55e6/downloads/wwdc2026-256_sd.mp4?dl=1)

### Chapters

- Introduction
- Media authoring
- Subtitle generation methods
- Availability and support
- Presenting subtitles in your app
- Subtitle style preview
- Demo
- Next steps

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
