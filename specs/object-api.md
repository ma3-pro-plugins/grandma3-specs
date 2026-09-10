# Object API

Plugins interact with the grandMA3 object tree and global Lua API (handles, properties, methods, hooks, and related helpers). These docs describe parts of that surface from experience and testing.

Narrative Specs here follow **Target** in [`versions.md`](versions.md) (latest adopted build). They are not a second copy of the Help Dump.

**TypeScript typings** — Community packages such as `grandma3-ts-types` declare grandMA3 globals for TypeScript-to-Lua. They are **not maintained by MA Lighting** and can drift from a given console build. Treat them as a guide, not an authoritative contract.

**Official per-version Help Dumps** — Under [`lua-functions/`](lua-functions/) we keep text exports of the console’s built-in Lua/API help (one file per software version; the filename ends with the version, e.g. `grandMA3_lua_functions 2.5.0.3.txt`). Those come from MA’s `HelpLua` command and are the best single-file raw reference for what a given release documents. Intended layout later: `raw/<version>/lua-functions.txt`.

**Official command keywords (General Keywords)** — MA Lighting’s grandMA3 User Manual lists every keyword alphabetically (syntax, definitions, examples): [General Keywords (grandMA3 2.3)](https://help.malighting.com/grandMA3/2.3/HTML/csk_general_keywords.html). Prefer the manual version that matches Target when extracting.

**Which file to open** — Read Target from [`versions.md`](versions.md). Use the `grandMA3_lua_functions X.X.X.X.txt` whose version suffix equals Target (or the closest available dump if a brand-new patch is not exported yet).

**PhaserRecipe (MA ≥ 2.4)** — Cue-part/preset phaser recipes, named addressing, value sources, presets as step values, `<From Preset>` attributes: [`phaser-recipe.md`](phaser-recipe.md).
