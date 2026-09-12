# GrandMA3 versions

**Target** (what Specs on `main` describe): **2.5.0.3**

- Lua engine on Target: **5.5.0**
- Last 2.4 line we keep dumps for: **2.4.2.2** (Lua 5.4.8)
- Git tag when this Target was adopted: `ma-2.5.0.3` (create/update the tag when adopting a release)

Agents must treat topic Specs and live Keyword Specs as truth for **Target** only. Older behavior is not mirrored in parallel Spec files — use a `ma-<version>` git tag or versioned Help Dumps. Keyword history is `introduced` / `deprecated` on each file; archived keywords live under [`keywords/archive/`](keywords/archive/).

## Matching references

| Kind | Path for Target |
| --- | --- |
| Keyword Specs (general + option) | [`keywords/`](keywords/) — only live dictionary; Official + Extra in each file |
| Archived keywords | [`keywords/archive/`](keywords/archive/) — gone from Target, or deprecated ≥ 24 months |
| Help Dump (current layout) | [`lua-functions/grandMA3_lua_functions 2.5.0.3.txt`](lua-functions/grandMA3_lua_functions%202.5.0.3.txt) |
| Lua Enums catalog (typings, MA 2.5.0.2) | [`enums/grandMA3_lua_enums 2.5.0.2.md`](enums/grandMA3_lua_enums%202.5.0.2.md) — how to use: [`enums.md`](enums.md) |
| Help Dump (intended layout) | `raw/2.5.0.3/lua-functions.txt` (not migrated yet) |
| Release notes (MD) | [`release-notes/Release_Notes_v2.5.0.3.md`](release-notes/Release_Notes_v2.5.0.3.md) |

Other Help Dumps in [`lua-functions/`](lua-functions/) are historical raw references, not the Spec baseline.

## Lua engine

Each station runs plugin code in its own Lua VM (see [`plugins.md`](plugins.md)).

| grandMA3 release | Lua version |
| --- | --- |
| **2.5.x** | **5.5.0** (MA: “Lua Core has been updated to Lua v5.5.0”) |
| **2.4.x** | **5.4.8** |
| Before 2.4.x | Earlier Lua 5.4.x (exact patch level not tracked here) |

Plugin TypeScript is still transpiled with TSTL’s Lua **5.4** emit, but it **runs** on the engine above. Breaking 5.4 → 5.5 behavior (immutable `for` control variables, `#` on sparse arrays): [`lua-5.4-to-5.5.md`](lua-5.4-to-5.5.md) (a **Migration Spec**, not a substitute for Target Specs).

## Adopting a new MA release

1. Set **Target** in this file (full `X.Y.Z.W` when known).
2. Add Help Dump + release-notes for that build.
3. Re-crawl general **and** option keywords into `keywords/` (replace Official, keep Extra; do not blank `introduced`).
4. Apply keyword lifecycle: set `deprecated` when known; move gone keywords and those deprecated ≥ 24 months into `keywords/archive/`.
5. Rewrite Specs that changed; refresh [`ma-bugs.md`](ma-bugs.md).
6. Tag `main` as `ma-X.Y.Z.W`.
