# PhaserRecipe (MA ≥ 2.4)

Cue-part / preset **PhaserRecipe** objects (violet recipe lines) hold phaser steps, value sources, and MAtricks-like props on one object. They are **not** StandardRecipe (`HRecipe`): Cmd `Store Recipe` creates a StandardRecipe.

Official product notes: [`release-notes/Release_Notes_v2.4.md`](release-notes/Release_Notes_v2.4.md) (phaser recipes, shapes, Value Absolute/Relative). Typings: `grandma3-ts-types` `PhaserRecipe` / `PhaserRecipeSteps` / `PhaserRecipeStep` / `PhaserRecipeValueSource` in `typings/grandMA3.DataPool/functions.d.ts`.

---

## Object tree

Under a cue **Part** (or a Preset):

```text
Part
  PhaserRecipe
    PhaserRecipeSteps
      PhaserRecipeStep          -- Step 1, Step 2, … (step index is read-only)
        PhaserRecipeValueSource -- one or more per step (attributes / filters / preset)
```

`PhaserRecipe` also shares `RecipeBaseProps` with StandardRecipe (`selection`, `values`, `preset`, SpeedX/FadeX/…, MAtricks). Phaser-only extras include `measure`, `playbackNShot`, `playbackDirection`, `shape`.

`PhaserRecipeValueSource` props (typings): `attributes`, `shape`, `preset`, `curve`, `transX/Y/Z`, `widthX/Y/Z`, `accelX/Y/Z`, `decelX/Y/Z`, `rawValueAbs`, `rawValueRel`, `valueAbsolute`, `valueRelative`.

---

## Create

Use Object-API **Acquire** on the cue part. Cmd Store / `recipe.store()` creates a **StandardRecipe**.

```lua
local recipe = cuePart:Acquire('PhaserRecipe')
-- older builds: cuePart:Aquire('PhaserRecipe')
```

Acquire may leave children invalid until the main task settles. Re-find the child by class `PhaserRecipe` after a wait.

Acquire typically creates `PhaserRecipeSteps` with two steps already stamped (Step 1 / Step 2). The step **property cannot be edited** (`Property 'Step' … can not be edited`).

---

## Addressing

Numeric `ToAddr()` (e.g. `Sequence 13.1.0.1`) is often **Illegal** for cmdline `Set` / `Assign` on PhaserRecipe and its value sources. Prefer the **named cue-part keyword path**:

```text
Sequence 13 Cue 1 Part 0.1
Sequence 13 Cue 1 Part 0.1."PhaserRecipeSteps".1.1
```

Shape:

```text
{cuePartAddr}.{recipeIndex}
{cuePartAddr}.{recipeIndex}."PhaserRecipeSteps".{stepNumber}.{vsNumber}
```

`cuePartAddr` example: `Sequence 13 Cue 1 Part 0` (also seen as `Cue 1.0 Part 0` in some dumps).

---

## Selection and attributes

```text
Assign Group 1 At Sequence 13 Cue 1 Part 0.1
Assign Attribute "ColorRGB_R" At Sequence 13 Cue 1 Part 0.1."PhaserRecipeSteps".1.1
Assign Attribute "Pan" At …."PhaserRecipeSteps".1.1
```

`Set <vs> Property "attributes" "ColorRGB_G"` can return **Illegal value**. Use **Assign Attribute**.

Missing value-source slots: `Store` the named VS addr (Object `Append` of `PhaserRecipeValueSource` can produce a VS that `Assign Attribute` rejects as Illegal object). **Delete** of a PhaserRecipeValueSource is also Illegal.

Pinning a **named** attribute (`Assign Attribute "ColorRGB_R"`, …) limits that value source to that attribute. A Color Value Preset assigned afterwards still plays only R. To take **every** attribute stored in a preset, leave the value source unpinned and use `<From Preset>` (next section).

---

## Numeric / spline value-source writes

Cmdline `Set` on the named VS addr. PascalCase property names (`AccelX`, `RawValueRel`, `RawValueAbs`, `WidthX`, …).

Free vs Proportional spline: suffix on Accel/Decel strings (`"30F"` = Free, `"30P"` = Proportional). Display reads often show `"F 0%"` / `"P 0%"`.

Negative numerics: quote the value (`Property RawValueRel "-10"`). Non-negative may be bare.

Recipe-level fade/speed/delay ranges are **merged Thru** properties on the PhaserRecipe (`FadeX`, `SpeedX`, `DelayX`, …), not separate From/To cmdline cells. Phase uses `PhaseFromX` / `PhaseToX` (legacy dumps may still show merged `PhaseX`).

---

## Presets as step values

MA 2.4 docs: Value Absolute / Value Relative cells may be **presets**, not only numbers.

**Confirmed on 2.4 and 2.5.0.3** (Lua 5.5). Color presets round-trip as the value-source **`preset` property**.

| Probe | Version | Notes |
| --- | --- | --- |
| `Cue Phaser Step Preset Check` | 2.4 | `[StepPresetCheck]` — 2.4 reference; do **not** re-run on 2.5 (unquoted Set opens PresetPopup) |
| `Cue Phaser Step Preset Check 25` | 2.5.0.3 | `[StepPresetCheck25]` — isolated PASS, no PresetPopup |

### `<From Preset>` (all attributes in the preset)

A value source can take its **attributes from the assigned preset** instead of one named attribute. Display / UI shows `"<From Preset>"` (2.5 shapes-editor copy also uses that label: [`release-notes/Release_Notes_v2.5.0.2.md`](release-notes/Release_Notes_v2.5.0.2.md)). Cook then runs the phaser on **every attribute stored in that preset** (e.g. Color `ColorRGB_R` / `G` / `B` on one value source). One value source per step is enough; you do not add a row per attribute.

**How to get it (2.4 and 2.5)**

1. Create/store the value source with **no** `Assign Attribute "…"`.
2. Assign the preset at the value source **with no Property suffix**:

```text
Assign Preset 4.11 At Sequence 8 Cue 1 Part 0.1."PhaserRecipeSteps".1.1
```

Cmd `OK`. After wait, `Get('preset')` is userdata (`class=Preset`). Attributes become `<From Preset>`. MA places the preset on **absolute or relative** from the **content of the preset** (do not force `Property "ValueAbsolute"` / `"ValueRelative"`).

Confirmed: LiveFX Color instance seed on **2.5**; the same bare Assign on **2.4** (LiveFX: `Property "ValueAbsolute"` → **Illegal object**).

**What blocks it**

If the value source already has a named attribute (`Assign Attribute "ColorRGB_R"`, leftover seed pin, etc.), a later `Assign Preset … At <vs>` **keeps that attribute**. It does not switch to `<From Preset>`. Never pin before Assign (or recreate an unpinned value source).

Earlier 2.5 probes that **re-assigned `ColorRGB_R` after each clear** also stayed on R — that was the pin, not a 2.5 limitation of `<From Preset>`.

### Write (2.4 and 2.5)

Preferred (handle + `<From Preset>` on an unpinned VS; abs vs rel from preset content):

```text
Assign Preset 4.10 At Sequence 13 Cue 1 Part 0.1."PhaserRecipeSteps".1.1
```

Also OK on **both** versions (handle write; does not improve on bare Assign):

```text
Assign Preset 4.10 At <vsNamedAddr> Property "preset"
Assign Preset 4.10 At <vsNamedAddr> Property "Preset"
```

```lua
vs:Set('preset', presetHandle)  -- handle from GetObject('Preset 4.10')
```

Bare `Assign` does **not** unpin an already named attribute.

### Write — `Property "ValueAbsolute"` / `"ValueRelative"` (avoid)

On **2.4**, `Assign Preset … At <vs> Property "ValueAbsolute"` is **Illegal object** (LiveFX log: Assign at `PhaserRecipeSteps`.2.1).

On **2.5.0.2+** that Property form is legal and writes the preset onto the absolute cell, but it **forces absolute** and skips MA choosing absolute vs relative from the preset. Prefer bare Assign on both versions.

`Assign … Property "ValueRelative"` on 2.5 is Cmd OK but still fills **absolute `preset`** in earlier probes; `valueRelative` stayed empty. Do not treat it as a relative write — use bare Assign instead.

### Read (both versions)

| Access | After successful Assign |
| --- | --- |
| `vs:Get('preset')` | Preset **userdata handle** (`ToAddr()` = `Preset 4.10`) |
| `vs:Get('preset', Enums.Roles.Display)` | e.g. `"FeatureGroup 4 'Color'.Preset 10 '…'"` |
| `vs.preset` | same handle |
| `vs:Get('valueAbsolute')` | **name string** (e.g. `"H_0 S_0#2 "`), not a handle |
| `vs:Get('rawValueAbs')` | empty when the absolute is a preset |
| `vs:Get('attributes')` / Display | `"<From Preset>"` (or raw `nil` / Display `"<From Preset>"`) after bare Assign on an unpinned VS. Named attribute string if the VS was pinned first. |

Compare identity via the **preset handle** (`ToAddr()` / object equality), not by parsing `valueAbsolute`. Do not assume a seed name such as `ColorRGB_R` when matching value sources that use `<From Preset>`.

### Do not use (both versions)

| Command | Result |
| --- | --- |
| Quoted `Set <vs> Property "preset" "Preset 4.10"` | Cmd **OK**, then **clears** `preset` to nil |
| Quoted `Set <vs> Property "Preset" "Preset 4.10"` | same clear |
| `Assign Preset … At <vs> Property "ValueAbsolute"` (2.4) | **Illegal object** — use bare Assign |
| Quoted `Set <vs> Property "ValueAbsolute" "Preset 4.10"` | Illegal value |
| Quoted `Set <vs> Property "RawValueAbs" "Preset 4.10"` | Illegal value |
| `Assign Preset … At <step>` (PhaserRecipeStep, not VS) | Illegal object |
| `vs:Set('preset', "Preset 4.10")` (string) | Set reports ok; **no** handle on read |
| `Set Property "attributes" "ColorRGB_G"` (etc.) | Illegal value — use **Assign Attribute** |

### Do not use (2.5 only)

| Command | Result |
| --- | --- |
| Unquoted `Set <vs> Property "preset" Preset 4.10` | **Failed**, opens **PresetPopup** (`preset_popup.lua` syntax error) |
| Unquoted `Set <vs> Property "ValueAbsolute" Preset 4.10` | **Failed**, ~8s stall / UI menu |

`Cook Sequence N /o /nc` after Assign did **not** drop the preset handles (2.4 and 2.5.0.3). Whether playback of Color presets **requires** cook after each Assign is not covered here.

---

## Cook

```text
Cook Sequence 13 /o /nc
```

Overwrite cook (`/o`) cooks the cue-part recipe into playback data. Merge cook (`/m`) is a different product path.

---

## StandardRecipe vs PhaserRecipe (terminology)

| | StandardRecipe | PhaserRecipe |
| --- | --- | --- |
| UI | Green recipe line | Violet recipe line |
| Create | Cmd Store Recipe | `Acquire('PhaserRecipe')` |
| Typical “values” | Assign a (phaser) **Preset** on the recipe `values` / `preset` | Steps + **value sources** on the recipe itself |
| Step preset as value | n/a (preset is the whole phaser) | Bare `Assign Preset At <valueSource>` on an unpinned VS → `preset` handle, attributes `<From Preset>`, abs vs rel from the preset. |
