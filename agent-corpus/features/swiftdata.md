---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 2400
---

# SwiftData
> Feature-level research page for SwiftData.

## Entries

- [2026 240 - Build Intelligent Siri Experiences With App Schemas](../sessions/wwdc2026-240-build-intelligent-siri-experiences-with-app-schemas.md) - `deep-researched`
- [2026 275 - Code-Along: Add Persistence With Swiftdata](../sessions/wwdc2026-275-code-along-add-persistence-with-swiftdata.md) - `deep-researched`
- [2026 271 - Code-Along: Build Powerful Drag And Drop In SwiftUI](../sessions/wwdc2026-271-code-along-build-powerful-drag-and-drop-in-swiftui.md) - `deep-researched`
- [2026 344 - Code-Along: Make Your App Available To Siri](../sessions/wwdc2026-344-code-along-make-your-app-available-to-siri.md) - `deep-researched`
- [2026 321 - Dive Into Lazy Stacks And Scrolling With SwiftUI](../sessions/wwdc2026-321-dive-into-lazy-stacks-and-scrolling-with-swiftui.md) - `deep-researched`
- [2026 343 - Explore Advanced App Intents Features For Siri And Apple Intelligence](../sessions/wwdc2026-343-explore-advanced-app-intents-features-for-siri-and-apple-intelligence.md) - `deep-researched`
- [2026 295 - Validate Your App Intents Adoption With AppIntentsTesting](../sessions/wwdc2026-295-validate-your-app-intents-adoption-with-appintentstesting.md) - `deep-researched`
- [2026 310 - What's New In Shortcuts](../sessions/wwdc2026-310-what-s-new-in-shortcuts.md) - `deep-researched`
- [2026 274 - What's New In Swiftdata](../sessions/wwdc2026-274-what-s-new-in-swiftdata.md) - `deep-researched`
- [2026 259 - Xcode, Agents, And You](../sessions/wwdc2026-259-xcode-agents-and-you.md) - `deep-researched`
- [2026 297 - Best Practices For Integrating Visual Intelligence In Your App](../sessions/wwdc2026-297-best-practices-for-integrating-visual-intelligence-in-your-app.md) - `metadata-only`
- [2026 8017 - Swiftdata Group Lab](../sessions/wwdc2026-8017-swiftdata-group-lab.md) - `metadata-only`
- [2025 291 - Swiftdata: Dive Into Inheritance And Schema Migration](../sessions/wwdc2025-291-swiftdata-dive-into-inheritance-and-schema-migration.md) - `deep-researched`
- [2025 244 - Get To Know App Intents](../sessions/wwdc2025-244-get-to-know-app-intents.md) - `metadata-only`

## Synthesis

### What This Page Can Answer

- Whether this feature area appears in the indexed WWDC corpus.
- Which sessions and Apple documentation links are relevant.
- Which claims are backed by deep-researched session notes versus metadata-only indexing.

### Evidence-Backed Claims

- Bring your app's content and actions to siri with app intents. model your data using app entities, adopt app schemas to enable powerful system actions, and support natural language interactions powered by apple intelligence. explore how to enable semantic search, perform actions across apps, and create contextual experiences using onscreen awareness and content transfer. find out best practices and testing tools to build fast, reliable siri experiences. Source: WWDC 2026 session 240.
- The code-along identifies transient SwiftUI state worth persisting, converts observable types to @Model, and attaches schema with modelContainer. Source: WWDC 2026 session 275.
- It uses Codable custom values, relationships, @Query, FetchDescriptor, SortDescriptor, and dynamic query initialization. Source: WWDC 2026 session 275.
- New reordering APIs handle simple rearranging without full drag/drop machinery. Source: WWDC 2026 session 271.
- `reorderable` plus `reorderContainer` enables card movement, and drag containers allow multiple selected items to lift together. Source: WWDC 2026 session 271.
- Dive deep into an xcode project showing how you can make your app available to siri. learn how to adopt app schemas to let people ask questions about calendar events and take natural language actions like scheduling. discover best practices for making content available in the spotlight semantic index and providing context for on-screen awareness. Source: WWDC 2026 session 344.
- Lazy stacks estimate sizes and resolve subviews in ways that affect scroll accuracy and programmatic scrolling. Source: WWDC 2026 session 321.
- Filter data before view construction instead of conditionally hiding rows inside lazy content. Source: WWDC 2026 session 321.
- Polish how your app works with siri using advanced app intents apis. learn techniques that let people accomplish more with just their voice, help apple intelligence find your content, and provide context for on-screen awareness so siri understands what's happening in your app. Source: WWDC 2026 session 343.
- AppIntentsTesting validates App Intents through the same infrastructure used by Siri, Shortcuts, and Spotlight. Source: WWDC 2026 session 295.
- Tests can execute intents, inspect results, and validate app entities and entity queries without UI automation. Source: WWDC 2026 session 295.
- Shortcuts gains new automation patterns, richer app-content integration, Use Model transcript behavior, and synced storage for information from apps. Source: WWDC 2026 session 310.

### Related APIs And Concepts

- ActivityItemView
- AddToPlaylistIntent
- AlarmKit
- AlbumView
- AppEntity
- AppEnum
- AppIntent
- AppIntents
- AppIntentsTesting
- AppKit
- AppShortcutsProvider
- AppleDocumentSearch
- Artifacts
- AttendeeEntity
- AudioEntity
- Automation
- CSSearchableIndex
- CalendarEntity
- CalendarListView
- CalendarModel
- CloudKit
- Codable
- ContactEntity
- ContentUnavailableView
- ContentView
- ConversationView
- CreateCalendarIntent
- CreateEventIntent

## Small Observations (Don't Delete)

- This is a neutral feature page, not a recommendation to adopt the feature.
- Prefer deep-researched sessions for strong answers.
- Verify beta SDK names before turning research into code.

<!-- docbot: end -->
