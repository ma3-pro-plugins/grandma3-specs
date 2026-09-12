---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/recipes.html"
---

# Recipes (Topic Spec)

Concept map (thin): [`concepts/recipes.md`](concepts/recipes.md).

Manual hub + subtopics (one Spec for the hub — **standard** / cue+preset recipes): [Recipes](https://help.malighting.com/grandMA3/2.5/HTML/recipes.html), [Cue Recipe](https://help.malighting.com/grandMA3/2.5/HTML/cue_recipe.html), [Preset Recipe](https://help.malighting.com/grandMA3/2.5/HTML/presets_recipes.html), [Recipe Editor Window](https://help.malighting.com/grandMA3/2.5/HTML/recipe-editor-window.html), [Edit Recipe Mode](https://help.malighting.com/grandMA3/2.5/HTML/edit-recipe-mode.html), [Recipe Editor (sheet)](https://help.malighting.com/grandMA3/2.5/HTML/recipe-sheet.html).

**PhaserRecipe** (violet lines, MA ≥ 2.4, Object API / named addressing) stays in **[`phaser-recipe.md`](phaser-recipe.md)** — link it; do **not** copy its property tables here. `Store Recipe` / Cmd store creates a **StandardRecipe** (`HRecipe`), not a PhaserRecipe.

## What a recipe is

A recipe is one or more **recipe lines** that describe what to cook: selection, values (often a preset reference), MAtricks, fade/delay/speed/phase. Cooking writes those values into a **cue part**, **preset**, or the **programmer**. Cooked data shows a pot icon; it can be removed again.

Recipes live in **cue parts** and **presets**. Cue-part recipes must be cooked; preset recipes cook automatically. Values stored **directly** in the cue part outrank that part's recipe; values stored in a **preset** outrank that preset's recipe. An attribute can therefore come from cue part, cue-part recipe, preset, or preset recipe — only one outputs.

| Important (manual) |
| --- |
| Storing recipes into a **feature-group** preset pool (e.g. Dimmer) stores **all** values; the input filter is ignored. |

### Selection must be a group

A recipe line's **Selection** is a **group** (group number/name in the Selection column). Empty groups show red and will not cook. Build groups first — [`groups.md`](groups.md).

Do not invent fixture-list Selection CLI; use groups.

## Cook (standard recipes)

[`Cook`](keywords/Cook.md) cooks recipes on an object without opening the editor. Options Official lists: [`/Merge`](keywords/options/Merge.md), [`/MergeLowPriority`](keywords/options/Mergelowpriority.md), [`/Overwrite`](keywords/options/Overwrite.md), [`/Remove`](keywords/options/Remove.md), and `/Restart` (Cook Official links the Restart page). **Cook does not list `/NoConfirmation`** — do not append it.

Cooks dimmer preset 1.1:

```
Cook Preset 1.1
```

Cook can target a whole sequence (manual: an entire sequence can be cooked in one command):

```
Cook Sequence 1
```

Confirm object addressing on Keyword Specs before use. Phaser-line cook with `/Restart` / `/MergeLowPriority` is covered under [`phaser-recipe.md`](phaser-recipe.md) / Recipe Editor Window notes (e.g. `Cook PhaserRecipe1 /Restart /MergeLowPriority`).

Cue-part cook modes (manual flowchart): **Merge** keeps existing cue-part values; **Overwrite** replaces with recipe (attributes not in the recipe are removed from the overwritten cue).

## Edit recipe mode

[`EditRecipe`](keywords/Editrecipe.md) enables recipe edit mode (optional object).

```
EditRecipe
```

```
EditRecipe Cue 1
```

```
EditRecipe Preset 2.2
```

```
EditRecipe Sequence 1
```

```
EditRecipe Page 1.204
```

## Store recipes from the programmer

With recipes in the programmer (Recipe Editor Window / Edit Recipe Mode), store destinations (manual):

- **Cue part** destination → selected programmer part only — e.g. `Store Cue Part 1`
- **Cue** destination → all parts as cue parts — e.g. `Store Cue 1`
- **Preset** destination → selected part into the preset — e.g. `Store Preset 1.3`

After store, recipes clear from the Recipe Editor.

Unattended store: [`automation.md`](automation.md) — use Store options Official lists (`/Merge`, `/Overwrite`, …) **and** [`/NoConfirmation`](keywords/options/Noconfirmation.md) when Store lists it.

[`/Recipe`](keywords/options/Recipe.md) with Store: Official two-step example stores programmer recipes **without** selection (then tap a preset in the GUI):

```
Store /Recipe "NoSelection"
```

`/Recipe "Normal"` keeps selection when storing recipes into a preset. Prefer documented Store + option forms; do not invent destinations.

## Clean up unused recipe lines

[`CleanUp`](keywords/Cleanup.md) with [`/Type "Recipe"`](keywords/options/Type.md) (and optional [`/Recipe`](keywords/options/Recipe.md) value) removes non-outputting recipes:

```
CleanUp Sequence 1 Cue 2 Part 0 /Type "Recipe"
```

```
CleanUp Sequence 1 Cue 2 Part 0 /Type "Recipe" /Recipe "NoOutput"
```

```
CleanUp Preset 2.2 /Type "Recipe" /Recipe "NotCooked"
```

`/Recipe` values (Official): `NoOutput`, `NotCooked`, `CookedButOverwritten`, plus Store-only `Normal` / `NoSelection`.

## GUI surfaces (facts only)

| Surface | Role |
| --- | --- |
| Cue / Preset editors | Add Standard Recipe / Add Phaser Recipe, Cook, Take Selection, Turn Into Recipe, Recipe Template |
| Recipe Editor Window | Tools → Recipe Editor; parts + lines; Edit Recipe title-bar toggle |
| Recipe sheet columns | Selection (groups), Values, Filter/World, MAtricks, Enabled, … — edit via GUI/context area |

**Recipe Template** (preset setting): open green pot; loads recipe lines into the programmer part when called. Presets **without** selection cook onto the current programmer selection (template-style). Presets **with** selection cook into the preset and can be referenced/played like other presets.

Pot colors (manual): green = standard cook ok (object only recipe data); violet = phaser cook ok; red = a line failed; orange = cooked + uncooked mix; open green/violet = standard/phaser recipe template. Mixed standard+phaser → two pots.

## Related

- Groups (Selection): [`groups.md`](groups.md), [`concepts/groups.md`](concepts/groups.md)
- PhaserRecipe depth: [`phaser-recipe.md`](phaser-recipe.md)
- Presets / cues: [`concepts/presets.md`](concepts/presets.md), [`concepts/cues-sequences.md`](concepts/cues-sequences.md)
- MAtricks / shapes: [`concepts/matricks.md`](concepts/matricks.md), [`concepts/shapes.md`](concepts/shapes.md)
- Programmer: [`concepts/programmer.md`](concepts/programmer.md)
- Automation: [`automation.md`](automation.md)
