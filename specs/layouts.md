---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/layouts.html"
---

# Layouts (Topic Spec)

Concept map (thin): [`concepts/layouts.md`](concepts/layouts.md). Keyword: [`keywords/Layout.md`](keywords/Layout.md).

Manual hub + subtopics (one object, not seven Specs): [Create](https://help.malighting.com/grandMA3/2.5/HTML/layout_create.html), [Multipatch](https://help.malighting.com/grandMA3/2.5/HTML/layout_multipatch.html), [Edit Layout](https://help.malighting.com/grandMA3/2.5/HTML/layout_edit.html), [View Settings](https://help.malighting.com/grandMA3/2.5/HTML/layout_view_settings.html), [Edit View](https://help.malighting.com/grandMA3/2.5/HTML/layout_edit_view.html), [Edit Elements](https://help.malighting.com/grandMA3/2.5/HTML/layout_elements_edit.html), [Encoder Bar](https://help.malighting.com/grandMA3/2.5/HTML/layout_encoder_bar.html).

Layouts are **2D drafts** of fixtures, macros, groups, and other pool objects. They live in the **Layouts pool** (a Data Pool child). Display/edit is the **Layout Viewer**. **Max 10 000 elements** per layout.

Selection-grid positions of selected fixtures are what get assigned onto a new layout (not 3D stage XYZ). Groups do **not** store values — layouts store **elements** (fixture/object + canvas position/size/appearance).

## Create and assign (CLI)

Creates **layout 5** and puts the **current fixture selection** on it:

```
Assign Layout 5
```

Adds **group 5** as a pool-element button on layout 4:

```
Assign Group 5 At Layout 4
```

Adds **macro 1** as an element on layout 1:

```
Assign Macro 1 At Layout 1
```

Assigns an **output station** (onPC/console host) named HostName onto layout 3 (indicator bar shows network state):

```
Assign "HostName" At Layout 3
```

Keywords: [`Assign`](keywords/Assign.md), [`Layout`](keywords/Layout.md), [`Group`](keywords/Group.md), [`Macro`](keywords/Macro.md). Official Layout Assign examples: `Assign Layout 5`, `Assign Group 5 At Layout 4`. Assign Official option: [`/Tab`](keywords/options/Tab.md). [`/NoConfirmation`](keywords/options/Noconfirmation.md) is listed on the option Spec as a general keyword for Assign.

Unattended store/assign: [`automation.md`](automation.md) (`/NoConfirmation` when that function lists it).

## Multipatch fixtures

Requires patched multipatch fixtures. Selects/assigns **fixture 1** plus its multipatch 1–5 (manual then taps the viewer to place). Light-red selection; primary ID flashes yellow/red in the fixture sheet:

```
Assign Fixture 1 Multipatch 1 Thru 5
```

Placement into a specific layout via tap is **GUI**. Official Layout examples use `Assign Layout N` (selection onto layout) or `Assign Group N At Layout M` — no multipatch `At Layout` suffix on Official.

## Clone into a layout

Clones show data from fixtures 1–6 onto fixtures 7–12 **only for layout 3** (`If Layout`). New elements land offset; element settings clone too. Clone opens a priority pop-up unless you pass an Official Clone option (`/Overwrite`, `/MergeLowPriority`, `/MergeHighPriority`):

```
Clone Fixture 1 Thru 6 At Fixture 7 Thru 12 If Layout 3 /Overwrite
```

[`Clone`](keywords/Clone.md) does **not** list `/NoConfirmation` — use a Clone option to skip the priority dialog. [`If`](keywords/If.md) here is a CLI filter, not a programming `if`.

## Layout object (Edit Layout)

GUI: Edit + tap the pool object (or swipey). Settings include Name / Scribble / Pool Appearance / **Canvas Appearance** (window background; falls back to pool appearance) / Tags / Notes.

Canvas: `PositionX`, `PositionY`, `DimensionW`, `DimensionH` — two layouts can hold the same fixtures at different zoom/position.

Toggles (manual): **Markers** (layer markers on elements), **Value Colors** (dimmer colors like the fixture sheet — needs a dimmer fixture and value visibility on the element), **ViewPosActive** (reload recalls stored view zoom/position; default off), **Executor Style** (sequences show cues like the executor bar).

**Layout Element Defaults** (user **profile**, not the show object): templates applied when assigning a new object (groups, worlds, sequences, …). Also via Menu → Preferences and Timings → Layout Elements. Render styles: **Default** (follow layout), **Pool**, **Executor**.

Layout Official has **no Set-property table**. Layout *element* props (typings — grandma3-ts-types, MA 2.4.2.2 dump, Layouts.d.ts): `assignType`, `action` (AssignmentButtonFunctionsSequence), `appearance`, `borderSize`, `borderColor`, `customTextColor`, `customTextAlignmentH` (`Center`|`Left`|`Right`), `customTextAlignmentV` (`Center`|`Top`|`Bottom`|`Above`), `customTextSize` (`Default`|10|12|14|16|18|20|24|28|32), `customTextText`, `fullResolution`, `height`, `id`, visibilityElement/Bar/ObjectName/ID/CID/Border/Value/IndicatorBar/SelectionRelevance, `padding*`, `posX`/`posY`, `width`.

## Layout Viewer and Setup mode

Open: Add Window → Tools → Layout Viewer.

**Setup on:** edit single layout elements (toolbar + encoder bar). **Setup off:** operate like the programmer (select fixtures / fire pool objects).

Title-bar **Fit Type**: Elements / Canvas / Both, then Zoom to Fit. Canvas fit mode (Bar / Crop / Stretch) is a view setting.

## Elements (Edit Layout Elements)

Multi-user: editing an element can **lock** it — [`concepts/users.md`](concepts/users.md) / Object Ownership.

Three editor tabs (GUI; property names below are **manual labels**, not proven CLI):

| Tab | Agent-relevant |
| --- | --- |
| **General** | Name, fixture **ID** / **CID**, **Object** (assignment), **Action** (`<Layout Default>` or `<Object Default>` when tapped), Appearance / Full Resolution / Mirror / Appearance Rotation |
| **Arrangement** | Position X/Y, padding, border, width/height, visibility of name/ID/CID/border/bar/value, indicator bar (pool objects), Selection Relevance |
| **Custom Text** | Label, size/color, align (including outside / above / below), vertical text |

Many high-resolution images can drop GUI quality; images ≤ 150 px always render lower quality.

## Encoder bar (position / arrangement)

Visible when Setup is on. **Position:** Pos X/Y, Width/Height, Scale, Ratio, Rotate (grayed for a single fixture), Change on EncoderEvent (Yes = live to network; No = send ~2s after last turn), Reset Position, Edit Selected.

**Arrangement** types: **Line**, **Grid**, **Circle** (same ideas as 3D placement), **Camera** (match a 3D camera; Camera / Scale / Ratio / Move X). Align + dual encoders spread a multi-selection.

## View settings (agent notes)

Display: which Layout is linked, Setup, Layer readout (**DMX** / **Value** / **Output**), Lasso Filter (All / Fixtures / Others), Show Selection (not in Setup), Right Click To Edit, Lock Position, Selection Mode (**2D Grid** vs **Linearize** onto the selection grid), Auto Fit / Fit Type / snap grid.

A title-bar control can **push the current layout fixture arrangement into the Selection Grid**.


## Plugin access

Lua plugins that **read** layout objects. Write path stays the Assign/Store CLI above.

```text
ShowData().DataPools
  DataPool n
    Layouts
      Layout n                 -- CLI: Layout n
        (elements) n           -- CLI: Layout n.1 Thru …  (observed)
```

Resolves layout 5 in the selected data pool:

```lua
local layout = ObjectList("Layout 5")[1]
if layout ~= nil then
  Printf("%s count %d", layout:GetClass(), layout:Count())
end
```

Same pool via **observed** `DataPool().Layouts` (`ShowData().DataPools` for a numbered pool):

```lua
local layouts = DataPool().Layouts
Printf("layout count %d", layouts:Count())
```

Confirm element class with `GetClass()` on `layout[i]` / `layout:Ptr(i)` before treating a child as a fixture vs a pool-object button.

## Related

- Data pools: [`concepts/datapools.md`](concepts/datapools.md)
- Groups / selection grid: [`groups.md`](groups.md), [`concepts/operate-fixtures.md`](concepts/operate-fixtures.md)
- Executors (Executor Style / render): [`concepts/executors.md`](concepts/executors.md)
- Automation: [`automation.md`](automation.md)
