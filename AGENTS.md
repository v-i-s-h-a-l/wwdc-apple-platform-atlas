# Agent Instructions

This repository is optimized for AI-agent research routing across Apple platform and WWDC material.

## First Read

1. Read `llms.txt`.
2. Read `agent-router.json` if you need machine-readable routing.
3. Read `agent-corpus/QUESTION_ROUTING.md` if you need natural-language routing guidance.
4. Read `agent-corpus/COVERAGE_STATUS.md` before making strong claims.
5. Read `ROADMAP.md`, `docs/VISION.md`, and `docs/AGENT_HANDOFF.md` before changing corpus direction.

## Retrieval Rules

- Do not load the whole corpus unless the task explicitly requires global synthesis.
- For feature questions, start in `agent-corpus/features/`.
- For video/session questions, start in `agent-corpus/sessions/`.
- For Apple topic questions, start in `agent-corpus/topics/`.
- For exact SDK names or signatures, follow Apple documentation links and verify against current SDK docs.
- If a page says `metadata-only`, say that the answer is based on metadata and needs deeper review.

## Source Rules

- Do not treat generated summaries as primary sources.
- Use generated summaries as routing and synthesis.
- Use Apple video/documentation links for exact claims.
- Do not add full transcript text to the repo.

## Public-Safety Rules

- Do not commit local paths, private project names, credentials, tokens, helper ports, or machine-specific commands.
- Do not publish unsanitized source caches.
- Run `python3 scripts/validate_public_repo.py` before committing public-facing changes.

## Editing Rules

- Generated corpus files should be regenerated from source data and scripts.
- Keep reusable workflow changes aligned with the sibling `agentic-research-router` protocol repository.
- Keep this repository focused on the Apple/WWDC corpus: sessions, Apple documentation, feature maps, topic maps, coverage status, and public reader output.
