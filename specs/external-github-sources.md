# External GitHub sources

Inventory of third-party repositories that gather grandMA3 knowledge. Use later to extract into `specs/`.

This is a **source map**, not a Spec. Verify anything extracted against the target software version in `versions.md` and against our Help Dumps under `specs/lua-functions/`.

**Last commit** = tip of the default branch (not GitHub `updated_at`).

**Audience**
- **Lua** — plugin / scripting developers
- **Operator** — console users who work in the command line, macros, playback, OSC — not writing Lua plugins

**Depth** (how much *new explanatory knowledge* we can extract)
- **prose** — written explanations, syntax notes, worked examples beyond a dump
- **typed-dump** — HelpLua / API list reshaped for an editor (EmmyLua / TypeScript). Little or no behavior text. Usually redundant with our Help Dumps
- **examples** — plugins/macros/scripts to reverse-engineer; little standalone docs
- **encoded** — knowledge buried in integration code (Companion actions, OSC maps)
- **empty** — claim without content

Gathered 2026-09-10; depth audit 2026-09-10.

---

## Lua / plugin audience

| Repo | Stars | Last commit | What's actually in it | Depth | Extract? |
| --- | ---: | --- | --- | --- | --- |
| [MacTirney/GrandMA3-API-Documentation](https://github.com/MacTirney/GrandMA3-API-Documentation) | 58 | 2024-03 | Markdown API reference: Object-Free + Object API with About / Syntax / Args / Return / example links; plus a short "Helpful Keywords" and "Basic Plugin Information". Content is largely official-help style, frozen around MA ~1.9 | prose (dated) | **Yes** — cross-check gaps vs official help + our dumps; do not treat as current |
| [hossimo/GMA3Plugins](https://github.com/hossimo/GMA3Plugins) | 111 | 2024-05 | Released Lua plugins in-repo; points to an [unofficial API wiki](https://github.com/hossimo/GMA3Plugins/wiki) (wiki edits ≠ git last commit) | prose (wiki) + examples | **Yes** — wiki first; plugins only when a behavior isn't documented elsewhere |
| [patopesto/GrandMA3-Plugins](https://github.com/patopesto/GrandMA3-Plugins) | 20 | 2025-10 | Plugins + `APIDump` tooling; generated site [grandma3.bambinito.net](https://grandma3.bambinito.net) claims Lua engine/API reference | prose (site) + examples | **Yes** — site reference vs our Help Dumps; note version skew |
| [DeeeLight/FromDarkToLightTutorials](https://github.com/DeeeLight/FromDarkToLightTutorials) | 41 | 2025-04 | Folder of Lua tutorial plugins ("Lua for GrandMA3", Custom UI, etc.) for a YouTube series — code samples, not a written API book | examples | Maybe — patterns / UI recipes, not reference |
| [PeramatoG/gma3-lua-snippets](https://github.com/PeramatoG/gma3-lua-snippets) | 4 | 2025-12 | Reusable Lua components (e.g. PIN keypad UI) | examples | Maybe — component patterns |
| [enlore/grandma3-stuff](https://github.com/enlore/grandma3-stuff) | 3 | 2026-02 | Short overview notes + GDTF media-server fixture example + AI-oriented `CLAUDE.md`. Notes mostly link out to official help / MacTirney / hossimo | thin prose | Low — little unique console knowledge |
| [imhofroger/GMA3_LUA](https://github.com/imhofroger/GMA3_LUA) | 48 | 2020-02 | Early Lua script collection | examples (stale) | Low |
| [ma3-pro-plugins/ma3-plugin-issues](https://github.com/ma3-pro-plugins/ma3-plugin-issues) | 3 | 2023-06 | Repro notes / issues for plugin edge cases (org sibling) | thin prose | Maybe — bug/behavior tickets |

### Typed dumps / IDE helpers (Lua audience — poor Spec sources)

These reshape HelpLua (or similar) into editor stubs. **We already keep versioned Help Dumps** — do not extract "docs" from these unless we need enum names or annotation quirks.

| Repo | Stars | Last commit | What's actually in it | Depth | Extract? |
| --- | ---: | --- | --- | --- | --- |
| [jefffarrow/grandMA3_lua_functions](https://github.com/jefffarrow/grandMA3_lua_functions) | 51 | 2026-04 | Only `definitions/grandMA3_lua_functions.lua` + `grandMA3_lua_enums.lua` — EmmyLua `---@` stubs from HelpLua; no per-function explanations | typed-dump | **No** for Specs (redundant with `specs/lua-functions/`) |
| [ma3-pro-plugins/grandma3-ts-types](https://github.com/ma3-pro-plugins/grandma3-ts-types) | 20 | 2026-08 | TypeScript `.d.ts` for the Lua API (org sibling) | typed-dump | No for Specs; useful for TS plugin builds |
| [LightYourWay/grandMA3-types](https://github.com/LightYourWay/grandMA3-types) | 14 | 2026-07 | Alternate / earlier TS defs | typed-dump | No for Specs |
| [MayBeLinux/requirements_Lua-grandMA3](https://github.com/MayBeLinux/requirements_Lua-grandMA3) | 3 | 2025-10 | Despite the name: vendored Lua libs (`socket`, `http`, `json`, debuggee, …) plus small `gma3_*.lua` helpers — not an API textbook | examples / libs | Low for Specs |
| [apoxhu/MA3-Lua-API](https://github.com/apoxhu/MA3-Lua-API) | 8 | 2019-12 | README one-liner only — no API pages in the repo | empty | **No** |

### Plugin tooling (Lua audience — packaging, not knowledge)

| Repo | Stars | Last commit | What's actually in it | Depth | Extract? |
| --- | ---: | --- | --- | --- | --- |
| [ma3-pro-plugins/ma3-pro-plugins-lib](https://github.com/ma3-pro-plugins/ma3-pro-plugins-lib) | 14 | 2025-02 | TS library for plugins | examples / lib | Low for Specs |
| [ma3-pro-plugins/ma3-ts-plugin-template](https://github.com/ma3-pro-plugins/ma3-ts-plugin-template) | 14 | 2024-11 | TS plugin template | tooling | No |
| [LightYourWay/grandMA3-cli-tools](https://github.com/LightYourWay/grandMA3-cli-tools) | 9 | 2026-07 | TS utilities around Lua workflows | tooling | Low |
| [LightYourWay/grandMA3-tstl-plugin](https://github.com/LightYourWay/grandMA3-tstl-plugin) | 6 | 2026-06 | TypeScriptToLua → MA3 Lua | tooling | No |
| [LightYourWay/grandMA3-plugin-starter](https://github.com/LightYourWay/grandMA3-plugin-starter) | 5 | 2026-07 | TS starter | tooling | No |
| [bootsie123/ma3-plugin-action](https://github.com/bootsie123/ma3-plugin-action) | 7 | 2026-09 | GitHub Action → plugin XML | tooling | Maybe packaging conventions only |
| [ma3-pro-plugins/MA3ProPluginsPublic](https://github.com/ma3-pro-plugins/MA3ProPluginsPublic) | 6 | 2023-05 | Misc shared bits | mixed | Low |

---

## Operator / non-Lua audience

Console command syntax, macros, playback, OSC — useful without writing plugins. GitHub is weak here; **official MA help (Command Syntax and Keywords)** remains the primary source.

| Repo | Stars | Last commit | What's actually in it | Depth | Extract? |
| --- | ---: | --- | --- | --- | --- |
| [MacTirney/GrandMA3-API-Documentation](https://github.com/MacTirney/GrandMA3-API-Documentation) `Docs/Helpful Keywords.md` | 58 | 2024-03 | Small set of keywords (Lua, LuaFile, HelpLua, Mode2 switch, GetUser/GlobalVariable) with syntax/examples; then links to official keyword lists | thin prose | Low — incomplete; prefer official keyword chapters |
| [bitfocus/companion-module-malighting-grandma3](https://github.com/bitfocus/companion-module-malighting-grandma3) | 17 | 2026-09 | Companion module: `src/actions.ts` etc. encode real console commands / OSC for buttons | encoded | **Yes** — mine action strings for command/OSC coverage |
| [yastefan/grandMA3-Chataigne-Module](https://github.com/yastefan/grandMA3-Chataigne-Module) | 36 | 2026-09 | Chataigne ↔ grandMA3 OSC control (updated for 2.5 pools) | encoded | **Yes** — OSC/command maps |
| [xxpasixx/pam-osc](https://github.com/xxpasixx/pam-osc) | 52 | 2025-11 | MIDI → Open Stage Control → MA3 + feedback plugin | encoded + examples | **Yes** — OSC/feedback patterns |
| [ArtGateOne/MA3_OSC_FEEDBACK](https://github.com/ArtGateOne/MA3_OSC_FEEDBACK) | 18 | 2023-06 | OSC feedback plugin | examples | Maybe |
| [sonext-software/spresenter-plugin-grandma3](https://github.com/sonext-software/spresenter-plugin-grandma3) | 0 | 2026-08 | Spresenter nodes: cmdline, executors, faders, macros, sequences over OSC | encoded | Maybe |
| [stoatworks-labs/mynah](https://github.com/stoatworks-labs/mynah) | 0 | 2026-09 | Uses "grandMA3 grammar" for a video switcher CLI — not MA docs | n/a | **No** for Specs |

---

## Adjacent (MA2 / show files — low priority)

| Repo | Last commit | Audience | Notes |
| --- | --- | --- | --- |
| [Hobadee/grandMA2_LUA_ldoc](https://github.com/Hobadee/grandMA2_LUA_ldoc) | 2023-03 | Lua (MA2) | Historical LDoc only |
| [MacTirney/GrandMA2-API-Documentation](https://github.com/MacTirney/GrandMA2-API-Documentation) | 2024-03 | Lua (MA2) | MA2 counterpart |
| [aGuyNamedJonas/grandma2-snippets](https://github.com/aGuyNamedJonas/grandma2-snippets) | 2019-03 | Operator (MA2) | Macros/snippets |
| [FlorianANAYA/GrandMA2-help](https://github.com/FlorianANAYA/GrandMA2-help) | 2024-11 | Operator (MA2) | Programming tips / macros |
| [exscriber/Ma2-API](https://github.com/exscriber/Ma2-API) | 2025-03 | Lua (MA2) | Typedefs |
| [MichaelGreenNZ/MG_MA3_StartShow](https://github.com/MichaelGreenNZ/MG_MA3_StartShow) | 2026-06 | Operator | Popular show file — almost no prose |

---

## Suggested next extractions (revised)

1. **hossimo wiki** — only if pages still have unique behavior notes after skimming; git tree alone is mostly plugins.
2. **MacTirney Object-Free / Object API Markdown** — diff against official help + Help Dumps for gaps; mark version (~1.9).
3. **patopesto / bambinito Lua reference** — compare to current Help Dumps.
4. **Companion + Chataigne + pam-osc** — mine command/OSC strings for operator-facing `specs/` (biggest non-Lua GitHub signal).
5. **Skip** jefffarrow, apoxhu, TS type packages, and mynah as Spec sources.

## Audit notes

- **jefffarrow**: confirmed stubs only (`---@param` / `function Foo() end`), no narrative docs — matches user observation; demoted from extract candidate.
- **apoxhu**: empty beyond README claim.
- **MayBeLinux "requirements"**: not HelpLua docs; mostly third-party Lua libraries.
- **Operator knowledge on GitHub** is mostly *encoded* in show-control integrations, not cheatsheets.
