---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/system.html"
---

# System Overview (Topic Spec)

Concept map (thin): [`concepts/system.md`](concepts/system.md).

Manual hub + subtopics: [System Overview](https://help.malighting.com/grandMA3/2.5/HTML/system.html), [Standalone Device](https://help.malighting.com/grandMA3/2.5/HTML/system_standalone.html), [Locally Networked Devices](https://help.malighting.com/grandMA3/2.5/HTML/system_local.html), [World Server](https://help.malighting.com/grandMA3/2.5/HTML/system_world.html), [Parameters](https://help.malighting.com/grandMA3/2.5/HTML/system_parameter.html).

**Thin Spec:** station vs session vs World Server vs parameters. Playback / programmer depth lives on their concepts. **Do not duplicate** multi-station master/follower matrices — [`multi-station.md`](multi-station.md).

## Station

Any grandMA3 device that can create and run a session is a **station** (console or onPC, including onPC + command wing). A station holds the show file.

| Status (manual) | Meaning |
| --- | --- |
| **Standalone** | Network off; alone |
| **IdleMaster** | Network on, alone, ready for a session |
| **GlobalMaster** | Session master |
| **Connected** | In session, not master |

Status appears in the Network menu title bar and as command-line icons.

To leave a session / return toward standalone (manual: turn network off via GUI or CLI):

```
LeaveSession
```

Keyword: [`LeaveSession`](keywords/Leavesession.md). Session join / network menus: [`concepts/networking.md`](concepts/networking.md) → [`multi-station.md`](multi-station.md).

Standalone / IdleMaster: limited to parameters the station unlocks; only local DMX ports. **Ethernet DMX** still needs an active session (IdleMaster alone is enough).

## Session (local networked)

Two or more stations in one session = local networked system. One **GlobalMaster** owns remote-input / sequence-command execution; others are **Connected**. Device types and nodes: Device Overview / networking concepts — do not expand here.

Cross-cut automation (where CmdLine / Macro / Cue Command / OSC run): **[`multi-station.md`](multi-station.md)**.

## World Server

If the station sees the internet it tries to connect to a World Server (default `worldserver.malighting.de`; changeable in Network Menu). Globe icon in the command line shows connection.

Offers: **fixture type** import (GDTF / grandMA3 Share) and **crash log** upload. Set server address to `"0"` in the Network menu to disable. Tech support: bring the station online, then provide crash time + serial ([`Version`](keywords/Version.md)).

## Parameters

MA counts **parameters** (calculated control functions), not raw DMX channels. 16-bit / 24-bit does not multiply parameter cost the way channel-count licensing would. Parameter List shows the show's parameters. Virtual parameters (e.g. XYZ) may exist alongside pan/tilt. Unlock / node count must cover the patched parameter load — details in the Parameters manual topic and patch concepts.

## Automation entry points (pointers only)

| Path | Spec |
| --- | --- |
| CLI / OSC / remote | [`command-line.md`](command-line.md), [`osc.md`](osc.md), [`remote-command.md`](remote-command.md) |
| Plugins | [`plugins.md`](plugins.md) |
| Macros | [`concepts/macros.md`](concepts/macros.md) |
| Programmer | [`concepts/programmer.md`](concepts/programmer.md) |
| Playback | [`concepts/cues-sequences.md`](concepts/cues-sequences.md), [`concepts/executors.md`](concepts/executors.md) |
| Data pools | [`concepts/datapools.md`](concepts/datapools.md) |

## Related

- Multi-station: [`multi-station.md`](multi-station.md)
- Networking concept: [`concepts/networking.md`](concepts/networking.md)
- Hardware layout (lab): [`hardware-layout.md`](hardware-layout.md)
