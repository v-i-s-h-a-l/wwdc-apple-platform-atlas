# Agent Handoff

This repository is the Apple platform and WWDC corpus. The generic protocol lives in the sibling Agentic Research Router repository.

## First Read

1. `llms.txt`
2. `agent-router.json`
3. `agent-corpus/QUESTION_ROUTING.md`
4. `agent-corpus/COVERAGE_STATUS.md`
5. `ROADMAP.md`
6. `docs/VISION.md`
7. `agent-corpus/RESEARCH_QUEUE.md`

## Current State

- The corpus includes WWDC26 sessions plus relevant WWDC25 context.
- Some sessions are deep-researched and transcript-derived.
- Some sessions are metadata-only and should be treated as discovery/routing records.
- Full transcript text is intentionally not stored.
- The public reader is `index.html`; agents should prefer the compact routing files first.

## Safe Work

Good changes here:

- Promote queued metadata-only sessions into deep-researched notes.
- Improve feature pages and concept routes.
- Add or refresh Apple documentation links.
- Improve public reader usability.
- Strengthen validation and link checks.
- Align output with the generic router schemas.

Avoid changes here:

- Adding full transcript bodies.
- Adding private project references or local paths.
- Moving generic protocol design back into this corpus.
- Making corpus usage depend on a specific agent provider.

## Validation

Run:

```bash
python3 scripts/validate_public_repo.py
python3 -m py_compile scripts/*.py
python3 -m json.tool agent-router.json >/dev/null
python3 -m json.tool agent-corpus/manifest.json >/dev/null
```

Use GitHub Actions as the final remote validation after pushing.
