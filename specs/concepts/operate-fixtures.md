---
title: Operate Fixtures
topic_spec: ../operate-fixtures.md
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/operate_fixtures.html"
---

# Operate Fixtures

Selection, align, clone, fixture sheet, selection grid/bar, gels, sMArt, and related operate-fixture topics. The Programmer hub is split to [`programmer.md`](programmer.md).

**Topic Spec (depth — selection, parent/child, align, clone):** [`../operate-fixtures.md`](../operate-fixtures.md).

## Syntax pointers

Selects fixtures **1 through 10** in the programmer:

```
Fixture 1 Thru 10
```

Selects the fixtures stored in **group 3** (Group default function is SelFix):

```
Group 3
```

Selection helpers (confirm each Spec): [`Thru`](../keywords/Thru.md), [`Plus`](../keywords/Plus.md), [`Minus`](../keywords/Minus.md), [`If`](../keywords/If.md).

Align / Clone / Gel Official options and examples: Topic Spec [`../operate-fixtures.md`](../operate-fixtures.md); keywords [`Align`](../keywords/Align.md), [`Clone`](../keywords/Clone.md), [`Gel`](../keywords/Gel.md).

## Selection grid (XYZ)

Fixtures sit in a 3D **selection grid** (axes **X**, **Y**, **Z**). Origin is **0/0/0**. Each fixture is a box; the grid stores spatial relationships for MAtricks, phasers, and selection order. This is **not** 3D Viewer / patch XYZ — [`xyz.md`](xyz.md).

MAtricks properties come in matching **X / Y / Z** triples (`X`, `XBlock`, `fadeFromX`, …). Those act on the corresponding grid axis. Official: MAtricks X, Y, and Z directions are relative to the entire range of selected fixtures. Recipe rows embed the same families — [`../recipes.md`](../recipes.md).

Moves the grid cursor to **X=1, Y=2, Z=1**:

```
Grid 1/2/1
```

Groups store grid position with the selection — [`groups.md`](groups.md). Keyword: [`Grid`](../keywords/Grid.md). Depth (cursor, Move Grid Cursor, Align Range): [`../operate-fixtures.md`](../operate-fixtures.md).

## Related

- **Topic Spec:** [`../operate-fixtures.md`](../operate-fixtures.md)
- Programmer values: [`programmer.md`](programmer.md)
- Patch: [`patch.md`](patch.md)
- Store selection as a group: [`groups.md`](groups.md) / [`../groups.md`](../groups.md)
- MAtricks (X/Y/Z on the grid): [`matricks.md`](matricks.md) / [`../matricks.md`](../matricks.md)
- Recipes (embedded MAtricks): [`recipes.md`](recipes.md) / [`../recipes.md`](../recipes.md)
