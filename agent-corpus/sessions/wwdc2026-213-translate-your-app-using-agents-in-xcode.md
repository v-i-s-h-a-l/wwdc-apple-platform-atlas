---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Translate Your App Using Agents In Xcode
> Neutral research record for Apple WWDC 2026 session 213.

## Entries

- ID: `wwdc2026-213`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/213/
- Apple topics: AI & Machine Learning, Developer Tools
- Platforms: ios, ipados, macos, tvos, visionos, watchos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Find out how xcode and coding agents help you translate string catalogs using the context of your app. we'll walk through strategies for reviewing translated output and iterating on your localizations, so you can deliver a tailored experience to people around the world.

### What Was Announced Or Covered

- Xcode agents use String Catalog context from where and how strings appear in the app.
- Agents can build targets to discover user-facing strings and generate translated catalogs in batches.
- Review must include truncation, localized schemes, terminology glossaries, and TestFlight feedback from native speakers.
- Apple groups this session under AI & Machine Learning, Developer Tools; use it as source material for translate your app using agents in xcode.
- find out how xcode and coding agents help you translate string catalogs using the context of your app. we'll walk through strategies for reviewing translated output and iterating on your localizations, so you can deliver a tailored experience to people around the world.
- Chapter coverage includes: Introduction; Add translations; Review and iterate; Best practices.
- Transcript-derived capability tags: agent, swiftui, xcode.
- API and framework terms to verify in SDK docs: AGENTS, APIs, LLMs, TRANSLATION.

### APIs And Concepts

- StringCatalogs
- TestFlight
- XcodeAgents
- AGENTS
- LLMs
- TRANSLATION
- agent
- swiftui
- xcode

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.
- UI changes should be checked across light/dark mode, Dynamic Type, keyboard navigation, and platform-specific layout behavior.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/213/4/be1ee662-a447-4df4-89a5-5411447c0eeb/downloads/wwdc2026-213_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/213/4/be1ee662-a447-4df4-89a5-5411447c0eeb/downloads/wwdc2026-213_sd.mp4?dl=1)

### Chapters

- Introduction
- Add translations
- Review and iterate
- Best practices

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
