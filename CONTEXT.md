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

**Keyword Spec**:
One file per command-line keyword (general **and** option keywords) under [`specs/keywords/`](specs/keywords/). This is the **only** keyword tree agents load. Official manual text and contributor Extra live in the **same** file. Not a raw dump.
_Avoid_: a second `raw/…/keywords/` dictionary; splitting “official” and “ours” into two folders

**Raw reference**:
Immutable, versioned dumps (Help Dumps, release-note PDFs/MD, optional crawl snapshots). Not rewritten when Specs update. Not used as the keyword dictionary.
_Avoid_: putting narrative Specs or Keyword Specs under raw/

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

Topic Specs under `specs/*.md` and Keyword Specs under `specs/keywords/` always describe **Target**. When MA changes behavior, rewrite in place on `main`. Do not keep parallel Spec trees per version.

### Keywords: one tree

Path: `specs/keywords/` (general) and `specs/keywords/options/` (option keywords). One `_index.md` lists both. Archived keywords: [`specs/keywords/archive/`](specs/keywords/archive/).

Each keyword file:

- Frontmatter:
  - `keyword`, `kind` (`general` | `option`), `shortcuts`, `manual_url`
  - `introduced` — first MA version known to have it (`X.Y.Z.W` or `X.Y`). **Omit if unknown; never guess.**
  - `deprecated` — MA version that deprecated it. Omit if it is current.
- `## Official` — seeded/updated from the Target user manual. A crawler may replace this section and may update `shortcuts` / `manual_url` / `deprecated` when the manual states them. A crawler must not blank `introduced` or Extra.
- `## Extra` — contributor knowledge (when to use, gotchas, OSC, examples from shows). **Crawlers must not overwrite Extra.**

Agents read Official + Extra as one Spec. There is no duplicate “enriched” tree.

**Official examples (AI-friendly):** The HTML manual shows commands inside the console CLI chrome, e.g. `User name[Fixture]>Group 3`. That prefix is the input-box label, not part of the command. Keyword Specs must store **only the command after `>`** (no `User name[…]`, no `>`). Prefer a fenced code block:

```
Group 3
```

The crawl-keywords skill (`scripts/extract_keyword.py`) strips this chrome automatically.

**Crawler:** Prefer [`.agents/skills/crawl-keywords/`](.agents/skills/crawl-keywords/) — a reusable HTML→Spec script — over one-off parsing. The skill replaces `## Official` only and preserves Extra / `introduced`.

Optional crawl snapshots (HTML/JSON for diffing a new manual) may live under `specs/raw/<version>/manual-crawl/`. Those are provenance, not the reference.

Command-line **grammar** (pools, handles, quotes, thru/at, how options attach) is a Target Spec: `specs/command-line.md` (to be added). That file is not a keyword list.

### Keyword lifecycle

Keywords are Target Specs, not a versioned dump. History lives **on the file**:

| Field | Meaning |
| --- | --- |
| `introduced` | First version that had this keyword, when we have evidence |
| `deprecated` | Version that marked it deprecated. File stays in the live tree while Target still documents or accepts it |

**While deprecated but still on Target:** keep the file in `specs/keywords/` (or `options/`). Agents must not suggest it for new commands unless the user is matching existing syntax.

**Archive (move, do not delete)** to `specs/keywords/archive/` (options: `archive/options/`) when either:

1. **Gone from Target** — a crawl of the Target manual no longer lists it (treat as removed; do not wait), or
2. **Deprecated ≥ 24 months** — 24 months after the deprecation release’s date (use [`specs/release-notes/`](specs/release-notes/) for that date). If the calendar date is unknown, keep it live until the date is known.

Archive keeps Official + Extra so old shows can still be decoded. Do not load `archive/` when writing new macros/OSC for Target. Git tag `ma-<version>` is how to recover the whole Spec tree as of an older Target, including keywords that were current then.


### Topic Specs, Concepts, and provenance

The repo has **three agent-facing layers**. Do not collapse them into one folder.

| Layer | Path | Job |
| --- | --- | --- |
| **Map** | [`specs/concepts/`](specs/concepts/) | System overview + subsystem pages. Thin: what it is, boundaries, **pointers** to Topic Specs and keyword clusters. Not a second copy of deep notes. |
| **Topic Specs** | [`specs/*.md`](specs/) (flat) | Curated automation behavior: plugins, OSC, macros, long command patterns, lab conclusions. Stay flat — **do not mass-move** into `concepts/`. |
| **Keyword Specs** | [`specs/keywords/`](specs/keywords/) | One CLI token each (Official from manual + Extra). |

Also: **grammar** — [`specs/command-line.md`](specs/command-line.md) (to be added): pools, handles, quotes, thru/at, how options attach. Not a keyword list and not a subsystem essay.

**Audience split:** The official HTML manual is operator/GUI-first. Topic Specs and Keyword Extra are **automation/syntax-first**. Same MA topic can appear in both places for different jobs.

**Provenance (`source`)** on Topic Specs and Concept pages (YAML frontmatter when present; omit if unknown):

| Value | Meaning |
| --- | --- |
| `manual` | Drawn primarily from the Target user manual (possibly summarized) |
| `observed` | Confirmed on console / onPC / logs in real use |
| `lab` | Bench layout or convenience note (e.g. hardware rows) — not claimed as a manual chapter |
| `mixed` | Manual + observed/lab combined |

Optional: `manual_url` when a specific manual page backs the Spec.

**Syntax-first enrichment (later track):** GUI how-tos in the manual can be rewritten as **command recipes** (using Keyword Specs) for plugins/OSC. Those recipes belong in Topic Spec Extra / Concept “Syntax” sections — **never invent commands**; only map steps that keywords and observed behavior support. Do not replace Keyword `## Official` with a guessed GUI→CLI translation.

**Agent load order:**

1. [`specs/versions.md`](specs/versions.md) → Target
2. [`specs/concepts/`](specs/concepts/) if the subsystem is unfamiliar
3. Topic Spec for automation depth
4. [`specs/keywords/_index.md`](specs/keywords/_index.md) → one keyword file
5. Help Dump when a Lua/API listing is needed
6. [`specs/ma-bugs.md`](specs/ma-bugs.md) for open Target bugs

### What is versioned

| Kind | Where | Rule |
| --- | --- | --- |
| Target pointer | `specs/versions.md` | Single source of Target + Lua engine |
| Help Dumps | Today: `specs/lua-functions/` (version in filename). Intended: `specs/raw/<version>/lua-functions.txt` | Immutable; keep old builds |
| Topic Specs | `specs/*.md` (flat) | Target only; automation-first curated notes |
| Concept map | `specs/concepts/` | Target only; thin overview + pointers |
| Keyword Specs (live) | `specs/keywords/` (+ `options/`) | Target only; Extra preserved across crawls |
| Keyword Specs (archived) | `specs/keywords/archive/` | Deprecated ≥ 24 months, or gone from Target |
| Crawl snapshots (optional) | `specs/raw/<version>/manual-crawl/` | Provenance; agents do not load these as docs |
| Release-notes Markdown | `specs/release-notes/` | One file per MA release |
| Release-notes PDFs | `specs/release-notes-pdf/` | Source PDFs |
| Open bugs on Target | `specs/ma-bugs.md` | Bugs that still affect Target |
| Fixed / historical bugs | `specs/bugs/fixed/` (when archived) | Moved out of `ma-bugs.md` when Fixed |

### Git tags

When this repo adopts a new MA release (Target bumps):

1. Update `specs/versions.md`
2. Add the matching Help Dump (and release notes)
3. Re-crawl keywords into `specs/keywords/` (replace Official, keep Extra; do not blank `introduced`)
4. Apply keyword lifecycle (set `deprecated`, archive gone / ≥ 24 months)
5. Rewrite other Specs that changed
6. Tag `main` as `ma-<version>` (e.g. `ma-2.5.0.3`)

That tag freezes Specs **as they were when that build was Target**. Use it to recover old behavior; do not maintain a second Spec tree on `main`.

### Agent flow

1. Read `specs/versions.md` → Target
2. If the subsystem is unfamiliar, open [`specs/concepts/`](specs/concepts/) (map), then the Topic Spec it points to
3. Treat Topic Specs and live Keyword Specs as Target truth (automation/syntax-first)
4. Open the Help Dump for that Target (or the closest dump we have) when you need the Lua/API listing
5. For command tokens, open `specs/keywords/_index.md` then the one keyword file (include option keywords). Skip `archive/` unless decoding old syntax.
6. If `deprecated` is set, do not use that keyword in new commands unless matching existing show syntax.
7. Use `ma-bugs.md` for open issues; ignore or archive entries with **Fixed in** on or before Target when advising for current Target
