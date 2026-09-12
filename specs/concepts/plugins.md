---
title: Plugins
topic_spec:
  - ../plugins.md
  - ../object-api.md
  - ../hooks.md
  - ../message-queue.md
  - ../addonvars.md
  - ../plugin-access.md
  - ../enums.md
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/plugins.html"
---

# Plugins

Manual hub for Lua plugins: handles, interface/variable functions, Object-Free API, Object API.

Plugins are show objects in the **Plugins** pool (inside a DataPool). Each station runs plugin code in its **own Lua VM** against the shared object model.

## Topic Specs (depth)

| Spec | Covers |
| --- | --- |
| [`../plugins.md`](../plugins.md) | Lifecycle, where `Plugin N` runs, ~16K Cmd string limit, quoting JSON args |
| [`../object-api.md`](../object-api.md) | Help Dumps / API surface |
| [`../hooks.md`](../hooks.md) | Hooks |
| [`../message-queue.md`](../message-queue.md) | `OpenMessageQueue` / `SendLuaMessage` |
| [`../addonvars.md`](../addonvars.md) | AddonVariables |
| [`../plugin-access.md`](../plugin-access.md) | Read objects (`GetObject` / `ObjectList` / `:Get` / parent-children) |
| [`../enums.md`](../enums.md) | Lua `Enums` catalog |
| [`../lua-5.4-to-5.5.md`](../lua-5.4-to-5.5.md) | Migration (2.4→2.5) |

Target Lua: [`../versions.md`](../versions.md).

## Syntax

Runs **plugin 1** (default function is Go+):

```
Plugin 1
```

Calls the plugin named MyPlugin and passes a JSON argument string:

```
Call Plugin "MyPlugin" '{"ok":true}'
```

Imports `FileName.xml` from the plugin library into the plugin pool, overwriting (`/o`) an empty slot:

```
Import Plugin Library "FileName.xml" At Plugin "" /o
```

## Curated

- Where a plugin runs (local vs master) depends on CmdLine / Macro / Cue Command — [`../multi-station.md`](../multi-station.md).
- Prefer **single-quoted** wrappers for JSON arguments; double-quoted wrappers break on embedded `"`.
- Near size limits, prefer `SendLuaMessage` / queues over stuffing huge args into `Cmd()`.
- Register hooks on startup / show load so every station’s VM is wired.
- Prove imports via DumpLog — [`remote-in-out.md`](remote-in-out.md).
