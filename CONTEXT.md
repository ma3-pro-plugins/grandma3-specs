# grandma3-specs

A public reference for how grandMA3 behaves, used by coding agents that send OSC, write macros, or write Lua plugins.

## Language

**Spec**:
A descriptive note about how the console or Lua engine behaves **on the current Target** (see Versioning). Not a coding convention and not a procedure.
_Avoid_: discussion, playbook, rule

**Target**:
The grandMA3 software build this repo’s Specs describe right now. Always the latest build we have adopted. Agents read it from [`specs/versions.md`](specs/versions.md).
_Avoid_: guessing the version from memory or from an old Help Dump filename

**Help Dump**:
A versioned text export of MA’s built-in Lua/API help, produced by the `HelpLua` command. Immutable raw reference — one file (or folder) per software build.
_Avoid_: typings, official API contract, grandma3_lua_functions (as the repo name)

**Release Notes**:
Searchable Markdown derived from an official MA release-notes PDF. The PDF is the source; the Markdown is a grep/diff index. Versioned by MA release.
_Avoid_: polished documentation, replacement for the PDF

**Raw reference**:
Immutable, versioned dumps and extracts (Help Dumps, keyword lists, similar). Not rewritten when behavior Specs update.
_Avoid_: putting narrative Specs under raw/

**Skill**:
A portable Agent Skills folder (`SKILL.md` plus optional `scripts/` / `references/`) that says when to act and points at Specs.
_Avoid_: Cursor-only `.cursor/skills` as the canonical location

**gma3_library**:
The absolute path to the user’s grandMA3 shared library root (`…/gma3_library`). Write skills do not guess this path.
_Avoid_: hardcoded machine paths, assuming `~/MALightingTechnology/…`

**Migration Spec**:
A Spec that documents a **delta** between two releases (e.g. Lua 5.4 → 5.5). Not the standing description of current behavior.
_Avoid_: using a migration Spec as the only source for current Target truth

## Versioning

### Specs = latest only

Topic Specs under `specs/*.md` always describe **Target**. When MA changes behavior, rewrite the Spec in place on `main`. Do not keep parallel Spec trees per version.

### What is versioned

| Kind | Where | Rule |
| --- | --- | --- |
| Target pointer | `specs/versions.md` | Single source of Target + Lua engine |
| Help Dumps | Today: `specs/lua-functions/` (version in filename). Intended: `specs/raw/<version>/lua-functions.txt` | Immutable; keep old builds |
| Keyword / manual extracts | Intended: `specs/raw/<version>/…` | Immutable when added |
| Release-notes Markdown | `specs/release-notes/` | One file per MA release |
| Release-notes PDFs | `specs/release-notes-pdf/` | Source PDFs |
| Open bugs on Target | `specs/ma-bugs.md` | Bugs that still affect Target |
| Fixed / historical bugs | `specs/bugs/fixed/` (when archived) | Moved out of `ma-bugs.md` when Fixed |

### Git tags

When this repo adopts a new MA release (Target bumps):

1. Update `specs/versions.md`
2. Add the matching Help Dump (and any other raw extracts)
3. Rewrite Specs that changed
4. Tag `main` as `ma-<version>` (e.g. `ma-2.5.0.3`)

That tag freezes Specs **as they were when that build was Target**. Use it to recover old behavior; do not maintain a second Spec tree on `main`.

### Agent flow

1. Read `specs/versions.md` → Target
2. Treat Specs as Target truth
3. Open the Help Dump / raw files for that Target (or the closest dump we have)
4. Use `ma-bugs.md` for open issues; ignore or archive entries with **Fixed in** on or before Target when advising for current Target
