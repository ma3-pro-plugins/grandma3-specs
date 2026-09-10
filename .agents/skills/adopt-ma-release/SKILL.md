---
name: adopt-ma-release
description: >-
  Adopt a new grandMA3 software release into grandma3-specs: bump Target,
  download release notes PDF, convert to Markdown, re-crawl keyword Specs,
  apply keyword lifecycle, and tag ma-X.Y.Z.W. Run explicitly when a newer
  build than Target appears (or the user names a version).
---

# Adopt a grandMA3 release

Run this when Target should move to a newer MA build. Do **not** invent a version — take it from the downloads page or the user’s explicit `X.Y.Z.W`.

**Downloads:** https://www.malighting.com/downloads/products/grandma3/  
**Manual (HTML):** `https://help.malighting.com/grandMA3/<major.minor>/HTML/`  
**Checklist source of truth:** [`CONTEXT.md`](../../../CONTEXT.md) + [`specs/versions.md`](../../../specs/versions.md)

## Hard rules

1. **Direct commit to `main`** unless the user asked for a PR.
2. Specs and live Keyword Specs always describe **Target only** — rewrite in place; do not keep parallel version trees.
3. Keyword crawl: replace `## Official` only; keep `## Extra` and frontmatter `introduced`.
4. Never guess `introduced` / `deprecated`.
5. Strip CLI chrome from examples (`User name[…]>` → bare command). Prefer [crawl-keywords](../crawl-keywords/SKILL.md).
6. Release-notes MD is a grep index — use [convert-release-notes](../convert-release-notes/SKILL.md); keep the PDF as source.

## Detect latest on downloads

```bash
python3 .agents/skills/adopt-ma-release/scripts/latest_from_downloads.py
# prints e.g. 2.5.0.3 and release-notes PDF filename / force-download URL fragment
```

Compare to Target in `specs/versions.md`. If equal, stop (nothing to adopt).

## Workflow

Given new version `V` (full `X.Y.Z.W`) and major.minor `M` (e.g. `2.5`):

1. **Release notes PDF**
   - From the downloads page, find the `*Release_Notes*vV*.pdf` (or closest matching) `eID=csForceDownload&download=…` link.
   - Download into `specs/release-notes-pdf/Release_Notes_vV.pdf` (normalize filename; keep MA’s dated name in a comment in the commit message if useful).
   - Run convert-release-notes → `specs/release-notes/Release_Notes_vV.md`.

2. **Bump Target**
   - Update `specs/versions.md`: Target = `V`, Lua engine if release notes say so, matching reference table, “Adopting” note.
   - Update any INDEX / CONTEXT pointers that hard-code the old Target only if they claim “current”.

3. **Re-crawl keywords** (general + option)
   - Manual base: `https://help.malighting.com/grandMA3/M/HTML/`
   - Follow [crawl-keywords](../crawl-keywords/SKILL.md): indexes → download → `extract_keyword.py` with `--merge-into` for existing Specs.
   - Rebuild `specs/keywords/_index.md` and `specs/keywords/options/_index.md`.
   - **Lifecycle:** keywords gone from the new indexes → move to `specs/keywords/archive/` (options → `archive/options/`). Set `deprecated` only when evidenced. Archive deprecated ≥ 24 months per CONTEXT.

4. **Help Dump** (if available)
   - Add/update the Target Help Dump under the current layout (`specs/lua-functions/…`) or intended `specs/raw/V/` when that migration is done. Do not invent dump contents.

5. **Specs / bugs**
   - Skim release notes for behavior deltas; rewrite affected Specs; refresh `specs/ma-bugs.md` (move Fixed entries).

6. **Tag**
   - After commits are on `main`: create annotated tag `ma-V` on that commit. Do not retag casually.

7. **Report**
   - Tell the user: old Target → new Target, keyword counts (added/updated/archived), release-notes paths, tag name, any manual follow-ups (missing Help Dump, Lua engine unknown).

## Optional: monthly check only

A scheduled routine may **detect** a newer downloads version than Target and alert the user (or offer to run this skill). Detection alone must not bump Target or commit without an explicit adopt run.

## Do not use for

- Refreshing keywords on the **same** Target without a version bump (use crawl-keywords alone)
- MA2 / grandMA2 anything
- Inventing Help Dump text from the manual
