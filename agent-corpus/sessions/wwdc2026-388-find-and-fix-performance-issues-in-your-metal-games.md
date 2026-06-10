---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Find And Fix Performance Issues In Your Metal Games
> Neutral research record for Apple WWDC 2026 session 388.

## Entries

- ID: `wwdc2026-388`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/388/
- Apple topics: Developer Tools, Graphics & Games
- Platforms: ios, ipados, macos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Track down hard-to-find game performance issues with powerful metal tools. discover how to collect rich performance data using game performance overview in instruments, run background traces with metalperftrace on macos and control center on ios, and use the new statereporting api to correlate metrics directly to your game's runtime state. turn hours of telemetry into clear, actionable insights.

### What Was Announced Or Covered

- Metal game performance tooling includes Game Performance Overview in Instruments, background traces with metalperftrace, and Control Center trace collection on iOS.
- StateReporting contextualizes metrics by runtime state, while MetricKit extends observation into field data.
- The workflow turns large traces into filtered overviews and aggregate performance analysis.
- Apple groups this session under Developer Tools, Graphics & Games; use it as source material for find and fix performance issues in your metal games.
- track down hard-to-find game performance issues with powerful metal tools. discover how to collect rich performance data using game performance overview in instruments, run background traces with metalperftrace on macos and control center on ios, and use the new statereporting api to correlate metrics directly to your game's runtime state. turn hours of telemetry into clear, actionable insights.
- Chapter coverage includes: Introduction; Metal performance metrics; Trace collection; Analyze performance traces; Contextualize with StateReporting.
- Transcript-derived capability tags: agent, instruments, metrickit, structured output, xcode.
- API and framework terms to verify in SDK docs: API, CPU, DNS, FPS, GPU, HUD, JSON, MetricKit.

### APIs And Concepts

- Metal
- Instruments
- GamePerformanceOverview
- metalperftrace
- StateReporting
- MetricKit
- DNS
- FPS
- HUD
- agent
- structured output
- xcode

### Risks And Constraints

- Performance claims should include trace collection method, game state, hardware, OS, and before/after comparison.
- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/388/4/682e727f-75f9-441f-81d9-2d6f38bde4b0/downloads/wwdc2026-388_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/388/4/682e727f-75f9-441f-81d9-2d6f38bde4b0/downloads/wwdc2026-388_sd.mp4?dl=1)

### Chapters

- Introduction
- Metal performance metrics
- Trace collection
- Analyze performance traces
- Contextualize with StateReporting
- Collect field data with MetricKit
- Next steps

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
