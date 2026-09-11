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

## Concepts follow the manual TOC

Concept pages under `specs/concepts/` use **kebab filenames that mirror grandMA3 help.html chapter hubs** (agent-relevant chapters), not ad-hoc subsystem nicknames. Live map: [`specs/concepts/_index.md`](../../specs/concepts/_index.md). Old filenames may remain under `specs/concepts/_legacy/` for reference only.

1. **Structure first** — add/adjust the chapter page to match the Target manual hub (`manual_url` to that hub HTML). Frontmatter: `title`, `source: mixed` (or other provenance), `manual_url`.
2. **GUI → syntax** — rewrite operator/GUI how-tos as command-line examples using **only** tokens that exist under `specs/keywords/`. No images. Bare commands (strip CLI chrome). Never invent keywords or options.
3. **Then integrate curated** — fold useful bits from `_legacy/` and from Topic Specs into short **Curated** / Extra-style sections on the matching new page. Do not invent facts; link Topic Specs for depth (especially multi-station, OSC, plugins, PhaserRecipe).

### Concept page completeness

Every **agent-relevant** concept page (not an explicit out-of-scope stub) must include:

1. **What it is** — a short description taken from the Target manual hub (or a labeled Curated fact). A list of child pool names or subtopic titles is **not** a description. If there is **no Topic Spec** for the hub, the concept page *must* carry this description.
2. **Primary syntax** — at least one bare-command example of the basic action (store / select / run) when that action exists in Keyword Specs. Example: store a group from the programmer (`Fixture 1 Thru 10` then `Store Group 1`).
3. **Examples state the result** — every command example (concepts, Topic Specs, Keyword Extra) needs a short line saying what the command **does** / what object or state it produces. Do not only describe operator steps ("select fixtures, then store"). Concept pages stay brief; Topic Specs may add more examples. Example: "creates Group 1 with fixtures 1 through 10 in it."
4. **Subtopics** — distinct behaviors get their **own heading** (not a buried clause) plus links to sibling concepts, Topic Specs, and Keyword Specs. Example: Group Masters are a separate heading on [`groups.md`](../../specs/concepts/groups.md), affecting playback of fixtures in the group, with a link to [`masters.md`](../../specs/concepts/masters.md) and the Group Masters manual topic.

When the user flags a missing description or a buried subtopic, fix that page **and audit the rest of `specs/concepts/`** for the same gap.

Recipe rows: a recipe line's **Selection** must be a **group**. Record that on both [`groups.md`](../../specs/concepts/groups.md) and [`recipes.md`](../../specs/concepts/recipes.md).

**Groups depth** (programmer selection → store, `+` / `-` selection builds, `/Merge` `/Remove` `/Overwrite` into an existing group) lives in Topic Spec [`specs/groups.md`](../../specs/groups.md). Keep [`specs/concepts/groups.md`](../../specs/concepts/groups.md) thin with a few primary examples and a pointer.

**Automation** (macros, plugin `Cmd`, OSC — any unattended CLI): Topic Spec [`specs/automation.md`](../../specs/automation.md). Commands that can prompt must use [`/NoConfirmation`](../../specs/keywords/options/Noconfirmation.md); prefer explicit store modes plus `/NoConfirmation`. Do not bury this only on the option Keyword Spec.

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
