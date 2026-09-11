---
title: Sequences, cues & playback
source: mixed
---

# Sequences, cues & playback

Looks for playback live in **cues** inside **sequences**, usually fired from **executors**. Agents store looks into cues, then Go+/Goto them — or call sequences by command.

## Objects

| Object | Spec | Notes |
| --- | --- | --- |
| [`Sequence`](../keywords/Sequence.md) | Object keyword | Pool of cues; selected sequence is the default target for bare `Cue …` |
| [`Cue`](../keywords/Cue.md) | Object keyword | **Only** object type whose numeric IDs may be decimal fractions (`0.001`–`9999.999`). Elsewhere `.` is parent.child |
| Executors | — | Physical/virtual playback assignments; layout note: [`../hardware-layout.md`](../hardware-layout.md) (`source: lab`) |

Default SelFix on Cue: calling a cue without a function can select fixtures that have values in that cue (see Cue Spec).

## Common commands

```text
Store Cue 1
Store Sequence 2 Cue 3.5
Go+ Sequence 1
Go- 
Goto Cue 5
```

Playback keywords (see keyword index for Official text): `Go+`, `Go-`, `Goto`, `Load`, `Pause`, `Off`, `On`, `Call`, …

## Parts & recipes

Cues can have **parts**; phaser content may use **PhaserRecipe** objects — automation depth in [`../phaser-recipe.md`](../phaser-recipe.md), map in [`phasers.md`](phasers.md).

## Multi-station

Cue-command plugins run on the **master**; CmdLine/Macro paths run **local**. Details: [`../multi-station.md`](../multi-station.md).
