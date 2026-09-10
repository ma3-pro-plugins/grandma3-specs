---
title: OSC & remote command
source: mixed
---

# OSC & remote command

How to get a command string onto a station and prove it ran. Depth: [`../osc.md`](../osc.md), [`../remote-command.md`](../remote-command.md).

## OSC input (short)

| Item | Value |
| --- | --- |
| Transport | **UDP** OSC (not TCP) |
| Address | `/cmd` (desk **In & Out → OSC**; some docs write `/gma3/cmd`) |
| Default port | **8000** (match the desk) |
| Payload | One grandMA3 command string (same as typing the CLI) |

Enable **Enable Input** + **Receive Command** on the station. `nc`/TCP probes are not proof that OSC works.

**Host:** default `127.0.0.1` when agent and onPC share a machine. Do not guess LAN IPs. In a session, send to the **current master**; use `RemoteCommand` to reach followers — see Topic Specs.

## Proof loop

1. `Echo <unique-stamp>` to the target station  
2. `DumpLog /nc` on **that same** station  
3. Accept `OSCInput: /cmd … Echo …` and `OK:Echo "…"` in the newest system-monitor log  

Sender helper: [`.agents/skills/ma3-osc/`](../../.agents/skills/ma3-osc/).

## RemoteCommand

Relays a command string to another station by IP. Quoting and ~16K command-length limits matter (JSON in double quotes breaks) — details in [`../remote-command.md`](../remote-command.md) and [`../plugins.md`](../plugins.md).

## Related keywords

`Echo`, `DumpLog`, `RemoteCommand`, `Lua`, `Import`, `ReloadUI` — open each Keyword Spec before use.
