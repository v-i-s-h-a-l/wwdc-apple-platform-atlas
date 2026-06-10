---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Modernize Your UIKit App
> Neutral research record for Apple WWDC 2026 session 278.

## Entries

- ID: `wwdc2026-278`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/278/
- Apple topics: SwiftUI & UI Frameworks
- Platforms: ios, ipados, macos, tvos, visionos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Discover the latest updates to uikit. learn how to update your iphone app layouts to work great when resized with iphone mirroring and on ipad. explore new apis for tab and navigation bars, find out how to prepare your app for new apple intelligence capabilities, and get introduced to a skill for your coding agent of choice that helps modernize your codebase.

### What Was Announced Or Covered

- UIKit modernization now requires scene lifecycle, bounds/trait/effective-geometry based layout, and avoiding UIScreen.main or idiom checks.
- Resizable iPhone environments appear through iPhone Mirroring and iPad, while iPhone apps can opt into sidebars and navigation bar minimization.
- Apple Intelligence can consume drag handlers and View Annotations, and Xcode modernization skills can be exported through xcrun agent skills.
- Apple groups this session under SwiftUI & UI Frameworks; use it as source material for modernize your uikit app.
- discover the latest updates to uikit. learn how to update your iphone app layouts to work great when resized with iphone mirroring and on ipad. explore new apis for tab and navigation bars, find out how to prepare your app for new apple intelligence capabilities, and get introduced to a skill for your coding agent of choice that helps modernize your codebase.
- Chapter coverage includes: Introduction; App adaptivity; Legacy API: App lifecycle; Legacy API: Main screen; Full-screen mode for games.
- Transcript-derived capability tags: agent, app intents, apple intelligence, device hub, siri, xcode.
- API and framework terms to verify in SDK docs: API, APIs, SDK, SDKs, UIKit, UIRequiresFullscreen, UIScene, UISceneDelegate, UITabBarController, UIView.

### APIs And Concepts

- UIScene
- UIView
- ViewAnnotations
- barMinimizationBehavior
- xcrun
- AgentSkills
- SDK
- SDKs
- UIKit
- UIRequiresFullscreen
- UISceneDelegate
- UITabBarController
- WWDC2014
- WWDC24
- WWDC25
- agent
- app intents
- apple intelligence

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.
- UI changes should be checked across light/dark mode, Dynamic Type, keyboard navigation, and platform-specific layout behavior.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/278/4/8c3f2e61-52d3-4915-9543-96e2f13adc8b/downloads/wwdc2026-278_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/278/4/8c3f2e61-52d3-4915-9543-96e2f13adc8b/downloads/wwdc2026-278_sd.mp4?dl=1)

### Chapters

- Introduction
- App adaptivity
- Legacy API: App lifecycle
- Legacy API: Main screen
- Full-screen mode for games
- Legacy API: User interface idiom
- Legacy API: Interface orientation
- UIView Body protocols for motion & location

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
