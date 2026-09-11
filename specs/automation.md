---
source: mixed
---

# Automation (macros, plugins, OSC)

**Automation** here means any command string that must run **without an operator answering a pop-up**:

| Path | How commands arrive |
| --- | --- |
| Macro | Macro pool lines |
| Plugin | `Cmd` / Object API that issues CLI |
| OSC | `/cmd` (or desk-configured command address) payload |

Same CLI grammar for all three. Concept / grammar: [`concepts/command-syntax.md`](concepts/command-syntax.md), [`command-line.md`](command-line.md).

## /NoConfirmation (required for unattended runs)

Many functions (`Store`, `Delete`, `Copy`, `Import`, `Shutdown`, …) can open a **confirmation or store-mode** pop-up. A human can tap; a macro, plugin, or OSC client **stalls** until someone dismisses it (or the action never finishes cleanly).

**Rule:** on every command that might prompt, append [`/NoConfirmation`](keywords/options/Noconfirmation.md) (`/N`, `/NC`). Prefer naming the store mode explicitly (`/Merge`, `/Overwrite`, `/Remove`, …) **and** `/NoConfirmation` so the desk does not ask.

```
Store Cue 2 /NoConfirmation
```

Stores the active programmer values as Cue 2 on the selected sequence **without** a confirmation pop-up.

```
Store Group 1 /Overwrite /NoConfirmation
```

Overwrites Group 1 with the current selection and suppresses the store-mode pop-up.

```
Delete Sequence 8 /NoConfirmation
```

Deletes sequence 8 without a confirm dialog.

Official token list (which functions accept it): open the option Spec. Do not invent other "silent" flags.

## Also pass explicit options

`/NoConfirmation` only suppresses the dialog. If Store still needs a mode (merge vs overwrite vs remove), **say it on the command**. Otherwise defaults or a suppressed dialog can leave the wrong result.

See group store modes: [`groups.md`](groups.md). Cue/preset Store options: [`keywords/options/_index.md`](keywords/options/_index.md), [`keywords/Store.md`](keywords/Store.md).

## Where it runs

Session master vs follower, Cue Command vs CmdLine/OSC relay: [`multi-station.md`](multi-station.md). OSC prove loop: [`osc.md`](osc.md). Plugin `Cmd` limits: [`plugins.md`](plugins.md).

## Related skills

- [ma3-osc](../.agents/skills/ma3-osc/SKILL.md)
- [write-macro](../.agents/skills/write-macro/SKILL.md)
- [write-plugin](../.agents/skills/write-plugin/SKILL.md)
