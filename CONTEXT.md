# grandma3-specs

A public reference for how grandMA3 behaves, used by coding agents that send OSC, write macros, or write Lua plugins.

## Language

**Spec**:
A descriptive note about how the console or Lua engine behaves. Not a coding convention and not a procedure.
_Avoid_: discussion, playbook, rule

**Help Dump**:
A versioned text export of MA’s built-in Lua/API help, produced by the `HelpLua` command.
_Avoid_: typings, official API contract, grandma3_lua_functions (as the repo name)

**Release Notes**:
Searchable Markdown derived from an official MA release-notes PDF. The PDF is the source; the Markdown is a grep/diff index.
_Avoid_: polished documentation, replacement for the PDF

**Skill**:
A portable Agent Skills folder (`SKILL.md` plus optional `scripts/` / `references/`) that says when to act and points at Specs.
_Avoid_: Cursor-only `.cursor/skills` as the canonical location

**gma3_library**:
The absolute path to the user’s grandMA3 shared library root (`…/gma3_library`). Write skills do not guess this path.
_Avoid_: hardcoded machine paths, assuming `~/MALightingTechnology/…`
