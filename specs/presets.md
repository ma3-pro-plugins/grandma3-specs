---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/presets.html"
---

# Presets (Topic Spec)

Concept map (thin): [`concepts/presets.md`](concepts/presets.md). Keyword: [`keywords/Preset.md`](keywords/Preset.md).

Manual hub + subtopics (one Spec): [Pools](https://help.malighting.com/grandMA3/2.5/HTML/presets_pools.html), [Create](https://help.malighting.com/grandMA3/2.5/HTML/presets_create.html), [Recipes](https://help.malighting.com/grandMA3/2.5/HTML/presets_recipes.html), [Use](https://help.malighting.com/grandMA3/2.5/HTML/presets_use.html), [Edit](https://help.malighting.com/grandMA3/2.5/HTML/presets_edit.html).

A preset holds **attribute and timing values** for a selection and may be **referenced** from cues, recipes, or the programmer. Updating the preset updates references — cues/recipes do not need rewriting. Cyan markers mark preset-linked values (tracking sheet / fixture sheet).

## Preset pools

Pools exist **per feature group** (default input filter = that feature group) plus **All 1–5** (no feature-group filter). A **Dynamic** pool window follows the selected feature group in the Feature Group Control Bar — it is not a separate pool of objects.

Addressing is `Preset FeatureGroup.Preset` (e.g. Dimmer = 1 → `Preset 1.3`). Confirm Feature Group numbering from the show / Keyword Official.

Pool/window settings (Name, Input Filter, Cue Part, Display Mode, DataPool, colors, …) are mostly **GUI**. Assign a filter or world as input filter via CLI when needed — see Create below. Data pools: [`concepts/datapools.md`](concepts/datapools.md).

## Preset modes (store / call)

Modes: **Selective (S)**, **Global (G)**, **Universal (U)**. Each pool has a default mode (letter on the pool title). A preset can hold combinations of mode data; pool object letters show what is stored vs the active mode.

| Mode | Meaning (manual) |
| --- | --- |
| Selective | Data valid for each fixture with active stored data |
| Global | Per fixture type; lowest-ID fixture holds shared type data; divergent fixtures add Selective |
| Universal | Valid for all fixtures that have the stored attributes |

Store/update may also use **Default** (respect pool/preset), **Force Global**, **Force Universal** (strip lower-level data on update — confirm [`/ForceGlobal`](keywords/options/Forceglobal.md), [`/ForceUniversal`](keywords/options/Forceuniversal.md)).

Call-time temporary mode overrides (even when the preset’s stored mode would not match the selection): [`/Selective`](keywords/options/Selective.md), [`/Global`](keywords/options/Global.md), [`/Universal`](keywords/options/Universal.md).

Absolute and relative layers can both live in a preset (markers differ). Absolute vs relative updates are handled separately — [`Recast`](keywords/Recast.md) may be needed for cues to pick up a newly added layer.

## Create (store)

Workflow: select fixtures → put values in the programmer → `Store Preset …`. Values must pass the pool **input filter** (feature-group pools filter by FG; All pools do not by default).

Creates **preset 4.2** from the active programmer (store-mode / confirm pop-ups suppressed for automation — [`automation.md`](automation.md)):

```
Store Preset 4.2 /NoConfirmation
```

Store options that affect presets (confirm each option Spec before use): [`/Embed`](keywords/options/Embed.md), [`/MAtricks`](keywords/options/Matricks.md) (store active MAtricks into the preset), [`/KeepActivation`](keywords/options/Keepactivation.md), [`/InputFilter`](keywords/options/Inputfilter.md), mode options above. Prefer explicit `/Merge` `/Overwrite` `/Remove` when storing onto an existing preset — [`keywords/Store.md`](keywords/Store.md), [`keywords/options/_index.md`](keywords/options/_index.md).

Assign a filter (or world) as **input filter** on a preset:

```
Assign Filter 12 At Preset 4.2
```

Assigns **filter 12** as the input filter on **preset 4.2** (Official also documents `Assign World … At Preset …`).

```
Assign World 5 At Preset 2.4
```

Assigns **world 5** as input filter on **preset 2.4**.

**MAgic** presets: calling into the programmer **extracts** hard values (no lasting preset reference). Keep a reference by using the preset from a **recipe**. Recipe **Selection** must be a **group** — [`concepts/recipes.md`](concepts/recipes.md), [`phaser-recipe.md`](phaser-recipe.md), [`groups.md`](groups.md).

## Recipe presets

GUI: Edit Preset Object (swipey) → Add Standard Recipe / Turn into Recipe / Take Selection / Cook / Recast / CleanUp Recipes / Reset MAtricks for Selected. Recipe Template (open cooking-pot icon) cooks into the programmer part.

Cooks **preset 1.1** recipes:

```
Cook Preset 1.1
```

Recasts **preset 21.1** into objects that reference it (e.g. after attributes were added/removed):

```
Recast Preset 21.1
```

Depth for PhaserRecipe / cook semantics: [`phaser-recipe.md`](phaser-recipe.md).

## Use (call / playback)

With a selection, `At Preset …` links attributes to the preset (if mode + attributes make it valid). With **no** selection, tapping/calling a preset can **SelFix** the fixtures that can use it (default pool action SelFix/At — confirm window settings).

Applies a reference to **All 1** preset 45 on the selected fixtures:

```
At Preset 21.45
```

Clears the programmer, selects fixture 7, and calls dimmer preset **1.3** with a temporary **Universal** mode (fixture was not in the selective store):

```
ClearAll; Fixture 7; At Preset 1.3 /Universal
```

Selects fixtures that can use dimmer preset 5 (`SelectFixtures` / Official `SelFix` shortcut — [`keywords/Selectfixtures.md`](keywords/Selectfixtures.md)):

```
SelFix Preset 1.5
```

Extracts preset data into hard programmer values (breaks the reference):

```
Extract Preset 4.2
```

Related Extract forms (Official): `Extract Selection`, `Extract Fixture …`, `Extract Cue …`, and `/Single` — [`keywords/Extract.md`](keywords/Extract.md).

**Executors:** assign with [`Assign`](keywords/Assign.md). Global/Universal presets on executors should use **At** (calls into programmer, not executor playback). Selective presets can use Go+/Toggle/Flash-style playback. OffFade and related playback prefs: Menu → Preferences and Timing → Preset (GUI).

## Edit / update

`Edit` + tap preset pulls values into the programmer (output unless Blind). `Update` opens the Update Menu; modes include Original Content Only vs Add New Content ([`/AddNewContent`](keywords/options/Addnewcontent.md)), plus Preset Mode / Input Filter. Confirm option Specs.

Updates **preset 4.2** from active programmer values (suppress confirm for automation):

```
Update Preset 4.2
```

Sets the **Name** of preset 2.3 (Official Set form; [`Label`](keywords/Label.md) also works for names):

```
Set Preset 2.3 Name "Stage Left"
```

Object settings via Assign/Set (Appearance, InputFilter, Scribble, Name, MoveGridCursor, CuePart, MAgic, …): confirm tables on [`keywords/Preset.md`](keywords/Preset.md). Do not invent property names.

## Related

- Groups / selection: [`groups.md`](groups.md)
- Worlds / filters as input filters: [`worlds-filters.md`](worlds-filters.md)
- MAtricks stored into presets: [`matricks.md`](matricks.md), [`/MAtricks`](keywords/options/Matricks.md)
- Automation: [`automation.md`](automation.md)
- Multi-station (where CmdLine runs): [`multi-station.md`](multi-station.md)
