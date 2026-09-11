---
title: Command-line grammar
source: mixed
---

# Command-line grammar

How grandMA3 command **strings** are built for Target. Token meanings live in [`keywords/`](keywords/) — this Spec is composition rules only.

Audience: plugins (`Cmd` / `CmdIndirect`), OSC `/cmd`, macros, `RemoteCommand`. Operator GUI click-paths are out of scope.

**Provenance:** Rules below are distilled from Keyword Spec Official text (2.5 manual crawl) plus Topic Spec observations (`plugins.md`, `osc.md`, `remote-command.md`). Where unsure, the text says so — open the linked Keyword Spec rather than guessing.

Manual syntax overview (GUI-oriented): [General Syntax Rules](https://help.malighting.com/grandMA3/2.5/HTML/csk_syntax_rules.html).

## 1. What a command is

One **command** is a sequence of keywords, IDs/names, and options parsed by the station.

Several commands may sit on one line, separated by [`;` (Semicolon)](keywords/Semicolon.md). This line turns **sequence 5 off**, then **deletes group 3**:

```text
Off Sequence 5; Delete Group 3
```

The command line does **not** accept a multi-line paste. Spec **CLI** fences that are a unit (select then store, etc.) must be that one-line `;` form so GitHub copy is pasteable. Unrelated examples: one command per fence. OSC/`Cmd` may send that same one-line chain as a single payload; one command per call is still fine when the task is a single statement.

## 2. Core pattern

Most commands look like:

```text
[Function] [ObjectType] [IdOrName] [/Option [Value]]…
```

| Piece | Role | Examples |
| --- | --- | --- |
| **Function** | What to do | `Store`, `Delete`, `Go+`, `At`, `Call`, `Assign` |
| **Object type** | What kind of thing | `Cue`, `Fixture`, `Group`, `Sequence`, `Macro`, `Plugin` |
| **Id or name** | Which instance | `1`, `3.5`, `"My Cue"`, `Next` |
| **Option** | Modifier (`/` + name) | `/Merge`, `/nc`, `/Overwrite` |

Many object keywords have a **default function** when the function is omitted (e.g. Group → SelFix, Macro → Go+). Always check that keyword’s Spec before relying on the default.

### Function vs helping keyword

Some tokens are only helpers inside a larger command ([`Thru`](keywords/Thru.md), [`If`](keywords/If.md), [`EndIf`](keywords/Endif.md), [`+`](keywords/Plus.md), …). [`At`](keywords/At.md) is special: it is both a function (apply values) and a helping “destination” marker after other functions.

[`At`](keywords/At.md) is also one of the few functions that may accept an **object list before** the function (see Official hint on that Spec).

## 3. Addresses: numbers, names, dots

### Numbers and names

- Numeric IDs: `Fixture 2`, `Cue 1`
- Names: usually quoted — `Sequence "Main"` (exact quote rules: see §6; when in doubt, match Official examples on the Keyword Spec)

### Dot (`.`)

From [`. (Dot)`](keywords/Dot.md):

- **No spaces** around the dot.
- Fractional values: `At 10.5`
- Hierarchy: `Parent.Child` — e.g. `Fixture 31.2`, `Preset 4.2`, `ViewButton 2.1`

### Cue IDs are special

From [`Cue`](keywords/Cue.md): cue numbers may be decimals in `0.001`–`9999.999`. For **other** object types, a dot means parent.child, not a fractional ID.

Stores the active programmer values as **cue 1.5** of the selected sequence (cue IDs may be decimals):

```text
Store Cue 1.5
```

Applies **preset 4.2** to fixture **31.2** (dot on Fixture is parent.child, not a fractional cue ID):

```text
Fixture 31.2 At Preset 4.2
```

### Ranges and lists

| Token | Use | Example |
| --- | --- | --- |
| [`Thru`](keywords/Thru.md) | Inclusive range | `Fixture 3 Thru 6` |
| Open-ended Thru | Uses last start/end when omitted | `Fixture Thru 10` |
| [`+`](keywords/Plus.md) | Combine IDs / relative At | `Delete Cue 1 + 2` |
| [`-`](keywords/Minus.md) | Remove from lists / negative | see Spec |

### `#` handles

[`#[Object]`](keywords/Hashsquarebrackets.md) addresses by handle instead of number/name — see that Spec before using in plugins.

## 4. Selection and “If”

Selection is often built by resolving object lists (fixtures, groups, …).

[`If`](keywords/If.md) filters or deselects relative to another object list (and has Clone-related helping uses). Close multi-part If forms with [`EndIf`](keywords/Endif.md) when the Spec’s pattern requires it.

Filters the current selection with **group 5** (`If` is a CLI filter keyword, not a programming `if`):

```text
If Group 5
```

Do not treat `If` as a general-purpose programming `if` — it is a command-line filter keyword.

## 5. Options (`/…`)

Options are **option keywords** (dictionary under [`keywords/options/`](keywords/options/)).

From [`/ (Slash)`](keywords/Slash.md):

- Introduce options with `/` **without spaces**: `/Merge` not `/ Merge`.
- Same glyph is also a calculator separator — context-dependent.

Merges the active programmer values into **cue 1** of the selected sequence:

```text
Store Cue 1 /Merge
```

Writes the system-monitor log with **no confirmation pop-up** (`/nc` = `/NoConfirmation`):

```text
DumpLog /nc
```

Imports `File.xml` from the plugin library into the plugin pool, **overwrite** (`/o`):

```text
Import Plugin Library "File.xml" At Plugin "" /o
```

**Never invent option names.** If it is not in `keywords/options/`, do not emit it.

## 6. Quotes and embedding (automation-critical)

Observed rules for **plugin / RemoteCommand** string arguments ([`plugins.md`](plugins.md), [`remote-command.md`](remote-command.md)):

| Wrapper | JSON / embedded `"` in arg | Result |
| --- | --- | --- |
| Double `"..."` | Yes | Often **fails parse** (`Illegal name:`) |
| Single `'...'` | Yes | Works for typical `json.encode` payloads |
| Single `'...'` | Arg contains `'` | Breaks — apostrophe terminates the wrapper |

Practical guidance:

1. Prefer **single-quoted** wrappers around JSON plugin args.
2. Avoid apostrophes inside those payloads, or use another transport (`SendLuaMessage`, …).
3. Receivers must **not** strip backslashes before `json.decode`.

Exact CLI quoting for every object-name context is still easiest to copy from Official examples on the relevant Keyword Spec — expand Extra here when we have more observed cases.

## 7. Length limit (~16K)

Empirical (MA 2.3.2 playground; treat as still relevant until re-measured on Target): the **entire** command string passed through `Cmd()` / similar parsers caps around **~16382** characters. Fixed keywords/quotes eat the budget. Near the limit, prefer message queues / Lua APIs over giant CLI args — [`plugins.md`](plugins.md).

## 8. Oops / undo

[`Oops`](keywords/Oops.md) undoes last CLI action, selection, or programmer action (see Spec + `/NoConfirmation`).

## 9. Where the command runs

Cross-cutting rules (session master, Cue Command → master, OSC relay): [`multi-station.md`](multi-station.md).

| Path | Typical station | Spec |
| --- | --- | --- |
| OSC `/cmd` to a host | That host (if it accepts OSC); in a session prefer master | [`osc.md`](osc.md), [`multi-station.md`](multi-station.md) |
| CmdLine / Macro local | Local station | [`plugins.md`](plugins.md) |
| Cue command calling a plugin | **Master** | [`multi-station.md`](multi-station.md) |
| `RemoteCommand IP …` | Target IP (quoting rules apply) | [`remote-command.md`](remote-command.md) |

## 10. Proof

For OSC-driven work: `Echo` stamp → `DumpLog /nc` → look for `OK:` / `Failed:` — [`osc.md`](osc.md), concept [`concepts/osc-remote.md`](concepts/osc-remote.md).

## 11. What this Spec is not

- Not a keyword encyclopedia — use [`keywords/_index.md`](keywords/_index.md).
- Not GUI tutorials — those stay in the MA manual until syntax-first enrichment lands in Extra/Concepts.
- Not a promise that every Official syntax diagram is reproduced here — when composing a rare form, open the Keyword Spec.

## Related

- Concepts: [`concepts/command-line.md`](concepts/command-line.md), [`concepts/programmer.md`](concepts/programmer.md)
- CONTEXT layers: [`../CONTEXT.md`](../CONTEXT.md)
