---
title: Macros
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/macros.html"
---

# Macros

Macros are **commands stored in a pool object**. A line can be a single command or a `;`-joined chain. Macros live in the **Macro pool**, which is a child of a Data Pool (same as groups, sequences, plugins — show data, not a per-user copy).

Default function of [`Macro`](../keywords/Macro.md) is **Go+**: calling a macro with no function **runs** it.

**Depth (MacroLine props Official + typings):** [`../macros.md`](../macros.md).

This command **runs macro 1** (starts it / Go+):

```
Macro 1
```

This command **stores a new empty macro 2**:

```
Store Macro 2
```

Imports a library macro file into **macro 42**:

```
Import Macro Library "color.xml" At Macro 42
```

Sets user variable **Green** to 5 (for use inside macro lines):

```
SetUserVariable "Green" 5
```

Macro lines are ordinary CLI strings (bare commands). Where a macro **runs** in a session (which station): [`../multi-station.md`](../multi-station.md). Unattended lines: [`../automation.md`](../automation.md) (`/NoConfirmation`).

## Related

- Command syntax: [`command-syntax.md`](command-syntax.md), [`../command-line.md`](../command-line.md)
- Agenda / timed runs: [`agenda.md`](agenda.md)
- Startup notes: [`../startup-dmxremote-agenda.md`](../startup-dmxremote-agenda.md)
- Data pools: [`datapools.md`](datapools.md)
