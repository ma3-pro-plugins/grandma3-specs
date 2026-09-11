---
title: Data Pools
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/datapool.html"
---

# Data Pools

Much of the data belonging to a show file is stored in **pools**. Many of those pools exist as children of a **Data Pool** parent object.

A new show file creates a **default Data Pool**. That object contains the other pools.

New Data Pool objects can be created, giving an entirely new set of pools. This is useful if several shows or acts share the same patch (for example, each song in a band catalog in its own data pool).

There is no Topic Spec for this hub — keep the description here.

Keyword: [`Datapool`](../keywords/Datapool.md).

Goes to the **next cue** of sequence 2 **inside data pool 2** (not the selected data pool):

```
Go+ DataPool 2 Sequence 2
```

## Pools inside a Data Pool

| Destination | Concept |
| --- | --- |
| Worlds / Filters | [`worlds-filters.md`](worlds-filters.md) |
| Bitmaps / Generators / Shapes | [`bitmap.md`](bitmap.md), [`generators.md`](generators.md), [`shapes.md`](shapes.md) |
| Preset pools | [`presets.md`](presets.md) |
| Groups | [`groups.md`](groups.md) |
| Sequences | [`cues-sequences.md`](cues-sequences.md) |
| Plugins / Macros / Quickeys | [`plugins.md`](plugins.md), [`macros.md`](macros.md), [`quickeys.md`](quickeys.md) |
| MAtricks | [`matricks.md`](matricks.md) |
| Executor configs / Pages | [`executors.md`](executors.md) |
| Layouts / Timecodes | [`layouts.md`](layouts.md), [`timecode.md`](timecode.md) |

Target 2.5: Shapes moved from destination 16 to destination 4. Macros that address data-pool destinations **by number** need updating; name-based addresses are unaffected.

Pool windows can link to the selected data pool or a specific one (manual Common Window Settings).
