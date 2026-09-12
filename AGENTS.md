# Agents

This repository is a grandMA3 reference for coding agents.

**Consuming** Specs (write OSC/macros/Lua): follow [`.agents/rules/consume.md`](.agents/rules/consume.md) and skill [use-specs](.agents/skills/use-specs/SKILL.md).

**Contributing** Specs (edit this repo): follow [`.agents/rules/contribute.md`](.agents/rules/contribute.md) and skill [contribute-specs](.agents/skills/contribute-specs/SKILL.md).

## Consume checklist

1. Open [`specs/versions.md`](specs/versions.md) first (Target + Lua engine).
2. Open [INDEX.md](INDEX.md) and load only the file that matches the task.
3. Unfamiliar subsystem → [`specs/concepts/`](specs/concepts/) (thin map + pointers). Depth is in flat Topic Specs under `specs/*.md`.
4. Multi-station / master / where commands run → [`specs/multi-station.md`](specs/multi-station.md).
5. Unattended automation (macro / plugin `Cmd` / OSC) → [`specs/automation.md`](specs/automation.md) (`/NoConfirmation`).
6. Read show objects from Lua (`GetObject` / `ObjectList` / `:Get` / parent-children) → [`specs/plugin-access.md`](specs/plugin-access.md).
7. Specs under `specs/*.md` and Keyword Specs under `specs/keywords/` describe **Target only**. Skills under `.agents/skills/` are procedures.
8. Command syntax: `specs/keywords/` is the **only** keyword tree. Skip `archive/` for new commands. Honor `deprecated`.
9. Help Dump for Target: see `versions.md`. Open bugs: `specs/ma-bugs.md`.
10. Do not write plugin or macro files until the user gives an absolute `gma3_library` path.
11. Do not guess station IPs. Default OSC to `127.0.0.1` unless the user names a host.

Versioning vocabulary and layout: [CONTEXT.md](CONTEXT.md). Provenance `source`: `manual` | `observed` | `lab` | `mixed`.
