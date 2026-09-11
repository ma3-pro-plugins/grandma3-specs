---
title: grandMA3 system overview
source: mixed
---

# System overview

High-level map of grandMA3 for coding agents (OSC, macros, Lua plugins). **Not** an operator GUI manual.

## Layers in this repo

1. **Concepts** (`specs/concepts/`) — orientation and pointers only.
2. **Topic Specs** (`specs/*.md`) — automation-first depth (behavior, gotchas, long commands).
3. **Keyword Specs** (`specs/keywords/`) — one CLI token each (Official + Extra).
4. **Grammar** — [`../command-line.md`](../command-line.md).
5. **Raw** — Help Dumps, release notes (versioned listings).

Load order: [`../versions.md`](../versions.md) → this map → Topic Spec → keyword file → Help Dump if needed.

## Mental model (station)

A **station** (console or onPC) holds a show file:

| Piece | Role for automation |
| --- | --- |
| **Data pools** | Named pools of objects (fixtures, presets, sequences, macros, plugins, …) |
| **Programmer** | Live values for the current selection before Store/Update |
| **Playback** | Sequences on executors; Go+/Go-/Goto drive cues |
| **Session** | Optional multi-station link; one **GlobalMaster** — see [`multi-station.md`](multi-station.md) |

Automation usually enters via:

- Command line / OSC — [`../osc.md`](../osc.md), [`../remote-command.md`](../remote-command.md), [`../command-line.md`](../command-line.md)
- Lua plugins — [`../plugins.md`](../plugins.md), [`../object-api.md`](../object-api.md)
- Macros (stored command lines)

## Command shape (one line)

Typical pattern (details in grammar Spec):

```text
[Function] [Object] [IdOrName] [/Option…]
```

Examples agents actually send:

```text
Fixture 1 Thru 10 At 50
Store Cue 1
Call Plugin "MyPlugin" '{"a":1}'
DumpLog /nc
```

Bare commands only — never include console CLI chrome (`User name[Fixture]>`).

## Subsystems

Full table: [`_index.md`](_index.md).

| If you need… | Start here |
| --- | --- |
| Tokens / syntax rules | [`../command-line.md`](../command-line.md) + keyword index |
| Live values / Store | [`programmer.md`](programmer.md) |
| Cues / Go | [`sequences-playback.md`](sequences-playback.md) |
| Phasers / recipes | [`phasers.md`](phasers.md) → [`../phaser-recipe.md`](../phaser-recipe.md) |
| OSC / prove commands | [`osc-remote.md`](osc-remote.md) |
| Plugins / Lua VM | [`plugins-lua.md`](plugins-lua.md) |

## Provenance

Frontmatter `source`: `manual` | `observed` | `lab` | `mixed` — see [`CONTEXT.md`](../../CONTEXT.md).
