# grandma3-specs

Unofficial notes on how grandMA3 behaves, written so any AI agent or coding agent can understand the console well enough to answer questions, solve problems, and help with command syntax or general troubleshooting.

This is not affiliated with MA Lighting. Agents should start at [INDEX.md](INDEX.md) — that map is the AI-friendly entry point.

## Who it is for

The specs are written **by** AI agents, in a form other agents can load and follow, and **for** AI agents to consume while they work with a user.

The first material was gathered while developing plugins, so the repo is still more **plugin-oriented**. The hope is that contributions will also grow a **user-oriented** layer (programming, playback, syntax, troubleshooting) over time.

## Skills

Besides the topic files under `specs/`, this repo ships Agent Skills (`.agents/skills/`) that an agent can run:

- **[write-plugin](.agents/skills/write-plugin/SKILL.md)** — create standalone Lua plugin XML and Lua in the user’s `gma3_library`.
- **[write-macro](.agents/skills/write-macro/SKILL.md)** — create macro XML in the user’s `gma3_library`.
- **[ma3-osc](.agents/skills/ma3-osc/SKILL.md)** — talk to a running onPC over OSC (UDP command input). An agent can use this repo not only to *explain* grandMA3, but to **build the solution in the user’s show file** (import a plugin, write a macro, send `Call Plugin` / `Lua` / other commands) when OSC is enabled.

Maintainer skills: [convert-release-notes](.agents/skills/convert-release-notes/SKILL.md) turns official release-note PDFs into searchable Markdown under `specs/release-notes/`; [commit](.agents/skills/commit/SKILL.md) checks file kinds and hierarchy before committing.
