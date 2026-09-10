---
name: crawl-keywords
description: >-
  Crawl grandMA3 HTML manual keyword pages into Keyword Specs under
  specs/keywords/ (Official section only). Use when adding or refreshing
  general or option keyword Specs from help.malighting.com.
---

# Crawl keyword Specs from the manual

Seed or refresh **Official** text for Keyword Specs. Never invent shortcuts or `introduced`.

**Indexes:**

- General: `https://help.malighting.com/grandMA3/<major.minor>/HTML/csk_general_keywords.html`
- Options: `https://help.malighting.com/grandMA3/<major.minor>/HTML/option_keywords.html`

**Output tree:** `specs/keywords/` and `specs/keywords/options/` (see [`CONTEXT.md`](../../../CONTEXT.md)).

## Hard rules

1. **One tree** — write Keyword Specs under `specs/keywords/`, not `raw/…/keywords/`.
2. **Replace Official only** — keep `## Extra` and frontmatter `introduced` when merging.
3. **Examples are bare commands** — the manual shows `User name[Fixture]>Store Cue 1`. Specs must store only `Store Cue 1` (strip the CLI prompt and the `>`). Agents copy examples into OSC/macros; chrome is noise.
4. **Omit `introduced` / `deprecated` unless evidenced** — never guess.
5. Crawl **general and option** keywords.

## Tool

`scripts/extract_keyword.py` in this skill folder.

```bash
python3 -m venv .venv-kw
.venv-kw/bin/pip install beautifulsoup4 lxml html2text

# New Spec from a downloaded HTML page:
.venv-kw/bin/python .agents/skills/crawl-keywords/scripts/extract_keyword.py \
  --input /tmp/keyword_store.html \
  --kind general \
  --manual-url https://help.malighting.com/grandMA3/2.5/HTML/keyword_store.html \
  --output specs/keywords/Store.md

# Refresh Official; keep Extra + introduced:
.venv-kw/bin/python .agents/skills/crawl-keywords/scripts/extract_keyword.py \
  --input /tmp/keyword_store.html \
  --kind general \
  --manual-url https://help.malighting.com/grandMA3/2.5/HTML/keyword_store.html \
  --merge-into specs/keywords/Store.md \
  --output specs/keywords/Store.md
```

## Workflow

1. Read `specs/versions.md` for Target; pick the matching manual major.minor (e.g. Target `2.5.0.3` → `/grandMA3/2.5/HTML/`).
2. Download index HTML; collect `keyword_*.html` / `ok_*.html` hrefs.
3. For each page (or a batch): download HTML → run `extract_keyword.py` → write/merge Spec.
4. Rebuild `specs/keywords/_index.md` and `specs/keywords/options/_index.md`.
5. Apply keyword lifecycle (deprecated / archive) per CONTEXT.
6. Commit on `main` unless the user asked for a PR.

## Do not use for

- Concepts / show-file overview (`specs/concepts/`) — that is manual plan A, curated separately
- Help Dump / Lua API extraction
