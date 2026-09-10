# External GitHub sources

Inventory of third-party repositories (and a few non-GitHub mirrors) that gather grandMA3 knowledge. Use this list later to extract and consolidate into `specs/`.

This file is a **source map**, not a Spec. Facts extracted from these repos should land in topic specs after verification against a target software version in `versions.md`.

Gathered: 2026-09-10. **Last commit** is the tip commit date on the default branch (not GitHub’s repo `updated_at`, which also moves on stars/wiki/issues). Confidence is about extractable docs, not code quality.

## Plugin / API / developer sources

| Repo | Stars | Last commit | Why useful | Confidence |
| --- | ---: | --- | --- | --- |
| [hossimo/GMA3Plugins](https://github.com/hossimo/GMA3Plugins) | 111 | 2024-05 | Plugins plus an [unofficial API documentation wiki](https://github.com/hossimo/GMA3Plugins/wiki) — long-running community Lua reference | high |
| [MacTirney/GrandMA3-API-Documentation](https://github.com/MacTirney/GrandMA3-API-Documentation) | 58 | 2024-03 | Structured Lua API docs: Object API / Object-Free API modules, helpful keywords, plugin basics under `Docs/` and `modules/` | high |
| [jefffarrow/grandMA3_lua_functions](https://github.com/jefffarrow/grandMA3_lua_functions) | 51 | 2026-04 | VS Code / LuaLS definition library of in-built functions and enums (HelpLua-style dump shaped for editors) | high |
| [DeeeLight/FromDarkToLightTutorials](https://github.com/DeeeLight/FromDarkToLightTutorials) | 41 | 2025-04 | Worked Lua tutorial examples from a YouTube series — good for patterns and teaching notes | medium |
| [patopesto/GrandMA3-Plugins](https://github.com/patopesto/GrandMA3-Plugins) | 20 | 2025-10 | Plugins + docs site; includes `APIDump` used to generate [grandma3.bambinito.net](https://grandma3.bambinito.net) Lua reference | high |
| [ma3-pro-plugins/grandma3-ts-types](https://github.com/ma3-pro-plugins/grandma3-ts-types) | 20 | 2026-08 | TypeScript definitions for the grandMA3 Lua API (org sibling) | high |
| [LightYourWay/grandMA3-types](https://github.com/LightYourWay/grandMA3-types) | 14 | 2026-07 | Earlier / alternate TS defs for the Lua API | medium |
| [ma3-pro-plugins/ma3-pro-plugins-lib](https://github.com/ma3-pro-plugins/ma3-pro-plugins-lib) | 14 | 2025-02 | TypeScript library for grandMA3 plugins (org sibling) | medium |
| [ma3-pro-plugins/ma3-ts-plugin-template](https://github.com/ma3-pro-plugins/ma3-ts-plugin-template) | 14 | 2024-11 | TS plugin template + build script (org sibling) | low (tooling) |
| [LightYourWay/grandMA3-cli-tools](https://github.com/LightYourWay/grandMA3-cli-tools) | 9 | 2026-07 | TS utilities aimed at making Lua easier for operators | medium |
| [apoxhu/MA3-Lua-API](https://github.com/apoxhu/MA3-Lua-API) | 8 | 2019-12 | Early unofficial Lua API documentation repo (thin README; check wiki/history) | medium |
| [MayBeLinux/requirements_Lua-grandMA3](https://github.com/MayBeLinux/requirements_Lua-grandMA3) | 3 | 2025-10 | "Requirements" / Lua defs shaped for grandMA3 | medium |
| [PeramatoG/gma3-lua-snippets](https://github.com/PeramatoG/gma3-lua-snippets) | 4 | 2025-12 | Reusable Lua snippets and components | medium |
| [enlore/grandma3-stuff](https://github.com/enlore/grandma3-stuff) | 3 | 2026-02 | Research notes: Lua, GDTF, media-server integration | medium |
| [imhofroger/GMA3_LUA](https://github.com/imhofroger/GMA3_LUA) | 48 | 2020-02 | Collection of Lua scripts — examples more than prose docs | low–medium |
| [bootsie123/ma3-plugin-action](https://github.com/bootsie123/ma3-plugin-action) | 7 | 2026-09 | GitHub Action that generates plugin XML — useful for packaging conventions | low (tooling) |
| [LightYourWay/grandMA3-tstl-plugin](https://github.com/LightYourWay/grandMA3-tstl-plugin) | 6 | 2026-06 | TypeScriptToLua export to grandMA3-compatible Lua | low (tooling) |
| [LightYourWay/grandMA3-plugin-starter](https://github.com/LightYourWay/grandMA3-plugin-starter) | 5 | 2026-07 | TS plugin starter project | low (tooling) |
| [ma3-pro-plugins/ma3-plugin-issues](https://github.com/ma3-pro-plugins/ma3-plugin-issues) | 3 | 2023-06 | Issue tracker / repro notes (org sibling) | medium |
| [ma3-pro-plugins/MA3ProPluginsPublic](https://github.com/ma3-pro-plugins/MA3ProPluginsPublic) | 6 | 2023-05 | Misc shared public material (org sibling) | low |

### Non-GitHub developer references tied to the above

- [grandma3.bambinito.net](https://grandma3.bambinito.net) — generated Lua API reference (from patopesto `APIDump`)
- [hossimo/GMA3Plugins wiki](https://github.com/hossimo/GMA3Plugins/wiki) — unofficial API wiki (wiki edits are not reflected in the Last commit column above)
- Official: [help.malighting.com grandMA3](https://help.malighting.com/grandMA3/) (Lua Object API, HelpLua, command keywords)

## Command syntax / OSC / user-oriented sources

True "command-line syntax" dumps on GitHub are thinner than plugin/API material. Best bets:

| Repo | Stars | Last commit | Why useful | Confidence |
| --- | ---: | --- | --- | --- |
| [MacTirney/GrandMA3-API-Documentation](https://github.com/MacTirney/GrandMA3-API-Documentation) (`Docs/Helpful Keywords.md`) | 58 | 2024-03 | Keyword list for Lua/`Lua` command-line use — overlaps user command vocabulary | high |
| [bitfocus/companion-module-malighting-grandma3](https://github.com/bitfocus/companion-module-malighting-grandma3) | 17 | 2026-09 | Companion actions encode many real console commands / OSC paths — good for mining syntax | medium |
| [yastefan/grandMA3-Chataigne-Module](https://github.com/yastefan/grandMA3-Chataigne-Module) | 36 | 2026-09 | OSC control surface for grandMA3 — command/OSC mapping examples | medium |
| [xxpasixx/pam-osc](https://github.com/xxpasixx/pam-osc) | 52 | 2025-11 | MIDI → Open Stage Control → grandMA3 with feedback plugin — OSC/command patterns | medium |
| [ArtGateOne/MA3_OSC_FEEDBACK](https://github.com/ArtGateOne/MA3_OSC_FEEDBACK) | 18 | 2023-06 | OSC feedback plugin | medium |
| [stoatworks-labs/mynah](https://github.com/stoatworks-labs/mynah) | 0 | 2026-09 | "grandMA3 grammar" applied to another product — interesting for how people model MA3 command grammar | low |
| [sonext-software/spresenter-plugin-grandma3](https://github.com/sonext-software/spresenter-plugin-grandma3) | 0 | 2026-08 | OSC automation nodes: cmdline, executors, faders, macros, sequences | medium |

Primary command-syntax source remains **official MA help** (Command Syntax and Keywords), not GitHub. Community repos mostly encode syntax indirectly via OSC modules, Companion actions, and macros.

## Adjacent (MA2, show files, low priority for extraction)

| Repo | Last commit | Notes |
| --- | --- | --- |
| [Hobadee/grandMA2_LUA_ldoc](https://github.com/Hobadee/grandMA2_LUA_ldoc) | 2023-03 | MA2 Lua LDoc — historical patterns only |
| [MacTirney/GrandMA2-API-Documentation](https://github.com/MacTirney/GrandMA2-API-Documentation) | 2024-03 | MA2 counterpart of the MA3 API docs |
| [aGuyNamedJonas/grandma2-snippets](https://github.com/aGuyNamedJonas/grandma2-snippets) | 2019-03 | MA2 macros/snippets |
| [FlorianANAYA/GrandMA2-help](https://github.com/FlorianANAYA/GrandMA2-help) | 2024-11 | MA2 programming tips / macros |
| [exscriber/Ma2-API](https://github.com/exscriber/Ma2-API) | 2025-03 | MA2 Lua typedefs |
| [MichaelGreenNZ/MG_MA3_StartShow](https://github.com/MichaelGreenNZ/MG_MA3_StartShow) | 2026-06 | Popular start-show file — little prose |
| Most `*Plugins` Lua repos (BakaCowpoke, 4ubiks, PeramatoG, etc.) | — | Example plugins; extract only when a behavior isn't documented elsewhere |

## Suggested next extractions (top 5)

1. **hossimo/GMA3Plugins wiki** — crawl wiki pages into draft topic notes; diff against existing `specs/` and Help Dumps. (Repo code last commit 2024-05; wiki may be newer.)
2. **MacTirney/GrandMA3-API-Documentation** — ingest `Docs/` + `modules/` Object / Object-Free docs; map each function to Help Dump + `object-api.md`. (Last commit 2024-03 — treat as dated relative to current MA.)
3. **patopesto / grandma3.bambinito.net** — compare generated API reference to our Help Dumps; note version skew. (Repo last commit 2025-10.)
4. **jefffarrow/grandMA3_lua_functions** `definitions/` — use as a cross-check for enums and free functions vs `specs/lua-functions/`. (Last commit 2026-04.)
5. **bitfocus Companion MA3 module + Chataigne/pam-osc** — mine command strings and OSC addresses to grow user-oriented command/OSC coverage beyond `specs/osc.md`. (Actively maintained 2025–2026.)

## Search notes

Queries used on GitHub (2026-09-10): `grandma3 lua`, `grandMA3 plugin`, `grandma3 documentation OR cheatsheet OR syntax OR commands`, org `ma3-pro-plugins`, plus README skims of the highest-star doc repos. Many hits are single-purpose plugins without extractable prose; they are omitted unless they encode OSC/command mappings or API dumps.

Last-commit audit: 2026-09-10 via `list_commits` (default branch tip) for every named repo in the tables above.
