---
name: convert-release-notes
description: >-
  Convert grandMA3 release-notes PDFs to searchable Markdown for offline grep,
  diff, and agent scanning. Use when adding or regenerating Release_Notes_*.md
  from Release_Notes_*.pdf under specs/release-notes-pdf/.
---

# Convert release notes PDF → Markdown

Produce a **grep/diff index**, not polished documentation. The PDF stays the source of truth.

**Input:** `specs/release-notes-pdf/Release_Notes_<version>.pdf`  
**Output:** `specs/release-notes/Release_Notes_<version>.md`

Do not optimize for pixel-perfect layout, icons, or hand-edited prose.

## Tool

`scripts/pdf-to-md.py` in this skill folder. Uses pypdf **layout** extraction.

Why layout mode: better word spacing than default `extract_text()`. Grep on the PDF binary and `strings` do not work reliably.

## Workflow

1. Place the official PDF in `specs/release-notes-pdf/` (e.g. `Release_Notes_v2.5.0.3.pdf`).
2. Ensure **pypdf** is available (one-time venv is fine):

   ```bash
   python3 -m venv .venv-pdf
   .venv-pdf/bin/pip install pypdf
   ```

3. Run from the repository root:

   ```bash
   .venv-pdf/bin/python .agents/skills/convert-release-notes/scripts/pdf-to-md.py \
     --input specs/release-notes-pdf/Release_Notes_v2.5.0.3.pdf \
     --output specs/release-notes/Release_Notes_v2.5.0.3.md
   ```

   If `--output` is omitted and the input sits in `release-notes-pdf/`, the script writes the sibling `release-notes/` folder.

4. Spot-check the `.md`:
   - `rg "Waldbüttelbrunn|Page [0-9]+ of"` → no matches (footers stripped)
   - Main sections present (`## 1. Features` …)
   - Search terms of interest are findable (`Deprecated`, `Lua`, …)

5. Commit the Markdown next to the other release-note files.

## Diff / grep

```bash
diff -u specs/release-notes/Release_Notes_v2.5.0.2.md \
        specs/release-notes/Release_Notes_v2.5.0.3.md | less

rg -i "plugin|lua|deprecated" specs/release-notes/
```

## What the script does

- Extracts all pages with `pypdf.PdfReader` + `extraction_mode="layout"`
- Removes repeated MA copyright / page footer lines
- Promotes main sections to headings where it can
- Converts `·` / `o` bullets to Markdown lists
- Wraps `Hint:` / `Important:` / `Known Limitation:` blocks in blockquotes

Known limits: icons become blanks; multi-column lines can break; some words concatenate (`ifthe`). Fix only when they block grep.

## Do not use for

- Plugin or runtime code paths
- Replacing the official PDF
