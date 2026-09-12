---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/worldfilter.html"
---

# Worlds and Filters (Topic Spec)

Concept map (thin): [`concepts/worlds-filters.md`](concepts/worlds-filters.md). Keywords: [`keywords/World.md`](keywords/World.md), [`keywords/Filter.md`](keywords/Filter.md).

Manual hub + subtopics (one Spec): [Create World](https://help.malighting.com/grandMA3/2.5/HTML/worldfilter_world_create.html), [Create Filter](https://help.malighting.com/grandMA3/2.5/HTML/worldfilter_filter_create.html), [At Filter](https://help.malighting.com/grandMA3/2.5/HTML/worldfilter_at_filter.html), [Sheet Masking / filter rules](https://help.malighting.com/grandMA3/2.5/HTML/worldfilter_filter_rules.html).

**Worlds** limit which fixtures/attributes the programmer (and affected sheets) can touch — useful in multi-user so each user works in a designated world. **Filters** block attributes/layers (and can carry filter rules) for store/update/recall and for **sheet masking**.

The **selected world** and the **selected or called filter** always dictate what the programmer can do. Worlds/filters can be assigned to objects (sequence, preset, …) as input/output filters and to sheets as masks. Pool icons mark Input Filter / Output Filter / both.

Multi-user / session: [`concepts/users.md`](concepts/users.md), [`multi-station.md`](multi-station.md). Data pools: [`concepts/datapools.md`](concepts/datapools.md).

## Worlds

World **1** (“Full” in a new show) is **locked** — all fixtures/attributes; cannot edit or delete.

A world is a matrix of **rows (fixtures)** × **columns (attributes)**. Store from the programmer:

- Current **fixture selection** → rows (if none selected → all fixtures)
- **Active attributes** → columns (if none active → all attributes)

Worlds store **membership**, not values — but you still need attributes **active** to include those columns.

Calls **world 3** (limits programmer/sheets to that world):

```
World 3
```

Labels world 3:

```
Label World 3 "All Fixtures"
```

Stores **world 5** from the current programmer selection / active attributes (automation-friendly):

```
Store World 5 /NoConfirmation
```

Stores a world with an explicit **Selection** property (**Normal** = include subfixtures/grouping; **Strict** = only exactly selected). Manual syntax:

```
Store World 5 Property "Selection" "Strict" /NoConfirmation
```

Confirm option strings on Keyword Specs / Official before variants. Selection-property changes on the **currently selected** world are not visible until you select another world and come back.

Deletes world 5 (not world 1):

```
Delete World 5 /NoConfirmation
```

World as preset/sequence input filter: [`presets.md`](presets.md) (`Assign World … At Preset …`).

## Filters

Default factory filters include All, Prog Only, Only Dimmer, Only Position, Only Color, Selection Only, Parked Only. Filter **1** (“All”) is locked and auto-updates with the attribute structure.

**Selected** filter: yellow frame. **Called** filter ([`Call`](keywords/Call.md)): yellow pulsating frame — applies to the **next** Store / Update / At / Clone only. If called ≠ selected (or At Filter was edited), selected shows a yellow line above the object. When a non-1 filter is selected/called, the **At** key flashes.

Calls **filter 4**:

```
Filter 4
```

Official Filter option: [`/Overwrite`](keywords/options/Overwrite.md) only. FilterAction (typings): `Select` \| `Call` \| `None` (pool / window settings choose Call vs Select).

### Create a filter

Three manual paths:

1. Edit an empty filter pool object → **Edit Filter** menu (rules GUI)
2. `Store Filter …` from current At Filter / filter settings
3. Assign an object (e.g. a group) onto a filter pool object

```
Store Filter 8 /NoConfirmation
```

Stores a new **filter 8** from the current filter settings (At Filter / editor context). Prefer explicit store mode if overwriting.

```
Assign Group 2 At Filter 8
```

Assigns **group 2** onto **filter 8** (manual syntax; Official shows `Assign Group X at Filter Y`).

Filter **rules** (Attributes, Selected(), Parked(), ID Type, Patch, Name, Used In Object, …) are configured in the **GUI** editor. Dynamic rules show a marker on the pool object. Rule-row enums (typings): FilterRuleTypes `Show` \| `Hide`; FilterRuleStatic `Yes` \| `No`. Automate via Object API / Keyword Spec — no evidenced CLI `Set` property names for rule rows on the Filter Keyword Spec.

Import/export of filter objects: GUI Import/Export in the editor. Old exports from ≤2.2.5.2 are not fully supported on ≥2.3.2.0 (fixture patch filters discarded) — migrate via 2.2.5.2 first if needed.

### At Filter window

Mostly GUI: see/add/store current filter attribute/feature toggles; Line Height / Select All / Select None. Store via `Store` + empty filter pool object (same as Create). No additional evidenced CLI beyond Store/Filter/Assign above.

### Sheet masking (filter rules topic)

Masks on **Fixture Sheet**, **Content Sheet**, **Track Sheet**. Assign Filter or World to Mask1–16 / mask toolbar (GUI: sheet settings → Mask Buttons; swipey Assign onto toolbar). Defaults: Fixture Sheet uses Prog Only + Selection Only; Content/Track use Selection Only.

Programming **layers** in filters are **not** compatible with sheet masking or input/output filtering (manual).

Assigning masks is **GUI-first** (sheet settings → Mask Buttons). Official Assign for filters includes **Assign Filter At Preset** (see [`presets.md`](presets.md)); sheet Mask1–16 targets are GUI.

## Related

- Preset / sequence input filters: [`presets.md`](presets.md)
- Layouts (filters can hide ID types in layouts — see layouts manual / [`concepts/layouts.md`](concepts/layouts.md) when present)
- Groups: [`groups.md`](groups.md)
- Automation: [`automation.md`](automation.md)
