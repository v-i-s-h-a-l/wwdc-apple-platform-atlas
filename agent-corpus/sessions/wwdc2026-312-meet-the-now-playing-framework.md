---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Meet The Now Playing Framework
> Neutral research record for Apple WWDC 2026 session 312.

## Entries

- ID: `wwdc2026-312`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/312/
- Apple topics: Audio & Video
- Platforms: ios, ipados, macos, tvos, visionos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Get a first look at now playing — a swift framework that connects your app's media playback to system surfaces like the lock screen, control center, dynamic island, and carplay. discover how to publish playback state and respond to commands using its observable api. explore remote playback sessions, a new capability that lets your app represent media playing on external devices and bring full playback controls to those same system surfaces.

### What Was Announced Or Covered

- The Now Playing framework centralizes media playback presence, controls, and system integration.
- Media apps should treat Now Playing as part of the user experience across lock screen, remote controls, and platform surfaces.
- The session belongs with MusicKit, subtitles, accessibility, and media-session architecture.
- Apple groups this session under Audio & Video; use it as source material for meet the now playing framework.
- get a first look at now playing — a swift framework that connects your app's media playback to system surfaces like the lock screen, control center, dynamic island, and carplay. discover how to publish playback state and respond to commands using its observable api. explore remote playback sessions, a new capability that lets your app represent media playing on external devices and bring full playback controls to those same system surfaces.
- Chapter coverage includes: Introduction; Media sessions; Remote media sessions; Media sharing extensions.
- Transcript-derived capability tags: vision.
- API and framework terms to verify in SDK docs: API, APIs, APNs, MediaSession, PlayerModel, RemotePlayerModel, SDK, TVs.

### APIs And Concepts

- NowPlaying
- MediaPlayback
- RemoteCommand
- MusicKit
- APNs
- MediaSession
- PlayerModel
- RemotePlayerModel
- SDK
- TVs
- vision

### Risks And Constraints

- Playback state should be tested across interruptions, backgrounding, remote controls, and multiple output routes.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/312/5/3f128d25-f1c6-49d3-a9c0-0bdc22af5f95/downloads/wwdc2026-312_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/312/5/3f128d25-f1c6-49d3-a9c0-0bdc22af5f95/downloads/wwdc2026-312_sd.mp4?dl=1)

### Chapters

- Introduction
- Media sessions
- Remote media sessions
- Media sharing extensions

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
