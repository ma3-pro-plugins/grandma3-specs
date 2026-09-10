# Agents

This repository is a grandMA3 reference for coding agents.

1. Open [`specs/versions.md`](specs/versions.md) first. That file states **Target** (the grandMA3 build Specs describe) and the Lua engine.
2. Open [INDEX.md](INDEX.md) and load only the file that matches the task.
3. Specs under `specs/*.md` and Keyword Specs under `specs/keywords/` describe **Target only** (latest adopted). They are rewritten in place when MA changes. Skills under `.agents/skills/` are procedures.
4. Command syntax: `specs/keywords/` is the **only** keyword tree (general + option). Each file is Official (from the manual) plus Extra (contributors). Do not look under `raw/` for keywords.
5. For Lua/API surface dumps, use the Help Dump whose version matches Target (today under `specs/lua-functions/`; see `versions.md`). Release notes are versioned under `specs/release-notes/`.
6. Open bugs that still affect Target live in `specs/ma-bugs.md`. Do not invent fixed-version behavior from stale Specs — use a git tag `ma-<version>` if you need the tree as it was when an older build was Target.
7. Do not write plugin or macro files until the user gives an absolute `gma3_library` path.
8. Do not guess station IPs. Default OSC to `127.0.0.1` unless the user names a host.

Versioning vocabulary and layout: [CONTEXT.md](CONTEXT.md).
