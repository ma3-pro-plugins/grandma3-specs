---
title: Executors
topic_spec:
  - ../executors.md
  - ../hardware-layout.md
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/executor.html"
---

# Executors

Executors are **handles** (physical keys, knobs, faders, or on-screen virtual executors) that control other objects. A sequence is often assigned to an executor; several executors can control the same object. The executor sends commands to the object in the pool.

**Topic Spec (depth — assign, pages, AssignmentButtonFunctionsSequence / AssignmentFaderFunctions / SpecialExecutor typings):** [`../executors.md`](../executors.md).

Assign / On / Off / Go family — Keyword Specs + finite key/fader/special lists on the Topic Spec. Bare sequence `Go+` also works (see [`cues-sequences.md`](cues-sequences.md)).

```
Assign Sequence 1 At Executor 201
```

Assigns sequence 1 to executor **201** (2nd physical row: fader + key — see layout below). Confirm [`Assign`](../keywords/Assign.md), [`Executor`](../keywords/Executor.md), [`Sequence`](../keywords/Sequence.md).

## Physical console layout

Lab note for **hardware** executor numbers (grandMA3 console surface). Virtual Playback Window executors follow the same numbering model. Canonical Topic Spec (edit there if this disagrees): **[`../hardware-layout.md`](../hardware-layout.md)** (`source: lab`). Do not fork the row table into [`../executors.md`](../executors.md) beyond a short pointer.

Executors are laid out in **4 rows** on the physical console (bottom to top):

| Range | Row (from bottom) | Controls |
| --- | --- | --- |
| 101–190 | 1st | Key only |
| 201–290 | 2nd | Fader + key |
| 301–390 | 3rd | Encoder + key |
| 401–490 | 4th | Encoder + key |

Within each row, executors are physically grouped in sets of 5 (e.g. 101–105, 106–110, 111–115), with a gap between groups. That grouping applies to all four rows.

So: pick **201–290** when you need a fader handle; **301–390** / **401–490** when you need an encoder + key; **101–190** for key-only.

## Related

- **Topic Spec:** [`../executors.md`](../executors.md)
- Masters (including group masters): [`masters.md`](masters.md), [`groups.md`](groups.md)
- Sequences / cues: [`cues-sequences.md`](cues-sequences.md)
- Pages / executor configs live in the Data Pool: [`datapools.md`](datapools.md)
- Lab layout Spec: [`../hardware-layout.md`](../hardware-layout.md)
