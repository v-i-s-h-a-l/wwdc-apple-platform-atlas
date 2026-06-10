---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Deliver Workout Insights With Healthkit Workout Zones
> Neutral research record for Apple WWDC 2026 session 207.

## Entries

- ID: `wwdc2026-207`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/207/
- Apple topics: SwiftUI & UI Frameworks, Health & Fitness
- Platforms: ios, ipados, visionos, watchos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Healthkit makes it easier to provide workout insights — like heart rate and cycling power zones — in your app. learn to leverage the built-in, personalized zones or create custom ones. discover how to use the current zone and time spent in each zone to provide meaningful guidance during and after workouts.

### What Was Announced Or Covered

- HealthKit zone groups map workout samples to personalized thresholds.
- Completed workouts expose time spent per zone; live builders emit updates when the current zone changes.
- Apps can use preferred Health settings zones or provide proprietary custom configurations.
- Apple groups this session under SwiftUI & UI Frameworks, Health & Fitness; use it as source material for deliver workout insights with healthkit workout zones.
- healthkit makes it easier to provide workout insights — like heart rate and cycling power zones — in your app. learn to leverage the built-in, personalized zones or create custom ones. discover how to use the current zone and time spent in each zone to provide meaningful guidance during and after workouts.
- Chapter coverage includes: Introduction; Accessing workout zones; Live zone updates; Preferred zones; Custom zones.
- API and framework terms to verify in SDK docs: API, APIs, HKHealthStore, HKLiveWorkoutBuilderDelegate, HKQuantity, HKQuantityType, HKUnit, HKWorkout, HKWorkoutActivity, HKWorkoutBuilder.
- Treat this WWDC26 session as the current primary source, then confirm exact API availability against installed SDK docs.

### APIs And Concepts

- HealthKit
- HKWorkoutZoneGroup
- HKLiveWorkoutZoneUpdate
- HKWorkoutZoneConfiguration
- HKLiveWorkoutBuilder
- HKHealthStore
- HKLiveWorkoutBuilderDelegate
- HKQuantity
- HKQuantityType
- HKUnit
- HKWorkout
- HKWorkoutActivity
- HKWorkoutBuilder

### Risks And Constraints

- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Privacy and security claims should be tied to Apple documentation, entitlement checks, and data-boundary decisions in the app design.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/207/5/8627c1d4-7a34-46f2-8491-f0d1c138edd1/downloads/wwdc2026-207_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/207/5/8627c1d4-7a34-46f2-8491-f0d1c138edd1/downloads/wwdc2026-207_sd.mp4?dl=1)

### Chapters

- Introduction
- Accessing workout zones
- Live zone updates
- Preferred zones
- Custom zones

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
