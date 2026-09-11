---
title: Command Syntax and Keywords
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/command_syntax_keywords.html"
---

# Command Syntax and Keywords

The command line is how operators (and agents via OSC/macros/Lua `Cmd`) talk to the console: keywords, special characters, and identifiers.

**Depth:** grammar Spec [`../command-line.md`](../command-line.md). **Token dictionary:** [`../keywords/_index.md`](../keywords/_index.md).

Basic shape (manual):

```
[Function] [Object]
```

Example:

```
Delete Sequence 1
```

## Keyword kinds (syntax rules)

From [Syntax Rules](https://help.malighting.com/grandMA3/2.5/HTML/csk_syntax_rules.html):

| Kind | Role |
| --- | --- |
| **Function** (command) keywords | Verbs — what to do |
| **Object** keywords | Address show objects |
| **Help** keywords | Relate functions and objects |
| **Layer** / cue-timing / readout / At-value / playback / fader / operator keywords | Specialized families (see Official Keyword Specs) |
| **Option** keywords | Temporary filters on a command (`/Overwrite`, …) — [`../keywords/options/_index.md`](../keywords/options/_index.md) |

General rules (manual):

- Objects have a **default function** if none is given.
- Most functions have a **default object/type** if none is given.
- Objects form a hierarchy; unsupported functions may pass to parent/child — see Hierarchical Structure in the manual.

## Examples (bare commands)

```
Store Sequence 8 Cue 20 /Overwrite
Copy Cue 2 At 6
```

Abbreviations use each keyword’s shortcuts (subject to change — prefer full names in Specs). Capitalization of **property values** is case-sensitive; keyword command tokens are not distinguished by case.

## Curated

- Do not invent options or keywords — only tokens present under [`../keywords/`](../keywords/).
- OSC / prove loop: [`remote-in-out.md`](remote-in-out.md) → [`../osc.md`](../osc.md).
- Programmer-oriented recipes: [`programmer.md`](programmer.md).
