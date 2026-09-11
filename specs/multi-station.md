---
source: mixed
---

# Multi-station

Cross-cutting Topic Spec for **sessions, master/follower, and where commands run**. Other Specs and concepts only **mention** multi-station briefly and link here.

Related: [`api-objects-network.md`](api-objects-network.md) (MAnetSocket / HostTypes), [`remote-command.md`](remote-command.md), [`osc.md`](osc.md), [`plugins.md`](plugins.md).

## Sessions

- grandMA3 can run with multiple stations in one session. There is always at most one **Master** station.
- A station may join with a **MasterPriority**. If the joiner’s priority is higher than the current master’s, the joiner becomes master.
- The showfile is shared; changes sync to other stations (UDP).
- Each station runs plugins in its **own Lua VM**; all stations see the same MA objects ([`plugins.md`](plugins.md)).

## Where a command / plugin runs

Observed for direct plugin calls (e.g. `Plugin 1`) — [`plugins.md`](plugins.md):

| Invocation path | Station that runs it |
| --- | --- |
| CmdLine | **Local** station |
| Macro | **Local** station |
| Cue Command | **Master** station |

Factor this into OSC / `RemoteCommand` design. Do not assume “the station that stored the cue” is where the plugin VM runs.

## OSC in a session

Full OSC transport stays in [`osc.md`](osc.md). Session rules:

- On a **non-master** station, direct OSC is unreliable.
- Send OSC to the **current master**, then relay with `RemoteCommand IP <target-ip> "…"` when the follower must execute locally ([`remote-command.md`](remote-command.md)).
- Master can flip with `MasterPriority` — do **not** hard-code a lab IP as master.
- Default host when agent and onPC share a machine: `127.0.0.1`. Do not guess LAN IPs.

### Detecting master (DumpLog)

| Source | What to look for |
| --- | --- |
| **Master** system monitor | `Station Status: GlobalMaster` (in session), or `IdleMaster` / `Standalone` when alone |
| **Non-master** system monitor | `Station Status: Connected` while in session |
| ManetSocket / peer lines | `master = …` or a peer `Changed Status:GlobalMaster` |

`IdleMaster` on a **follower’s** log does not mean that host is session master. Ask the user, or read the **master station’s own** log.

## Network object API

MAnetSocket / session host types: [`api-objects-network.md`](api-objects-network.md).

## Concept map

Thin pointer page: [`concepts/multi-station.md`](concepts/multi-station.md).
