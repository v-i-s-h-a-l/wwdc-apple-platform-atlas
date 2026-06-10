#!/usr/bin/env python3
"""Build a transcript-derived WWDC Session Atlas without caching full transcripts."""

from __future__ import annotations

import html
import json
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any
from urllib.parse import urljoin
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "sources" / "cache"
OUT = ROOT / "data" / "session-atlas.json"

WWDC26_INDEX = "https://developer.apple.com/videos/wwdc2026/"
WWDC25_INDEX = "https://developer.apple.com/videos/wwdc2025/"

RELEVANT_TERMS = [
    "foundation model",
    "core ai",
    "apple intelligence",
    "app intents",
    "siri",
    "swiftui",
    "swiftdata",
    "swift testing",
    "xcode",
    "device hub",
    "instruments",
    "metrickit",
    "core spotlight",
    "vision",
    "visual intelligence",
    "mlx",
    "core ml",
    "speech",
    "accessibility",
    "webkit",
    "security",
    "privacy",
    "agent",
    "evaluation",
    "structured output",
    "tool calling",
]

PHASE1_TRANSCRIPT_KEYS = {
    ("2026", sid)
    for sid in [
        "203",
        "204",
        "207",
        "213",
        "219",
        "220",
        "222",
        "223",
        "227",
        "240",
        "241",
        "242",
        "243",
        "246",
        "258",
        "259",
        "260",
        "261",
        "267",
        "268",
        "269",
        "271",
        "272",
        "274",
        "275",
        "277",
        "278",
        "289",
        "298",
        "299",
        "321",
        "322",
        "324",
        "325",
        "326",
        "334",
        "335",
        "339",
        "343",
        "344",
        "345",
        "347",
        "370",
        "372",
    ]
}

PHASE2_TRANSCRIPT_KEYS = {
    ("2026", sid)
    for sid in [
        "215",
        "216",
        "221",
        "232",
        "233",
        "250",
        "256",
        "262",
        "265",
        "292",
        "295",
        "303",
        "305",
        "310",
        "312",
        "314",
        "315",
        "319",
        "328",
        "330",
        "357",
        "388",
        "389",
    ]
} | {
    ("2025", sid)
    for sid in [
        "219",
        "220",
        "222",
        "225",
        "226",
        "229",
        "231",
        "238",
        "243",
        "282",
        "284",
        "291",
        "308",
        "310",
        "316",
        "323",
        "337",
        "344",
        "356",
    ]
}

TRANSCRIPT_KEYS = PHASE1_TRANSCRIPT_KEYS | PHASE2_TRANSCRIPT_KEYS

RESEARCH_QUEUE: dict[tuple[str, str], dict[str, str]] = {
    ("2026", "262"): {
        "priority": "P0",
        "wave": "Developer Workflow",
        "reason": "Swift language, concurrency, testing, subprocess, Foundation, embedded Swift, interoperability, and performance guidance affect almost every future Apple-platform codebase.",
    },
    ("2026", "295"): {
        "priority": "P0",
        "wave": "Developer Workflow",
        "reason": "AppIntentsTesting is the verification backbone for Siri, Shortcuts, Spotlight, entities, queries, and view annotations.",
    },
    ("2026", "310"): {
        "priority": "P0",
        "wave": "App Intelligence",
        "reason": "Shortcuts, Use Model transcripts, and app-entity storage connect agent answers to user automations and synced content.",
    },
    ("2026", "319"): {
        "priority": "P0",
        "wave": "App Intelligence",
        "reason": "Private Cloud Compute changes model routing, availability, reasoning levels, context size, usage limits, and fallback design.",
    },
    ("2026", "232"): {
        "priority": "P0",
        "wave": "App Intelligence",
        "reason": "Local MLX agents on Mac are directly relevant to agentic development loops, privacy, offline use, and tool integration.",
    },
    ("2026", "250"): {
        "priority": "P0",
        "wave": "Platform UI",
        "reason": "Design principles shape how agents should evaluate generated UI beyond API correctness.",
    },
    ("2026", "292"): {
        "priority": "P0",
        "wave": "Platform UI",
        "reason": "Search is a common AI-adjacent information architecture surface and needs platform-specific placement, navigation, and content guidance.",
    },
    ("2026", "221"): {
        "priority": "P0",
        "wave": "Platform UI",
        "reason": "Dynamic Type on tvOS expands accessibility coverage beyond iOS/macOS and informs large-screen UI review.",
    },
    ("2026", "303"): {
        "priority": "P1",
        "wave": "System Frameworks",
        "reason": "Launch responsiveness for camera workflows is a high-signal performance case for agents working on media apps.",
    },
    ("2026", "305"): {
        "priority": "P1",
        "wave": "System Frameworks",
        "reason": "Core Image RAW processing is relevant for creative and camera workflows that combine deterministic imaging with generative features.",
    },
    ("2026", "265"): {
        "priority": "P1",
        "wave": "System Frameworks",
        "reason": "gRPC Swift links Swift concurrency, real-time bidirectional APIs, service deployment, and generated code workflows.",
    },
    ("2026", "312"): {
        "priority": "P1",
        "wave": "System Frameworks",
        "reason": "Now Playing is a system surface for media state, remote control behavior, and cross-device continuity.",
    },
    ("2026", "256"): {
        "priority": "P1",
        "wave": "Accessibility And Media",
        "reason": "Generated subtitles and subtitle styles combine accessibility, media, and user-facing quality details.",
    },
    ("2026", "233"): {
        "priority": "P1",
        "wave": "App Intelligence",
        "reason": "Distributed MLX inference and fine-tuning define when local Mac clusters are viable versus cloud infrastructure.",
    },
    ("2026", "328"): {
        "priority": "P1",
        "wave": "App Intelligence",
        "reason": "Numerical computing in Swift with MLX informs custom model and high-performance Swift examples.",
    },
    ("2026", "330"): {
        "priority": "P1",
        "wave": "App Intelligence",
        "reason": "Metal tensors are the low-level optimization path for custom ML operations and model performance.",
    },
    ("2026", "357"): {
        "priority": "P1",
        "wave": "Developer Workflow",
        "reason": "Agentic game porting is a concrete example of coding agents plus domain tools, Metal adoption, and autonomous troubleshooting.",
    },
    ("2026", "388"): {
        "priority": "P1",
        "wave": "Developer Workflow",
        "reason": "Metal game performance adds field telemetry, StateReporting, MetricKit, and trace collection patterns.",
    },
    ("2026", "389"): {
        "priority": "P1",
        "wave": "Developer Workflow",
        "reason": "Container machines affect local development environments for Linux services, toolchains, and cross-platform agents on macOS.",
    },
    ("2026", "215"): {
        "priority": "P2",
        "wave": "Safari And Web",
        "reason": "The HTML model element is relevant to product visualization, spatial web, and embedded web/native comparisons.",
    },
    ("2026", "216"): {
        "priority": "P2",
        "wave": "Safari And Web",
        "reason": "Safari web extensions matter for privacy-preserving browser automation, native messaging, and distribution.",
    },
    ("2026", "314"): {
        "priority": "P2",
        "wave": "Safari And Web",
        "reason": "CSS Grid Lanes affects dense adaptive layouts and accessibility-preserving masonry-like designs.",
    },
    ("2026", "315"): {
        "priority": "P2",
        "wave": "Safari And Web",
        "reason": "Customizable select shows how native controls can gain design-system flexibility without losing accessibility semantics.",
    },
}

DOCS = {
    "Foundation Models": "https://developer.apple.com/documentation/foundationmodels",
    "Core AI": "https://developer.apple.com/documentation/coreai",
    "App Intents": "https://developer.apple.com/documentation/appintents",
    "Core Spotlight": "https://developer.apple.com/documentation/corespotlight",
    "SwiftUI": "https://developer.apple.com/documentation/swiftui",
    "SwiftData": "https://developer.apple.com/documentation/swiftdata",
    "Swift Testing": "https://developer.apple.com/documentation/testing",
    "Xcode": "https://developer.apple.com/xcode/",
    "Instruments": "https://developer.apple.com/documentation/xcode/improving-your-app-s-performance",
    "Vision": "https://developer.apple.com/documentation/vision",
}

INDUSTRY = [
    {
        "area": "Structured outputs",
        "sources": [
            "https://platform.openai.com/docs/guides/structured-outputs",
            "https://ai.google.dev/gemini-api/docs/structured-output",
        ],
        "agentUse": "Use Apple Generable/Guided Generation for Swift-native app flows; compare against provider JSON Schema when building cross-platform agents.",
    },
    {
        "area": "Tool calling",
        "sources": [
            "https://platform.openai.com/docs/api-reference/responses/create",
            "https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/overview/",
            "https://ai.google.dev/gemini-api/docs/function-calling",
        ],
        "agentUse": "Map Apple Tools and App Intents to narrow, typed, confirmable actions; avoid broad command tools unless isolated.",
    },
    {
        "area": "Local/private inference",
        "sources": [
            "https://developer.apple.com/documentation/foundationmodels",
            "https://developer.apple.com/documentation/coreai",
            "https://ml-explore.github.io/mlx/build/html/index.html",
        ],
        "agentUse": "Prefer local/PCC routes for user-private context, then provider models when availability, model family, or cross-platform reach dominates.",
    },
]

CURATED_SESSION_OVERLAYS: dict[tuple[str, str], dict[str, Any]] = {
    ("2026", "258"): {
        "highlights": [
            "Xcode 27 adds a redesigned customizable toolbar and themes, subtler predictive inline issues, and stronger support for untitled projects and standalone Swift files.",
            "Agent conversations live in editor panes with artifacts, screenshots, previews, `/plan`, and reusable project context.",
            "Device Hub unifies simulators and real devices, while Organizer adds storage, animation hitch metrics, Metric Goals, and generated recommendations.",
            "Instruments adds Top Functions and the Xcode Cloud onboarding flow is streamlined for faster build/test automation.",
        ],
        "apiTerms": ["Xcode", "DeviceHub", "TopFunctions", "MetricGoals", "StringCatalogs", "XcodeCloud"],
        "agentNotes": [
            "Use Xcode 27 notes to define the agent loop: inspect context, plan, edit, build, preview, profile, and verify.",
            "Ask agents for localized artifacts, previews, and screenshots rather than accepting prose-only claims.",
        ],
    },
    ("2026", "259"): {
        "highlights": [
            "Xcode agents can inspect project structure, build settings, open files, selected code, and Apple documentation.",
            "Plan mode scopes broad work before edits, while queued messages, image attachments, inline annotations, and artifacts keep collaboration inspectable.",
            "Sub-agent orchestration can split localization, accessibility, and UI refinement into parallel reviewable workstreams.",
        ],
        "apiTerms": ["AppleDocumentSearch", "XcodeAgents", "PlanMode", "Artifacts", "SubAgents"],
        "agentNotes": [
            "Require `/plan` before broad edits and require a concrete verification surface for each agent task.",
            "Use agent walkthroughs to produce architecture notes that can be fed back into later coding sessions.",
        ],
    },
    ("2026", "227"): {
        "highlights": [
            "Agents plus previews enable native UI prototype iteration inside Xcode.",
            "Prompts should ask for multiple UI directions, realistic data, empty states, long labels, and unbounded lists.",
            "Human judgment still owns taste, information hierarchy, and final interaction polish.",
        ],
        "agentNotes": [
            "Ask for several UI variants first, then remix the strongest choices into a refined implementation.",
            "Use previews and screenshots as review artifacts for each iteration.",
        ],
    },
    ("2026", "213"): {
        "highlights": [
            "Xcode agents use String Catalog context from where and how strings appear in the app.",
            "Agents can build targets to discover user-facing strings and generate translated catalogs in batches.",
            "Review must include truncation, localized schemes, terminology glossaries, and TestFlight feedback from native speakers.",
        ],
        "apiTerms": ["StringCatalogs", "TestFlight", "XcodeAgents"],
        "agentNotes": ["Make strings localizable before asking agents to translate, then verify layouts under target languages."],
    },
    ("2026", "260"): {
        "highlights": [
            "Device Hub ships with Xcode 27 as a single control surface for devices and simulators.",
            "It supports live display, touch, hardware controls, zoom, resize, keyboard capture, diagnostics, app containers, profiles, and provisioning.",
            "Bug reproduction can mirror a real device configuration into a simulator, and `devicectl` supports automation and CI.",
        ],
        "apiTerms": ["DeviceHub", "devicectl"],
        "agentNotes": ["Use Device Hub as the bridge between code edits and reproducible device evidence."],
    },
    ("2026", "267"): {
        "highlights": [
            "Swift Testing migration should be incremental: keep existing XCTest until touched and write new tests with Swift Testing.",
            "Interoperability modes include Limited, Complete, Strict, and None.",
            "Migration patterns include `Issue.record`, `Test.cancel`, `#require`, parameterized tests, and exit tests for crash/precondition paths.",
        ],
        "apiTerms": ["SwiftTesting", "XCTest", "Issue", "Test", "ParameterizedTests", "ExitTests"],
        "agentNotes": ["Have agents migrate one file or active area at a time, then verify in Xcode Cloud or local test plans."],
    },
    ("2026", "268"): {
        "highlights": [
            "Responsiveness work starts with Time Profiler and branches into high-CPU work, execution contention, or system blocking.",
            "Call Tree, Flame Graph, and Top Functions expose different CPU views; Swift Executors can reveal Main Actor saturation.",
            "System Trace plus Inspector helps diagnose low-CPU main-thread blocking such as synchronous file I/O.",
            "Fixes should be verified with comparison runs, not assumed from code inspection.",
        ],
        "apiTerms": ["Instruments", "TimeProfiler", "TopFunctions", "SwiftExecutors", "SystemTrace", "MainActor"],
        "agentNotes": ["For performance tasks, require trace evidence before accepting an agent's fix."],
    },
    ("2026", "243"): {
        "highlights": [
            "Foundation Models apps need observability because outputs are probabilistic and multi-model pipelines can hide slow or failing steps.",
            "The Foundation Models Instruments template shows instructions, prompts, responses, errors, sessions, requests, inferences, and tool calls.",
            "Important metrics include time-to-first-token, tokens-per-second, total latency, prompt size, model configuration, and streaming behavior.",
            "Traces may contain sensitive prompt data, so collection and sharing need privacy discipline.",
        ],
        "apiTerms": ["FoundationModels", "Instruments", "TimeToFirstToken", "TokensPerSecond", "ToolCalls"],
        "agentNotes": ["Debug agentic app behavior with Instruments plus Evaluations; do not rely only on one successful generated response."],
    },
    ("2026", "261"): {
        "highlights": [
            "Xcode Cloud builds and tests Apple-platform code in parallel across devices, OS versions, and Xcode versions.",
            "Build machines are ephemeral, TestFlight distribution can be configured from Xcode, and webhooks expose lifecycle payloads.",
            "Additional repositories support split or shared codebases.",
        ],
        "apiTerms": ["XcodeCloud", "TestFlight", "Webhooks"],
        "agentNotes": ["Use Xcode Cloud as regression infrastructure after agent-assisted changes land."],
    },
    ("2026", "222"): {
        "highlights": [
            "MetricKit is the collection layer for real-world app health and gains a rebuilt Swift-first API in iOS 27.",
            "Metrics cover launch, hangs, animation, CPU, GPU, disk, and network; diagnostics identify code paths for crashes, hangs, and failures.",
            "StateReporting segments metrics by app flow, while reportable metadata adds structured context.",
        ],
        "apiTerms": ["MetricKit", "MetricManager", "StateReporting", "ReportableMetadata", "StateEntry"],
        "agentNotes": ["Use MetricKit and StateReporting to monitor whether agent-authored changes improve or regress real user flows."],
    },
    ("2026", "269"): {
        "highlights": [
            "SwiftUI auto-adopts much of Liquid Glass, but mixed UIKit/SwiftUI apps need extra resizability and presentation review.",
            "Document APIs add custom creation sources, direct URL access, writable snapshots, and large-document performance improvements.",
            "Reorderable containers work beyond List, including grids and watchOS; swipe actions expand beyond list rows.",
            "AsyncImage now honors HTTP caching and supports custom URLRequest or URLSession, while @State is macro-backed with lazy class initialization.",
        ],
        "apiTerms": ["SwiftUI", "DocumentCreationSource", "FileDocument", "ReferenceFileDocument", "reorderable", "reorderContainer", "AsyncImage", "State", "ContentBuilder"],
        "agentNotes": ["Use this as the high-priority SwiftUI rollup seed for documents, reordering, image loading, and performance-sensitive state."],
    },
    ("2026", "321"): {
        "highlights": [
            "Lazy stacks estimate sizes and resolve subviews in ways that affect scroll accuracy and programmatic scrolling.",
            "Filter data before view construction instead of conditionally hiding rows inside lazy content.",
            "Environment changes can trigger offscreen body work; cache-backed observable loaders can cooperate better with internal prefetching.",
            "Avoid post-appearance size changes that move offscreen scroll targets.",
        ],
        "apiTerms": ["LazyVStack", "LazyHStack", "ScrollView", "scrollTransition", "Prefetching"],
        "agentNotes": ["Use this session for dense list/browser performance guidance: stable layout, data-level filtering, and predictable scroll targets."],
    },
    ("2026", "271"): {
        "highlights": [
            "New reordering APIs handle simple rearranging without full drag/drop machinery.",
            "`reorderable` plus `reorderContainer` enables card movement, and drag containers allow multiple selected items to lift together.",
            "Preview formations and Drag Configuration customize app-specific drag/drop rules and visuals.",
            "Transferable remains the conceptual foundation for richer drag/drop payloads.",
        ],
        "apiTerms": ["reorderable", "reorderContainer", "dragContainer", "DragConfiguration", "Transferable"],
        "agentNotes": ["Treat this as an implementation recipe for card grids, media boards, and editor canvases."],
    },
    ("2026", "272"): {
        "highlights": [
            "@Observable can modernize NSView/UIKit view updates before a full SwiftUI migration.",
            "Observation can track reads in draw, layout, and update-layer paths for legacy views.",
            "SwiftUI Canvas, NSHostingView, NSGestureRecognizerRepresentable, NSHostingMenu, and NSHostingSceneRepresentation support incremental migration.",
        ],
        "apiTerms": ["Observable", "NSObservationTrackingEnabled", "UIObservationTrackingEnabled", "NSHostingView", "NSGestureRecognizerRepresentable", "NSHostingMenu", "NSHostingSceneRepresentation"],
        "agentNotes": ["Use for mixed legacy apps where a rewrite is too risky but new SwiftUI islands are useful."],
    },
    ("2026", "274"): {
        "highlights": [
            "@Query gains sectioning through sectionBy.",
            "SwiftData can store custom or third-party Codable types when they cannot become @Model types.",
            "ResultsObserver, ModelResultsObserver, HistoryObserver, and ModelContext.fetchHistory support non-SwiftUI observation and persistent-history workflows.",
        ],
        "apiTerms": ["SwiftData", "Query", "sectionBy", "Codable", "ResultsObserver", "ModelResultsObserver", "HistoryObserver", "ModelContext"],
        "agentNotes": ["Roll up SwiftData as moving beyond SwiftUI-only usage into observers, history, and sync-aware architectures."],
    },
    ("2026", "275"): {
        "highlights": [
            "The code-along identifies transient SwiftUI state worth persisting, converts observable types to @Model, and attaches schema with modelContainer.",
            "It uses Codable custom values, relationships, @Query, FetchDescriptor, SortDescriptor, and dynamic query initialization.",
            "The implementation handles search, recent views, errors, and date-edited side effects.",
        ],
        "apiTerms": ["Model", "modelContainer", "Query", "FetchDescriptor", "SortDescriptor", "SwiftData"],
        "agentNotes": ["Use this as the concrete SwiftData implementation baseline for examples and agent prompts."],
    },
    ("2026", "322"): {
        "highlights": [
            "SwiftUI graphics effects are framed as a pipeline of small layout and rendering stages.",
            "Layer shaders pass SwiftUI data into Metal shaders; shaders are stateless, so time is driven externally.",
            "The pattern supports transcript-style scrolling, active-row highlighting, alignment guides, canvases, scroll views, and layered visuals.",
        ],
        "apiTerms": ["Shader", "layerEffect", "Metal", "AlignmentGuide", "Canvas"],
        "agentNotes": ["Use for rich editor, reading, and creative-canvas UI recipes."],
    },
    ("2026", "278"): {
        "highlights": [
            "UIKit modernization now requires scene lifecycle, bounds/trait/effective-geometry based layout, and avoiding UIScreen.main or idiom checks.",
            "Resizable iPhone environments appear through iPhone Mirroring and iPad, while iPhone apps can opt into sidebars and navigation bar minimization.",
            "Apple Intelligence can consume drag handlers and View Annotations, and Xcode modernization skills can be exported through xcrun agent skills.",
        ],
        "apiTerms": ["UIScene", "UIView", "ViewAnnotations", "barMinimizationBehavior", "xcrun", "AgentSkills"],
        "agentNotes": ["Critical for existing apps: ask agents to modernize scene lifecycle, geometry assumptions, navigation, and annotations separately."],
    },
    ("2026", "289"): {
        "highlights": [
            "AppKit modernization favors gesture recognizers, control events, and view APIs over mouseDown tracking loops.",
            "macOS 27 adds custom text selection APIs for standard text behavior in any view.",
            "Keyboard navigation, status items, graceful termination, state restoration, Liquid Glass, corner configuration, and concentricity need explicit review.",
        ],
        "apiTerms": ["AppKit", "GestureRecognizers", "TextSelection", "StateRestoration", "cornerConfiguration", "Concentricity"],
        "agentNotes": ["Use as a separate AppKit modernization checklist rather than merging it into SwiftUI guidance."],
    },
    ("2026", "370"): {
        "highlights": [
            "Built-in text views provide platform behavior, while custom TextKit views expose storage, layout, and rendering control.",
            "New rendering surface APIs help customize text view rendering; UITextView and NSTextView can be wrapped into SwiftUI.",
            "Line numbers, collapsible sections, and reusable text attachment view providers support serious editor and reader apps.",
        ],
        "apiTerms": ["TextKit", "NSTextContentStorage", "NSTextLayoutManager", "NSTextViewportLayoutController", "NSTextViewportRenderingSurface", "NSTextAttachmentViewProvider"],
        "agentNotes": ["Editor and reader apps need TextKit details, not only SwiftUI TextEditor summaries."],
    },
    ("2026", "277"): {
        "highlights": [
            "Widgets are SwiftUI views even when the containing app is UIKit-based.",
            "Reuse timeline providers across families, declare supported families thoughtfully, and use widgetURL for deep links.",
            "App Intents configure widgets, while tinted/accented environments require explicit rendering choices.",
        ],
        "apiTerms": ["WidgetKit", "TimelineProvider", "widgetURL", "AppIntents", "widgetAccentedRenderingMode"],
        "agentNotes": ["Roll up with Live Activities as SwiftUI-powered system surfaces."],
    },
    ("2026", "223"): {
        "highlights": [
            "Live Activities separate static attributes from dynamic content state, and each presentation is a SwiftUI view.",
            "iOS 27 adds landscape Dynamic Island visibility plus limited-width and small family layouts.",
            "ActivityKit, push notifications, and App Intents drive timely interactive updates.",
        ],
        "apiTerms": ["ActivityKit", "WidgetKit", "DynamicIsland", "AppIntents"],
        "agentNotes": ["Include data/update lifecycle and interaction rules, not just visual placements."],
    },
    ("2026", "203"): {
        "highlights": [
            "PencilKit remains the low-latency drawing core, while PaperKit builds on it.",
            "Handwriting recognition can power indexing, find, and text extraction.",
            "iOS 27 improves model access, stable identity, selection changes, stroke slicing, masks, path conversion, and Metal-backed rendering.",
        ],
        "apiTerms": ["PencilKit", "PKCanvasView", "PKDrawing", "PKStroke", "PKStrokePath", "PKStrokeRecognizer", "UIFindInteraction"],
        "agentNotes": ["Connect to creative-canvas, handwriting, indexing, and generative layout workflows."],
    },
    ("2026", "372"): {
        "highlights": [
            "PaperKit is Apple’s canvas and markup layer for Notes-style experiences.",
            "New data model APIs expose markup subelements, support programmatic creation and modification, and allow read-only template elements.",
            "Adornments provide non-persisted custom controls that track zoom and scroll, and images can be placed into the canvas.",
        ],
        "apiTerms": ["PaperKit", "PaperMarkup", "Adornments", "MarkupElements"],
        "agentNotes": ["Use with PencilKit and Image Playground style workflows for creative document apps."],
    },
    ("2026", "219"): {
        "highlights": [
            "Reading apps need granular line, word, and character navigation.",
            "Standard UIKit and SwiftUI text views already provide much of this; custom text should adopt UITextInput fully.",
            "Navigation APIs, linked groups, page-turn traits, editor rotors, and custom actions improve assistive reading and editing workflows.",
        ],
        "apiTerms": ["UITextInput", "accessibilityNextTextNavigationElement", "accessibilityLinkedGroup", "causesPageTurn", "UIAccessibilityReadingContent"],
        "agentNotes": ["Use as a checklist for custom readers, editors, and paginated text surfaces."],
    },
    ("2026", "220"): {
        "highlights": [
            "Custom controls need label, value, hint, activation point, announcements, and current state through accessibilityValue.",
            "Custom actions provide non-gesture alternatives; direct interaction and passthrough gestures are reserved for controls that need native gestures.",
            "Complex visual controls require semantic bounds and a deliberate assistive interaction model.",
        ],
        "apiTerms": ["Accessibility", "accessibilityValue", "CustomActions", "ActivationPoint", "DirectTouch"],
        "agentNotes": ["Use as a reusable review checklist for generated SwiftUI custom controls."],
    },
    ("2026", "207"): {
        "highlights": [
            "HealthKit zone groups map workout samples to personalized thresholds.",
            "Completed workouts expose time spent per zone; live builders emit updates when the current zone changes.",
            "Apps can use preferred Health settings zones or provide proprietary custom configurations.",
        ],
        "apiTerms": ["HealthKit", "HKWorkoutZoneGroup", "HKLiveWorkoutZoneUpdate", "HKWorkoutZoneConfiguration", "HKLiveWorkoutBuilder"],
        "agentNotes": ["Useful as a HealthKit visualization input for SwiftUI dashboards and live workout surfaces."],
    },
    ("2026", "204"): {
        "highlights": [
            "Safari 27 includes broad quality work plus many beta web platform features.",
            "CSS Grid Lanes enables masonry-like layouts, Customizable Select keeps native form/accessibility benefits, and HTML Model supports 3D product views.",
            "Immersive website environments add a fullscreen-like immersive API, while Safari web extension packaging improves distribution.",
        ],
        "apiTerms": ["WebKit", "CSSGridLanes", "CustomizableSelect", "HTMLModel", "ImmersiveAPI", "SafariWebExtensions", "MapKitJS"],
        "agentNotes": ["Peripheral to native UI, but relevant for embedded web content, Safari extensions, and visionOS web surfaces."],
    },
    ("2026", "262"): {
        "highlights": [
            "Swift updates span everyday language ergonomics, anyAppleOS availability, warning control with @diagnose, module selectors, and editor support.",
            "Concurrency guidance includes better diagnostics and stronger Sendable-related behavior for code that crosses task boundaries.",
            "Library updates cover Swift Testing, Subprocess 1.0, Foundation, cross-platform Swift, Swift-C interoperability, Swift-Java, WebAssembly, and JavascriptKit.",
            "Performance work includes optimizer control with @inline(always) and @specialized plus ownership-system and noncopyable-type improvements.",
            "New standard library types such as UniqueBox, UniqueArray, and Ref are positioned for safer high-performance code.",
        ],
        "apiTerms": ["Swift", "anyAppleOS", "diagnose", "SwiftTesting", "Subprocess", "Foundation", "Sendable", "CInterop", "JavaInterop", "WebAssembly", "JavascriptKit", "EmbeddedSwift", "inline", "specialized", "Noncopyable", "UniqueBox", "UniqueArray", "Ref"],
        "risksAndConstraints": [
            "Beta language and library features need exact compiler and SDK verification before an agent turns examples into production code.",
            "Performance annotations should be justified with profiling evidence rather than applied broadly.",
        ],
        "agentNotes": ["Use as the Swift language baseline for future agents: concurrency, tests, subprocesses, interop, embedded targets, and performance tuning should be routed to separate implementation tasks."],
    },
    ("2026", "265"): {
        "highlights": [
            "gRPC Swift provides a high-performance RPC path for live apps and services using Swift concurrency and bidirectional streaming.",
            "The workflow starts from protobuf service definitions, generated Swift code, and Xcode generator configuration.",
            "Client lifecycle management, scene/background behavior, and child-view propagation are part of the app architecture, not just networking glue.",
            "The session demonstrates binary efficiency, streaming RPC implementation, and backend deployment considerations.",
        ],
        "apiTerms": ["gRPC", "SwiftConcurrency", "Protobuf", "BidirectionalStreaming", "ClientManager", "AsyncSequence"],
        "risksAndConstraints": [
            "Agents should separate schema design, generated-code integration, client lifecycle, and service deployment so networking changes remain reviewable.",
        ],
        "agentNotes": ["Use for real-time collaborative, live sports, chat, operations, and device-control workflows that need typed streaming APIs."],
    },
    ("2026", "295"): {
        "highlights": [
            "AppIntentsTesting validates App Intents through the same infrastructure used by Siri, Shortcuts, and Spotlight.",
            "Tests can execute intents, inspect results, and validate app entities and entity queries without UI automation.",
            "The framework covers chained intent flows, test-only intents, Spotlight indexing, and view annotation verification.",
            "It turns App Intents adoption into normal testable developer workflow instead of manual Siri/Shortcuts smoke testing.",
        ],
        "apiTerms": ["AppIntentsTesting", "AppIntent", "AppEntity", "EntityQuery", "Spotlight", "ViewAnnotations", "TestOnlyIntent"],
        "risksAndConstraints": [
            "Intent tests should include entity-query edge cases, chained actions, missing data, and invalid user requests before relying on Siri or Spotlight behavior.",
        ],
        "agentNotes": ["Require AppIntentsTesting coverage whenever an agent exposes entities/actions to Siri, Shortcuts, Spotlight, or Apple Intelligence surfaces."],
    },
    ("2026", "310"): {
        "highlights": [
            "Shortcuts gains new automation patterns, richer app-content integration, Use Model transcript behavior, and synced storage for information from apps.",
            "Use Model helps refine how an app entity is presented to LLMs inside Shortcuts-driven automations.",
            "The session connects app entities, automation triggers, model-readable content, and cross-device shortcut state.",
        ],
        "apiTerms": ["Shortcuts", "UseModel", "AppEntity", "AppIntents", "Automation", "SyncedStorage"],
        "risksAndConstraints": [
            "Model-readable entity descriptions should avoid overexposing private fields and should be tested with realistic user shortcut phrasing.",
        ],
        "agentNotes": ["Use with App Intents and Foundation Models notes when designing automations where app content becomes input to model-mediated workflows."],
    },
    ("2026", "232"): {
        "highlights": [
            "Local agentic AI on Mac combines MLX, Mac hardware, local model serving, and code agents such as opencode for private/offline workflows.",
            "The agentic loop covers chat, tool integration, Xcode integration, local server setup, and performance tuning.",
            "Distributed inference is introduced as a way to scale local agent responsiveness across multiple Macs.",
        ],
        "apiTerms": ["MLX", "MLXLM", "OpenCode", "LocalAgent", "Xcode", "DistributedInference", "ToolIntegration"],
        "risksAndConstraints": [
            "Local agents still need sandboxing, tool allowlists, repository boundaries, and measurable latency/quality targets.",
        ],
        "agentNotes": ["Use as the Mac-local alternative to hosted coding agents when privacy, offline operation, or local tool access is the primary constraint."],
    },
    ("2026", "233"): {
        "highlights": [
            "MLX distributed workflows scale inference and fine-tuning across multiple Macs with cluster configuration and distributed communication.",
            "The session covers model parallelism, pipeline parallelism, request batching, LoRA fine-tuning, and all-reduce APIs.",
            "CLI, Python, Swift, and C++ APIs make the same distributed concepts available at different integration layers.",
        ],
        "apiTerms": ["MLX", "DistributedCommunication", "PipelineParallelism", "ModelParallelism", "LoRA", "AllReduce", "MLXSwift"],
        "risksAndConstraints": [
            "Use distributed local inference only when interconnect overhead, model size, request volume, and operational complexity justify it.",
        ],
        "agentNotes": ["Route scale-up questions here after checking whether a single local MLX model, PCC, or provider model would be simpler."],
    },
    ("2026", "250"): {
        "highlights": [
            "Apple frames great design around purpose, agency, responsibility, familiarity, flexibility, simplicity, craft, and delight.",
            "The session is not API-driven; it is a review lens for whether generated UI helps users understand, control, and trust the experience.",
            "The principles are especially useful when reviewing AI-generated UI that may be technically correct but visually or behaviorally unfocused.",
        ],
        "apiTerms": ["DesignPrinciples", "HumanInterfaceGuidelines"],
        "risksAndConstraints": [
            "Do not let agents treat visual novelty as quality; evaluate generated screens against purpose, control, familiarity, accessibility, and platform conventions.",
        ],
        "agentNotes": ["Use as a critique checklist for frontend/UI agents before accepting generated Apple-platform interface changes."],
    },
    ("2026", "292"): {
        "highlights": [
            "Search design guidance covers search field behavior, placement patterns, navigation models, platform differences, and best practices.",
            "Search is positioned as both content discovery and navigation, not just filtering text in a list.",
            "The session helps decide when search belongs globally, within a tab/sidebar, inside content, or across platform-specific surfaces.",
        ],
        "apiTerms": ["Search", "SearchField", "Navigation", "InformationArchitecture"],
        "risksAndConstraints": [
            "Search UI should define scope, empty states, ranking, query persistence, keyboard behavior, and accessibility before implementation.",
        ],
        "agentNotes": ["Use for document browsers, media libraries, workspace apps, and AI/RAG surfaces where search scope and result explanation matter."],
    },
    ("2026", "221"): {
        "highlights": [
            "Dynamic Type on tvOS brings large-screen accessibility constraints into focus for apps that historically used fixed text sizes.",
            "The session helps adapt layouts, focus behavior, and media-oriented screens for variable text without clipping or occlusion.",
            "It broadens the corpus accessibility model beyond phone, tablet, and desktop assumptions.",
        ],
        "apiTerms": ["DynamicType", "tvOS", "Accessibility", "FocusEngine"],
        "risksAndConstraints": [
            "Generated tvOS screens should be checked under large accessibility text sizes and focus navigation, not only default typography.",
        ],
        "agentNotes": ["Use as a tvOS accessibility routing source when agents modify media, dashboard, or living-room interfaces."],
    },
    ("2026", "303"): {
        "highlights": [
            "Responsive camera apps require fast launch paths, careful capture setup, and measurement of what blocks first usable interaction.",
            "The session is a performance case study for media apps where startup latency is user-visible and time-sensitive.",
            "Agent-created camera features should preserve launch speed while adding capture, preview, or processing behavior.",
        ],
        "apiTerms": ["AVFoundation", "Camera", "LaunchPerformance", "Responsiveness", "Instruments"],
        "risksAndConstraints": [
            "Camera changes should be verified on device because simulator behavior and desktop profiling can miss hardware startup costs.",
        ],
        "agentNotes": ["Use for performance-sensitive media workflows and require timing evidence before accepting camera startup changes."],
    },
    ("2026", "305"): {
        "highlights": [
            "Core Image improvements for RAW processing matter for pro camera, photo editing, and computational imaging workflows.",
            "The session connects image pipeline quality with performance and user-visible editing capabilities.",
            "Use it as deterministic imaging context alongside generative Image Playground or model-assisted photo features.",
        ],
        "apiTerms": ["CoreImage", "RAW", "CIRAWFilter", "ImageProcessing", "Camera"],
        "risksAndConstraints": [
            "RAW pipeline changes need quality, color, performance, and memory checks on representative assets.",
        ],
        "agentNotes": ["Route photo-editor and camera-pipeline questions here when deterministic RAW controls are needed before generative assistance."],
    },
    ("2026", "312"): {
        "highlights": [
            "The Now Playing framework centralizes media playback presence, controls, and system integration.",
            "Media apps should treat Now Playing as part of the user experience across lock screen, remote controls, and platform surfaces.",
            "The session belongs with MusicKit, subtitles, accessibility, and media-session architecture.",
        ],
        "apiTerms": ["NowPlaying", "MediaPlayback", "RemoteCommand", "MusicKit"],
        "risksAndConstraints": [
            "Playback state should be tested across interruptions, backgrounding, remote controls, and multiple output routes.",
        ],
        "agentNotes": ["Use for media apps where system playback integration is part of the product surface, not an afterthought."],
    },
    ("2026", "256"): {
        "highlights": [
            "Generated subtitles and subtitle styles combine accessibility, media quality, localization, and playback presentation.",
            "Apps should consider subtitle generation, styling, readability, and user preference behavior together.",
            "This session is relevant for video, education, social, and immersive media workflows.",
        ],
        "apiTerms": ["Subtitles", "GeneratedSubtitles", "AVFoundation", "Accessibility", "Localization"],
        "risksAndConstraints": [
            "Generated subtitle workflows need review for accuracy, language coverage, timing, styling contrast, and user correction paths.",
        ],
        "agentNotes": ["Use as accessibility/media context when agents add captions, transcript summaries, or localized video experiences."],
    },
    ("2026", "328"): {
        "highlights": [
            "MLX numerical computing in Swift brings array-oriented model and math workflows closer to Apple-platform application code.",
            "The session is relevant when agents need to reason about Swift-native ML prototyping instead of Python-only pipelines.",
            "It complements Core AI, Metal tensors, and distributed MLX sessions.",
        ],
        "apiTerms": ["MLX", "MLXSwift", "Arrays", "NumericalComputing", "AppleSilicon"],
        "risksAndConstraints": [
            "Numerical examples should include device, memory, precision, and performance assumptions before being reused.",
        ],
        "agentNotes": ["Use when deciding whether a model/math workflow can live in Swift rather than a separate Python service."],
    },
    ("2026", "330"): {
        "highlights": [
            "Metal tensors target custom machine-learning operation performance where higher-level frameworks are insufficient.",
            "The session belongs in the low-level optimization path for Core AI, MLX, and custom model operations.",
            "Agents should treat this as expert-level performance material rather than a default implementation route.",
        ],
        "apiTerms": ["Metal", "MetalTensors", "MPS", "CustomMLOperations", "GPU"],
        "risksAndConstraints": [
            "Low-level ML operations need correctness tests, numerical tolerance checks, GPU profiling, and fallback paths.",
        ],
        "agentNotes": ["Use only after simpler Core AI, MLX, or framework-level APIs cannot satisfy performance or operation requirements."],
    },
    ("2026", "357"): {
        "highlights": [
            "Game Porting Toolkit 4 adds agentic skills that help coding assistants adopt Metal 4, MetalFX, frame pacing, controllers, and Apple hardware tuning.",
            "The workflow demonstrates domain-specific agent skills plus command-line Metal debugging tools.",
            "It is a concrete case study for using agents with specialized diagnostics instead of generic code edits.",
        ],
        "apiTerms": ["GamePortingToolkit", "AgentSkills", "Metal4", "MetalFX", "FramePacing", "GPUCommandLineTools"],
        "risksAndConstraints": [
            "Porting agents should produce render correctness evidence and performance traces, not only compile fixes.",
        ],
        "agentNotes": ["Use as an example of domain-tool-augmented coding agents that can inspect and troubleshoot platform-specific graphics issues."],
    },
    ("2026", "388"): {
        "highlights": [
            "Metal game performance tooling includes Game Performance Overview in Instruments, background traces with metalperftrace, and Control Center trace collection on iOS.",
            "StateReporting contextualizes metrics by runtime state, while MetricKit extends observation into field data.",
            "The workflow turns large traces into filtered overviews and aggregate performance analysis.",
        ],
        "apiTerms": ["Metal", "Instruments", "GamePerformanceOverview", "metalperftrace", "StateReporting", "MetricKit"],
        "risksAndConstraints": [
            "Performance claims should include trace collection method, game state, hardware, OS, and before/after comparison.",
        ],
        "agentNotes": ["Use for graphics performance tasks where agents need explicit telemetry collection and state-correlated diagnosis."],
    },
    ("2026", "389"): {
        "highlights": [
            "Container machines provide lightweight persistent Linux environments on macOS through Apple's container tooling.",
            "The session covers creation, listing, starting shells, running commands, and understanding containerization design principles.",
            "This is relevant to local backend services, Linux toolchains, and agent sandboxes on Mac developer machines.",
        ],
        "apiTerms": ["Container", "ContainerMachine", "Linux", "macOS", "DevelopmentEnvironment"],
        "risksAndConstraints": [
            "Agents should keep host filesystem access, networking, credentials, and lifecycle cleanup explicit when using local containers.",
        ],
        "agentNotes": ["Use as local infrastructure context for agents that need Linux services or isolated command environments on macOS."],
    },
    ("2026", "215"): {
        "highlights": [
            "The HTML model element brings interactive 3D content to websites across iOS, iPadOS, macOS, and visionOS.",
            "The session covers USDZ preparation, loading/fallbacks, model backgrounds, interactions, transitions, animation playback, AR, spatial behavior, and production optimization.",
            "It is useful for comparing native spatial product views with web-delivered 3D experiences.",
        ],
        "apiTerms": ["HTMLModel", "USDZ", "AR", "SpatialWeb", "ModelElement"],
        "risksAndConstraints": [
            "3D web assets need fallback images, loading states, performance budgets, and accessibility alternatives.",
        ],
        "agentNotes": ["Use when choosing between native RealityKit/SwiftUI spatial UI and standards-based web product visualization."],
    },
    ("2026", "216"): {
        "highlights": [
            "Safari web extensions can be built and tested without Xcode while still supporting content blocking, page modification, packaging, distribution, native messaging, and permissions.",
            "The workflow uses manifests, action UI, declarativeNetRequest, content scripts, and app communication.",
            "Privacy-preserving permission design is central to the extension model.",
        ],
        "apiTerms": ["SafariWebExtensions", "Manifest", "declarativeNetRequest", "ContentScripts", "NativeMessaging", "Permissions"],
        "risksAndConstraints": [
            "Extensions need narrow permissions, clear user consent, and careful native messaging boundaries.",
        ],
        "agentNotes": ["Use for browser automation or augmentation ideas where a Safari extension may be safer than arbitrary page scripting."],
    },
    ("2026", "314"): {
        "highlights": [
            "CSS Grid Lanes supports adaptive masonry-like layouts for varied content shapes while retaining structured CSS layout control.",
            "Flow Tolerance helps balance visual layout flexibility with accessibility-preserving source and reading order.",
            "Web Inspector is part of the iteration workflow for debugging lane placement and responsive behavior.",
        ],
        "apiTerms": ["CSSGridLanes", "FlowTolerance", "WebInspector", "CSSGrid"],
        "risksAndConstraints": [
            "Dense layouts should preserve meaningful reading order, keyboard navigation, and responsive behavior before visual compactness.",
        ],
        "agentNotes": ["Use for public reader or gallery layouts where agents might otherwise produce inaccessible masonry grids."],
    },
    ("2026", "315"): {
        "highlights": [
            "The HTML select element gains deeper styling through appearance: base-select, picker-related pseudo-elements, and richer option content.",
            "The session keeps the native control's accessibility and robustness while allowing stronger design-system alignment.",
            "Fallback behavior remains part of the implementation story for unsupported browsers.",
        ],
        "apiTerms": ["HTMLSelect", "CSSAppearance", "base-select", "selectedcontent", "Picker"],
        "risksAndConstraints": [
            "Custom select styling should not replace native semantics, keyboard behavior, form behavior, or assistive technology support.",
        ],
        "agentNotes": ["Use as a web-control pattern where agents can improve visual fit while preserving native semantics."],
    },
    ("2025", "286"): {
        "highlights": [
            "Baseline for WWDC26 Foundation Models work: LanguageModelSession, guided generation, streaming, tools, transcripts, availability, and Instruments.",
            "Watch before WWDC26 Foundation Models, provider integrations, agentic apps, and agentic profiling sessions.",
        ],
        "apiTerms": ["FoundationModels", "LanguageModelSession", "Generable", "Guide", "ToolCalling", "Streaming"],
    },
    ("2025", "301"): {
        "highlights": [
            "Deep prerequisite for agentic and tool-heavy Foundation Models sessions.",
            "Covers session context, transcript behavior, generable types, guides, regex constraints, dynamic schemas, and tool calls.",
        ],
        "apiTerms": ["LanguageModelSession", "Generable", "Guide", "DynamicSchemas", "ToolCalls"],
    },
    ("2025", "248"): {
        "highlights": [
            "Prompt design and safety are prerequisites for the WWDC26 Evaluations track.",
            "Key practices include model-limit awareness, instructions versus prompts, guardrails, unhappy-path tests, and evaluation datasets.",
        ],
        "apiTerms": ["FoundationModels", "Evaluations", "Guardrails"],
    },
    ("2025", "244"): {
        "highlights": [
            "Foundation for WWDC26 Siri, App Schemas, and semantic Spotlight integration.",
            "Covers AppIntent, AppEnum, AppEntity, EntityQuery, AppShortcutsProvider, Transferable, IndexedEntity, OpenIntent, and target-content navigation.",
        ],
        "apiTerms": ["AppIntent", "AppEnum", "AppEntity", "EntityQuery", "AppShortcutsProvider", "Transferable", "IndexedEntity", "OpenIntent"],
    },
    ("2025", "275"): {
        "highlights": [
            "Introduces 2025 App Intents features that lead into WWDC26 advanced Siri and Apple Intelligence integrations.",
            "Covers interactive snippets, deferred properties, entity view annotations, Visual Intelligence integration, OpenIntent, Spotlight actions, and on-screen entities.",
        ],
        "apiTerms": ["AppIntents", "InteractiveSnippets", "ViewAnnotations", "VisualIntelligence", "OpenIntent"],
    },
    ("2025", "260"): {
        "highlights": [
            "Strong bridge into Core Spotlight and model-mediated Shortcuts.",
            "Covers Shortcuts Use Model, app entities as model content, rich text, generated Find actions from IndexedEntity, Spotlight on Mac, and PredictableIntent.",
        ],
        "apiTerms": ["Shortcuts", "UseModel", "IndexedEntity", "CoreSpotlight", "PredictableIntent"],
    },
    ("2025", "256"): {
        "highlights": [
            "Baseline SwiftUI behavior for AI features shipping on iOS/macOS 26.",
            "Covers Liquid Glass adoption, framework performance changes, Instruments support, SwiftUI web/rich text, and spatial layout.",
        ],
        "apiTerms": ["SwiftUI", "LiquidGlass", "Instruments", "RichText", "SpatialLayout"],
    },
    ("2025", "266"): {
        "highlights": [
            "Important for streaming model output and responsive AI UI.",
            "Covers main actor defaults, Sendable closures, async tasks, SwiftUI event loop, actor offloading, and data-race avoidance.",
        ],
        "apiTerms": ["SwiftUI", "Concurrency", "MainActor", "Sendable", "AsyncSequence"],
    },
    ("2025", "306"): {
        "highlights": [
            "AI UI will often stream and mutate state; this session teaches SwiftUI update attribution.",
            "Covers the SwiftUI Instruments template, view update causes, long body updates, responsiveness metrics, animation, and layout analysis.",
        ],
        "apiTerms": ["SwiftUI", "Instruments", "ViewUpdates", "Responsiveness"],
    },
    ("2025", "247"): {
        "highlights": [
            "Developer workflow baseline before Xcode 27: coding assistant, Playgrounds, debugging, tabs, String Catalog comments, Instruments links, and security settings.",
            "Watch before WWDC26 Xcode 27 and AI-assisted development sessions.",
        ],
        "apiTerms": ["Xcode", "CodingAssistant", "Playgrounds", "StringCatalogs", "Instruments"],
    },
    ("2025", "315"): {
        "highlights": [
            "Prerequisite for WWDC26 MLX local-agent and distributed sessions.",
            "Covers MLX arrays, unified memory, lazy computation, transforms, Python and Swift APIs, and Apple silicon acceleration.",
        ],
        "apiTerms": ["MLX", "MLXSwift", "UnifiedMemory", "LazyComputation"],
    },
    ("2025", "298"): {
        "highlights": [
            "Practical LLM inference and fine-tuning context for Mac-side agentic development.",
            "Covers MLX LM, text generation, quantization, fine-tuning, Swift integration, and model loading.",
        ],
        "apiTerms": ["MLX", "MLXLM", "Quantization", "FineTuning"],
    },
}


def fetch(url: str) -> str:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=30) as response:
        return response.read().decode("utf-8", "replace")


def fetch_page_cached(url: str, path: Path, *, refresh: bool = False) -> str:
    if not refresh and path.exists() and path.stat().st_size > 0:
        text = path.read_text(encoding="utf-8")
        if is_video_cache_path(path):
            text = sanitize_video_html_cache(text, path)
        return text
    text = fetch(url)
    if is_video_cache_path(path):
        text = strip_transcript_section(text)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return text


def is_video_cache_path(path: Path) -> bool:
    return bool(re.match(r"wwdc20\d\d-\d+\.html$", path.name))


def strip_transcript_section(text: str) -> str:
    return re.sub(
        r'\n?\s*<section id="transcript-content".*?</section>\s*',
        "\n<!-- transcript-content stripped: full transcript text is not cached. -->\n",
        text,
        flags=re.S,
    )


def sanitize_video_html_cache(text: str, path: Path) -> str:
    cleaned = strip_transcript_section(text)
    if cleaned != text:
        path.write_text(cleaned, encoding="utf-8")
    return cleaned


def sanitize_cached_video_pages() -> None:
    for path in CACHE.glob("wwdc20*-*.html"):
        if is_video_cache_path(path):
            sanitize_video_html_cache(path.read_text(encoding="utf-8"), path)


def assert_no_transcript_cache() -> None:
    unsafe = []
    for path in CACHE.glob("*"):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if 'id="transcript-content"' in text or "WEBVTT" in text or ".webvtt" in text:
            unsafe.append(str(path.relative_to(ROOT)))
    if unsafe:
        raise RuntimeError("Transcript cache safety failed: " + ", ".join(unsafe[:12]))


def clean(value: str) -> str:
    value = re.sub(r"<span class=\"vc-card__keywords hidden\".*?</span>", " ", value, flags=re.S)
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def public_safe_text(value: str) -> str:
    value = re.sub(r"https?://127\.0\.0\.1:\d+", "[local service URL]", value)
    value = re.sub(r"\b127\.0\.0\.1\b", "[local host]", value)
    value = re.sub(r"https?://localhost:\d+", "[local service URL]", value)
    value = re.sub(r"\blocalhost\b", "[local host]", value)
    return value


def attrs(value: str) -> dict[str, str]:
    return {k: html.unescape(v) for k, v in re.findall(r'([\w:-]+)="([^"]*)"', value)}


def parse_index(text: str, year: str) -> list[dict[str, Any]]:
    sessions: dict[str, dict[str, Any]] = {}
    pattern = re.compile(
        rf'<a href="/videos/play/{year}/(\d+)/?"[^>]*>(.*?)</a>(?P<tail>.{{0,2600}}?)(?=<a href="/videos/play/{year}/|\Z)',
        re.S,
    )
    for match in pattern.finditer(text):
        sid = match.group(1)
        raw_label = match.group(2)
        metadata = raw_label + match.group("tail")
        metadata_attrs = attrs(metadata)
        label = clean(raw_label)
        duration_match = re.match(r"^(\d{1,3}:\d{2})\s+(.+)$", label)
        title = metadata_attrs.get("data-filter-title-en") or (duration_match.group(2) if duration_match else label)
        description = metadata_attrs.get("data-filter-description-en", "")
        sessions[sid] = {
            "id": sid,
            "year": year.replace("wwdc", ""),
            "title": title,
            "duration": duration_match.group(1) if duration_match else "",
            "description": description,
            "topics": [x for x in metadata_attrs.get("data-filter-topics", "").split("|") if x],
            "platforms": [x for x in metadata_attrs.get("data-filter-platform", "").split("|") if x],
            "keywords": [x for x in metadata_attrs.get("data-filter-keywords", "").split(",") if x],
            "url": f"https://developer.apple.com/videos/play/{year}/{sid}/",
        }
    return sorted(sessions.values(), key=lambda item: (item["topics"], item["title"]))


def parse_video_page(page: str, url: str) -> dict[str, Any]:
    def meta(name: str) -> str:
        for prefix in ["property", "name", "itemprop"]:
            match = re.search(rf'<meta {prefix}="{re.escape(name)}" content="([^"]*)"', page)
            if match:
                return html.unescape(match.group(1))
        return ""

    chapters = []
    for match in re.finditer(
        r'<li class="chapter-item" data-start-time="(\d+)">([^<]+)-\s*<a[^>]+>(.*?)</a>',
        page,
        re.S,
    ):
        chapters.append({"seconds": int(match.group(1)), "time": clean(match.group(2)), "title": clean(match.group(3))})

    code_samples = []
    for match in re.finditer(
        r'<p>(\d+:\d+)\s*-\s*<a[^>]*>(.*?)</a></p>\s*<pre class="code-source"><code>(.*?)</code></pre>',
        page,
        re.S,
    ):
        sample = public_safe_text(clean(match.group(3)))
        code_samples.append({"time": match.group(1), "title": clean(match.group(2)), "excerpt": sample[:500]})

    resources = []
    block = re.search(r"<h2>Resources</h2>(.*?)(?:<h2>Related Videos</h2>|</section>)", page, re.S)
    if block:
        for href, label in re.findall(r'<a href="([^"]+)">(.*?)</a>', block.group(1), re.S):
            resources.append({"title": clean(label), "url": urljoin(url, href)})

    return {
        "published": meta("datePublished") or meta("uploadDate"),
        "manifest": meta("og:video"),
        "image": meta("og:image"),
        "chapters": chapters,
        "codeSamples": code_samples[:10],
        "resources": resources[:12],
    }


def transcript_text_ephemeral(manifest_url: str) -> str:
    if not manifest_url:
        return ""
    try:
        manifest = fetch(manifest_url)
    except Exception:
        return ""
    match = re.search(r'#EXT-X-MEDIA:TYPE=SUBTITLES,[^\n]*LANGUAGE="en"[^\n]*URI="([^"]+)"', manifest)
    if not match:
        return ""
    subtitle_url = urljoin(manifest_url, match.group(1))
    try:
        subtitle_index = fetch(subtitle_url)
    except Exception:
        return ""
    urls = [urljoin(subtitle_url, line.strip()) for line in subtitle_index.splitlines() if line.strip().endswith(".webvtt")]
    try:
        with ThreadPoolExecutor(max_workers=10) as pool:
            vtts = list(pool.map(fetch, urls))
    except Exception:
        vtts = []
    entries: list[str] = []
    seen: set[str] = set()
    for vtt in vtts:
        for cue in re.finditer(r"\d\d:\d\d:\d\d\.\d{3} --> .*?\n(.+?)(?=\n\n|\Z)", vtt, re.S):
            text = clean(cue.group(1))
            if text and text not in seen:
                entries.append(text)
                seen.add(text)
    return " ".join(entries)


def split_sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'])", text)
    return [p.strip() for p in parts if 45 <= len(p.strip()) <= 260]


def derive_notes(session: dict[str, Any], transcript: str) -> dict[str, Any]:
    haystack = " ".join([session["title"], session["description"], transcript])
    transcript_lower = transcript.lower()

    api_terms = sorted(
        set(
            re.findall(
                r"\b(?:[A-Z][A-Za-z0-9]+(?:Framework|Kit|Tool|Intent|Entity|Query|Model|Session|Profile|View|Scene|Document|Testing|Data|Hub|Cloud|Compute)|[A-Z]{2,}[A-Za-z0-9]*)\b",
                haystack,
            )
        )
    )
    api_terms = [term for term in api_terms if len(term) > 2 and term not in {"Apple", "WWDC", "Introduction"}][:24]

    capability_terms = sorted(
        term
        for term in RELEVANT_TERMS
        if term in transcript_lower or term in " ".join([session["title"], session["description"]]).lower()
    )
    chapter_topics = [chapter["title"] for chapter in session.get("chapters", [])[:8]]
    resources = [resource["title"] for resource in session.get("resources", [])[:6]]
    highlights = synthesize_highlights(session, capability_terms, chapter_topics, api_terms, bool(transcript))
    risks = synthesize_risks(transcript_lower, capability_terms, session)

    return {
        "analysisStatus": "transcript-derived" if transcript else "metadata-only",
        "highlights": highlights,
        "apiTerms": api_terms,
        "capabilityTerms": capability_terms,
        "chapterTopics": chapter_topics,
        "resourceTitles": resources,
        "transcriptStats": {
            "charactersReadEphemerally": len(transcript),
            "storedCharacters": 0,
        },
        "risksAndConstraints": risks,
        "agentNotes": derive_agent_notes(session, api_terms),
    }


def synthesize_highlights(
    session: dict[str, Any],
    capability_terms: list[str],
    chapter_topics: list[str],
    api_terms: list[str],
    transcript_read: bool,
) -> list[str]:
    topic_label = ", ".join(session.get("topics", [])[:2]) or "Apple platform development"
    highlights = [
        f"Apple groups this session under {topic_label}; use it as source material for {session['title']}.",
    ]
    if session.get("description"):
        highlights.append(session["description"])
    if chapter_topics:
        highlights.append("Chapter coverage includes: " + "; ".join(chapter_topics[:5]) + ".")
    if capability_terms:
        label = "Transcript-derived" if transcript_read else "Metadata-derived"
        highlights.append(label + " capability tags: " + ", ".join(capability_terms[:10]) + ".")
    if api_terms:
        highlights.append("API and framework terms to verify in SDK docs: " + ", ".join(api_terms[:10]) + ".")
    if session["year"] == "2025":
        highlights.append("Treat this WWDC25 session as prerequisite context for understanding the WWDC26 changes, not as the newest API source.")
    else:
        highlights.append("Treat this WWDC26 session as the current primary source, then confirm exact API availability against installed SDK docs.")
    return highlights[:6]


def synthesize_risks(transcript_lower: str, capability_terms: list[str], session: dict[str, Any]) -> list[str]:
    risks = []
    title = session["title"].lower()
    combined = " ".join([title, transcript_lower, " ".join(capability_terms)])
    if any(term in combined for term in ["agent", "tool", "app intents", "siri"]):
        risks.append("For agentic or intent-driven flows, require narrow tool scopes, user-visible confirmations, and regression tests around unintended actions.")
    if any(term in combined for term in ["foundation model", "core ai", "model", "mlx", "core ml"]):
        risks.append("Model behavior can vary by availability, device class, context size, and selected provider; keep fallbacks and evaluations explicit.")
    if any(term in combined for term in ["privacy", "security", "private cloud compute", "permission"]):
        risks.append("Privacy and security claims should be tied to Apple documentation, entitlement checks, and data-boundary decisions in the app design.")
    if any(term in combined for term in ["performance", "instruments", "metrickit", "xcode"]):
        risks.append("Performance or tooling guidance should be verified with a local build, simulator/device run, and trace or metric evidence.")
    if any(term in combined for term in ["swiftui", "accessibility", "ui framework"]):
        risks.append("UI changes should be checked across light/dark mode, Dynamic Type, keyboard navigation, and platform-specific layout behavior.")
    return risks[:5]


def derive_agent_notes(session: dict[str, Any], api_terms: list[str]) -> list[str]:
    title = session["title"].lower()
    notes = []
    if "swiftui" in title or "ui" in " ".join(session.get("topics", [])).lower():
        notes.append("When generating UI code, map this session's APIs to stable view structure, accessibility, and responsive layout guidance.")
    if "xcode" in title or "agent" in title or "device hub" in title:
        notes.append("Use this session to update agent development workflows: build, run, inspect, profile, localize, and verify on devices/simulators.")
    if "foundation model" in title or "core ai" in title or "model" in title:
        notes.append("Use this session to choose between on-device Foundation Models, PCC, provider models, MLX, Core ML, and Core AI custom models.")
    if "intent" in title or "siri" in title or "shortcuts" in title:
        notes.append("Use this session to expose app data/actions through stable App Entities, App Intents, schemas, Spotlight, and Siri.")
    if "security" in title or "privacy" in title:
        notes.append("Use this session as a threat-model input for tool calling, confirmations, prompt injection, and data-boundary design.")
    if api_terms:
        notes.append("Track API terms for SDK verification before using generated code: " + ", ".join(api_terms[:8]) + ".")
    return notes[:5]


def is_relevant_2025(session: dict[str, Any]) -> bool:
    text = " ".join([session["title"], session["description"], " ".join(session["topics"]), " ".join(session["keywords"])]).lower()
    return any(term in text for term in RELEVANT_TERMS)


def should_deep_analyze(session: dict[str, Any]) -> bool:
    return (session["year"], session["id"]) in TRANSCRIPT_KEYS


def enrich_session(session: dict[str, Any], year_key: str) -> dict[str, Any]:
    cache_path = CACHE / f"{year_key}-{session['id']}.html"
    page = fetch_page_cached(session["url"], cache_path)
    details = parse_video_page(page, session["url"])
    transcript = transcript_text_ephemeral(details["manifest"]) if should_deep_analyze(session) else ""
    analysis_input = {**session, "chapters": details["chapters"], "resources": details["resources"]}
    notes = derive_notes(analysis_input, transcript)
    enriched = {
        **session,
        "published": details["published"],
        "image": details["image"],
        "chapters": details["chapters"],
        "codeSamples": details["codeSamples"],
        "resources": details["resources"],
        **notes,
        "transcriptPolicy": "Full transcript read ephemerally when analysisStatus is transcript-derived; full text is not stored.",
    }
    overlay = CURATED_SESSION_OVERLAYS.get((session["year"], session["id"]))
    if overlay:
        for key, value in overlay.items():
            if isinstance(value, list):
                existing = enriched.get(key, [])
                enriched[key] = merge_unique(value, existing)
            else:
                enriched[key] = value
        enriched["curatedOverlay"] = True
    queue_item = RESEARCH_QUEUE.get((session["year"], session["id"]))
    if queue_item:
        enriched["researchPriority"] = queue_item["priority"]
        enriched["researchWave"] = queue_item["wave"]
        enriched["researchReason"] = queue_item["reason"]
    return enriched


def merge_unique(primary: list[Any], secondary: list[Any]) -> list[Any]:
    merged = []
    seen = set()
    for item in [*primary, *secondary]:
        marker = json.dumps(item, sort_keys=True) if isinstance(item, (dict, list)) else str(item)
        if marker not in seen:
            merged.append(item)
            seen.add(marker)
    return merged


def build_rollups(sessions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rollups = []
    groups = [
        (
            "SwiftUI and UI Frameworks",
            lambda s: has_any(s, ["swiftui", "swiftdata", "uikit", "appkit", "textkit", "widgetkit", "activitykit", "pencilkit", "paperkit"]),
        ),
        (
            "Xcode, Agents, and Developer Tools",
            lambda s: has_any(s, ["xcode", "agent", "device hub", "swift testing", "instruments", "metrickit", "xcode cloud", "devicectl"]),
        ),
        (
            "AI, Models, and Agentic Apps",
            lambda s: has_any(s, ["foundation model", "core ai", "mlx", "evaluation", "visual intelligence", "image playground", "private cloud compute"]),
        ),
        (
            "App Intents, Siri, and System Surfaces",
            lambda s: has_any(s, ["app intents", "app intent", "siri", "shortcuts", "core spotlight", "spotlight", "widgetkit", "activitykit"]),
        ),
        (
            "Accessibility, Security, and Quality",
            lambda s: has_any(s, ["accessibility", "security", "privacy", "app attest", "trust insights", "permission", "metrickit", "instruments"]),
        ),
    ]
    for title, matcher in groups:
        subset = [s for s in sessions if matcher(s)]
        subset = sorted(
            subset,
            key=lambda s: (
                s["year"] != "2026",
                s.get("analysisStatus") != "transcript-derived",
                not s.get("curatedOverlay"),
                s["title"].lower(),
            ),
        )
        terms = []
        for session in subset:
            terms.extend(session.get("apiTerms", []))
        rollups.append(
            {
                "title": title,
                "videoCount": len(subset),
                "transcriptDerivedCount": sum(1 for s in subset if s["analysisStatus"] == "transcript-derived"),
                "topApiTerms": sorted(set(terms))[:40],
                "importantVideos": [
                    {"id": s["id"], "year": s["year"], "title": s["title"], "url": s["url"]}
                    for s in subset[:14]
                ],
                "agentUse": rollup_agent_use(title),
            }
        )
    return rollups


def has_any(session: dict[str, Any], needles: list[str]) -> bool:
    haystack = " ".join(
        [
            session.get("title", ""),
            session.get("description", ""),
            " ".join(session.get("topics", [])),
            " ".join(session.get("keywords", [])),
            " ".join(session.get("apiTerms", [])),
            " ".join(session.get("capabilityTerms", [])),
        ]
    ).lower()
    return any(needle in haystack for needle in needles)


def rollup_agent_use(title: str) -> list[str]:
    if "SwiftUI" in title:
        return [
            "Use these sessions to select native SwiftUI interactions before reaching for UIKit/AppKit bridges.",
            "Feed agents the specific session notes when asking for document, drag/drop, scrolling, accessibility, or TextKit work.",
        ]
    if "Xcode" in title:
        return [
            "Use these sessions to define an agent verification loop: code, build, run, inspect, profile, and revise.",
            "Keep Device Hub, Instruments, MetricKit, Swift Testing, and Xcode Cloud as separate workflow tools rather than one vague 'test it' instruction.",
        ]
    if "AI" in title:
        return [
            "Use Foundation Models for app-native LLM features, Core AI for custom on-device models, and Evaluations for regression checks.",
            "Route tasks by privacy, latency, context size, model capability, and availability.",
        ]
    return [
        "Use the video notes as focused context before asking an agent to modify app architecture or user-facing behavior.",
    ]


def build_user_journeys() -> list[dict[str, Any]]:
    return [
        {
            "title": "Evaluation-driven local-first assistant",
            "scenario": "A notes or workspace app answers questions over private local data, escalates only hard reasoning to PCC, and tracks regressions with Evaluations.",
            "buildingBlocks": ["Foundation Models", "Private Cloud Compute", "Core Spotlight", "Evaluations", "Instruments"],
            "agentPromptUse": "Ask the coding agent to implement local route first, add PCC fallback second, then write an evaluation dataset before polishing UI.",
        },
        {
            "title": "Siri-aware productivity surface",
            "scenario": "A calendar, project, or creative app exposes entities and actions so Siri can answer questions, transfer content across apps, and show custom snippets.",
            "buildingBlocks": ["App Entities", "App Schemas", "IndexedEntity", "AppIntentsTesting", "Custom snippets"],
            "agentPromptUse": "Give agents the entity model and require AppIntentsTesting coverage before UI integration.",
        },
        {
            "title": "Agentic Xcode development loop",
            "scenario": "A developer uses Xcode agents to prototype, Device Hub to inspect device behavior, Instruments to profile, and MetricKit/Xcode Cloud to watch post-merge quality.",
            "buildingBlocks": ["Xcode 27 agents", "Device Hub", "Instruments", "Top Functions", "Xcode Cloud", "MetricKit"],
            "agentPromptUse": "Tell agents which verification surface proves success: preview, simulator run, screenshot, trace, test report, or cloud build.",
        },
        {
            "title": "Creative visual intelligence editor",
            "scenario": "A SwiftUI document app uses Vision tap-to-segment, Core AI custom models, and Foundation Models image input to isolate objects and suggest layouts.",
            "buildingBlocks": ["SwiftUI Document", "Vision", "Core AI", "Foundation Models image input", "Apple Pencil"],
            "agentPromptUse": "Separate deterministic Vision/Core AI tools from generative layout suggestions; require fallback and user confirmation for destructive edits.",
        },
    ]


def main() -> None:
    CACHE.mkdir(parents=True, exist_ok=True)
    sanitize_cached_video_pages()
    wwdc26 = parse_index(fetch_page_cached(WWDC26_INDEX, CACHE / "wwdc2026-index.html", refresh=True), "wwdc2026")
    wwdc25 = [s for s in parse_index(fetch_page_cached(WWDC25_INDEX, CACHE / "wwdc2025-index.html", refresh=True), "wwdc2025") if is_relevant_2025(s)]

    # Preserve WWDC26 first; WWDC25 is prerequisite/context.
    selected = wwdc26 + wwdc25
    enriched = []
    for index, session in enumerate(selected, start=1):
        year_key = "wwdc2026" if session["year"] == "2026" else "wwdc2025"
        try:
            if index == 1 or index % 20 == 0 or should_deep_analyze(session):
                print(
                    f"[{index}/{len(selected)}] {year_key}-{session['id']} "
                    f"{'transcript' if should_deep_analyze(session) else 'metadata'}: {session['title']}",
                    flush=True,
                )
            enriched.append(enrich_session(session, year_key))
        except Exception as error:  # noqa: BLE001 - keep inventory resilient.
            enriched.append({**session, "analysisStatus": "metadata-only", "error": str(error), "highlights": [session.get("description", "")], "apiTerms": [], "risksAndConstraints": [], "agentNotes": []})

    topics: dict[str, list[dict[str, Any]]] = {}
    for session in enriched:
        for topic in session.get("topics", []) or ["Uncategorized"]:
            topics.setdefault(topic, []).append({"id": session["id"], "year": session["year"], "title": session["title"]})

    atlas = {
        "meta": {
            "title": "WWDC Apple Platform Session Atlas",
            "generatedAt": "2026-06-10",
            "transcriptCachingPolicy": "Full transcripts are never written to disk. Transcript text is fetched ephemerally and reduced to structured notes.",
            "coverage": {
                "wwdc26SessionCount": len(wwdc26),
                "wwdc25RelevantSessionCount": len(wwdc25),
                "totalSessionCount": len(enriched),
                "transcriptDerivedCount": sum(1 for s in enriched if s["analysisStatus"] == "transcript-derived"),
            },
        },
        "topicGroups": topics,
        "sessions": enriched,
        "frameworkRollups": build_rollups(enriched),
        "industryComparisons": INDUSTRY,
        "documentationIndex": DOCS,
        "userJourneys": build_user_journeys(),
        "reviewStatus": {
            "draft": False,
            "status": "published",
            "reviewLenses": ["Apple platform", "AI architecture", "SwiftUI UX", "security/privacy", "developer workflow", "product journeys"],
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(atlas, indent=2, ensure_ascii=False), encoding="utf-8")
    assert_no_transcript_cache()
    print(json.dumps(atlas["meta"]["coverage"], indent=2))


if __name__ == "__main__":
    main()
