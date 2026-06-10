# Source Policy

The repository stores routing data and derived research notes, not raw source dumps.

## Allowed

- Official source URLs
- Metadata from official pages
- Chapter titles and timestamps when available
- Short derived summaries
- API and concept terms
- Coverage status
- Links to documentation and related resources
- Sanitized source collection metadata

## Disallowed

- Full transcript bodies
- Credentials or tokens
- Local filesystem paths
- Private project names
- Local helper ports or commands
- Unsanitized browser/session caches

## Transcript Rule

Transcript text may be fetched ephemerally during generation. It must be reduced into structured notes and discarded.

## Public Export Rule

Before publishing:

```bash
python3 scripts/validate_public_repo.py
```

The validator checks JSON, required files, private-reference patterns, and transcript-cache markers.
