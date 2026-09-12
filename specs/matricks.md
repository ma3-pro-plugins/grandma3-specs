---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/matricks.html"
---

# MAtricks (Topic Spec)

Concept map (thin): [`concepts/matricks.md`](concepts/matricks.md). Keyword: [`keywords/Matricks.md`](keywords/Matricks.md). Shuffle: [`keywords/Shuffle.md`](keywords/Shuffle.md). Selection: [`keywords/Selection.md`](keywords/Selection.md).

Manual hub + subtopics (one Spec): [Blocks](https://help.malighting.com/grandMA3/2.5/HTML/matricks_block.html), [Groups](https://help.malighting.com/grandMA3/2.5/HTML/matricks_group.html), [Wings](https://help.malighting.com/grandMA3/2.5/HTML/matricks_wings.html), [Width](https://help.malighting.com/grandMA3/2.5/HTML/matricks_width.html), [Shuffle](https://help.malighting.com/grandMA3/2.5/HTML/matricks_shuffle.html), [Transform](https://help.malighting.com/grandMA3/2.5/HTML/matricks_transform.html).

MAtricks divides a fixture **selection** into sub-selections (and can shuffle that selection). Typical use: step through a selection one fixture or subgroup at a time (`Next` / `Prev`), or spread values across the selection grid. Each user profile has **two selections** (Selection 1 and Selection 2).

MAtricks **pool objects** live in the Data Pool. Active MAtricks can also be stored into presets via [`/MAtricks`](keywords/options/Matricks.md) — [`presets.md`](presets.md). Recipes can attach MAtricks **or** hold the same X/Y/Z properties on the row (assigning a pool object spreads those values as **defaults**) — [`recipes.md`](recipes.md). Recipe **Selection** must be a **group** — [`phaser-recipe.md`](phaser-recipe.md), [`groups.md`](groups.md). Those X/Y/Z families act on the **selection grid** — [`concepts/operate-fixtures.md`](concepts/operate-fixtures.md).

## Pool object vs active selection MAtricks

Stores current MAtricks settings into **pool object 3**:

```
Store MAtricks 3 /NoConfirmation
```

Calls/applies **MAtricks 1** from the pool:

```
Call MAtricks 1
```

Labels pool object 2:

```
Label MAtricks 2 "Great"
```

Assigns MAtricks 4 onto the first recipe of cue 1 part 0 on the selected sequence (Official):

```
Assign MAtricks 4 At Cue 1 Part 0.1
```

Active selection properties use `Set Selection … MAtricks "Property" …` (Official property table):

| Axis props | Block | Group | Wings | Width | Shuffle | Shift |
| --- | --- | --- | --- | --- | --- | --- |
| X Y Z | XBlock YBlock ZBlock | XGroup YGroup ZGroup | XWings YWings ZWings | XWidth YWidth ZWidth | XShuffle YShuffle ZShuffle | XShift YShift ZShift |

Sets **X** to 2 on the active selection:

```
Set Selection MAtricks "X" 2
```

Sets **XBlock** to 4 on **selection 2**:

```
Set Selection 2 MAtricks "XBlock" 4
```

Disables MAtricks on the active selection:

```
Off Selection MAtricks
```

Toggles MAtricks on the active selection:

```
Toggle Selection MAtricks
```

Resets MAtricks on selection 1:

```
Reset Selection 1 MAtricks
```

Speed-from example (Official; confirm units):

```
Set Selection MAtricks "SpeedFromX" "Hz 10"
```

After changing grid props, `Next` / `Previous` (and axis variants) step the active sub-selection — [`keywords/Next.md`](keywords/Next.md), [`keywords/Previous.md`](keywords/Previous.md). `ClearAll` / `ClearSelection` appear in the hub as related clear forms — confirm [`keywords/ClearAll.md`](keywords/ClearAll.md) before use.

## Blocks

**XBlock** (and Y/Z) groups adjacent fixtures on an axis into blocks while **X** (etc.) still selects which member inside each block is active. Example (manual): with X=1, raising XBlock to 2 selects every other fixture in pairs; XBlock=5 yields fewer grid “boxes”.

```
Set Selection MAtricks "XBlock" 2
```

Sets **XBlock** to 2 on the active selection (then use Next/Prev to step).

## Groups (MAtricks groups — not Group pool)

**XGroup** splits the selection into N interleaved groups (manual: XGroup=2 → two interleaved halves). Distinct from pool [`Group`](keywords/Group.md) objects.

```
Set Selection MAtricks "XGroup" 2
```

Splits the active selection into **2** MAtricks groups on X.

## Wings

**XWings** mirrors/folds the selection into wing counts (used heavily with Transform Mirror). GUI `+`/`−` on the Wings field; CLI:

```
Set Selection MAtricks "XWings" 2
```

Sets **XWings** to 2 on the active selection.

## Width

**XWidth** (etc.) sets how many fixtures sit on an axis before wrapping in the selection grid (manual shuffle example uses XWidth=5 for a 5×4 layout).

```
Set Selection MAtricks "XWidth" 5
```

Sets **XWidth** to 5 on the active selection.

## Shuffle

[`Shuffle`](keywords/Shuffle.md) randomizes selection order on the selection grid. MAtricks tool Shuffle bumps **XShuffle/YShuffle/ZShuffle**. ShuffleMode values (typings — grandma3-ts-types, MA 2.4.2.2 dump): `Auto`|`Linked`|`Unlinked`.

```
MAtricks "XShuffle" 4
```

Sets **XShuffle** to 4 (Official Shuffle Spec example form).

```
MAtricks "YShuffle" +
```

Increments **YShuffle** (Official).

To shuffle then store the order into a group, use normal group store after shuffle — [`groups.md`](groups.md).

## Transform / Invert

**Transform** lives under Invert Options in the MAtricks window. **Mirror** mirrors values according to Blocks/Groups/Wings; **None** clears related inverts. Official MAtricks **Properties** table has no Transform / InvertStyle / InvertX|Y|Z tokens (GUI / Object API). Values (typings — grandma3-ts-types, MA 2.4.2.2 dump): `phaserTransform` / Transform `None`|`Mirror`; `invertStyle` `Pan`|`Tilt`|`P+T`|`All`; `invertX`/`invertY`/`invertZ` boolean. Manual notes: Mirror turns InvertStyle toward Pan; mirrored fixtures show green; Mirror can force hard values in the programmer (symmetry), which affects cue/preset referencing.

## Related

- Selection grid / operate fixtures: [`operate-fixtures.md`](operate-fixtures.md), [`concepts/operate-fixtures.md`](concepts/operate-fixtures.md), [`groups.md`](groups.md)
- Presets + `/MAtricks`: [`presets.md`](presets.md)
- Phaser / recipes: [`phaser-recipe.md`](phaser-recipe.md), [`concepts/recipes.md`](concepts/recipes.md)
- Automation: [`automation.md`](automation.md)
