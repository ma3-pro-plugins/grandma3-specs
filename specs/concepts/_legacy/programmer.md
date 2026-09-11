---
title: Programmer & values
source: mixed
---

# Programmer & values

The **programmer** holds live attribute values for the current fixture selection until you Store, Update, or Clear them. Automation that “sets a look” almost always goes: select → `At` values → `Store`/`Update`.

## Typical flow

```text
Fixture 1 Thru 5
At 50
Store Cue 2
```

- Selection object keywords (`Fixture`, `Group`, …) often default to selecting fixtures (SelFix) when used without an explicit function — see each Keyword Spec.
- [`At`](../keywords/At.md) applies values **live in the programmer** (and can mean “destination” after some functions). Relative values use `+` / `-` with `At` (see [`Plus`](../keywords/Plus.md)).
- [`Store`](../keywords/Store.md) writes programmer (or other sources, via options) into show objects. Default object type when omitted: **Cue** on the selected sequence.
- [`Update`](../keywords/Update.md) changes existing stored data (see Spec).
- [`Clear`](../keywords/Clear.md) / selection clears — confirm options on the Keyword Spec before using in plugins.

## Selection helpers

| Keyword | Why it matters |
| --- | --- |
| [`Thru`](../keywords/Thru.md) | Ranges: `Fixture 3 Thru 6` |
| [`+`](../keywords/Plus.md) / [`-`](../keywords/Minus.md) | Add/remove from lists; relative At |
| [`If`](../keywords/If.md) | Filter / deselect relative to another object list |
| [`Blind`](../keywords/Blind.md) | Programmer output path (see Spec) |
| [`Park`](../keywords/Park.md) | Hold values (see Spec) |

## Store options (common)

Store takes many option keywords (`/Merge`, `/Overwrite`, `/CueOnly`, `/Look`, `/Selective`, …). Prefer the option Keyword Spec under [`../keywords/options/`](../keywords/options/) — do not invent option names.

## Depth elsewhere

- Full token list: [`../keywords/_index.md`](../keywords/_index.md)
- Grammar (ranges, dots, quotes, options): [`../command-line.md`](../command-line.md)
