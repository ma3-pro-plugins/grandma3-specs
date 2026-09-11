# Rules: consuming grandma3-specs

For agents **using** this repo to write OSC, macros, or Lua — not for editing the Specs themselves.

1. Read [`specs/versions.md`](../../specs/versions.md) first (Target + Lua).
2. Prefer Specs over guessing or forum snippets.
3. Load order: Concept map (`specs/concepts/`) if unfamiliar → Topic Spec → Keyword Spec → Help Dump.
4. `specs/keywords/` is the only keyword dictionary. Skip `archive/` for new commands. Honor `deprecated`.
5. Do not invent keywords, options, or GUI→CLI translations.
6. Multi-station / master / where-commands-run → [`specs/multi-station.md`](../../specs/multi-station.md). Do not invent session behavior from memory.
7. Do not write plugin/macro files until the user gives absolute `gma3_library`. Do not guess station IPs (default OSC `127.0.0.1`).
8. Full agent checklist: [`AGENTS.md`](../../AGENTS.md). Vocabulary: [`CONTEXT.md`](../../CONTEXT.md).

Contribute / edit Specs? Use [`.agents/rules/contribute.md`](contribute.md) and the [contribute-specs](../skills/contribute-specs/SKILL.md) skill instead.
