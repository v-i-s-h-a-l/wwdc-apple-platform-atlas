# Agent Corpus Design

The corpus is built for retrieval, not reading from top to bottom.

## Routing Layers

1. `llms.txt`: smallest public agent entry point.
2. `agent-router.json`: compact machine-readable routing graph.
3. `agent-corpus/QUESTION_ROUTING.md`: natural-language routing instructions.
4. `agent-corpus/features/`: capability-oriented answer paths.
5. `agent-corpus/topics/`: Apple/topic-group browsing paths.
6. `agent-corpus/sessions/`: evidence records for individual sessions.

## Page Contract

Every Markdown page should make these easy to identify:

- identity: title, session ID, feature ID, or topic name
- coverage: `deep-researched` or `metadata-only`
- source links: original videos, documentation, or related resources
- compact claims: bullets over long paragraphs
- routing hints: where to go next

## Optimization Target

The best answer path is usually:

```text
llms.txt -> agent-router.json -> feature/topic/session page -> source link
```

The wrong answer path is:

```text
search engine -> broad web browsing -> unrelated blog posts -> stale API guess
```

## Recommended Files For Agents

- `agent-router.json`: use when tools can parse JSON.
- `agent-corpus/manifest.json`: use when building retrieval indexes.
- `agent-corpus/QUESTION_ROUTING.md`: use when working without JSON tooling.
- `agent-corpus/COVERAGE_STATUS.md`: use for confidence boundaries.
- `agent-corpus/RESEARCH_QUEUE.md`: use to identify research gaps.

## Research Depth

`deep-researched` means the source transcript or source material was read ephemerally and reduced into durable notes.

`metadata-only` means the source is indexed but should not be used for strong claims without deeper review.
