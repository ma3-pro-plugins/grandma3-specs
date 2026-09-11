---
title: Groups
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/group.html"
---

# Groups

Groups contain a selection of fixtures (one or many). The fixtures' **selection order** and **grid position** are stored with the group. Groups do **not** store attribute values — only selection, order, and grid.

Using a group is a fast way to select those fixtures. Groups live in the **Groups pool** (a child of a Data Pool — [`datapools.md`](datapools.md)).

Cues and presets do **not** store a group reference; they store fixture values only.

## Store a group from the programmer

These commands create **Group 1** with fixtures 1 through 10 in it (order and grid from the current selection; no attribute values):

```
Fixture 1 Thru 10
Store Group 1
```

Calling a group without a function **SelFix**es its fixtures (default function of [`Group`](../keywords/Group.md)). This selects the fixtures stored in group 3:

```
Group 3
```

Other examples (`Store Group 5` stores the **current** programmer selection into group 5):

```
Store Group 5
List Group
Delete Group 5
```

Confirm Store/Delete options on Keyword Specs: [`Store`](../keywords/Store.md), [`Delete`](../keywords/Delete.md). Groups do not store values — only selection, order, and grid (needed for ranged input and phasers).

## Recipes

Groups are a **basic building block of recipes**. A recipe row must have a **Selection**, and that Selection must be a **group**. Recipes can store a reference to groups; cues/presets cannot.

See [`recipes.md`](recipes.md) and [`../phaser-recipe.md`](../phaser-recipe.md).

## Group Masters

Groups can also act as **group masters**: they affect **playback** of the fixtures inside the group (level/intensity of those fixtures), not the stored group selection itself.

There are four kinds (Positive, Negative, Scaling, Additive) — details in the [Group Masters](https://help.malighting.com/grandMA3/2.5/HTML/group_master.html) manual topic and the concept map [`masters.md`](masters.md). Keyword for master objects: [`Master`](../keywords/Master.md).

Groups can be assigned to executors as handles for that master level (see [`executors.md`](executors.md)).

## Related

- Programmer / selection: [`programmer.md`](programmer.md), [`operate-fixtures.md`](operate-fixtures.md)
- Data pools: [`datapools.md`](datapools.md)
