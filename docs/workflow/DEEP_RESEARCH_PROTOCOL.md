# Deep Research Protocol

This protocol defines how a source moves from indexed metadata to deep-researched corpus material.

## Promotion Criteria

Promote a source when it materially improves agent routing for:

- high-use developer workflows
- new or changed APIs
- safety, privacy, evaluation, or verification
- framework migrations
- platform-wide design or accessibility changes
- topics likely to produce hallucinated answers without current source grounding

## Required Output

A promoted source should include:

- coverage set to `deep-researched`
- concise highlights
- API and concept terms
- risks and constraints
- agent-facing notes
- source links
- related sessions or documentation where available

## Source Handling

Full transcripts may be fetched and read during generation, but they must not be written to disk. The durable artifact is the derived research record.

## Review Lenses

Review promoted sources through these lenses:

- agent routing efficiency
- source fidelity
- API exactness
- safety and privacy
- token cost
- public-readiness
- future reuse for other corpora

## Gaps

If a source remains metadata-only, keep it discoverable and label it clearly. Metadata-only records are useful for routing but not sufficient for strong answers.
