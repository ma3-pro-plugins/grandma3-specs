---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/group.html"
---

# Groups (Topic Spec)

Concept map (thin): [`concepts/groups.md`](concepts/groups.md). Keyword: [`keywords/Group.md`](keywords/Group.md).

Groups store **fixture selection**, **order**, and **selection-grid** position — **not** attribute values. Creating or editing a group always goes through the **programmer selection**: the fixtures currently selected are what `Store Group …` writes.

## Programmer selection → group

1. Build a selection in the programmer (`Fixture …`, `Group …`, `+` / `-`, …).
2. `Store Group N` writes that selection into group `N`.

Empty selection stores an empty group (or merges/removes nothing useful — prefer an explicit selection).

```
Fixture 1 Thru 10; Store Group 1 /NoConfirmation
```

Creates **Group 1** containing fixtures 1–10 (order/grid from the selection). `/NoConfirmation` avoids the store-mode pop-up — required for unattended automation; see [`automation.md`](automation.md).

## Build a selection with + and −

Combine fixtures (or groups) into one selection, then store:

```
Fixture 1 Thru 5 + Fixture 10 Thru 12; Store Group 2 /NoConfirmation
```

Creates **Group 2** with fixtures 1–5 and 10–12.

```
Group 1 + Group 2; Store Group 3 /NoConfirmation
```

Creates **Group 3** from the union of the fixtures in groups 1 and 2 (current selection after calling both with `+`).

Subtract from a selection before store:

```
Group 5 - Fixture 2; Store Group 6 /NoConfirmation
```

Creates **Group 6** with every fixture from group 5 except fixture 2.

Keywords: [`Plus`](keywords/Plus.md), [`Minus`](keywords/Minus.md), [`Thru`](keywords/Thru.md).

## Store into an existing group

Storing onto a group that already exists opens a **store-mode** pop-up unless you pass an option (and `/NoConfirmation` for automation). Group-relevant Store options (Official lists Group under each):

| Option | Effect on the group |
| --- | --- |
| [`/Merge`](keywords/options/Merge.md) | Add the current programmer selection into the existing group (merge selection / grid per GridMergeMode). |
| [`/Remove`](keywords/options/Remove.md) | Remove the currently selected fixtures from the existing group. |
| [`/Overwrite`](keywords/options/Overwrite.md) | Replace the group so it contains **only** the current programmer selection. |

Examples (each states the result):

```
Fixture 20 Thru 25; Store Group 1 /Merge /NoConfirmation
```

Adds fixtures 20–25 into existing **Group 1** (other members stay).

```
Fixture 3; Store Group 1 /Remove /NoConfirmation
```

Removes fixture 3 from **Group 1**; other members stay.

```
Fixture 1 Thru 4; Store Group 1 /Overwrite /NoConfirmation
```

**Group 1** now contains only fixtures 1–4.

[`/GridMergeMode`](keywords/options/Gridmergemode.md) controls how merged fixtures land on the selection grid (manual Create Groups: Append X vs Off). Confirm the option Spec before use.

## Call / list / delete

```
Group 3
```

Selects (SelFix) the fixtures in group 3 — default function of Group.

```
List Group
```

Lists groups in the pool (command-line history).

```
Delete Group 5 /NoConfirmation
```

## Recipes and masters

- Recipe **Selection** must be a group — [`concepts/recipes.md`](concepts/recipes.md), [`phaser-recipe.md`](phaser-recipe.md).
- Group Masters affect **playback** of fixtures in the group — [`concepts/groups.md`](concepts/groups.md), [`concepts/masters.md`](concepts/masters.md).

## Related

- Programmer: [`concepts/programmer.md`](concepts/programmer.md)
- Automation / no pop-ups: [`automation.md`](automation.md)
- Data pools: [`concepts/datapools.md`](concepts/datapools.md)
