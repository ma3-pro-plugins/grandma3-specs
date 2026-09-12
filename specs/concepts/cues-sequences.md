---
title: Cues and Sequences
topic_spec: ../cues-sequences.md
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/cue_sequence.html"
---

# Cues and Sequences

Looks for playback live in **cues** inside **sequences**. Tracking, cue timing, MIB, recipes, store/update/copy/delete — manual subtopics.

**Topic Spec (depth — store modes, Update/Cook Official options, MIB + Sequence props typings, no Renumber keyword):** [`../cues-sequences.md`](../cues-sequences.md).

## Objects

| Object | Notes |
| --- | --- |
| [`Sequence`](../keywords/Sequence.md) | Cue pool; selected sequence is default for bare `Cue …` |
| [`Cue`](../keywords/Cue.md) | **Only** object type whose numeric IDs may be decimal fractions (`0.001`–`9999.999`) |

## Store / update / playback (syntax)

Stores the active programmer values as **cue 1** of the selected sequence:

```
Store Cue 1
```

Stores the active programmer values as **cue 3.5** of sequence 2:

```
Store Sequence 2 Cue 3.5
```

Updates **cue 1** of the selected sequence with the current active programmer values:

```
Update Cue 1
```

Starts sequence 1 / goes to its **next cue** (`Go+`):

```
Go+ Sequence 1
```

Goes to the **previous cue** of the selected sequence (`Go-`):

```
Go-
```

Jumps the selected sequence to **cue 5**:

```
Goto Cue 5
```

Playback keywords (Official on each Spec): `Go+` → [`Goplus`](../keywords/Goplus.md), `Go-` → [`Gominus`](../keywords/Gominus.md), [`Goto`](../keywords/Goto.md), plus Load/Pause/Off/On/Call as listed in the keyword index.

Store / Update / Cook option lists: Topic Spec [`../cues-sequences.md`](../cues-sequences.md) and Keyword Official tables ([`Update`](../keywords/Update.md), [`Cook`](../keywords/Cook.md), [`../keywords/options/`](../keywords/options/)). Unattended store/delete/copy: [`../automation.md`](../automation.md) (`/NoConfirmation` when Official lists it — not on Update).

## Related

- **Topic Spec:** [`../cues-sequences.md`](../cues-sequences.md)
- Executors: [`executors.md`](executors.md)
- Cue / phaser recipes: [`recipes.md`](recipes.md), [`../phaser-recipe.md`](../phaser-recipe.md) (recipe **Selection** is a group — [`groups.md`](groups.md) / [`../groups.md`](../groups.md))
- Cue-command plugins run on the **master** — [`../multi-station.md`](../multi-station.md)

## Curated

Default SelFix on Cue: calling a cue without a function can select fixtures that have values in that cue (see Cue Spec).
