---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Secure Your App: Mitigate Risks To Agentic Features
> Neutral research record for Apple WWDC 2026 session 347.

## Entries

- ID: `wwdc2026-347`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/347/
- Apple topics: AI & Machine Learning, Privacy & Security
- Platforms: ios, ipados, macos, tvos, visionos, watchos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Explore how to evaluate threats from indirect prompt injection, such as data exfiltration and unintended actions. discover system safeguards and security best practices for using app intents and the foundation models framework, including mitigations such as user confirmations, secure prompt design, and authentication.

### What Was Announced Or Covered

- Apple groups this session under AI & Machine Learning, Privacy & Security; use it as source material for secure your app: mitigate risks to agentic features.
- explore how to evaluate threats from indirect prompt injection, such as data exfiltration and unintended actions. discover system safeguards and security best practices for using app intents and the foundation models framework, including mitigations such as user confirmations, secure prompt design, and authentication.
- Chapter coverage includes: Introduction; Risks; Threat modeling; Implementing mitigations; Foundation Models.
- Transcript-derived capability tags: agent, app intents, apple intelligence, evaluation, foundation model, security, siri.
- API and framework terms to verify in SDK docs: API, APIs, AppIntent, BrewingTimerIntent, DeletePhotoIntent, LLM, LLMs, LanguageModelSession, OrderTeaTool, PII.
- Treat this WWDC26 session as the current primary source, then confirm exact API availability against installed SDK docs.

### APIs And Concepts

- AppIntent
- BrewingTimerIntent
- DeletePhotoIntent
- LLM
- LLMs
- LanguageModelSession
- OrderTeaTool
- PII
- PostAndFetchPublicFeedTool
- REDACTED
- agent
- app intents
- apple intelligence
- evaluation
- foundation model
- security
- siri

### Risks And Constraints

- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Privacy and security claims should be tied to Apple documentation, entitlement checks, and data-boundary decisions in the app design.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/347/4/07cdbfeb-280a-49e3-aeba-c18fbb0d32b4/downloads/wwdc2026-347_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/347/4/07cdbfeb-280a-49e3-aeba-c18fbb0d32b4/downloads/wwdc2026-347_sd.mp4?dl=1)

### Chapters

- Introduction
- Risks
- Threat modeling
- Implementing mitigations
- Foundation Models
- App Intents

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
