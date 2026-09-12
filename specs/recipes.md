---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/recipes.html"
---

# Recipes (Topic Spec)

Concept map (thin): [`concepts/recipes.md`](concepts/recipes.md).

Manual hub + subtopics (one Spec for the hub — **standard** / cue+preset recipes): [Recipes](https://help.malighting.com/grandMA3/2.5/HTML/recipes.html), [Cue Recipe](https://help.malighting.com/grandMA3/2.5/HTML/cue_recipe.html), [Preset Recipe](https://help.malighting.com/grandMA3/2.5/HTML/presets_recipes.html). GUI-only pages (Recipe Editor Window, Edit Recipe Mode, Recipe sheet) are not elaborated here.

**PhaserRecipe** (violet lines, MA ≥ 2.4, Object API / named addressing) stays in **[`phaser-recipe.md`](phaser-recipe.md)** — link it; do **not** copy its property tables here. `Store` of `{cuePart}.{n}` / Cmd store creates a **StandardRecipe** (`HRecipe`), not a PhaserRecipe.

## What a recipe is

A recipe is one or more **recipe lines** that describe what to cook: selection, values (often a preset reference), MAtricks, fade/delay/speed/phase. Cooking writes those values into a **cue part**, **preset**, or the **programmer**. Cooked data shows a pot icon; it can be removed again.

Recipes live in **cue parts** and **presets**. Cue-part recipes must be cooked; preset recipes cook automatically. Values stored **directly** in the cue part outrank that part's recipe; values stored in a **preset** outrank that preset's recipe. An attribute can therefore come from cue part, cue-part recipe, preset, or preset recipe — only one outputs.

| Important (manual) |
| --- |
| Storing recipes into a **feature-group** preset pool (e.g. Dimmer) stores **all** values; the input filter is ignored. |

### Selection must be a group

A recipe line's **Selection** must be a **group** (group number/name in the Selection column) — not a raw fixture list. Empty groups show red and will not cook. Build groups first — [`groups.md`](groups.md).


## MAtricks on a recipe

A recipe line can have a **MAtricks** pool object assigned (`matricks`). That assignment **spreads** the pool object's MAtricks properties onto the recipe row as **defaults**. The recipe also **owns** those same properties itself, so any MAtricks value can sit on the line with or without a pool object.

**typings:** `StandardRecipe` = `RecipeBaseProps` = `ObjProps` + `MAtrickOnlyProps` + the recipe fields below (`grandma3-ts-types` `typings/grandMA3.DataPool/functions.d.ts` + `MAtricks.d.ts`). PhaserRecipe shares `RecipeBaseProps` and adds extras — [`phaser-recipe.md`](phaser-recipe.md). Class split StandardRecipe / PhaserRecipe is MA **2.4+** (**typings** + **observed** `SupportedFeatures.ts` `cue.phaserRecipe`).

Assigns **MAtricks 1** onto recipe 1 (spreads that object's values as defaults on the row):

```
Assign MAtricks 1 At Sequence 1 Cue 2 Part 0.1
```

MAtricks properties exist **once per axis** (X, Y, Z). Those axes are the **selection grid** axes, not 3D Viewer / patch XYZ — [`concepts/operate-fixtures.md`](concepts/operate-fixtures.md) (Selection grid), [`matricks.md`](matricks.md).

### Recipe properties (typings `RecipeBaseProps`)

Lua `:Get` names below are **typings** (camelCase). CLI MAtricks tokens on the active selection are Official (`X`, `XBlock`, …) — [`matricks.md`](matricks.md). Confirm case on Target.

`ObjProps`: `name`, `nameAndApp`, `index`.

Handles / cook:

| Property | Type (typings) |
| --- | --- |
| `selection` | Group |
| `values` | Preset |
| `preset` | Preset |
| `matricks` | MAtrick (pool object; assignment spreads defaults) |
| `filter` | World or Filter |
| `enabled` | boolean |
| `selectionFromValue` | boolean |
| `selectionMode` | string |
| `recipeTemplate` | boolean |
| `emptyLastCooking` | boolean |
| `failedCookedPart` | `None` \| `Group` \| `Matricks` \| `Preset` \| `Filter` \| `GroupPartlyCooked` \| `IntegratedPresetMiss` |
| `hasAnyMatricksData` | boolean |
| `active` | boolean |
| `shuffleMode` | `Auto` \| `Linked` \| `Unlinked` |
| `moveGridCursor` | `None` \| `Append X` \| `New Line` |
| `preserveGridPositions` | boolean |
| `presetMode` | `Default` \| `Selective` \| `Global` \| `Universal` |
| `relative` / `relativeFade` / `relativeDelay` / `relativePhase` / `relativeSpeed` | boolean |
| `alignRangeX` / `alignRangeY` / `alignRangeZ` | boolean (Official Selection Grid: Rx / Ry / Rz — align across the whole selection vs per row/column) |

Embedded MAtricks (`MAtrickOnlyProps` — **same families on X, Y, and Z**):

| Family | X | Y | Z |
| --- | --- | --- | --- |
| index / count | `x` | `y` | `z` |
| Block | `xBlock` | `yBlock` | `zBlock` |
| Group | `xGroup` | `yGroup` | `zGroup` |
| Wings | `xWings` | `yWings` | `zWings` |
| Width | `xWidth` | `yWidth` | `zWidth` |
| Shuffle | `xShuffle` | `yShuffle` | `zShuffle` |
| Shift | `xShift` | `yShift` | `zShift` |
| fade From / To | `fadeFromX` `fadeToX` | `fadeFromY` `fadeToY` | `fadeFromZ` `fadeToZ` |
| delay From / To | `delayFromX` `delayToX` | `delayFromY` `delayToY` | `delayFromZ` `delayToZ` |
| speed From / To | `speedFromX` `speedToX` | `speedFromY` `speedToY` | `speedFromZ` `speedToZ` |
| phase From / To | `phaseFromX` `phaseToX` | `phaseFromY` `phaseToY` | `phaseFromZ` `phaseToZ` |
| invert | `invertX` | `invertY` | `invertZ` |

Not per-axis on the pool object: `invertStyle` (`Pan` \| `Tilt` \| `P+T` \| `All`), `phaserTransform` (`None` \| `Mirror`).

Also on the recipe (not in `MAtrickOnlyProps`): `fadeX`/`fadeY`/`fadeZ`, `delayX`/`delayY`/`delayZ`, `speedX`/`speedY`/`speedZ`, `phaseX`/`phaseY`/`phaseZ`; invert flags `xInv` `xInvB` `xInvG` `xInvW` (and `y*` / `z*`).

`xBlock` also allows `None` / `No Block`; `xGroup` `None` / `No Group`; `xWings` `None` / `No Wings`; `xShuffle` `None` (typings). Y/Z Block/Group/Wings are typed as number only in the same file — confirm on Target.

Other `RecipeBaseProps` (typings; several are `any`): `tags`, `previewCopy`, `initialName`, `initialMatricks`, `doShuffle`, `memoryType`, `selectionData`, `type`, `user`, `featureGroup`, `trigger`, `storedData`, `presetData`, `ownDataPresent`, `directProgrammerCooking`, `ownNonCookedDataPresent`, `mode`, `dependencies`, `references`, `maxDepth`, `action`, `generator`.

Reads the assigned MAtricks handle and the row's own `x` (defaults from that object if assigned):

```lua
local rec = GetObject("Sequence 1 Cue 2 Part 0.1")
if rec ~= nil then
  Printf("%s x=%s", tostring(rec:Get("matricks")), tostring(rec:Get("x")))
end
```


## Store a recipe line and set its values

Address a standard recipe as **`{cuePart}.{recipeIndex}`** or **`{preset}.{recipeIndex}`**. Same shape as PhaserRecipe named paths ([`phaser-recipe.md`](phaser-recipe.md)). **Observed** (production plugins / `ma_obj` `HRecipe`): creating the line is `Store` of that address; selection / values / MAtricks are **Assign … At** that address.

Creates **standard recipe 1** on cue 2 part 0 of sequence 1 (empty line):

```
Store Sequence 1 Cue 2 Part 0.1 /NoConfirmation
```

Assigns **group 1** as that line's Selection:

```
Assign Group 1 At Sequence 1 Cue 2 Part 0.1
```

Assigns **dimmer preset 1.1** as that line's Values:

```
Assign Preset 1.1 At Sequence 1 Cue 2 Part 0.1
```

Assigns **MAtricks 1** onto that line (spreads its values as defaults — see **MAtricks on a recipe**):

```
Assign MAtricks 1 At Sequence 1 Cue 2 Part 0.1
```

Second line on the **same cue part**, same group, **color** preset 4.1:

```
Store Sequence 1 Cue 2 Part 0.2 /NoConfirmation; Assign Group 1 At Sequence 1 Cue 2 Part 0.2; Assign Preset 4.1 At Sequence 1 Cue 2 Part 0.2
```

On the **selected** sequence, cue 2 part 0 recipe 1 is the same object (shorter form):

```
Store Cue 2 Part 0.1 /NoConfirmation
```

Into a **preset** (recipe 1 of preset 4.2):

```
Store Preset 4.2.1 /NoConfirmation
```

```
Assign Group 1 At Preset 4.2.1
```

```
Assign Preset 4.1 At Preset 4.2.1
```

`Set … Property "enabled"` / `"selection"` / `"values"` is used in plugins (**observed**). Prefer **Assign** for group / preset / MAtricks handles; confirm any `Set Property` token on the desk before automating.

Unattended store/cook: [`automation.md`](automation.md) — name the store/cook mode and append [`/NoConfirmation`](keywords/options/Noconfirmation.md) when Official lists it.

## Cook (standard recipes)

[`Cook`](keywords/Cook.md) cooks recipes on an object without opening the editor. **Cook Official options:** [`/Merge`](keywords/options/Merge.md), [`/MergeLowPriority`](keywords/options/Mergelowpriority.md), [`/Overwrite`](keywords/options/Overwrite.md), [`/Remove`](keywords/options/Remove.md), `/Restart` (Cook Official). Plus [`/NoConfirmation`](keywords/options/Noconfirmation.md) (option Spec lists Cook). Cue-part cook without an option **opens a pop-up** (manual).

Cooks dimmer preset 1.1:

```
Cook Preset 1.1
```

Cooks **sequence 1** (manual: an entire sequence can be cooked in one command):

```
Cook Sequence 1 /Merge /NoConfirmation
```

Cooks **cue 2** of sequence 1 after the two-line store above:

```
Cook Sequence 1 Cue 2 /Merge /NoConfirmation
```

Cue-part cook modes (manual flowchart): **Merge** keeps existing cue-part values; **Overwrite** replaces with recipe (attributes not in the recipe are removed from the overwritten cue). Default if you omit the option is **MergeLowPriority** (replace cooked data, leave non-cooked). Phaser-line cook with `/Restart` / `/MergeLowPriority`: [`phaser-recipe.md`](phaser-recipe.md).

## Store recipes that are already in the programmer

If recipe lines are already in the programmer (operator used the Recipe Editor), store destinations (manual):

- **Cue part** → selected programmer part only — e.g. `Store Cue Part 1 /NoConfirmation`
- **Cue** → all parts as cue parts — e.g. `Store Cue 1 /NoConfirmation`
- **Preset** → selected part into the preset — e.g. `Store Preset 1.3 /NoConfirmation`

After store, recipes clear from the Recipe Editor.

[`/Recipe`](keywords/options/Recipe.md) with Store: Official two-step example stores programmer recipes **without** selection (then tap a preset in the GUI):

```
Store /Recipe "NoSelection"
```

`/Recipe "Normal"` keeps selection when storing recipes into a preset. **RecipeStoreMode** (**typings**): `Normal`, `NoSelection`.

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

## Edit Recipe (GUI only)

[`EditRecipe`](keywords/Editrecipe.md) opens the **recipe editor window** (Official: "enables the recipe editor"). It is for an operator on the desk, not for unattended store/set. Do not use it in macros/plugins/OSC to create or fill lines — use `Store` + `Assign` above.

```
EditRecipe
```

## Plugin access

Generic handle/Get/parent-children: [`plugin-access.md`](plugin-access.md).

For Lua plugins that **read** (or walk) show data. Write path stays the CLI above (`Cmd` / `Store` / `Assign`).

Object tree (**observed** + **typings**; confirm `GetClass()` on Target):

```text
ShowData().DataPools
  DataPool n                          -- DataPool() is the selected pool
    Sequences
      Sequence n
        Cue n
          Part n                      -- Part 0 is the default part
            StandardRecipe r          -- CLI: Sequence n Cue n Part p.r
    PresetPools
      Dimmer | Position | Color | …   -- pool name
        Preset n
          StandardRecipe r            -- CLI: Preset pool.n.r
```

`Store {addr}` on that recipe slot creates **StandardRecipe**, not PhaserRecipe. PhaserRecipe children live under the same Part/Preset — [`phaser-recipe.md`](phaser-recipe.md).

Resolves the handle for recipe 1 on sequence 1 cue 2 part 0:

```lua
local rec = GetObject("Sequence 1 Cue 2 Part 0.1")
if rec ~= nil then
  Printf("%s", rec:GetClass())
end
```

Walks every child of that cue part (print class + index):

```lua
local part = GetObject("Sequence 1 Cue 2 Part 0")
if part ~= nil then
  for i = 1, part:Count() do
    local child = part[i]
    Printf("%d %s", i, child:GetClass())
  end
end
```

Selected data pool → sequences pool (**observed** `DataPool().Sequences`; `ShowData().DataPools` for a numbered pool):

```lua
local seqs = DataPool().Sequences
Printf("seq count %d", seqs:Count())
```

Full property list (including embedded MAtricks): **MAtricks on a recipe** above. Plugin reads use `:Get` — [`plugin-access.md`](plugin-access.md).

## GUI surfaces (facts only)

| Surface | Role |
| --- | --- |
| Cue / Preset editors | Add Standard Recipe / Add Phaser Recipe, Cook, Take Selection, Turn Into Recipe, Recipe Template |
| Recipe Editor Window | Tools → Recipe Editor; Edit Recipe title-bar toggle — [`EditRecipe`](keywords/Editrecipe.md) |
| Recipe sheet columns | Selection (groups), Values, Filter/World, MAtricks, Enabled, … |

**Recipe Template** (preset setting): open green pot; loads recipe lines into the programmer part when called. Presets **without** selection cook onto the current programmer selection (template-style). Presets **with** selection cook into the preset and can be referenced/played like other presets.

Pot colors (manual): green = standard cook ok (object only recipe data); violet = phaser cook ok; red = a line failed; orange = cooked + uncooked mix; open green/violet = standard/phaser recipe template. Mixed standard+phaser → two pots.

## Related

- Groups (Selection): [`groups.md`](groups.md), [`concepts/groups.md`](concepts/groups.md)
- PhaserRecipe depth: [`phaser-recipe.md`](phaser-recipe.md)
- Presets / cues: [`concepts/presets.md`](concepts/presets.md), [`concepts/cues-sequences.md`](concepts/cues-sequences.md)
- MAtricks / selection grid XYZ: [`matricks.md`](matricks.md), [`concepts/matricks.md`](concepts/matricks.md), [`concepts/operate-fixtures.md`](concepts/operate-fixtures.md)
- Shapes: [`concepts/shapes.md`](concepts/shapes.md)
- Programmer: [`concepts/programmer.md`](concepts/programmer.md)
- Automation: [`automation.md`](automation.md)
