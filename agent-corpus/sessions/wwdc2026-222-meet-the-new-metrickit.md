---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Meet The New Metrickit
> Neutral research record for Apple WWDC 2026 session 222.

## Entries

- ID: `wwdc2026-222`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/222/
- Apple topics: Developer Tools, System Services
- Platforms: ios, ipados, macos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Find and fix performance problems faster than ever. join us to explore how metrickit equips you with vital performance metrics and actionable diagnostics to help you understand exactly where your app has opportunities for improvements. we'll also cover how to intersect your app's metrics and diagnostics by app state by using the statereporting framework, providing you with the full picture to investigate optimizations in your app's experience.

### What Was Announced Or Covered

- MetricKit is the collection layer for real-world app health and gains a rebuilt Swift-first API in iOS 27.
- Metrics cover launch, hangs, animation, CPU, GPU, disk, and network; diagnostics identify code paths for crashes, hangs, and failures.
- StateReporting segments metrics by app flow, while reportable metadata adds structured context.
- Apple groups this session under Developer Tools, System Services; use it as source material for meet the new metrickit.
- find and fix performance problems faster than ever. join us to explore how metrickit equips you with vital performance metrics and actionable diagnostics to help you understand exactly where your app has opportunities for improvements. we'll also cover how to intersect your app's metrics and diagnostics by app state by using the statereporting framework, providing you with the full picture to investigate optimizations in your app's experience.
- Chapter coverage includes: Introduction; Metrics; Diagnostics; Context.
- Transcript-derived capability tags: metrickit.
- API and framework terms to verify in SDK docs: API, APIs, CPU, DNS, GPU, JSON, JSONEncoder, MXMetricManager, MetricKit.

### APIs And Concepts

- MetricKit
- MetricManager
- StateReporting
- ReportableMetadata
- StateEntry
- DNS
- JSONEncoder
- MXMetricManager

### Risks And Constraints

- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/222/4/86b76599-f095-4bd8-8004-f1dbd1bacb84/downloads/wwdc2026-222_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/222/4/86b76599-f095-4bd8-8004-f1dbd1bacb84/downloads/wwdc2026-222_sd.mp4?dl=1)

### Chapters

- Introduction
- Metrics
- Diagnostics
- Context

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
