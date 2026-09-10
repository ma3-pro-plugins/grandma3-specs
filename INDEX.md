# INDEX

Open the smallest file that fits the task. Specs are facts. Skills are procedures.

## Skills

- Convert an official release-notes PDF to searchable Markdown: [`.agents/skills/convert-release-notes/SKILL.md`](.agents/skills/convert-release-notes/SKILL.md)
- Commit changes (message, file kinds, hierarchy): [`.agents/skills/commit/SKILL.md`](.agents/skills/commit/SKILL.md)
- Send OSC, prove it landed, dump logs: [`.agents/skills/ma3-osc/SKILL.md`](.agents/skills/ma3-osc/SKILL.md)
- Write a standalone Lua plugin XML + Lua: [`.agents/skills/write-plugin/SKILL.md`](.agents/skills/write-plugin/SKILL.md)
- Write a macro XML file: [`.agents/skills/write-macro/SKILL.md`](.agents/skills/write-macro/SKILL.md)

## Specs — start here

- Current target software / Lua engine version: [`specs/versions.md`](specs/versions.md)
- OSC input (`/gma3/cmd`), DumpLog, import, Echo proof, session master from logs: [`specs/osc.md`](specs/osc.md)
- Official Help Dumps and how to pick one: [`specs/object-api.md`](specs/object-api.md)
- Plugin lifecycle (Lua VM, ReloadUI, signalTable, show load): [`specs/plugins.md`](specs/plugins.md)
- RemoteCommand behavior and quoting: [`specs/remote-command.md`](specs/remote-command.md)

## Specs — by topic

- Lua 5.4 → 5.5 / grandMA3 2.4 → 2.5 (`for` vars, `#` holes): [`specs/lua-5.4-to-5.5.md`](specs/lua-5.4-to-5.5.md)
- Sessions / master election / show sync: [`specs/multi-station-sessions.md`](specs/multi-station-sessions.md)
- DMXRemote / Agenda startup: [`specs/startup-dmxremote-agenda.md`](specs/startup-dmxremote-agenda.md)
- Hooks (including Group hooks vs Universal SpecialPurpose): [`specs/hooks.md`](specs/hooks.md)
- Network/session object API (MAnetSocket / HostTypes): [`specs/api-objects-network.md`](specs/api-objects-network.md)
- AddonVariables (AddonVars): [`specs/addonvars.md`](specs/addonvars.md)
- Hardware executor layout: [`specs/hardware-layout.md`](specs/hardware-layout.md)
- Known MA bugs: [`specs/ma-bugs.md`](specs/ma-bugs.md)
- Lua message queues (`OpenMessageQueue` / `SendLuaMessage`): [`specs/message-queue.md`](specs/message-queue.md)
- UserAttributePreferences EncoderResolution: [`specs/user-attribute-encoder-resolution.md`](specs/user-attribute-encoder-resolution.md)
- PhaserRecipe (MA ≥ 2.4): [`specs/phaser-recipe.md`](specs/phaser-recipe.md)

## Sources

- External GitHub inventory (for future extraction): [`specs/external-github-sources.md`](specs/external-github-sources.md)
- Help Dumps (pick the suffix that matches [`versions.md`](specs/versions.md)): [`specs/lua-functions/`](specs/lua-functions/)
- Release-notes Markdown (grep/diff): [`specs/release-notes/`](specs/release-notes/)
- Original release-notes PDFs: [`specs/release-notes-pdf/`](specs/release-notes-pdf/)
