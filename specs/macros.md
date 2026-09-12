---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/macros.html"
---

# Macros (Topic Spec)

Concept map (thin): [`concepts/macros.md`](concepts/macros.md). Keyword: [`keywords/Macro.md`](keywords/Macro.md).

Manual hub + subtopics (one Spec): [Command Editor](https://help.malighting.com/grandMA3/2.5/HTML/command-editor.html), [Create](https://help.malighting.com/grandMA3/2.5/HTML/macro_create.html), [Import](https://help.malighting.com/grandMA3/2.5/HTML/macro_import.html), [CLI interaction](https://help.malighting.com/grandMA3/2.5/HTML/command-line-interaction.html), [Edit](https://help.malighting.com/grandMA3/2.5/HTML/macro_edit.html), [Assign](https://help.malighting.com/grandMA3/2.5/HTML/macro_assign.html), [Variables](https://help.malighting.com/grandMA3/2.5/HTML/macro_variables.html), [Properties](https://help.malighting.com/grandMA3/2.5/HTML/use-property.html), [Examples](https://help.malighting.com/grandMA3/2.5/HTML/macro_examples.html).

Macros are **commands stored in a pool object** (one or more lines). The Macro pool is a **Data Pool** child — like groups, sequences, and plugins, it is show data shared among users in the show (not uniquely “macro-only” sharing). Data pools: [`concepts/datapools.md`](concepts/datapools.md).

Default function of Macro is **Go+**: `Macro n` **runs** the macro. `Store Macro n` stores a **new empty** macro.

Runs **macro 5** (Go+):

```
Macro 5
```

Stores a new empty **macro 2**:

```
Store Macro 2
```

Where a macro **runs** in a session: [`multi-station.md`](multi-station.md). Unattended lines: [`automation.md`](automation.md) (`/NoConfirmation` only when that function lists it — Store/Delete/Import/… do).

## Macro line fields

Each row (Official examples + **typings** `MacroLineProps`): **command** / Command, **wait** / Wait (time, or special **Follow** = 0 / **Go** = pause until Go+), **note**, **enabled** / Enabled (boolean), **addToCmdLine** / AddToCmdline (boolean), **execute** / Execute (boolean; Yes = auto-Please; No = leave text on the command line). Macro-level (**typings**): `scribble`, `note`, `appearance`.

Sets wait of macro 3 line 4 to the special **Go** value (Official):

```
Edit Macro 3.4 "Wait" "Go"
```

## Command Editor (GUI)

Edit Command pop-up (macros, cues, agenda, …). Title toggles (user-profile defaults):

| Toggle | Effect |
| --- | --- |
| Create Handle | After Please, converts the **last** object in the command to a `#[Object]` handle (not Thru ranges; convert objects one Please at a time) |
| Preview Variables | Shows variable contents when the variable exists |
| Resolve Executor Assignments | Pressing an executor inserts the **assigned object** handle instead of the page.executor address |

Handles: [`keywords/Hashsquarebrackets.md`](keywords/Hashsquarebrackets.md). Example converting intent — store a handle of sequence 1 then use it; Official Go+ form:

```
Go+ #[Sequence 23]
```

Goes to the next cue of sequence 23 via its handle (survives rename/move).

## Create (CLI)

GUI: Edit empty pool object → Insert New Macro Line → Command Editor. CLI (terminal / no GUI) uses ChangeDestination + Insert + Set Property (manual create walkthrough):

```
ChangeDestination Macro
```

Changes the command destination into the Macro pool (then `List` to see empty slots).

```
Store 10
```

Stores empty macro **10** at the current destination (equivalent intent to `Store Macro 10` from root).

```
ChangeDestination 10; Insert; Set 1 Property "Command" "Fixture 1 At 100"; Set 1 Property "Wait" "Follow"; ChangeDestination Root
```

Inserts a line, sets its **Command** and **Wait**, then returns to root. MacroLine property tokens for `Set … Property`: `"Command"`, `"Wait"`, `"Note"`, `"Enabled"`, `"Execute"`, `"AddToCmdline"` (see Macro line fields above; [`keywords/Set.md`](keywords/Set.md) / [`keywords/Property.md`](keywords/Property.md)).

## Import

GUI: editor Import, or Menu → Show Creator → Import → Macros. CLI (Official Import example):

```
Import Macro Library "color.xml" At Macro 42
```

Imports library macro file **color.xml** into **macro 42**. Append `/NoConfirmation` when Import would prompt — [`keywords/Import.md`](keywords/Import.md), [`/NoConfirmation`](keywords/options/Noconfirmation.md).

## Command-line interaction (CLI property)

Macros (and Quickeys) have a **CLI** property. **CLI off:** tapping the pool object executes without interacting with the command line (pool object shows CLI in red). Edit/Move/Delete then need an explicit object address.

Opens the editor for **macro 5**:

```
Edit Macro 5
```

Opens the CLI property editor for macro 5 (manual):

```
Edit Macro 5 Property "CLI"
```

(Property token is `"CLI"` as shown — MacroLine / macro-level props listed under Macro line fields.)

## Edit / delete lines

```
ChangeDestination Macro 5; Set 2 Property "Command" "ClearAll"; ChangeDestination Root
```

Overwrites the command text of **line 2** in macro 5.

```
ChangeDestination Macro 5; Delete 3; ChangeDestination Root
```

Deletes **line 3** of macro 5 (`Delete` lists `/NoConfirmation`).

## Assign to executors / keys

Macro stays in the pool; executor/view button runs that pool object.

```
Assign Macro 2 At Page 1.402
```

Assigns **macro 2** to page 1 executor 402 (Official Assign example).

```
Assign Macro 5 At Executor 201
```

Assigns **macro 5** to executor **201** on the **current** page (manual assign syntax). Confirm [`keywords/Assign.md`](keywords/Assign.md), [`keywords/Page.md`](keywords/Page.md), [`keywords/Executor.md`](keywords/Executor.md).

## Variables

Two scopes: **user** (profile) vs **global** (all users in the session). Types: Integer, Double, Text (typeless storage; quotes force text). Names are case-sensitive.

```
SetUserVariable "Green" 5
```

Creates/sets user variable **Green** to integer 5.

```
SetUserVariable MyFavoriteText "9"
```

Stores the **text** `"9"` (quotes), not the number 9.

```
SetGlobalVariable myShow At Root "MANetSocket" Property "Showfile"
```

Sets global **myShow** from the loaded showfile property (manual Properties topic).

Read/delete: [`GetUserVariable`](keywords/Getuservariable.md), [`GetGlobalVariable`](keywords/Getglobalvariable.md), [`DeleteUserVariable`](keywords/Deleteuservariable.md), [`DeleteGlobalVariable`](keywords/Deleteglobalvariable.md). Concatenation / nested quotes: manual Variables topic — confirm Official examples before complex quoting.

## Properties (Set / Label / List)

```
List Preset 2.1
```

Lists properties of preset 2.1 in command-line history (same pattern for macros/groups/…).

```
Set Preset 2.1 Property "Name" "Signer"
```

Sets the Name property of preset 2.1 to **Signer**.

```
Set Sequence 42 Property "Priority" At Sequence 1
```

Copies Priority from sequence 1 onto sequence 42.

```
SetUserVariable "mySeqPrioName" At Sequence 42 Property "Priority" /Look
```

Stores the **named** priority (not index) into a user variable — [`/Look`](keywords/options/Look.md) when listed for that use.

## Example patterns (manual)

Calling `Macro 2` **from inside** macro 1 stops with the parent; use **`Call Macro X`** so the child continues independently:

```
Call Macro 2
```

Calls/runs macro 2 without tying its lifetime to the caller the same way a bare `Macro 2` line does (manual Examples).

Factory-style “world is selection” pattern (delete + store + call a temp world) — worlds Spec for depth:

```
Delete World 999 /NoConfirmation; Store World 999 /NoConfirmation; World 999
```

Deletes world 999 without confirm, stores a new world 999 from the current programmer selection/active attributes, then calls it. Worlds: [`worlds-filters.md`](worlds-filters.md).

## Related

- Automation: [`automation.md`](automation.md)
- Agenda / timed: [`concepts/agenda.md`](concepts/agenda.md), [`startup-dmxremote-agenda.md`](startup-dmxremote-agenda.md)
- Command grammar: [`concepts/command-syntax.md`](concepts/command-syntax.md), [`command-line.md`](command-line.md)
- Skill: [write-macro](../.agents/skills/write-macro/SKILL.md)
