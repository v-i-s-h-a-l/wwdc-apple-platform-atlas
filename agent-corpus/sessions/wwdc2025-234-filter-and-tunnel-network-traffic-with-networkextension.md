---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Filter And Tunnel Network Traffic With Networkextension
> Neutral research record for Apple WWDC 2025 session 234.

## Entries

- ID: `wwdc2025-234`
- Coverage: `metadata-only`
- Analysis status: `metadata-only`
- Apple video: https://developer.apple.com/videos/play/wwdc2025/234/
- Apple topics: System Services
- Platforms: ios, ipados, macos, tvos, visionos, watchos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Learn about the apis in the networkextension framework that give your app the power and flexibility to extend the system's core networking features — like implementing network content filters, creating and managing vpn configurations, and more. in ios, ipados and macos 26, you can now build robust content filters that make traffic decisions using the entire url — not just the hostname — all without compromising privacy and security. we'll start by briefly covering many of the key use cases for the networkextension framework, including network relays and vpn. then, we'll dive into the new url filter api and its key components, including private information retrieval, privacy pass, and more.

### What Was Announced Or Covered

- Apple groups this session under System Services; use it as source material for filter and tunnel network traffic with networkextension.
- learn about the apis in the networkextension framework that give your app the power and flexibility to extend the system's core networking features — like implementing network content filters, creating and managing vpn configurations, and more. in ios, ipados and macos 26, you can now build robust content filters that make traffic decisions using the entire url — not just the hostname — all without compromising privacy and security. we'll start by briefly covering many of the key use cases for the networkextension framework, including network relays and vpn. then, we'll dive into the new url filter api and its key components, including private information retrieval, privacy pass, and more.
- Chapter coverage includes: Welcome; Tour NetworkExtension; Access remote resources; Filter content; Create URL filters.
- Metadata-derived capability tags: privacy, security.
- Treat this WWDC25 session as prerequisite context for understanding the WWDC26 changes, not as the newest API source.

### APIs And Concepts

- privacy
- security

### Risks And Constraints

- Privacy and security claims should be tied to Apple documentation, entitlement checks, and data-boundary decisions in the app design.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2025/234/4/54f59553-dbd4-48aa-8240-99dbbc735d7b/downloads/wwdc2025-234_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2025/234/4/54f59553-dbd4-48aa-8240-99dbbc735d7b/downloads/wwdc2025-234_sd.mp4?dl=1)

### Chapters

- Welcome
- Tour NetworkExtension
- Access remote resources
- Filter content
- Create URL filters

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
