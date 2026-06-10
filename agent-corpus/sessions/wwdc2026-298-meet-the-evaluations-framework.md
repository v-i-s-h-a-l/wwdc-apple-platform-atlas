---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Meet The Evaluations Framework
> Neutral research record for Apple WWDC 2026 session 298.

## Entries

- ID: `wwdc2026-298`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/298/
- Apple topics: AI & Machine Learning
- Platforms: ios, ipados, macos, visionos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Learn how to evaluate model-driven experiences using the evaluations framework. in a probabilistic world, unit tests alone won't suffice. discover how to define metrics, automatically grade outputs, and aggregate statistics to ensure your ai-powered features perform reliably across apple's platforms.

### What Was Announced Or Covered

- Apple groups this session under AI & Machine Learning; use it as source material for meet the evaluations framework.
- learn how to evaluate model-driven experiences using the evaluations framework. in a probabilistic world, unit tests alone won't suffice. discover how to define metrics, automatically grade outputs, and aggregate statistics to ensure your ai-powered features perform reliably across apple's platforms.
- Chapter coverage includes: Introduction; Demo app Book Tacker: a manual evaluation; Building your first evaluation; Running the evaluation and reading the report; Building robust datasets.
- Transcript-derived capability tags: agent, apple intelligence, evaluation, foundation model, swift testing, xcode.
- API and framework terms to verify in SDK docs: API.
- Treat this WWDC26 session as the current primary source, then confirm exact API availability against installed SDK docs.

### APIs And Concepts

- agent
- apple intelligence
- evaluation
- foundation model
- swift testing
- xcode

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Privacy and security claims should be tied to Apple documentation, entitlement checks, and data-boundary decisions in the app design.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/298/5/0ffb7161-1edb-4e6f-872d-55be82c4402d/downloads/wwdc2026-298_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/298/5/0ffb7161-1edb-4e6f-872d-55be82c4402d/downloads/wwdc2026-298_sd.mp4?dl=1)

### Chapters

- Introduction
- Demo app Book Tacker: a manual evaluation
- Building your first evaluation
- Running the evaluation and reading the report
- Building robust datasets
- Refining metrics and evaluators
- Evaluation-driven development and hill-climbing
- Model judges: qualitative metrics

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
