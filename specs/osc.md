# OSC, DumpLog, and remote commands

How a station accepts command input over OSC, how to prove a command ran, and how to import plugins or run Lua from that path.

## OSC command input

- Protocol: **UDP OSC**, not TCP.
- Address: `/cmd` (desk **In & Out → OSC** command input; some docs write `/gma3/cmd`)
- Default port: **8000** (match **In & Out → OSC** on the desk).
- Payload: one grandMA3 command string (the same text you would type on the command line).
- A zero-dependency sender lives in [`.agents/skills/ma3-osc/scripts/ma3-cmd.js`](../.agents/skills/ma3-osc/scripts/ma3-cmd.js) (`node … "DumpLog /nc"`). It sends UDP OSC to `/cmd`.

Enable on the station:

- **In & Out → OSC**
  - Enable Input: Yes
  - Receive Command: Yes
  - Port: **8000** (or the port you actually send to)

`nc -z … 8000` and `lsof` TCP LISTEN checks are **not** proof. OSC input is UDP; those tools can report “closed” while commands still land.

Sending a UDP packet only proves the packet left this machine. End-to-end proof is an Echo in that station’s system monitor after `DumpLog`.

## Host

Session master / follower and OSC relay rules: [`multi-station.md`](multi-station.md).

Default to **`127.0.0.1`** when the agent and onPC share a machine. Do not guess LAN IPs or “the master.” Use another host only when the user names it.

On a **non-master** station in a session, direct OSC is unreliable. Send OSC to the **current master** and relay with `RemoteCommand IP <target-ip> "<command>"`. See [`remote-command.md`](remote-command.md). Master can flip (`MasterPriority`); do not hard-code a lab IP as master.

How to tell which station is master (from that station’s DumpLog):

| Source | What to look for |
| --- | --- |
| **Master** system monitor | `Station Status: GlobalMaster` (in session), or `IdleMaster` / `Standalone` when alone |
| **Non-master** system monitor | `Station Status: Connected` while in session |
| ManetSocket / peer lines | `master = …` or a peer `Changed Status:GlobalMaster` |

`IdleMaster` on a **follower’s** log does not mean that host is session master. Ask the user, or read the **master station’s own** log.

## DumpLog and the system monitor

`DumpLog /nc` writes the system monitor to the station’s `gma3_library/system_monitor` folder.

Typical shared-library tail (prepend the user’s absolute `gma3_library`):

```text
<gma3_library>/system_monitor
```

If DumpLog appears to run but no new file appears, that folder may be full of old `.log` files. Delete or move them, then DumpLog again.

`Echo('…')` shows in the system monitor. `Printf('…')` goes to command-line history and is harder to grep in a DumpLog file.

## Echo proof

1. Send `Echo <unique-stamp>` over OSC to the target station (or via `RemoteCommand` to a non-master).
2. Send `DumpLog /nc` to **that same station**.
3. In the newest system-monitor file, accept:

   - `OSCInput: /cmd … Echo <unique-stamp>`
   - `OK:Echo "<unique-stamp>"`

If those lines are missing, stop and fix OSC on that station before more commands.

## Import Plugin Library

```text
Import Plugin Library "FileName.xml" At Plugin "" /o
```

`At Plugin ""` lets MA pick a free plugin index. Use `At Plugin N` only when the user wants a fixed slot.

Prove import from that station’s DumpLog: OSC input line, `Loading plugin: …`, then `OK:Import Plugin Library …` or `Failed:Import Plugin Library …`. Stop at the first definitive `OK:` or `Failed:` for that command.

Optional reload after import: `ReloadUI` (often `ReloadUI /nc`).

## Lua keyword over OSC

The station that processes the command runs the snippet ([Lua keyword](https://help.malighting.com/grandMA3/2.3/HTML/keyword_lua.html)):

```text
Lua "Echo('hello')"
```

The Lua body is one MA argument in double quotes. Prefer single quotes inside the Lua string. For `RemoteCommand` relays, Lua long brackets `[[…]]` avoid nested-quote fights. Nested `\"…\"` inside `RemoteCommand` often injects extra backslashes.

After send: `OSCInput: /cmd … Lua …`, then `OK:Lua …`, then the Echo line.

Help Dumps for names and arity: [`lua-functions/`](lua-functions/) (pick the file that matches [`versions.md`](versions.md)). See [`object-api.md`](object-api.md).

## Other command-line verbs used with OSC

| Command | Notes |
| --- | --- |
| `ReloadUI` / `ReloadUI /nc` | Reload the Lua engine / UI |
| `Restart /NoConfirmation /NoSave` | Restart the station without saving |
| `SaveShow "name"` | Save a show file |
| `Call Plugin N` / `Call Plugin N <token>` | Arg 1 to the plugin main is the Display; the token is arg 2. For a single token with no spaces, do not wrap it in nested `\"…\"` inside `RemoteCommand`. |

Command-string length (~16K) and `Call Plugin` quoting: [`plugins.md`](plugins.md).
