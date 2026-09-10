# External GitHub sources

Inventory of third-party repositories that gather **grandMA3** knowledge. Use later to extract into `specs/`.

This is a **source map**, not a Spec. Verify anything extracted against the target software version in `versions.md` and against our Help Dumps under `specs/lua-functions/`.

**Scope:** grandMA3 only. Do **not** list grandMA2 / MA2 repositories.

**Last commit** = tip of the default branch (not GitHub `updated_at`).

**Ranking**
1. Active knowledge sources (last commit within ~1 year) — Lua / operator tables first
2. Active typed-dumps and tooling (IDE / packaging helpers)
3. **Lua plugin example references** — low impact; sample plugins only, not Spec material
4. **Stale** (last commit older than 1 year) — always at the bottom; treat as **low confidence** even if prose once looked good

**Audience**
- **Lua** — plugin / scripting developers
- **Operator** — command line, macros, playback, OSC — not writing Lua plugins

**Depth**
- **prose** — written explanations beyond a dump
- **typed-dump** — HelpLua reshaped for an editor; usually redundant with our Help Dumps
- **examples** — plugins/scripts to reverse-engineer
- **encoded** — knowledge buried in integration code
- **empty** — claim without content

Cutoff for “stale”: last commit before **2025-09-10** (audit 2026-09-10). Never re-add `MayBeLinux/requirements_Lua-grandMA3` (vendored Lua libs, not docs).

---

## Lua / plugin — active knowledge

| Repo | Stars | Last commit | What's actually in it | Depth | Extract? |
| --- | ---: | --- | --- | --- | --- |
| [patopesto/GrandMA3-Plugins](https://github.com/patopesto/GrandMA3-Plugins) | 20 | 2025-10 | Plugins + `APIDump`; generated site [grandma3.bambinito.net](https://grandma3.bambinito.net) claims Lua engine/API reference | prose (site) + examples | **Yes** — site vs Help Dumps; note version skew |
| [enlore/grandma3-stuff](https://github.com/enlore/grandma3-stuff) | 3 | 2026-02 | Short overview + GDTF example + `CLAUDE.md`; mostly links to official help / MacTirney / hossimo | thin prose | Low |
| [ma3-pro-plugins/ma3-plugin-issues](https://github.com/ma3-pro-plugins/ma3-plugin-issues) | 3 | 2023-06 | *(moved — see Stale)* | — | — |

*(Only rows with last commit ≥ 2025-09 stay here. `ma3-plugin-issues` is stale — listed only under Stale below.)*

Wait — I should not leave a placeholder row. Fix the table to only patopesto and enlore.

