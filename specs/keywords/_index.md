# Keyword Specs

The **only** command-syntax dictionary for agents. General keywords and option keywords both live here. Target: see [`../versions.md`](../versions.md).

- General keywords: `specs/keywords/<Name>.md` (this folder, besides `_index.md`)
- Option keywords: [`options/`](options/)

Each file is a Keyword Spec:

1. YAML frontmatter (`keyword`, `kind`, `shortcuts`, `manual_url`)
2. `## Official` — from the Target user manual (crawler may replace)
3. `## Extra` — contributor notes (crawler must keep)

Do not load `specs/raw/` as a second keyword list. Grammar (how the command line works) will live in `specs/command-line.md`, not here.

Keyword files are not crawled yet — this index is the layout lock.
