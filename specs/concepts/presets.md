---
title: Presets
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/presets.html"
---

# Presets

A preset holds attribute/timing values for a selection and may be **referenced** from cues, recipes, or the programmer. Updating the preset updates references without rewriting each cue.

Pools exist per feature group (filtered) plus All 1–5 (unfiltered). Preset modes: **Selective**, **Global**, **Universal** (manual letters S/G/U).

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

See [`Preset`](../keywords/Preset.md), [`At`](../keywords/At.md), [`Store`](../keywords/Store.md), [`Update`](../keywords/Update.md).

## Related

- Data pools: [`datapools.md`](datapools.md)
- Recipes: [`recipes.md`](recipes.md)
