# Rules: contributing to grandma3-specs

For agents **editing** this repo (Specs, concepts, skills, indexes). Consumers use [consume.md](consume.md).

## Layers (do not collapse)

| Layer | Path | Job |
| --- | --- | --- |
| Map | `specs/concepts/` | Thin overview + pointers |
| Topic Specs | `specs/*.md` (flat) | Automation-first depth |
| Keyword Specs | `specs/keywords/` | Official + Extra per token |
| Grammar | `specs/command-line.md` | Composition rules only |

Do **not** mass-move Topic Specs into `concepts/`.

## Cross-cutting topics

**Multi-station** (sessions, master/follower, where CmdLine/Macro/Cue Command run, OSC relay in a session) lives in **[`specs/multi-station.md`](../../specs/multi-station.md)** (concept pointer: `specs/concepts/multi-station.md`).

- Other concepts/Topic Specs may **mention** multi-station in one short line and **link** there.
- Do **not** duplicate master/session matrices into `sequences-playback`, `plugins`, `osc`, etc. Keep transport/quoting depth in those Specs; keep session routing in `multi-station.md`.
- When a new fact is multi-station behavior, add or update `multi-station.md` first, then add a one-line pointer from the page you were editing.

Same pattern for future cross-cuts: one canonical Topic Spec, thin mentions elsewhere. When the user states such a rule, record it here and in CONTEXT.

## Provenance

Topic Spec / concept frontmatter `source`: `manual` | `observed` | `lab` | `mixed` (see CONTEXT). Optional `manual_url`.

## Keywords

- Replace `## Official` only when crawling; never overwrite `## Extra` or blank `introduced`.
- Filenames: PascalCase from HTML stem. Index via `rebuild_keyword_index.py` (Keyword + description, no shortcuts column).
- Never invent Official text or options.

## Syntax-first enrichment

GUI how-tos → command recipes only with evidenced keywords; live in Extra / Concept “Syntax”, not as a replacement for Keyword Official.

## Commits

Follow [`.agents/skills/commit/SKILL.md`](../skills/commit/SKILL.md). Direct to `main` unless the user asked for a PR.

## Procedure skill

Step-by-step when editing: [contribute-specs](../skills/contribute-specs/SKILL.md).
