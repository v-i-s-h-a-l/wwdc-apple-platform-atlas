# Publication Checklist

Use this before publishing or updating GitHub Pages.

## Required Checks

- `python3 scripts/validate_public_repo.py`
- `python3 -m json.tool data/session-atlas.json >/dev/null`
- `python3 -m json.tool agent-corpus/manifest.json >/dev/null`
- `python3 -m json.tool agent-corpus/session-lookup.json >/dev/null`
- `python3 -m json.tool agent-corpus/concept-routes.json >/dev/null`
- `python3 -m json.tool agent-router.json >/dev/null`

## Public Files

- `index.html` exists and is the public reader.
- `llms.txt` exists and points agents to compact routes.
- `agent-router.json` exists.
- `agent-corpus/` exists.
- `CONSTITUTION.md` exists.
- `AGENTS.md` exists.

## Safety

- No full transcripts.
- No local paths.
- No credentials.
- No private project references.
- No machine-specific helper commands.

## GitHub Pages

Recommended setting:

- Source: GitHub Actions
- Artifact: `_site/`, built by `scripts/build_site.py`
- Entry: `index.html`
