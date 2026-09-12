---
title: MAtricks
topic_spec: ../matricks.md
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/matricks.html"
---

# MAtricks

MAtricks divides a fixture **selection** into sub-selections (and can shuffle that selection). Typical use: step through a selection one fixture or subgroup at a time, or spread values across a grid.

MAtricks objects live in the Data Pool. Official selection property names and typings Transform/Invert/ShuffleMode lists: Topic Spec [`../matricks.md`](../matricks.md); Keyword: [`MAtricks`](../keywords/Matricks.md).

**Topic Spec (depth):** [`../matricks.md`](../matricks.md).

Sets MAtricks **X** to 2 on the active selection:

```
Set Selection MAtricks "X" 2
```

Sets **XBlock** to 4 on selection 2:

```
Set Selection 2 MAtricks "XBlock" 4
```

Calls pool object **MAtricks 1**:

```
Call MAtricks 1
```

See [`datapools.md`](datapools.md). Recipes can attach MAtricks: [`recipes.md`](recipes.md). Selection / groups: [`groups.md`](groups.md), [`operate-fixtures.md`](operate-fixtures.md). Keywords: [`MAtricks`](../keywords/Matricks.md), [`Shuffle`](../keywords/Shuffle.md), [`Selection`](../keywords/Selection.md).

## Related

- **Topic Spec:** [`../matricks.md`](../matricks.md)
- Data pools: [`datapools.md`](datapools.md)
- Recipes: [`recipes.md`](recipes.md)
- Groups / selection: [`groups.md`](groups.md), [`operate-fixtures.md`](operate-fixtures.md)
