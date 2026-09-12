---
title: Phasers
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/phaser.html"
---

# Phasers

Phasers create **dynamic** output from a **single** preset or cue by adding **two or more steps** of attribute values. A static look is one step; extra steps make a phaser.

Users also call them **effects**, **effect engine**, or **dimmer / color / position effects** (those three are the most common). The console name is Phaser.

They store into **cues and presets the same way static looks do**. Two ways to build the steps:

1. **Programmer** (classic) — steps in the programmer, then `Store Cue` / `Store Preset`. Manual: [Phasers](https://help.malighting.com/grandMA3/2.5/HTML/phaser.html) (programmer steps / Step key) and [Create a Sinus Dimmer Phaser](https://help.malighting.com/grandMA3/2.5/HTML/phaser_create_dimmer.html) (ends with store into a preset or cue).
2. **PhaserRecipe** (MA ≥ 2.4) — violet recipe lines on a cue part or preset. Depth: [`../phaser-recipe.md`](../phaser-recipe.md).

**Topic Spec (depth):** [`../phasers.md`](../phasers.md).

## Syntax

Selects the next programmer step so following At values land in step 2 (step 1 must already have data):

```
Next Step
```

Two-step dimmer phaser in the programmer, then stored as **cue 2** (same store as a static look):

```
Fixture 1 Thru 10; At 0; Next Step; At 100; Store Cue 2 /NoConfirmation
```

## Related

- **Topic Spec:** [`../phasers.md`](../phasers.md)
- Programmer: [`programmer.md`](programmer.md)
- Cues / sequences: [`cues-sequences.md`](cues-sequences.md)
- Presets: [`presets.md`](presets.md)
- Recipes: [`recipes.md`](recipes.md)
- PhaserRecipe: [`../phaser-recipe.md`](../phaser-recipe.md)
