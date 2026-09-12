---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/operate_programmer.html"
---

# Programmer (Topic Spec)

Concept map (thin): [`concepts/programmer.md`](concepts/programmer.md).

Manual: [The Programmer](https://help.malighting.com/grandMA3/2.5/HTML/operate_programmer.html), [Programmer Layers](https://help.malighting.com/grandMA3/2.5/HTML/fixture-sheet-dmx-layer.html), [Encoder Bar](https://help.malighting.com/grandMA3/2.5/HTML/ws_encoder_bar.html), [Colored Indicators](https://help.malighting.com/grandMA3/2.5/HTML/ws_colors_markers.html), [Phasers](https://help.malighting.com/grandMA3/2.5/HTML/phaser.html) (value / step / phaser layers).

Three programmer **levels** (selected / active / deactivated), Blind, Clear, Freeze, Preview: stay on the concept page. This Spec is the **layer** catalog.

## Layers

Each **attribute** can hold **different values on different layers at the same time**. That is true in the **programmer** and after those values are **stored into cues or presets**. Selecting a layer (encoder bar, Layer Toolbar, or the layer keyword) chooses which slot you edit or which readout the sheet shows. It does **not** clear the other slots.

Store writes **active** programmer values (every layer that is active). Absolute and relative **store and play back separately** ([Phasers](https://help.malighting.com/grandMA3/2.5/HTML/phaser.html)). Phaser layers (Speed, SpeedMaster, Phase, Measure) behave like other attribute layers when activating, storing, or clearing.

## Stored layers

These hold look data. One attribute can have several of them populated together.

### Value

| Layer | Keyword Spec | What it holds |
| --- | --- | --- |
| Absolute | [`Absolute`](keywords/Absolute.md) | Typical static look (red marker) |
| Relative | [`Relative`](keywords/Relative.md) | Offset on top of absolute / playback (mauve) |

Selects the **Absolute** layer (next encoder / `At` values land here):

```
Absolute
```

Sets **ColorRGB_R** to 10 on the Absolute layer (other layers on that attribute stay):

```
Attribute "ColorRGB_R" At Absolute 10
```

Selects the **Relative** layer:

```
Relative
```

### Individual timing

Per-attribute times. Not the same as cue-level [`Cuefade`](keywords/Cuefade.md) / [`Cuedelay`](keywords/Cuedelay.md).

| Layer | Keyword Spec | Marker |
| --- | --- | --- |
| Fade | [`Fade`](keywords/Fade.md) | Green |
| Delay | [`Delay`](keywords/Delay.md) | Orange |

Sets an individual **fade** of 2 seconds on the current selection / attributes:

```
Fade 2
```

Sets dimmer to 50 and an individual fade of 2 seconds:

```
At 50 Fade 2
```

Sets an individual **delay** of 4 seconds on the current selection:

```
Delay 4
```

### Step (phaser, per step)

Apply to the **current programmer step** ([`Step`](keywords/Step.md), `Next Step`, `Previous Step`). Depth: [`phasers.md`](phasers.md).

| Layer | Keyword Spec |
| --- | --- |
| Width | [`Width`](keywords/Width.md) |
| Transition | [`Transition`](keywords/Transition.md) |
| Acceleration | [`Acceleration`](keywords/Acceleration.md) |
| Deceleration | [`Deceleration`](keywords/Deceleration.md) |

### Phaser-wide (same for all steps of that attribute)

| Layer | Keyword Spec |
| --- | --- |
| Speed | [`Speed`](keywords/Speed.md) |
| SpeedMaster | [`Speedmaster`](keywords/Speedmaster.md) |
| Phase | [`Phase`](keywords/Phase.md) |
| Measure | [`Measure`](keywords/Measure.md) |

Selects the **Phase** layer:

```
Phase
```

Sets phase **0 through 360** on the selected attribute (needs at least two active programmer steps):

```
At Phase 0 Thru 360
```

Selects the **SpeedMaster** layer:

```
SpeedMaster
```

Sets attribute **Pan** to SpeedMaster 1:

```
Attribute "Pan" At SpeedMaster 1
```

## Sheet / readout layers

These change what the Fixture Sheet, Sequence Sheet, or Content Sheet **displays**. They do **not** store a look. A sheet set to **Auto** follows the selected layer (Official on CueAbsolute / CueRelative / DMXLayer / OutputLayer — Auto is a sheet setting, not a keyword).

| Layer | Keyword Spec | Shows |
| --- | --- | --- |
| CueAbsolute (CueAbs) | [`Cueabsolute`](keywords/Cueabsolute.md) | Sequence.cue:part that supplies the running **absolute** |
| CueRelative (CueRel) | [`Cuerelative`](keywords/Cuerelative.md) | Sequence.cue:part that supplies the running **relative** |
| OutputLayer | [`Outputlayer`](keywords/Outputlayer.md) | Output readout |
| DMXLayer | [`DmxLayer`](keywords/DmxLayer.md) | DMX-sheet values (tester cells highlight white) |
| GridPosition | [`Gridposition`](keywords/Gridposition.md) | XYZ selection-grid coordinates at the time values were set |

Selects the **CueAbsolute** sheet layer:

```
CueAbsolute
```

Selects the **DMXLayer**:

```
DMXLayer
```

Selects the **GridPosition** layer:

```
GridPosition
```

## Not layers

Do not treat these as programmer value layers:

- [`Physical`](keywords/Physical.md) — value **notation** (`At … Physical n`), not a stored layer
- FixtureLayer — patch class / layer **object**, not an attribute value slot
- [`Cuefade`](keywords/Cuefade.md) / [`Cuedelay`](keywords/Cuedelay.md) — **cue** timing, not per-attribute layers
- Release / Remove / Stomp — special programmer **values**, not layers
- [`Step`](keywords/Step.md) / Next / Previous — pick **which step** the step and value layers apply to

## Markers

From [Colored Indicators](https://help.malighting.com/grandMA3/2.5/HTML/ws_colors_markers.html): red = absolute programmer; mauve = relative; green = individual fade; orange = individual delay; purple = phaser; bright / dark cyan = preset absolute / relative; blue = parked. White on the **left** of the indicator bar is programmer information that will **not** store (deactivated) — [`Deactivate`](keywords/Deactivate.md).

## Related

- Concept (levels, Blind, Clear, Freeze, Preview): [`concepts/programmer.md`](concepts/programmer.md)
- Phasers / effects: [`phasers.md`](phasers.md)
- Cues (CueFade / CueDelay): [`cues-sequences.md`](cues-sequences.md)
- Presets: [`presets.md`](presets.md)
- Store only **active** values: [`keywords/Store.md`](keywords/Store.md)
