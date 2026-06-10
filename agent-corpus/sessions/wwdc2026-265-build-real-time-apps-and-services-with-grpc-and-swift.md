---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Build Real-Time Apps And Services With gRPC And Swift
> Neutral research record for Apple WWDC 2026 session 265.

## Entries

- ID: `wwdc2026-265`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/265/
- Apple topics: Developer Tools, Swift
- Platforms: ios, ipados, macos, tvos, visionos, watchos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Build engaging live experiences with grpc in your swift app and backend. grpc is an open-source rpc framework designed for high-performance, bidirectional streaming apis. explore how the grpc swift package provides a modern, safe runtime built with swift concurrency. learn how integrated tools streamline your workflow and help you deliver real-time features with ease.

### What Was Announced Or Covered

- gRPC Swift provides a high-performance RPC path for live apps and services using Swift concurrency and bidirectional streaming.
- The workflow starts from protobuf service definitions, generated Swift code, and Xcode generator configuration.
- Client lifecycle management, scene/background behavior, and child-view propagation are part of the app architecture, not just networking glue.
- The session demonstrates binary efficiency, streaming RPC implementation, and backend deployment considerations.
- Apple groups this session under Developer Tools, Swift; use it as source material for build real-time apps and services with grpc and swift.
- build engaging live experiences with grpc in your swift app and backend. grpc is an open-source rpc framework designed for high-performance, bidirectional streaming apis. explore how the grpc swift package provides a modern, safe runtime built with swift concurrency. learn how integrated tools streamline your workflow and help you deliver real-time features with ease.
- Chapter coverage includes: Introduction; Meet gRPC; App overview and demo setup; Defining the ListRaces RPC; Setting up Xcode to generate gRPC code.
- Transcript-derived capability tags: security, xcode.

### APIs And Concepts

- gRPC
- SwiftConcurrency
- Protobuf
- BidirectionalStreaming
- ClientManager
- AsyncSequence
- AWS
- CNCF
- DNS
- GRPCProtobufGenerator
- GitHub
- LiveStreamView
- OTel
- RPC
- RPCs
- RaceInfoView
- RaceScheduleView
- TLS

### Risks And Constraints

- Agents should separate schema design, generated-code integration, client lifecycle, and service deployment so networking changes remain reviewable.
- For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.
- Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.
- Privacy and security claims should be tied to Apple documentation, entitlement checks, and data-boundary decisions in the app design.
- Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/265/4/05249c6d-4136-4164-a8d0-5db0bbb22c7f/downloads/wwdc2026-265_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/265/4/05249c6d-4136-4164-a8d0-5db0bbb22c7f/downloads/wwdc2026-265_sd.mp4?dl=1)

### Chapters

- Introduction
- Meet gRPC
- App overview and demo setup
- Defining the ListRaces RPC
- Setting up Xcode to generate gRPC code
- Managing the gRPC client lifecycle
- Protobuf message format and binary efficiency
- Implementing a bidirectional streaming RPC

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
