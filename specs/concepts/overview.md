---
title: grandMA3 system overview
source: mixed
---

# System overview

High-level map of grandMA3 for coding agents (OSC, macros, Lua plugins). **Not** an operator GUI manual.

## Layers in this repo

1. **This concepts tree** — orientation and pointers only.
2. **Topic Specs** (`specs/*.md`) — automation-first depth (behavior, gotchas, long commands).
3. **Keyword Specs** (`specs/keywords/`) — one CLI token each.
4. **Grammar** — `specs/command-line.md` (when present).
5. **Raw** — Help Dumps, release notes (versioned listings, not narrative Specs).

## Mental model (station)

A **station** (console or onPC) runs a show file: pools of objects (fixtures, presets, sequences, macros, plugins, …), a **programmer** (active values), **playback** (sequences / executors), and optional **network session** with other stations.

Automation usually enters via:

- Command line / OSC (`/gma3/cmd`) — see [`../osc.md`](../osc.md), [`../remote-command.md`](../remote-command.md)
- Lua plugins — see [`../plugins.md`](../plugins.md), [`../object-api.md`](../object-api.md)
- Macros (stored command lines)

## Subsystems

See [`_index.md`](_index.md) for the subsystem list and links into Topic Specs + keyword clusters.

## Provenance

Concept pages use frontmatter `source`: `manual` | `observed` | `lab` | `mixed` (definitions in [`CONTEXT.md`](../../CONTEXT.md)).
