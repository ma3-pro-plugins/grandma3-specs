---
name: contribute-specs
description: >-
  Edit grandma3-specs (Topic Specs, concepts, keywords, grammar, rules).
  Use when adding or changing Specs, concept pages, indexes, or repo
  contribution rules — not when only consuming Specs to write show commands.
---

# Contribute to grandma3-specs

Read [`.agents/rules/contribute.md`](../../rules/contribute.md) first and follow it.

## Before writing

1. Confirm Target in `specs/versions.md`.
2. Decide layer: concept (thin pointer) vs Topic Spec (depth) vs Keyword Spec vs grammar.
3. If the fact is **multi-station / master / where commands run**, edit `specs/multi-station.md` (and only add a one-line link from other pages).


## Version facts (do not add SupportedFeatures)

Do **not** vendor a `SupportedFeatures`-style matrix. That is a runtime branch table for plugins on old desks. Specs on `main` describe **Target only**.

Put a version fact on the page that uses it:

- **Keywords** — `introduced` / `deprecated` is the token changelog. Omit `introduced` if unknown; never guess.
- **Topic Specs** — one “since MA x.y” line only when an agent would otherwise take the old path (e.g. `GetObject` 2.1.1.2, PhaserRecipe 2.4).
- **Migration Specs** — behavior that *broke* between releases (e.g. Lua 5.4 → 5.5).
- **Release-notes dumps** — the raw changelog. Do not rewrite them into a second highlights file.

Ingest a `SupportedFeatures` / `lib/ma_obj` flag as a **fact on that Spec** (issue #5: facts only, no vendoring). Do not copy the whole table.

## When the user states a new contribution rule

1. Add it to `.agents/rules/contribute.md` (and CONTEXT if it is structural vocabulary).
2. Do **not** only store it in chat memory — the repo is the source of truth for contributors.
3. Keep consumer rules in `.agents/rules/consume.md` / `AGENTS.md` if the rule affects readers too.

## After edits

1. Update `INDEX.md` / concept `_index.md` if new entry points appeared.
2. Rebuild keyword indexes only after keyword crawls (`rebuild_keyword_index.py`).
3. Commit with [commit](../commit/SKILL.md) when the user asks.
