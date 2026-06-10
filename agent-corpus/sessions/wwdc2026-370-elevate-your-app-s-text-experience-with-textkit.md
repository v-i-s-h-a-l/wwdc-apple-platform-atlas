---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 1600
---

# Elevate Your App's Text Experience With Textkit
> Neutral research record for Apple WWDC 2026 session 370.

## Entries

- ID: `wwdc2026-370`
- Coverage: `deep-researched`
- Analysis status: `transcript-derived`
- Apple video: https://developer.apple.com/videos/play/wwdc2026/370/
- Apple topics: App Services, SwiftUI & UI Frameworks
- Platforms: ios, ipados, macos, tvos, visionos, watchos
- Transcript characters stored: `0`

## Synthesis

### One-Line Answer

Discover how to combine the convenience of built-in text views with the control of textkit. we'll show you how new apis make it easy to extend uitextview and nstextview with custom behaviors like line numbers and collapsible sections. we'll also explore the textkit architecture and walk through new caching and reuse policies for text attachments. to get the most out of this session, watch “meet textkit 2” from wwdc21 and “what's new in textkit and text views” from wwdc22.

### What Was Announced Or Covered

- Built-in text views provide platform behavior, while custom TextKit views expose storage, layout, and rendering control.
- New rendering surface APIs help customize text view rendering; UITextView and NSTextView can be wrapped into SwiftUI.
- Line numbers, collapsible sections, and reusable text attachment view providers support serious editor and reader apps.
- Apple groups this session under App Services, SwiftUI & UI Frameworks; use it as source material for elevate your app’s text experience with textkit.
- discover how to combine the convenience of built-in text views with the control of textkit. we'll show you how new apis make it easy to extend uitextview and nstextview with custom behaviors like line numbers and collapsible sections. we'll also explore the textkit architecture and walk through new caching and reuse policies for text attachments. to get the most out of this session, watch “meet textkit 2” from wwdc21 and “what's new in textkit and text views” from wwdc22.
- Chapter coverage includes: Introduction; TextKit architecture; What's new in TextKit; Extending framework text views; Example: Code editor with line numbers.
- Transcript-derived capability tags: accessibility, swiftui.
- API and framework terms to verify in SDK docs: API, APIs, AppKit, CALayer, ContainerView, MyTextView, NSAttributedString, NSAttributedStrings, NSTextAttachment, NSTextAttachmentViewProvider.

### APIs And Concepts

- TextKit
- NSTextContentStorage
- NSTextLayoutManager
- NSTextViewportLayoutController
- NSTextViewportRenderingSurface
- NSTextAttachmentViewProvider
- AppKit
- CALayer
- ContainerView
- MyTextView
- NSAttributedString
- NSAttributedStrings
- NSTextAttachment
- NSTextContentManager
- NSTextContentStorageDelegate
- NSTextElement
- NSTextLayoutFragment
- NSTextParagraph

### Risks And Constraints

- UI changes should be checked across light/dark mode, Dynamic Type, keyboard navigation, and platform-specific layout behavior.

### Related Apple Resources

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/370/5/f61dbe38-7302-451a-b3ab-9851d5746315/downloads/wwdc2026-370_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/370/5/f61dbe38-7302-451a-b3ab-9851d5746315/downloads/wwdc2026-370_sd.mp4?dl=1)

### Chapters

- Introduction
- TextKit architecture
- What's new in TextKit
- Extending framework text views
- Example: Code editor with line numbers
- Example: Collapsible recipe sections
- Text attachments and view provider reuse
- Next steps

## Small Observations (Don't Delete)

- Treat this file as a research record, not an implementation checklist.
- `deep-researched` means priority transcript text was read ephemerally and reduced into notes.
- `metadata-only` means the session is indexed but needs deeper review before making strong claims.

<!-- docbot: end -->
