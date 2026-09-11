---
title: Concept map (manual TOC)
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/help.html"
---

# Concept map

Concept pages follow the **grandMA3 2.5 manual help.html chapter order** (agent-relevant hubs). Depth stays in flat Topic Specs under `specs/*.md` and Keyword Specs under `specs/keywords/`.

GUI how-tos from the manual are rewritten here as **syntax-first** command examples (Keyword Specs only — never invent tokens). After a new chapter page exists, useful bits from `_legacy/` and Topic Specs may be folded in as short **Curated** sections.

Layout rules: [`CONTEXT.md`](../../CONTEXT.md). Contribution: [`.agents/rules/contribute.md`](../../.agents/rules/contribute.md).

Target: [`../versions.md`](../versions.md). Grammar: [`../command-line.md`](../command-line.md). Keywords: [`../keywords/_index.md`](../keywords/_index.md).

## Chapters (manual order)

| Manual hub | Concept page | Topic Specs (depth) |
| --- | --- | --- |
| System Overview (`system.html`) | [`system.md`](system.md) | — |
| First Steps (`first_steps.html`) | [`first-steps.md`](first-steps.md) | out-of-scope for most agents |
| Show File Handling (`show_file_management.html`) | [`show-file-handling.md`](show-file-handling.md) | — |
| Command Syntax and Keywords (`command_syntax_keywords.html`) | [`command-syntax.md`](command-syntax.md) | [`../command-line.md`](../command-line.md) |
| Networking (`network.html`) | [`networking.md`](networking.md) | [`../multi-station.md`](../multi-station.md), [`../api-objects-network.md`](../api-objects-network.md) |
| Single / Multi User (`user.html`) | [`users.md`](users.md) | [`../multi-station.md`](../multi-station.md) |
| DMX In and Out (`dmx.html`) | [`dmx.md`](dmx.md) | — |
| Patch and Fixture Setup (`patch.html`) | [`patch.md`](patch.md) | — |
| Operate Fixtures (`operate_fixtures.html`) | [`operate-fixtures.md`](operate-fixtures.md) | — |
| The Programmer (`operate_programmer.html`) | [`programmer.md`](programmer.md) | — |
| Groups (`group.html`) | [`groups.md`](groups.md) | [`../groups.md`](../groups.md) |
| Presets (`presets.html`) | [`presets.md`](presets.md) | — |
| Worlds / Filters (`worldfilter.html`) | [`worlds-filters.md`](worlds-filters.md) | — |
| MAtricks (`matricks.html`) | [`matricks.md`](matricks.md) | — |
| Cues and Sequences (`cue_sequence.html`) | [`cues-sequences.md`](cues-sequences.md) | — |
| Executors (`executor.html`) | [`executors.md`](executors.md) | [`../hardware-layout.md`](../hardware-layout.md) |
| Masters (`masters.html`) | [`masters.md`](masters.md) | — |
| Recipes (`recipes.html`) | [`recipes.md`](recipes.md) | [`../phaser-recipe.md`](../phaser-recipe.md) |
| Phasers (`phaser.html`) | [`phasers.md`](phasers.md) | [`../phaser-recipe.md`](../phaser-recipe.md) |
| Macros (`macros.html`) | [`macros.md`](macros.md) | — |
| Agenda (`agenda.html`) | [`agenda.md`](agenda.md) | [`../startup-dmxremote-agenda.md`](../startup-dmxremote-agenda.md) |
| Plugins (`plugins.html`) | [`plugins.md`](plugins.md) | [`../plugins.md`](../plugins.md), [`../object-api.md`](../object-api.md), [`../hooks.md`](../hooks.md), [`../message-queue.md`](../message-queue.md), [`../addonvars.md`](../addonvars.md) |
| Data Pools (`datapool.html`) | [`datapools.md`](datapools.md) | — |
| Remote In and Out (`remote_inputs.html`) | [`remote-in-out.md`](remote-in-out.md) | [`../osc.md`](../osc.md), [`../remote-command.md`](../remote-command.md), [`../multi-station.md`](../multi-station.md) |
| Timecode (`timecode.html`) | [`timecode.md`](timecode.md) | — |
| Layouts (`layouts.html`) | [`layouts.md`](layouts.md) | — |
| Quickeys (`quickeys.html`) | [`quickeys.md`](quickeys.md) | — |
| Workspace (`workspace.html`) | [`workspace.md`](workspace.md) | out-of-scope for most agents |
| Shapes / Generators / Bitmap / XYZ / Local settings | [`shapes.md`](shapes.md), [`generators.md`](generators.md), [`bitmap.md`](bitmap.md), [`xyz.md`](xyz.md), [`local-settings.md`](local-settings.md) | out-of-scope for most agents |

## Alias

- [`multi-station.md`](multi-station.md) — thin pointer → [`networking.md`](networking.md) + Topic Spec [`../multi-station.md`](../multi-station.md)

## Legacy

Previous concept filenames live under [`_legacy/`](_legacy/) for reference only. Do not load `_legacy/` as the live map.
