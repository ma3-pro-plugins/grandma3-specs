---
name: ma3-osc
description: >-
  Drive grandMA3 over OSC (UDP /gma3/cmd), prove commands with Echo and DumpLog,
  import plugins, and run remote Lua. Use when sending console commands from an
  agent, preflighting OSC, or checking system-monitor logs. Not for Pro Plugins
  framework install actions or project-specific helpers.
---

# grandMA3 OSC

Facts live in [`specs/osc.md`](../../../specs/osc.md). Also read [`specs/remote-command.md`](../../../specs/remote-command.md) and [`specs/plugins.md`](../../../specs/plugins.md) when relaying or calling plugins.

This skill is the procedure. Do not invent a transport script; use whatever OSC sender the user or host project already has.

## Before any command

1. Confirm onPC is running and the intended show is open.
2. Confirm **In & Out → OSC**: Enable Input Yes, Receive Command Yes, port **8000** (unless the user named another port).
3. Target **`127.0.0.1`** unless the user named a host in this task. Never guess `10.0.0.x` or “master.”
4. Do not use `nc -z` or TCP `lsof` as OSC preflight.

If preflight already succeeded earlier in this chat and nothing restarted, do not repeat the full checklist unless commands stop landing.

## Prove OSC

1. Send `Echo <unique-stamp>` to the target host.
2. Send `DumpLog /nc` to **that same host**.
3. Read the newest file under `<gma3_library>/system_monitor` (ask for the absolute `gma3_library` if you do not have it).
4. Require `OSCInput: /cmd` and `OK:Echo "…"` for that stamp.

If the stamp is missing, stop and fix OSC. “Packet sent” is not proof.

## After that

- Import: `Import Plugin Library "FileName.xml" At Plugin "" /o` — see [`specs/osc.md`](../../../specs/osc.md).
- Lua: `Lua "Echo('…')"` — prefer single quotes inside the Lua string.
- Non-master seat: OSC to the **current master** + `RemoteCommand IP <ip> "<cmd>"`. Ask which IP is master; do not hard-code it.
- Single-token `Call Plugin` actions inside `RemoteCommand`: do not wrap the token in nested `\"…\"`.

## Out of scope

Project-specific senders, log-copy scripts, HTTP log servers, framework `__install` / `__uninstall`, and per-plugin test actions belong in the consuming repo.
