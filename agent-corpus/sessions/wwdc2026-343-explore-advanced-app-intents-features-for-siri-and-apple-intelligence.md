---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Explore Advanced App Intents Features For Siri And Apple Intelligence
> Neutral research record for Apple WWDC 2026 session 343.

## Entries

- ID: `wwdc2026-343`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/343/
- Apple topics: App Services, AI & Machine Learning
- Platforms: ios, ipados, visionos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Polish how your app works with siri using advanced app intents apis. learn techniques that let people accomplish more with just their voice, help apple intelligence find your content, and provide context for on-screen awareness so siri understands what's happening in your app.

### What Was Announced Or Covered

- Apple groups this session under App Services, AI & Machine Learning; use it as source material for explore advanced app intents features for siri and apple intelligence.
- polish how your app works with siri using advanced app intents apis. learn techniques that let people accomplish more with just their voice, help apple intelligence find your content, and provide context for on-screen awareness so siri understands what's happening in your app.
- Chapter coverage includes: Introduction; Customize how Siri responds; Visual responses; Interaction donations; Confirmations and entity ownership.
- Transcript-derived capability tags: agent, app intents, apple intelligence, core spotlight, siri, swiftui.
- API and framework terms to verify in SDK docs: API, APIs, AddToPlaylistIntent, AlarmKit, AlbumView, AppKit, AudioEntity, CSSearchableIndex, ConversationView, EntityQuery.
- Treat this WWDC26 session as the current primary source, then confirm exact API availability against installed SDK docs.

### APIs And Concepts

- AddToPlaylistIntent
- AlarmKit
- AlbumView
- AppKit
- AudioEntity
- CSSearchableIndex
- ConversationView
- EntityQuery
- IndexedEntity
- IndexedEntityQuery
- IntentValueQuery
- NSUserActivity
- NavigationSession
- NowPlayingView
- OwnershipProvidingEntity
- PianoRollView
- PlayAudioIntent
- PlaylistSnippetView

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- UI changes should be checked across light/dark mode, Dynamic Type, keyboard navigation, and platform-specific layout behavior.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/343/4/00190d1d-55b6-4eb2-9ee3-e09f3d8d1c7d/downloads/wwdc2026-343_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/343/4/00190d1d-55b6-4eb2-9ee3-e09f3d8d1c7d/downloads/wwdc2026-343_sd.mp4?dl=1)

### Chapters

- Introduction
- Customize how Siri responds
- Visual responses
- Interaction donations
- Confirmations and entity ownership
- Semantic index with IndexedEntity
- Structured search with IntentValueQuery
- In-app search

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
