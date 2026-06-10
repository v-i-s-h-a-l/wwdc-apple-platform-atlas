---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Discover Container Machines
> Neutral research record for Apple WWDC 2026 session 389.

## Entries

- ID: `wwdc2026-389`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/389/
- Apple topics: Swift, System Services, Developer Tools
- Platforms: macos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Meet container machines, a new tool included in container that offers a lightweight persistent linux environment on mac. explore how container machines work and how the design of containerization allows for a performant and seamless experience when developing for linux on macos.

### What Was Announced Or Covered

- Container machines provide lightweight persistent Linux environments on macOS through Apple's container tooling.
- The session covers creation, listing, starting shells, running commands, and understanding containerization design principles.
- This is relevant to local backend services, Linux toolchains, and agent sandboxes on Mac developer machines.
- Apple groups this session under Swift, System Services; use it as source material for discover container machines.
- meet container machines, a new tool included in container that offers a lightweight persistent linux environment on mac. explore how container machines work and how the design of containerization allows for a performant and seamless experience when developing for linux on macos.
- Chapter coverage includes: Introduction; Containerization; Design principles; Container machine; Demo.
- Transcript-derived capability tags: privacy, security, xcode.
- API and framework terms to verify in SDK docs: APIs, CLI, OCI.

### APIs And Concepts

- Container
- ContainerMachine
- Linux
- macOS
- DevelopmentEnvironment
- CLI
- OCI
- privacy
- security
- xcode

### Risks And Constraints

- Agents should keep host filesystem access, networking, credentials, and lifecycle cleanup explicit when using local containers.
- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Privacy and security claims should be tied to Apple documentation, entitlement checks, and data-boundary decisions in the app design.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/389/4/8dd035e7-0481-4028-b4bd-e91ba3634198/downloads/wwdc2026-389_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/389/4/8dd035e7-0481-4028-b4bd-e91ba3634198/downloads/wwdc2026-389_sd.mp4?dl=1)

### Chapters

- Introduction
- Containerization
- Design principles
- Container machine
- Demo
- Next steps

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
