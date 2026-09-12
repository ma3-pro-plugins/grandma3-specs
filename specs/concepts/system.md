---
title: System Overview
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/system.html"
---

# System Overview

Manual hub for how a station (console or onPC) stands alone or expands: standalone device, locally networked devices, World Server, and parameters.

**Depth** (Standalone / IdleMaster / GlobalMaster / Connected, World Server, parameters vs DMX): [`../system.md`](../system.md).

## Agent mental model

A **station** holds a show file. Automation usually enters via:

- Command line / OSC — [`../command-line.md`](../command-line.md), [`../osc.md`](../osc.md), [`../remote-command.md`](../remote-command.md)
- Lua plugins — [`plugins.md`](plugins.md) → [`../plugins.md`](../plugins.md)
- Macros — [`macros.md`](macros.md)

| Piece | Role for automation |
| --- | --- |
| **Data pools** | Named pools of objects (fixtures, presets, sequences, macros, plugins, …) — [`datapools.md`](datapools.md) |
| **Programmer** | Live values for the current selection before Store/Update — [`programmer.md`](programmer.md) |
| **Playback** | Sequences on executors — [`cues-sequences.md`](cues-sequences.md), [`executors.md`](executors.md) |
| **Session** | Optional multi-station link — [`networking.md`](networking.md) → [`../multi-station.md`](../multi-station.md) |

Leave the current session:

```
LeaveSession
```

## Subtopics (manual)

- Standalone Device
- Locally Networked Devices
- World Server
- Parameters

## Curated

- Bare commands only — never include console CLI chrome (`User name[Fixture]>`).
- Hardware executor layout (lab note): [`../hardware-layout.md`](../hardware-layout.md) (`source: lab`).
- Repo load order: [`../versions.md`](../versions.md) → this map → Topic Spec → Keyword Spec → Help Dump.
- Topic Spec: [`../system.md`](../system.md)
