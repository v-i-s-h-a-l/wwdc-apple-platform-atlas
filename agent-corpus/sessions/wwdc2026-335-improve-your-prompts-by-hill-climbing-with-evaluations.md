---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Improve Your Prompts By Hill-Climbing With Evaluations
> Neutral research record for Apple WWDC 2026 session 335.

## Entries

- ID: `wwdc2026-335`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/335/
- Apple topics: AI & Machine Learning
- Platforms: ios, ipados, macos, visionos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Learn comparative evaluation techniques to guide your prompt engineering and select the right model for your app. explore how to baseline performance, expand your evaluation strategy, and convert results to json for integration with other tools. discover when to apply different prompting strategies and how to iteratively refine prompts for best results.

### What Was Announced Or Covered

- Apple groups this session under AI & Machine Learning; use it as source material for improve your prompts by hill-climbing with evaluations.
- learn comparative evaluation techniques to guide your prompt engineering and select the right model for your app. explore how to baseline performance, expand your evaluation strategy, and convert results to json for integration with other tools. discover when to apply different prompting strategies and how to iteratively refine prompts for best results.
- Chapter coverage includes: Introduction; BookTracker's tagging problem; Analyzing the evaluation results; Drift between judge and human; Measuring drift with Cohen's kappa.
- Transcript-derived capability tags: agent, evaluation, swift testing, xcode.
- API and framework terms to verify in SDK docs: API, APIs.
- Treat this WWDC26 session as the current primary source, then confirm exact API availability against installed SDK docs.

### APIs And Concepts

- agent
- evaluation
- swift testing
- xcode

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/335/4/a464d330-6aa2-456d-9a07-eae997aef08c/downloads/wwdc2026-335_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/335/4/a464d330-6aa2-456d-9a07-eae997aef08c/downloads/wwdc2026-335_sd.mp4?dl=1)

### Chapters

- Introduction
- BookTracker's tagging problem
- Analyzing the evaluation results
- Drift between judge and human
- Measuring drift with Cohen's kappa
- Building a judge alignment evaluation
- Analyzing alignment failures
- Comparative evaluation: control vs experimental

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
