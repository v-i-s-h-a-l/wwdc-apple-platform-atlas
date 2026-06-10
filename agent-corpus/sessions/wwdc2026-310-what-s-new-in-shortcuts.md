---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# What's New In Shortcuts
> Neutral research record for Apple WWDC 2026 session 310.

## Entries

- ID: `wwdc2026-310`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/310/
- Apple topics: AI & Machine Learning, System Services
- Platforms: ios, ipados, macos, visionos, watchos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Explore techniques to build powerful shortcuts using your app's content. new automations unlock additional ways to integrate your app with the system. refine how your app entity is presented to llms using the new “use model” transcript feature. store rich information from your app inside shortcuts that is synced across devices. learn how to combine these features to create intelligent, powerful automations that integrate seamlessly with content and features from your app.

### What Was Announced Or Covered

- Shortcuts gains new automation patterns, richer app-content integration, Use Model transcript behavior, and synced storage for information from apps.
- Use Model helps refine how an app entity is presented to LLMs inside Shortcuts-driven automations.
- The session connects app entities, automation triggers, model-readable content, and cross-device shortcut state.
- Apple groups this session under AI & Machine Learning, System Services; use it as source material for what’s new in shortcuts.
- explore techniques to build powerful shortcuts using your app's content. new automations unlock additional ways to integrate your app with the system. refine how your app entity is presented to llms using the new “use model” transcript feature. store rich information from your app inside shortcuts that is synced across devices. learn how to combine these features to create intelligent, powerful automations that integrate seamlessly with content and features from your app.
- Chapter coverage includes: Introduction; Automations; Use Model; Storage.
- Transcript-derived capability tags: app intents, apple intelligence, siri.
- API and framework terms to verify in SDK docs: API, EntityPropertyQuery, SoupEntity, WWDC25.

### APIs And Concepts

- Shortcuts
- UseModel
- AppEntity
- AppIntents
- Automation
- SyncedStorage
- EntityPropertyQuery
- SoupEntity
- WWDC25
- app intents
- apple intelligence
- siri

### Risks And Constraints

- Model-readable entity descriptions should avoid overexposing private fields and should be tested with realistic user shortcut phrasing.
- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/310/4/50ce70ab-88da-49ff-8c57-d9136d231e76/downloads/wwdc2026-310_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/310/4/50ce70ab-88da-49ff-8c57-d9136d231e76/downloads/wwdc2026-310_sd.mp4?dl=1)

### Chapters

- Introduction
- Automations
- Use Model
- Storage

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
