---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/patch.html"
---

# Patch (Topic Spec)

Concept map (thin): [`concepts/patch.md`](concepts/patch.md). Keywords: [`Patch`](keywords/Patch.md), [`Fixture`](keywords/Fixture.md), [`Multipatch`](keywords/Multipatch.md), [`DMXUniverse`](keywords/DmxUniverse.md), [`DMXAddress`](keywords/DmxAddress.md), [`Stage`](keywords/Stage.md), [`FixtureLayer`](keywords/FixtureLayer.md), [`FixtureClass`](keywords/FixtureClass.md), [`Camera`](keywords/Camera.md), [`SelectFixtures`](keywords/Selectfixtures.md).

Manual hub + subtopics (one object, not eighteen Specs): [What are Fixtures](https://help.malighting.com/grandMA3/2.5/HTML/patch_what_are_fixtures.html), [Add Fixtures](https://help.malighting.com/grandMA3/2.5/HTML/patch_add_fixtures.html), [Add Multipatch](https://help.malighting.com/grandMA3/2.5/HTML/patch_add_multipatch.html), [MVR](https://help.malighting.com/grandMA3/2.5/HTML/patch_mvr.html), [Live Patch](https://help.malighting.com/grandMA3/2.5/HTML/patch_live.html), [DMX Sheet](https://help.malighting.com/grandMA3/2.5/HTML/patch_dmx_sheet.html), [DMX Universes](https://help.malighting.com/grandMA3/2.5/HTML/patch_dmx_universe.html), [Remove Fixtures](https://help.malighting.com/grandMA3/2.5/HTML/patch_remove_fixtures.html), [Position Fixtures](https://help.malighting.com/grandMA3/2.5/HTML/patch_position_fixtures.html), [3D Viewer](https://help.malighting.com/grandMA3/2.5/HTML/patch_3d_viewer.html), [Render Quality](https://help.malighting.com/grandMA3/2.5/HTML/patch_render_quality.html), [Camera Pool](https://help.malighting.com/grandMA3/2.5/HTML/patch_3d_camera.html), [Stages](https://help.malighting.com/grandMA3/2.5/HTML/patch_stage.html), [Classes and Layers](https://help.malighting.com/grandMA3/2.5/HTML/patch_classes_layers.html), [Attribute Definitions](https://help.malighting.com/grandMA3/2.5/HTML/patch_attribute_definitions.html), [Parameter List](https://help.malighting.com/grandMA3/2.5/HTML/patch_parameter_list.html), [DMX Curves](https://help.malighting.com/grandMA3/2.5/HTML/patch_dmx_curves.html).

Fixtures must exist in **Patch** before they can be controlled. The Patch menu also exposes Fixture Types, Attribute Definitions, Parameter List, DMX Universes, Stages, and DMX Curves. Condensed vs Full columns; Split View filters by Fixture Types / DMX Universes / Filters / Hierarchy / ID Types / Layers / Classes. Optional **Show 3D Positions** pane (does not show live DMX output).

Adding fixtures, editing fixture types, MVR export options, Live Patch column edits, 3D placement tools, render quality, and most stage/class/layer setup are **GUI**. Do not invent `Set … Property` names for those. Prefer evidenced CLI below.

## Patch address (CLI)

Patches **fixture 2** to universe **3**, address **123**:

```
Patch Fixture 2 3.123
```

Opens the Edit Patch UI for fixtures **1–10** (set or clear address in the pop-up):

```
Patch Fixture 1 Thru 10
```

## Multipatch

Multipatch fixtures mirror a **primary** fixture’s parameters. They can have their own DMX address (output when the primary is granted). They can sit on layouts / in 3D; they are **not** on the selection grid (no MAtricks). Selection color is light red; primary ID flashes yellow/red in the fixture sheet. Prefer `Fixture n Multipatch i` over the global Multipatch CID (CID can renumber when the patch changes).

Selects multipatch **2** of fixture **4**:

```
Fixture 4 Multipatch 2
```

Patches multipatch **3** of fixture **2** to universe **42**, address **6**:

```
Patch Fixture 2 Multipatch 3 42.6
```

Layouts multipatch assign (already used in layouts Spec) — selects/assigns fixture **1** multipatch **1–5** for placement:

```
Assign Fixture 1 Multipatch 1 Thru 5
```

Create Multipatch in the Patch menu is **GUI** (`Create Multipatch` button).

## List / select by universe or address

Lists the first ten fixtures in Fixture Edit Setup:

```
List Fixture Thru 10
```

Selects the fixture patched at universe **2**, address **1** (absolute):

```
SelectFixtures DMXAddress 513
```

Selects the fixture patched at universe **2.001**:

```
SelectFixtures DMXUniverse 2.001
```

Moves all channels of universe **1** onto universe **11**:

```
Move DMXUniverse 1 At DMXUniverse 11
```

## DMX tester (via universe / address)

Outputs **50%** on universe **1**, channel **3** (tester):

```
DMXUniverse 1.3 At 50
```

Outputs **42%** on universe **2**, channels **8–15** (tester):

```
DMXUniverse 2.8 Thru 15 At 42
```

Clears DMX testing on all channels of all universes:

```
Off DMXUniverse Thru
```

Absolute-address forms: [`DMXAddress`](keywords/DmxAddress.md) (`DMXAddress 3 At 50`, `Off DMXAddress Thru`).

## Classes and layers

No real difference between Class and Layer in grandMA3; each fixture may have one of each. Used for Patch Split View filters. Creating/assigning in the Patch grid is **GUI**.

Selects all fixtures linked to layer **Backtruss**:

```
SelectFixtures FixtureLayer "Backtruss"
```

[`FixtureClass`](keywords/FixtureClass.md) is the class-side object keyword — confirm Official before inventing `SelectFixtures FixtureClass …` forms beyond what that Spec shows.

## Stages

Fixtures live inside a **Stage** (default Stage 1). Multiple stages for multi-room / festival / studio. Deleting a stage deletes its fixtures and their programmed data. Stage create/edit/export is **GUI** in Patch → Stages. Keyword: [`Stage`](keywords/Stage.md).

## Live Patch vs full Patch

**Live Patch**: change only columns that do not need a show upload (name, patch address, pan/tilt offsets/inverts, 3D position/rotation, gel, notes/tags, beam/shadow/visibility, etc.). Changes apply immediately. Cannot add/remove fixtures.

**Full Patch**: add/remove fixtures, fixture types, structural changes. Closing Patch prompts Save and Exit. Removing a fixture row deletes programmed data for that fixture (cannot Oops). Clearing DMX address or ID leaves programming but the fixture is not editable / has no output / hidden from the Fixture Sheet.

## MVR

Import via Partial Show Read. Export from Patch → Export (grandMA3 XML under `gma3_library/patch` or MVR under `gma3_library/mvr`; Entire Patch or Selected Fixtures). Network exchange: MVR-xchange (In & Out). Option keyword `/MVR` exists for MVR-format export — confirm [`keywords/options/`](keywords/options/) before use.

## Attribute definitions / parameter list / DMX curves

- **Attributes**: max **1 024** different attributes per show; **366** predefined. Building blocks for fixture types (Activation / Feature / Deactivation groups). Edit in Patch → Attribute Definitions (**GUI**).
- **Parameter List** (RTChannels): defaults / highlight / lowlight (and presets) and DMX curve assignment are editable; coarse/fine/ultra addresses are informational here.
- **DMX Curves**: MinMax / Switch / Custom; max **9 999** curves per show. Assign on parameters; `UseForVisualization` can make 3D disagree with stage for color-calibrated fixtures. Edit inside Patch; save Patch to apply.

## DMX Universes (in Patch)

All **1 024** universes. Columns include Merge Mode, Request (Auto/On/Off), Granted, coarse params, used fixtures. Universe pool window exists. Network/port merge detail: [`dmx.md`](dmx.md).

## DMX Sheet

Window showing actual DMX output (sequences, programmer, merged in, masters). Absolute vs universe.address readout; Value / Attribute / ID masks. DMX Tester encoder bar clears via CLI above. Related priorities: [`dmx.md`](dmx.md).

## Position / 3D / render / camera (short facts)

- Position via Live Patch XYZ/rotation columns, 3D Viewer Setup tools (Line / Grid / Circle arrange), or position calibration — **GUI**. Axes: +X stage left, +Y upstage, +Z up; meters and degrees only.
- **3D Viewer**: Setup vs operate; stage box/floor; cameras from Camera Pool; title-bar Stage / Render Quality / Camera. While shaders compile, yellow status text.
- **Render Quality**: pool object selected by 3D Viewer (Beam modes No Beam → High Fancy, Shadow, Gobo, etc.) — **GUI** pool/editor.
- **Camera Pool**: default cameras; locked **Auto** camera frames selection (or whole stage). Edit Camera pop-up is **GUI** (FOV, Roll, Mode 3D/2D, …). Do not invent `Set Camera …` properties.

Selects camera **3** (manual also shows `Select Camera 3`):

```
Camera 3
```

## Related

- Groups / selection: [`groups.md`](groups.md), [`concepts/operate-fixtures.md`](concepts/operate-fixtures.md)
- Layouts multipatch: [`layouts.md`](layouts.md)
- DMX in/out / priorities: [`dmx.md`](dmx.md)
- Automation: [`automation.md`](automation.md)
