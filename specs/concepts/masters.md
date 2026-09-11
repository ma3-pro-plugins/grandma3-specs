---
title: Masters
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/masters.html"
---

# Masters

Masters are **timing and level overrides**. Different families cover grand master, selected-sequence masters, Highlight / Lowlight / Solo, and speed / playback / timing masters.

Address them with [`Master`](../keywords/Master.md). Assign a master to an executor:

```
Assign Master 1.1 At Executor 206
```

```
Assign Master 2.1 At Executor 207
```

Confirm names and indexes on the Keyword Spec — do not invent master category names.

## Group Masters

**Group Masters** are a separate family: a group that limits or adds to **playback of the fixtures in that group**. Details and the four kinds live on [`groups.md`](groups.md) (manual: [Group Masters](https://help.malighting.com/grandMA3/2.5/HTML/group_master.html)).

## Related

- Executors: [`executors.md`](executors.md)
- Sequences: [`cues-sequences.md`](cues-sequences.md)
