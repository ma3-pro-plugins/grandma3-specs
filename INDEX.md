# INDEX

Open the smallest file that fits the task. Specs are facts for **Target**. Skills are procedures.

**Target** (read first): [`specs/versions.md`](specs/versions.md) — Specs on `main` always describe that build. Versioning rules: [`CONTEXT.md`](CONTEXT.md).

## Skills

- Use this repo as a reference (consume): [`.agents/skills/use-specs/SKILL.md`](.agents/skills/use-specs/SKILL.md)
- Contribute Specs / concepts / rules: [`.agents/skills/contribute-specs/SKILL.md`](.agents/skills/contribute-specs/SKILL.md)
- Ingest log / source queues (do not re-extract): [`.agents/ingest/`](.agents/ingest/)
- Consume vs contribute rules: [`.agents/rules/consume.md`](.agents/rules/consume.md), [`.agents/rules/contribute.md`](.agents/rules/contribute.md)
- Crawl general/option keywords from the HTML manual into Keyword Specs: [`.agents/skills/crawl-keywords/SKILL.md`](.agents/skills/crawl-keywords/SKILL.md)
- Adopt a new grandMA3 software release (Target bump, release notes, keyword re-crawl, tag): [`.agents/skills/adopt-ma-release/SKILL.md`](.agents/skills/adopt-ma-release/SKILL.md)
- Convert an official release-notes PDF to searchable Markdown: [`.agents/skills/convert-release-notes/SKILL.md`](.agents/skills/convert-release-notes/SKILL.md)
- Commit changes (message, file kinds, hierarchy): [`.agents/skills/commit/SKILL.md`](.agents/skills/commit/SKILL.md)
- Send OSC, prove it landed, dump logs: [`.agents/skills/ma3-osc/SKILL.md`](.agents/skills/ma3-osc/SKILL.md)
- Write a standalone Lua plugin XML + Lua: [`.agents/skills/write-plugin/SKILL.md`](.agents/skills/write-plugin/SKILL.md)
- Write a macro XML file: [`.agents/skills/write-macro/SKILL.md`](.agents/skills/write-macro/SKILL.md)

## Specs — start here

- System map (manual TOC chapters): [`specs/concepts/_index.md`](specs/concepts/_index.md)
- Current Target software / Lua engine: [`specs/versions.md`](specs/versions.md)
- Command-line grammar (compose tokens): [`specs/command-line.md`](specs/command-line.md)
- Automation (macros / plugins / OSC, `/NoConfirmation`): [`specs/automation.md`](specs/automation.md)
- Groups (selection store, merge/remove/overwrite): [`specs/groups.md`](specs/groups.md)
- Layouts (assign/clone, elements, viewer): [`specs/layouts.md`](specs/layouts.md)
- Command-line keywords (general + option; Official + Extra): [`specs/keywords/_index.md`](specs/keywords/_index.md)
- OSC input (`/gma3/cmd`), DumpLog, import, Echo proof, session master from logs: [`specs/osc.md`](specs/osc.md)
- Official Help Dumps and how to pick one: [`specs/object-api.md`](specs/object-api.md)
- Plugin lifecycle (Lua VM, ReloadUI, signalTable, show load): [`specs/plugins.md`](specs/plugins.md)
- Plugin dialogs (MessageBox vs custom DialogFrame UI): [`specs/plugin-dialogs.md`](specs/plugin-dialogs.md)
- Plugin access (read objects: GetObject / ObjectList / Get / parent-children): [`specs/plugin-access.md`](specs/plugin-access.md)
- Lua Enums (`Enums.Name.Member` catalog): [`specs/enums.md`](specs/enums.md)
- RemoteCommand behavior and quoting: [`specs/remote-command.md`](specs/remote-command.md)

## Specs — by topic

- Lua 5.4 → 5.5 / grandMA3 2.4 → 2.5 (`for` vars, `#` holes) — Migration Spec: [`specs/lua-5.4-to-5.5.md`](specs/lua-5.4-to-5.5.md)
- Multi-station (sessions, master, where commands run): [`specs/multi-station.md`](specs/multi-station.md)
- DMXRemote / Agenda startup: [`specs/startup-dmxremote-agenda.md`](specs/startup-dmxremote-agenda.md)
- Hooks (including Group hooks vs Universal SpecialPurpose): [`specs/hooks.md`](specs/hooks.md)
- Network/session object API (MAnetSocket / HostTypes): [`specs/api-objects-network.md`](specs/api-objects-network.md)
- AddonVariables (AddonVars): [`specs/addonvars.md`](specs/addonvars.md)
- Hardware executor layout: [`specs/hardware-layout.md`](specs/hardware-layout.md)
- Known MA bugs (open on Target): [`specs/ma-bugs.md`](specs/ma-bugs.md)
- Lua message queues (`OpenMessageQueue` / `SendLuaMessage`): [`specs/message-queue.md`](specs/message-queue.md)
- UserAttributePreferences EncoderResolution: [`specs/user-attribute-encoder-resolution.md`](specs/user-attribute-encoder-resolution.md)
- PhaserRecipe (MA ≥ 2.4): [`specs/phaser-recipe.md`](specs/phaser-recipe.md)
- Phasers (programmer steps, effects alias, store like a static look): [`specs/phasers.md`](specs/phasers.md)


## Specs — concept hubs (one Topic Spec per manual hub)

Thin concept pages stay under [`specs/concepts/`](specs/concepts/). Depth for hubs that have manual subtopics:

- System: [`specs/system.md`](specs/system.md)
- Show file handling: [`specs/show-file-handling.md`](specs/show-file-handling.md)
- Users: [`specs/users.md`](specs/users.md)
- DMX: [`specs/dmx.md`](specs/dmx.md)
- Patch: [`specs/patch.md`](specs/patch.md)
- Operate fixtures: [`specs/operate-fixtures.md`](specs/operate-fixtures.md)
- Programmer (layers): [`specs/programmer.md`](specs/programmer.md)
- Presets: [`specs/presets.md`](specs/presets.md)
- Worlds / Filters: [`specs/worlds-filters.md`](specs/worlds-filters.md)
- MAtricks: [`specs/matricks.md`](specs/matricks.md)
- Cues and Sequences: [`specs/cues-sequences.md`](specs/cues-sequences.md)
- Executors (behavior): [`specs/executors.md`](specs/executors.md)
- Masters: [`specs/masters.md`](specs/masters.md)
- Recipes (standard; PhaserRecipe stays separate): [`specs/recipes.md`](specs/recipes.md)
- Phasers (programmer; PhaserRecipe stays separate): [`specs/phasers.md`](specs/phasers.md)
- Macros: [`specs/macros.md`](specs/macros.md)
- Agenda: [`specs/agenda.md`](specs/agenda.md)
- Timecode: [`specs/timecode.md`](specs/timecode.md)
- Quickeys: [`specs/quickeys.md`](specs/quickeys.md)

Already listed above: [`specs/groups.md`](specs/groups.md), [`specs/layouts.md`](specs/layouts.md), [`specs/automation.md`](specs/automation.md).

## Sources

- External GitHub inventory: [`specs/external-github-sources.md`](specs/external-github-sources.md)
- Help Dumps (match Target in [`versions.md`](specs/versions.md)): [`specs/lua-functions/`](specs/lua-functions/)
- Release-notes Markdown (grep/diff): [`specs/release-notes/`](specs/release-notes/)
- Original release-notes PDFs: [`specs/release-notes-pdf/`](specs/release-notes-pdf/)
