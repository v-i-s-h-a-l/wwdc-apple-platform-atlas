# Research System

This repository turns source collections into static routing artifacts for AI agents.

## Pipeline

```text
official sources
  -> normalized JSON
  -> generated corpus pages
  -> compact router indexes
  -> public reader
  -> validation
  -> static publication
```

## Artifacts

- `data/session-atlas.json`: normalized source of truth for the current corpus.
- `agent-corpus/`: generated Markdown research graph.
- `agent-router.json`: compact machine-readable routing graph.
- `llms.txt`: compact root agent entry point.
- `index.html`: public reader.

## Why Static

Static artifacts are cheap for agents to fetch, easy to inspect, easy to host, and safe to version. They also avoid runtime dependencies when an agent only needs routing context.

## Reusing The Pattern

To create another corpus:

1. Define the source inventory.
2. Define topic and feature routing dimensions.
3. Normalize sources into JSON.
4. Generate session/source pages.
5. Generate compact route indexes.
6. Validate safety and token budget.
7. Publish the static reader and corpus.
