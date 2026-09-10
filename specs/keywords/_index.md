# Keyword Specs

The **only** command-syntax dictionary for agents. General keywords and option keywords both live here. Target: see [`../versions.md`](../versions.md).

- General keywords: `specs/keywords/<Name>.md` (this folder, besides `_index.md`)
- Option keywords: [`options/`](options/)
- Archived: [`archive/`](archive/) — do not use for new Target commands

Each file is a Keyword Spec:

```yaml
---
keyword: Store
kind: general   # or option
shortcuts: [Sto]
manual_url: https://help.malighting.com/grandMA3/2.5/HTML/…
introduced: 1.0.0.1   # omit if unknown; never guess
# deprecated: 2.3.0.0  # omit if current
---
```

1. `## Official` — from the Target user manual (crawler may replace this section and may update `shortcuts` / `manual_url` / `deprecated`)
2. `## Extra` — contributor notes (crawler must keep; never blank `introduced`)

**Lifecycle:** deprecated-but-still-on-Target stays here (do not suggest for new commands). Move to `archive/` when gone from Target, or ≥ 24 months after the deprecation release. Details: [`CONTEXT.md`](../../CONTEXT.md).

Do not load `specs/raw/` as a second keyword list. Grammar (how the command line works) will live in `specs/command-line.md`, not here.

Keyword files are not crawled yet — this index is the layout lock.
