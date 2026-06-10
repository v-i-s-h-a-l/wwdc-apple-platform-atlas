# Vision

WWDC Apple Platform Atlas exists to help AI agents answer Apple platform questions with less browsing, fewer stale assumptions, and clearer source grounding.

The corpus should route agents from a question such as "what changed in SwiftData" or "where is AppIntentsTesting covered" to the right feature page, session page, Apple documentation link, and confidence boundary.

## What Good Looks Like

- An agent can start from `llms.txt` and find the right route quickly.
- Feature pages answer "what changed" and "was this announced" questions.
- Session pages preserve source links and derived notes without storing full transcripts.
- Coverage status tells agents when a claim is deep-researched versus metadata-only.
- Apple documentation links are easy to find for exact API verification.
- The public reader helps humans inspect the corpus without becoming the main product surface.

## Design Bias

The atlas should be dense, source-linked, and retrieval-friendly:

- compact route files
- source-backed Markdown pages
- explicit coverage labels
- small first-hop files
- generated artifacts from normalized source data
- no provider-specific agent assumptions

## Long-Term Direction

The corpus should become a durable Apple platform knowledge map:

- WWDC sessions and group labs
- Apple documentation references
- framework rollups
- API and concept routes
- migration notes
- safety, privacy, and evaluation guidance
- developer workflow journeys

The generic protocol belongs in the sibling Agentic Research Router repository. This repo should stay focused on Apple platform research.
