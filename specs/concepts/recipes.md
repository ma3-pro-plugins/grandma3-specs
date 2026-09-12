---
title: Recipes
topic_spec:
  - ../recipes.md
  - ../phaser-recipe.md
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/recipes.html"
---

# Recipes

Recipes store reusable programming as **recipe lines** on cue parts or presets. Each line describes what to cook (selection, values, MAtricks, fade/delay/speed/phase). Cooking writes those values into the cue part, preset, or programmer.

A recipe line's **Selection** is a **group**. Groups are a basic building block of recipes — see [`groups.md`](groups.md).

A line can hold **MAtricks** values itself (X/Y/Z families). Assigning a MAtricks pool object to `matricks` **spreads** those values onto the row as **defaults**. Depth + full property list: Topic Spec.

Recipes can live in cue parts and in presets. Cue-part recipes must be cooked; preset recipes cook automatically. Values stored directly in a cue part outrank that part's recipe; values stored in a preset outrank that preset's recipe.

**Topic Spec (depth — Store/Assign recipe lines, Cook, Plugin access):** [`../recipes.md`](../recipes.md).

## PhaserRecipe depth

Automation/API for PhaserRecipe (MA ≥ 2.4, distinct from StandardRecipe / `HRecipe`): **[`../phaser-recipe.md`](../phaser-recipe.md)**.

Phaser editor orientation: [`phasers.md`](phasers.md).

## Related

- **Topic Spec:** [`../recipes.md`](../recipes.md)
- Groups (Selection): [`groups.md`](groups.md)
- Presets: [`presets.md`](presets.md)
- Cues / sequences: [`cues-sequences.md`](cues-sequences.md)
- MAtricks: [`matricks.md`](matricks.md)
- Selection grid XYZ: [`operate-fixtures.md`](operate-fixtures.md)
