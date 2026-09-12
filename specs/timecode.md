---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/timecode.html"
---

# Timecode (Topic Spec)

Concept map (thin): [`concepts/timecode.md`](concepts/timecode.md). Keywords: [`Timecode`](keywords/Timecode.md), [`TimecodeSlot`](keywords/Timecodeslot.md), [`Store`](keywords/Store.md), [`Set`](keywords/Set.md), [`Go+`](keywords/Goplus.md), [`Top`](keywords/Top.md), [`Off`](keywords/Off.md), [`Select`](keywords/Select.md), [`Label`](keywords/Label.md), [`Menu`](keywords/Menu.md).

Manual hub + subtopics (one object): [Viewer](https://help.malighting.com/grandMA3/2.5/HTML/timecode_viewer.html), [Track Groups](https://help.malighting.com/grandMA3/2.5/HTML/timecode_track_groups.html), [Markers](https://help.malighting.com/grandMA3/2.5/HTML/timecode_markers.html), [Tracks](https://help.malighting.com/grandMA3/2.5/HTML/timecode_tracks.html), [Time Ranges](https://help.malighting.com/grandMA3/2.5/HTML/timceode_time_ranges.html) (manual HTML stem typo `timceode_`), [Events](https://help.malighting.com/grandMA3/2.5/HTML/timecode_events.html), [Slots](https://help.malighting.com/grandMA3/2.5/HTML/timecode_slots.html), [Create](https://help.malighting.com/grandMA3/2.5/HTML/timecode_create.html), [Settings](https://help.malighting.com/grandMA3/2.5/HTML/timecode_settings.html), [External Connections](https://help.malighting.com/grandMA3/2.5/HTML/timecode_external_connections.html).

A timecode show fires events (and can move faders) against a running time counter: **internal** timing or an **external** source via a Timecode Slot. Hierarchy: **Timecode show** → **Track Groups** → **Tracks** → **Time Ranges** → **Events** (subtracks hold fader motion). Shows live in the Timecode pool; **16** fixed Timecode Slots in the TimecodeSlots pool.

**Internal timecode / session master:** one-line link — [`multi-station.md`](multi-station.md). Track/event editing beyond store/playback is largely Viewer Setup **GUI** (or Object API).

Finite value sets (typings; Official TCSlot names kept below):

- **LoopMode** (typings): `Loop` \| `Pause` \| `Off`
- **TimecodeSlot** (typings alias): `TCSlot 1`–`8`, `<Selected>` — Official uses `Internal` / `Link Selected` / Slot n
- **TimecodePoolAction** (typings): `Select` \| `Toggle` \| `Go+` \| `Pause` \| `Off` \| `Top` \| `None`

## Store / set / play (CLI)

Stores a new timecode show named **Napalm Skies** (first free pool slot if unnumbered). `/NoConfirmation` is listed on [`Store`](keywords/Store.md) for unattended use — [`automation.md`](automation.md):

```
Store Timecode "Napalm Skies" /NoConfirmation
```

Sets duration of show **Intro** to **55** seconds:

```
Set Timecode "Intro" "Duration" "55"
```

Renames show **Intro** to **Prelude**:

```
Set Timecode "Intro" "Name" "Prelude"
```

Starts (plays) show **Prelude** (`Go` / [`Go+`](keywords/Goplus.md) per Timecode Official):

```
Go Timecode "Prelude"
```

Rewinds show **Prelude** to the top:

```
Top Timecode "Prelude"
```

Opens the label pop-up for timecode pool object **3**:

```
Label Timecode 3
```

`Set Timecode` also documents: Time, Offset, Loop Mode, Loop Count (internal only), TimeMarkers, **TCSlot** (`Internal` / `Link Selected` / Slot n), AutoStart / AutoStop / User Bits (external slot). Confirm values in [`Timecode`](keywords/Timecode.md) before use.

## Timecode slots (CLI)

Sixteen slots — edit only; cannot add/copy/delete/move. Slot settings are **not** in the show file (not synced by show transfer). Each slot can listen externally and/or **generate** time.

Selects timecode slot **4**:

```
Select TimecodeSlot 4
```

Starts the generator on slot **2** (`Go+` / `On`):

```
Go+ TimecodeSlot 2
```

Stops the generator on slot **2** and resets time (`Off`; `Pause` stops without reset — GUI/docs; use Official functions only):

```
Off TimecodeSlot 2
```

## Track groups (CLI)

Selects track group **2** of timecode show **1** (dotted path):

```
Select Timecode 1.2
```

Adding track groups / tracks / targets is Viewer Setup **GUI** (or Object API). Track **Target** may be Sequence, Sound, Timecode, Timecode Slot, Preset, Group, or Master.

## Viewer / markers / time ranges / events (short facts)

- **Viewer**: window or pool Edit pop-up; Setup mode = editor. Playback toolbar (play / record when Setup). Prefer Viewer over the thinner pool Edit pop-up for tools.
- **Markers**: on Track Groups; vertical lines; M<< / >>M jump. Add in Setup with Selection Target TimeRanges — **GUI**.
- **Time Ranges**: children of Tracks; auto-created for full show duration; may overlap; Events are children; event Time is relative to range start. Copy/paste ranges to repeat sections — **GUI**.
- **Events**: diamond on timeline; **Token** = action when cursor hits. Recorded events may show timed-cue / command / fader icons. Add/edit tokens in Setup — **GUI**.

## Settings / external (short facts)

- Settings via Viewer **Settings** or EditSetting on the pool object. **TC Slot**: `<Internal>`, `<Selected>`, or TCSlot 1…; **Offset TC Slot** shifts when the show fires vs incoming time.
- External: SMPTE/LTC, MIDI TC, ArtTimeCode in/out via Connector Configuration columns (SMPTE Mode / SMPTE TC / MIDI TC Mode / MIDI TC).

Opens Connector Configuration for SMPTE/MIDI TC columns:

```
Menu "ConnectorConfig"
```

Physical LTC/MIDI wiring is outside this Spec. Generator may also transmit SMPTE/MIDI when configured.

## Related

- Data pools: [`concepts/datapools.md`](concepts/datapools.md)
- Session / master: [`multi-station.md`](multi-station.md)
- DMX connector menu: [`dmx.md`](dmx.md)
- Automation: [`automation.md`](automation.md)
