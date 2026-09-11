---
title: Plugins & Lua
source: mixed
---

# Plugins & Lua

Plugins are show objects in the **Plugins** pool (inside a DataPool). Each station runs plugin code in its **own Lua VM** against the shared object model.

## Depth Specs

| Topic Spec | Covers |
| --- | --- |
| [`../plugins.md`](../plugins.md) | Lifecycle, where `Plugin N` runs, ~16K Cmd string limit, quoting JSON args |
| [`../object-api.md`](../object-api.md) | How to pick Help Dumps / API surface |
| [`../hooks.md`](../hooks.md) | Hooks (incl. Group vs Universal SpecialPurpose) |
| [`../message-queue.md`](../message-queue.md) | `OpenMessageQueue` / `SendLuaMessage` |
| [`../addonvars.md`](../addonvars.md) | AddonVariables |
| [`../lua-5.4-to-5.5.md`](../lua-5.4-to-5.5.md) | Migration Spec (2.4→2.5 engine) |

Target Lua version: [`../versions.md`](../versions.md).

## Calling plugins from the CLI

```text
Plugin 1
Call Plugin "MyPlugin" '{\"ok\":true}'
```

- Where a plugin runs (local vs master) depends on CmdLine / Macro / Cue Command — [`../multi-station.md`](../multi-station.md).
- Prefer **single-quoted** wrappers for JSON arguments; double-quoted wrappers break on embedded `"` — plugins Spec.
- Near size limits, prefer `SendLuaMessage` / queues over stuffing huge args into `Cmd()`.

## Hooks & startup

Register hooks on startup / show load so every station’s VM is wired (each station has its own Lua VM — [`../multi-station.md`](../multi-station.md)). Exact APIs: Help Dump for Target + hooks Spec.

## Import

```text
Import Plugin Library "FileName.xml" At Plugin "" /o
```

Prove via DumpLog (`OK:` / `Failed:`) — [`osc-remote.md`](osc-remote.md).
