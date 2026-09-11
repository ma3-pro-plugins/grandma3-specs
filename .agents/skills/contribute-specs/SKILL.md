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

## When the user states a new contribution rule

1. Add it to `.agents/rules/contribute.md` (and CONTEXT if it is structural vocabulary).
2. Do **not** only store it in chat memory — the repo is the source of truth for contributors.
3. Keep consumer rules in `.agents/rules/consume.md` / `AGENTS.md` if the rule affects readers too.

## After edits

1. Update `INDEX.md` / concept `_index.md` if new entry points appeared.
2. Rebuild keyword indexes only after keyword crawls (`rebuild_keyword_index.py`).
3. Commit with [commit](../commit/SKILL.md) when the user asks.
