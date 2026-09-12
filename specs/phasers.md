---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/phaser.html"
---

# Phasers (Topic Spec)

Concept map (thin): [`concepts/phasers.md`](concepts/phasers.md). Programmer steps: [`keywords/Step.md`](keywords/Step.md). PhaserRecipe objects (MA ≥ 2.4): [`phaser-recipe.md`](phaser-recipe.md).

Manual hub + programmer walkthroughs (one Spec, not one file per tutorial): [Phasers](https://help.malighting.com/grandMA3/2.5/HTML/phaser.html) (steps, layers, Stomp, Sync), [Phaser Editor](https://help.malighting.com/grandMA3/2.5/HTML/phaser_editor.html), [Create a Sinus Dimmer Phaser](https://help.malighting.com/grandMA3/2.5/HTML/phaser_create_dimmer.html), plus the other official create tutorials on that hub (circle, circle around a position preset, color rainbow).

## Also called effects

Users often say **effect**, **effects**, or **effect engine**. Dimmer, color, and position effects are the most common. The console and this repo use **Phaser**.

A **static look** is one step of values. A phaser is the same store target (cue or preset) with **two or more steps**. Absolute and relative layers store and play back separately (manual).

## Store like a static look

Build the phaser, then store it the same way as a static look (`Store Cue` / `Store Preset`). Unattended macros/plugins/OSC: name the store mode and append [`/NoConfirmation`](keywords/options/Noconfirmation.md) — [`automation.md`](automation.md).

Stores the active programmer (static look or phaser) as **cue 2** of the selected sequence:

```
Store Cue 2 /NoConfirmation
```

Stores the active programmer as **preset 4.2**:

```
Store Preset 4.2 /NoConfirmation
```

Two ways to get the steps in:

1. **Programmer** (classic) — build steps in the programmer, then store. This is what the [Phasers](https://help.malighting.com/grandMA3/2.5/HTML/phaser.html) hub and [Create a Sinus Dimmer Phaser](https://help.malighting.com/grandMA3/2.5/HTML/phaser_create_dimmer.html) teach.
2. **PhaserRecipe** (MA ≥ 2.4) — violet recipe lines on a cue part or preset. Not a StandardRecipe (`Store Recipe` creates `HRecipe`). Depth: [`phaser-recipe.md`](phaser-recipe.md).

## Programmer steps

Requires step 1 to already have data. Selects the **next** programmer step so the following values land in that step:

```
Next Step
```

Selects the **previous** programmer step:

```
Previous Step
```

Two-step dimmer phaser in the programmer (step 1 = 0, step 2 = full), then store as cue 2. Manual walkthrough: [Create a Sinus Dimmer Phaser](https://help.malighting.com/grandMA3/2.5/HTML/phaser_create_dimmer.html) (also shows Accel/Decel −100 and Phase `0 Thru 360` from the encoder bar):

```
Fixture 1 Thru 10; At 0; Next Step; At 100; Store Cue 2 /NoConfirmation
```

Deletes **step 3** from the programmer:

```
Delete Step 3
```

Hold **Step** and tap presets to stamp steps (same-attribute preset = next step; different attributes add to the current step) — that path is GUI; the CLI equivalent is `Next Step` / `At Preset …`. Confirm tokens on [`keywords/_index.md`](keywords/_index.md) (`Step`, `Next`, `Previous`, `Phase`, `Speed`, `Width`, `Transition`, Accel/Decel). Do not invent layer names.

## Stomp and Sync

**Stomp** stops a running phaser (programmer or playback) and leaves the last static output in programmer step 1. Calling a static preset onto attributes that are already phasing stomps them.

**Sync** keeps recall timing/phase predictable: encoder-bar option when calling a phaser into the programmer; cue-part setting when recalling from a cue — [`concepts/cues-sequences.md`](concepts/cues-sequences.md).

## Related

- Programmer: [`concepts/programmer.md`](concepts/programmer.md)
- Cues / sequences: [`cues-sequences.md`](cues-sequences.md)
- Presets: [`presets.md`](presets.md)
- Recipes: [`recipes.md`](recipes.md)
- PhaserRecipe API: [`phaser-recipe.md`](phaser-recipe.md)
