---
title: Groups
topic_spec: ../groups.md
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/group.html"
---

# Groups

Groups contain a selection of fixtures (one or many). The fixtures' **selection order** and **grid position** are stored with the group. Groups do **not** store attribute values — only selection, order, and grid.

Using a group is a fast way to select those fixtures. Groups live in the **Groups pool** (a child of a Data Pool — [`datapools.md`](datapools.md)).

Cues and presets do **not** store a group reference; they store fixture values only.

**Topic Spec (depth — store modes, merge/remove/overwrite, automation):** [`../groups.md`](../groups.md).

## Store a group from the programmer

Groups are built from the **current programmer selection** (fixtures selected in the programmer). `Store Group` writes that selection into the group — not dimmer/color values.

These commands create **Group 1** with fixtures 1 through 10 in it:

```
Fixture 1 Thru 10; Store Group 1
```

Combine fixtures with `+`, then store. Creates **Group 2** with fixtures 1–5 and 10–12:

```
Fixture 1 Thru 5 + Fixture 10 Thru 12; Store Group 2
```

Subtract from a selection with `-`, then store. Creates **Group 6** from group 5 without fixture 2:

```
Group 5 - Fixture 2; Store Group 6
```

Calling a group without a function **SelFix**es its fixtures (default function of [`Group`](../keywords/Group.md)). This selects the fixtures stored in group 3:

```
Group 3
```

For merge / remove / overwrite into an **existing** group, and `/NoConfirmation` for macros/plugins/OSC, use the Topic Spec: [`../groups.md`](../groups.md). Automation guide: [`../automation.md`](../automation.md).

Keywords: [`Store`](../keywords/Store.md), [`Plus`](../keywords/Plus.md), [`Minus`](../keywords/Minus.md), [`Thru`](../keywords/Thru.md), [`Delete`](../keywords/Delete.md).

## Recipes

Groups are a **basic building block of recipes**. A recipe row must have a **Selection**, and that Selection must be a **group**. Recipes can store a reference to groups; cues/presets cannot.

See [`recipes.md`](recipes.md) and [`../phaser-recipe.md`](../phaser-recipe.md).

## Group Masters

Groups can also act as **group masters**: they affect **playback** of the fixtures inside the group (level/intensity of those fixtures), not the stored group selection itself.

There are four kinds (Positive, Negative, Scaling, Additive) — details in the [Group Masters](https://help.malighting.com/grandMA3/2.5/HTML/group_master.html) manual topic and the concept map [`masters.md`](masters.md). Keyword for master objects: [`Master`](../keywords/Master.md).

Groups can be assigned to executors as handles for that master level (see [`executors.md`](executors.md)).

## Related

- **Topic Spec:** [`../groups.md`](../groups.md)
- Programmer / selection: [`programmer.md`](programmer.md), [`operate-fixtures.md`](operate-fixtures.md)
- Data pools: [`datapools.md`](datapools.md)
