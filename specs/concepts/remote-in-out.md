---
title: Remote In and Out
topic_spec:
  - ../osc.md
  - ../remote-command.md
  - ../multi-station.md
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/remote_inputs.html"
---

# Remote In and Out

DC / MIDI / DMX remotes, **OSC**, PSN, MVR-xchange, MSC, and related I/O.

## OSC (point to Topic Specs)

Automation depth: **[`../osc.md`](../osc.md)**. Session master / follower / `RemoteCommand` relay: **[`../multi-station.md`](../multi-station.md)**. Quoting / RemoteCommand: [`../remote-command.md`](../remote-command.md).

### Curated (from legacy osc-remote)

| Item | Value |
| --- | --- |
| Transport | **UDP** OSC (not TCP) |
| Address | `/cmd` (desk **In & Out → OSC**; some docs write `/gma3/cmd`) |
| Default port | **8000** (match the desk) |
| Payload | One grandMA3 command string |

Enable **Enable Input** + **Receive Command**. `nc`/TCP probes are not proof.

**Proof loop:** `Echo <stamp>` → `DumpLog /nc` on the **same** station → accept `OSCInput` + `OK:Echo` in newest system-monitor log. Helper: [`.agents/skills/ma3-osc/`](../../.agents/skills/ma3-osc/).

Related keywords: [`Echo`](../keywords/Echo.md), [`Dumplog`](../keywords/Dumplog.md), [`Remotecommand`](../keywords/Remotecommand.md), [`Lua`](../keywords/Lua.md), [`Import`](../keywords/Import.md) — open each Spec before use.
