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
2. **Primary syntax** — at least one bare-command example of the basic action (store / select / run) when that action exists in Keyword Specs. Example: store a group from the programmer (`Fixture 1 Thru 10; Store Group 1`).
3. **Examples state the result** — every command example (concepts, Topic Specs, Keyword Extra) needs a short line **immediately before or after that fence** saying what **that** command does. A section heading or a caption on a neighbor fence does not count. Do not only describe operator steps ("select fixtures, then store"). Concept pages stay brief; Topic Specs may add more examples. Example: "This command runs macro 1 (Go+)." / "creates Group 1 with fixtures 1 through 10 in it."
4. **CLI fences are pasteable** — GitHub’s copy button copies the fenced block as-is. The grandMA3 command line does **not** accept a multi-line paste. So a fenced **CLI** example must be **one line**:
   - One statement, or several that must run as a unit, joined with [`;` (Semicolon)](../../specs/keywords/Semicolon.md) and **no newlines** (e.g. `Fixture 1 Thru 5 + Fixture 10 Thru 12; Store Group 2 /NoConfirmation`).
   - Unrelated / alternative commands each get their **own** fence (do not `;`-join a catalog — copy would run all of them).
   - Not CLI (Lua, object trees, grammar templates, Keyword Official from the crawler): multi-line is fine.
5. **Subtopics** — distinct behaviors get their **own heading** (not a buried clause) plus links to sibling concepts, Topic Specs, and Keyword Specs. Example: Group Masters are a separate heading on [`groups.md`](../../specs/concepts/groups.md), affecting playback of fixtures in the group, with a link to [`masters.md`](../../specs/concepts/masters.md) and the Group Masters manual topic.

When the user flags a missing description or a buried subtopic, fix that page **and audit the rest of `specs/concepts/`** for the same gap.

Recipe rows: a recipe line's **Selection** must be a **group**. Record that on both [`groups.md`](../../specs/concepts/groups.md) and [`recipes.md`](../../specs/concepts/recipes.md).

**Groups depth** (programmer selection → store, `+` / `-` selection builds, `/Merge` `/Remove` `/Overwrite` into an existing group) lives in Topic Spec [`specs/groups.md`](../../specs/groups.md). Keep [`specs/concepts/groups.md`](../../specs/concepts/groups.md) thin with a few primary examples and a pointer.

**Layouts depth** (assign/clone CLI, multipatch, Setup vs operate, element editor, encoder bar, view settings) lives in one Topic Spec [`specs/layouts.md`](../../specs/layouts.md). Do **not** split the seven manual subtopic pages into seven Specs — they are one object. Keep [`specs/concepts/layouts.md`](../../specs/concepts/layouts.md) thin with a pointer.

**Hub depth (general)** — When a concept hub’s Target manual page has **child subtopics** with real CLI (or facts agents need), write **one** Topic Spec at `specs/<hub>.md`. Do **not** split those subtopic pages into separate Specs. Keep the concept page thin with a **Depth** pointer. Live map: [`specs/concepts/_index.md`](../../specs/concepts/_index.md).

Hubs with a Topic Spec today: `system`, `show-file-handling`, `users`, `dmx`, `patch`, `operate-fixtures`, `groups`, `presets`, `worlds-filters`, `matricks`, `cues-sequences`, `executors` (behavior; hardware numbers stay in [`hardware-layout.md`](../../specs/hardware-layout.md)), `masters`, `recipes` (standard recipes; PhaserRecipe stays in [`phaser-recipe.md`](../../specs/phaser-recipe.md)), `phasers` (programmer / effects; PhaserRecipe stays separate), `macros`, `agenda`, `timecode`, `layouts`, `quickeys`. Still pointer-only or out-of-scope: plugins (existing plugin Topic Specs), networking / remote-in-out, phasers, datapools, first-steps, workspace, shapes, generators, bitmap, xyz, local-settings.

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
