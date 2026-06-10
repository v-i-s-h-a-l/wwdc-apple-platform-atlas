# Daily Operations

Daily automation should protect corpus quality without generating noise.

## Daily Health Check

Run:

```bash
python3 scripts/validate_public_repo.py
```

This checks:

- required router files
- JSON parseability
- private-reference patterns
- transcript-cache markers
- required corpus entry points

## Daily Source Refresh

For WWDC-style corpora:

```bash
python3 scripts/build_session_atlas.py
python3 scripts/generate_markdown_corpus.py
python3 scripts/generate_session_atlas_html.py
cp session-atlas.html index.html
python3 scripts/generate_agent_router.py
python3 scripts/validate_public_repo.py
```

## Suggested Schedule

- Daily: health check and source index refresh.
- Twice weekly during active conference/release windows: promote queued sessions.
- Weekly: regenerate public reader and router files.
- Monthly: review architecture, token budget, stale links, and public-safety scan patterns.

## Automation Policy

Automated jobs should not silently publish low-confidence synthesis. Prefer opening a branch or artifact when new source material appears.
