---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/operate_fixtures.html"
---

# Operate Fixtures (Topic Spec)

Concept map (thin): [`concepts/operate-fixtures.md`](concepts/operate-fixtures.md).

Manual hub + subtopics (one Spec): [Align](https://help.malighting.com/grandMA3/2.5/HTML/operate_align.html), [Select Fixtures](https://help.malighting.com/grandMA3/2.5/HTML/operate_select_fixtures.html), [Fixture Graphic](https://help.malighting.com/grandMA3/2.5/HTML/operate_fixture_graphic.html), [Encoder Resolution Multiplier](https://help.malighting.com/grandMA3/2.5/HTML/operate_encoder_resolution_multiplier.html), [Parent Child](https://help.malighting.com/grandMA3/2.5/HTML/parent-child-fixture.html), [Fixture Sheet](https://help.malighting.com/grandMA3/2.5/HTML/operate_fixture_sheet.html), [Selection Bar](https://help.malighting.com/grandMA3/2.5/HTML/operate_selection_bar.html), [Clone](https://help.malighting.com/grandMA3/2.5/HTML/operate_clone.html), [Special](https://help.malighting.com/grandMA3/2.5/HTML/operate_special.html), [Gel Pool](https://help.malighting.com/grandMA3/2.5/HTML/operate_gel_pool.html), [sMArt](https://help.malighting.com/grandMA3/2.5/HTML/operate_smart.html), [Selection Grid](https://help.malighting.com/grandMA3/2.5/HTML/operate_selection.html).

**The Programmer is a separate concept** — values, layers, clear, blind, park: [`concepts/programmer.md`](concepts/programmer.md). Do not duplicate programmer.md here; this Spec is selection / align / clone / sheets / gels / grid.

## Select fixtures

Selects fixtures **1–5**:

```
Fixture 1 Thru 5
```

Selects 1–10 except 6–8:

```
Fixture 1 Thru 10 - 6 Thru 8
```

Union with `+`:

```
Fixture 1 Thru 5 + 9 Thru 10
```

```
Fixture 9 + 10
```

Selects (SelFix) fixtures stored in **group 3**:

```
Group 3
```

Keywords: [`Fixture`](keywords/Fixture.md), [`Thru`](keywords/Thru.md), [`Plus`](keywords/Plus.md), [`Minus`](keywords/Minus.md), [`Group`](keywords/Group.md). Persist a selection as a group: [`groups.md`](groups.md).

### Parent / child (subfixtures)

Dot is **parent.child** for fixtures (not cue decimals). Selects subfixture path **1.1.1**:

```
Fixture 1.1.1
```

Recursive / trailing-dot forms from the manual (pixels / children):

```
Fixture 301.
```

```
Fixture 301 Thru 303.
```

```
Fixture 301.1. Thru
```

```
Fixture 301.1. Thru 4 + 6
```

```
Fixture Thru .
```

```
Fixture Thru
```

## Align

[`Align`](keywords/Align.md) toggles encoder align modes. Modes / indexes (Official): Off=`0`, `/`=`1`, `<`=`2`, `>`=`3`, `><`=`4`, `<>`=`5`.

Sets align mode **`<`**:

```
Align "<"
```

Disables align:

```
Align 0
```

Fan values across the selection with At Thru (manual Align example):

```
At 75 Thru 10 Thru 75
```

## Clone

[`Clone`](keywords/Clone.md) copies show data fixture→fixture (cues/presets/etc.). Opens a priority pop-up unless you pass an Official Clone option: [`/Overwrite`](keywords/options/Overwrite.md), [`/MergeLowPriority`](keywords/options/Mergelowpriority.md), [`/MergeHighPriority`](keywords/options/Mergehightpriority.md). Clone’s own option list does **not** include `/NoConfirmation` — prefer those priority options (same pattern as [`layouts.md`](layouts.md)).

Clones entire show data from fixture 1 to fixture 2 (will prompt without an option):

```
Clone Fixture 1 At Fixture 2 /Overwrite
```

Clones fixtures 1+2 onto group 10 **only inside sequences 1–10**:

```
Clone Fixture 1 + 2 At Group 10 If Sequence 1 Thru 10 /Overwrite
```

Clones fixtures 1–12 onto 101–112 **only in data pool 1**:

```
Clone Fixture 1 Thru 12 At Fixture 101 Thru 112 If DataPool 1 /Overwrite
```

Clones pan of fixture 1 onto tilt of fixture 2:

```
Clone Fixture 1 Attribute "Pan" At Fixture 2 Attribute "Tilt" /Overwrite
```

[`If`](keywords/If.md) here is a CLI filter. Live programmer-only reuse is [`At`](keywords/At.md), not Clone.

## Gels / sMArt / sheets / graphics

[`Gel`](keywords/Gel.md) Official examples:

```
At Gel "Lee"."Mauve"
```

Applies Lee Mauve gel to the selection.

```
At Gel 8.44
```

Applies gel by swatch.number (8.44).

```
Export Gel 8
```

Exports gel swatch **8**.

Gel Pool / custom gels / sMArt / Feature Graphic / Fixture Graphic / Fixture Sheet / Selection Bar / Special Dialog / Encoder Resolution Multiplier are largely **GUI**.

## Selection grid (XYZ)

Official: [Selection Grid](https://help.malighting.com/grandMA3/2.5/HTML/operate_selection.html). Fixtures have a position in a **3D selection grid**. Each fixture is a box. The grid is spatial relationships for **MAtricks**, phasers, selection order, and effects — not necessarily 3D Viewer positions ([`concepts/xyz.md`](concepts/xyz.md)).

Origin **0/0/0**. Cursor syntax ([`keywords/Grid.md`](keywords/Grid.md)):

```
Grid 1/2/1
```

Moves the cursor to X=1, Y=2, Z=1 (Z may be omitted when it is 1). Span:

```
Grid 2/2 Thru 4/4
```

**Move Grid Cursor** (title bar / user profile; **typings** `GridCursorMovement`): `None` | `Append X` | `New Line`. **Preserve GridPositions** keeps gaps/offsets from origin. Align Range **Rx / Ry / Rz** (recipe `alignRangeX`/`Y`/`Z`) chooses align across the whole selection vs per row/column. Official: MAtricks X, Y, and Z directions are relative to the entire range of selected fixtures.

MAtricks property families are the same on all three axes and operate on these grid axes — [`matricks.md`](matricks.md). A recipe embeds those families and can also assign a pool MAtricks as defaults — [`recipes.md`](recipes.md). Store the grid with a group — [`groups.md`](groups.md).

Selection **grid** positions also matter for layouts and align — store via Group store or layout assign ([`layouts.md`](layouts.md)).

## Related

- Programmer (separate): [`concepts/programmer.md`](concepts/programmer.md)
- Groups / recipe Selection: [`groups.md`](groups.md), [`concepts/recipes.md`](concepts/recipes.md)
- MAtricks (grid axes): [`matricks.md`](matricks.md)
- Patch: [`concepts/patch.md`](concepts/patch.md)
- Layouts (clone into layout): [`layouts.md`](layouts.md)
- Encoder resolution lab note: [`user-attribute-encoder-resolution.md`](user-attribute-encoder-resolution.md)
