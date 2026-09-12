---
title: Presets
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/presets.html"
---

# Presets

A preset holds attribute/timing values for a selection and may be **referenced** from cues, recipes, or the programmer. Updating the preset updates references without rewriting each cue.

Pools exist per feature group (filtered) plus All 1–5 (unfiltered). Preset modes: **Selective**, **Global**, **Universal** (manual letters S/G/U).

**Depth:** [`../presets.md`](../presets.md).

## Syntax

Applies **preset 4.1** (feature-group 4, preset 1) to fixture 1 in the programmer:

```
Fixture 1 At Preset 4.1
```

Stores the active programmer values as **preset 4.2**:

```
Store Preset 4.2
```

Updates **preset 4.2** with the current active programmer values (references keep pointing here):

```
Update Preset 4.2
```

Calls dimmer preset **1.3** onto fixture 7 using a temporary Universal mode:

```
ClearAll; Fixture 7; At Preset 1.3 /Universal
```

See [`Preset`](../keywords/Preset.md), [`At`](../keywords/At.md), [`Store`](../keywords/Store.md), [`Update`](../keywords/Update.md). Unattended store: [`../automation.md`](../automation.md).

## Related

- Data pools: [`datapools.md`](datapools.md)
- Recipes: [`recipes.md`](recipes.md) (recipe Selection must be a group)
- Worlds / filters as input filters: [`worlds-filters.md`](worlds-filters.md)
