# External GitHub sources

Inventory of third-party repositories that gather **grandMA3** knowledge. Use later to extract into `specs/`.

This is a **source map**, not a Spec. Verify anything extracted against the target software version in `versions.md` and against our Help Dumps under `specs/lua-functions/`.

**Scope:** grandMA3 only. Do **not** list grandMA2 / MA2 repositories.

**Last commit** = tip of the default branch (not GitHub `updated_at`).

**Ranking**
1. Active knowledge sources (last commit within ~1 year)
2. Active typed-dumps and tooling
3. **Lua plugin example references** — low impact; sample plugins, not Spec material
4. **Stale** (last commit older than 1 year) — bottom of file; **low confidence** even if the prose once looked strong

**Audience:** **Lua** = plugin developers · **Operator** = command line / macros / playback / OSC

**Depth:** prose · typed-dump · examples · encoded · empty

Stale cutoff: last commit before **2025-09-10** (audit **2026-09-10**). Do not list `MayBeLinux/requirements_Lua-grandMA3` (garbage: vendored Lua libs, not docs).

---

## Lua / plugin — active knowledge

| Repo | Stars | Last commit | What's actually in it | Depth | Extract? |
| --- | ---: | --- | --- | --- | --- |
| [patopesto/GrandMA3-Plugins](https://github.com/patopesto/GrandMA3-Plugins) | 20 | 2025-10 | Plugins + `APIDump`; site [grandma3.bambinito.net](https://grandma3.bambinito.net) claims Lua engine/API reference | prose (site) + examples | **Yes** — site vs Help Dumps; note version skew |
| [enlore/grandma3-stuff](https://github.com/enlore/grandma3-stuff) | 3 | 2026-02 | Short overview + GDTF example + `CLAUDE.md`; mostly outbound links | thin prose | Low |

---

## Operator / non-Lua — active

Official MA help remains the primary command-syntax source. GitHub signal here is mostly encoded in integrations.

| Repo | Stars | Last commit | What's actually in it | Depth | Extract? |
| --- | ---: | --- | --- | --- | --- |
| [bitfocus/companion-module-malighting-grandma3](https://github.com/bitfocus/companion-module-malighting-grandma3) | 17 | 2026-09 | Companion `src/actions.ts` encodes console commands / OSC | encoded | **Yes** — mine action strings |
| [yastefan/grandMA3-Chataigne-Module](https://github.com/yastefan/grandMA3-Chataigne-Module) | 36 | 2026-09 | Chataigne ↔ MA3 OSC (2.5 pool updates) | encoded | **Yes** — OSC/command maps |
| [xxpasixx/pam-osc](https://github.com/xxpasixx/pam-osc) | 52 | 2025-11 | MIDI → Open Stage Control → MA3 + feedback plugin | encoded + examples | **Yes** — OSC/feedback patterns |
| [sonext-software/spresenter-plugin-grandma3](https://github.com/sonext-software/spresenter-plugin-grandma3) | 0 | 2026-08 | Spresenter OSC nodes: cmdline, executors, faders, macros, sequences | encoded | Maybe |
| [stoatworks-labs/mynah](https://github.com/stoatworks-labs/mynah) | 0 | 2026-09 | “grandMA3 grammar” for a video switcher — not MA docs | n/a | **No** |

---

## Typed dumps / IDE helpers — active (poor Spec sources)

HelpLua-shaped stubs. We already keep versioned Help Dumps — do not extract Specs from these.

| Repo | Stars | Last commit | What's actually in it | Depth | Extract? |
| --- | ---: | --- | --- | --- | --- |
| [jefffarrow/grandMA3_lua_functions](https://github.com/jefffarrow/grandMA3_lua_functions) | 51 | 2026-04 | EmmyLua `---@` stubs + enums only; no function narratives | typed-dump | **No** |
| [ma3-pro-plugins/grandma3-ts-types](https://github.com/ma3-pro-plugins/grandma3-ts-types) | 20 | 2026-08 | TypeScript `.d.ts` for Lua API | typed-dump | No for Specs |
| [LightYourWay/grandMA3-types](https://github.com/LightYourWay/grandMA3-types) | 14 | 2026-07 | Alternate TS defs | typed-dump | No for Specs |

---

## Plugin tooling — active (packaging, not knowledge)

| Repo | Stars | Last commit | What's actually in it | Depth | Extract? |
| --- | ---: | --- | --- | --- | --- |
| [LightYourWay/grandMA3-cli-tools](https://github.com/LightYourWay/grandMA3-cli-tools) | 9 | 2026-07 | TS utilities around Lua workflows | tooling | Low |
| [LightYourWay/grandMA3-tstl-plugin](https://github.com/LightYourWay/grandMA3-tstl-plugin) | 6 | 2026-06 | TypeScriptToLua → MA3 Lua | tooling | No |
| [LightYourWay/grandMA3-plugin-starter](https://github.com/LightYourWay/grandMA3-plugin-starter) | 5 | 2026-07 | TS starter | tooling | No |
| [bootsie123/ma3-plugin-action](https://github.com/bootsie123/ma3-plugin-action) | 7 | 2026-09 | GitHub Action → plugin XML | tooling | Maybe packaging only |

---

## Lua plugin example references (low impact)

Specific plugins / tutorial sample packs. Useful to peek at when hunting a pattern — **not** primary Spec sources.

| Repo | Stars | Last commit | Notes |
| --- | ---: | --- | --- |
| [PeramatoG/gma3-lua-snippets](https://github.com/PeramatoG/gma3-lua-snippets) | 4 | 2025-12 | Reusable UI/components (e.g. PIN keypad) |
| [patopesto/GrandMA3-Plugins](https://github.com/patopesto/GrandMA3-Plugins) (plugin folders) | 20 | 2025-10 | ViewScaler / ScreenSwap / TimecodeExporter / templates — knowledge value is the site, not these plugins alone |

---

## Stale (last commit &gt; 1 year) — low confidence

Do not treat as current. Prefer official help + our Help Dumps. Listed only so we remember they exist.

| Repo | Stars | Last commit | Audience | What's actually in it | Depth | Extract? |
| --- | ---: | --- | --- | --- | --- | --- |
| [hossimo/GMA3Plugins](https://github.com/hossimo/GMA3Plugins) | 111 | 2024-05 | Lua | Plugins + [API wiki](https://github.com/hossimo/GMA3Plugins/wiki) (wiki may move without git commits) | prose (wiki) + examples | Low (dated) — skim wiki only for unique notes |
| [MacTirney/GrandMA3-API-Documentation](https://github.com/MacTirney/GrandMA3-API-Documentation) | 58 | 2024-03 | Lua (+ thin operator keywords) | Markdown Object-Free / Object API (~MA 1.9 era) + small keyword page | prose (dated) | Low (dated) — gap-check only |
| [DeeeLight/FromDarkToLightTutorials](https://github.com/DeeeLight/FromDarkToLightTutorials) | 41 | 2025-04 | Lua examples | YouTube-series Lua sample plugins | examples | Low |
| [imhofroger/GMA3_LUA](https://github.com/imhofroger/GMA3_LUA) | 48 | 2020-02 | Lua examples | Early script collection | examples | Low |
| [ArtGateOne/MA3_OSC_FEEDBACK](https://github.com/ArtGateOne/MA3_OSC_FEEDBACK) | 18 | 2023-06 | Operator / examples | OSC feedback plugin | examples | Low |
| [ma3-pro-plugins/ma3-pro-plugins-lib](https://github.com/ma3-pro-plugins/ma3-pro-plugins-lib) | 14 | 2025-02 | Lua tooling | TS plugin library | lib | Low |
| [ma3-pro-plugins/ma3-ts-plugin-template](https://github.com/ma3-pro-plugins/ma3-ts-plugin-template) | 14 | 2024-11 | Lua tooling | TS template | tooling | No |
| [ma3-pro-plugins/MA3ProPluginsPublic](https://github.com/ma3-pro-plugins/MA3ProPluginsPublic) | 6 | 2023-05 | mixed | Misc shared bits | mixed | Low |
| [ma3-pro-plugins/ma3-plugin-issues](https://github.com/ma3-pro-plugins/ma3-plugin-issues) | 3 | 2023-06 | Lua | Old plugin edge-case notes | thin prose | Low |
| [apoxhu/MA3-Lua-API](https://github.com/apoxhu/MA3-Lua-API) | 8 | 2019-12 | Lua | README claim only — empty | empty | **No** |

---

## Suggested next extractions

1. **patopesto / bambinito** Lua reference — compare to current Help Dumps (only active prose-ish candidate).
2. **Companion + Chataigne + pam-osc** — mine command/OSC for operator-facing specs.
3. Optionally skim **hossimo wiki** / **MacTirney** for unique notes, but treat as low-confidence / dated.
4. **Skip** jefffarrow, apoxhu, TS type packages, mynah, and plugin-only example packs as Spec sources.
