---
name: commit
description: >-
  Create git commits in grandma3-specs with a message that describes the
  actual change, after checking file types and hierarchy placement. Use when
  the user asks to commit, write a commit message, or stage changes in this
  repo.
---

# Commit grandma3-specs

Commit only when the user asked. Do not push unless they asked.

This repo is a Markdown reference. Treat anything else as unusual.

## Before staging

Run, in parallel:

- `git status`
- `git diff` and `git diff --cached`
- `git log -10 --format='%s'`

Then classify **every** path that would be in the commit (staged, unstaged, or untracked you plan to add).

### 1. File kind

Expected: `.md`

If the commit includes any other extension or a file with no extension, **stop and alert the user**. List the paths and wait for an explicit OK before including them.

Do not silently add Help Dumps (`.txt`), PDFs, skill scripts, binaries, or generated files.

### 2. Placement

Specs are facts. Skills are procedures. Do not mix them.

| Kind | Where it belongs |
| --- | --- |
| Topic spec | `specs/<kebab-topic>.md` (not the repo root) |
| Help Dump | `specs/lua-functions/` |
| Release-notes Markdown | `specs/release-notes/Release_Notes_<version>.md` |
| Release-notes PDF (source) | `specs/release-notes-pdf/` |
| Skill | `.agents/skills/<skill-name>/SKILL.md` plus optional `scripts/` / `references/` |
| Agent map | `INDEX.md` (link new specs and skills here) |
| Vocabulary | `CONTEXT.md` |
| Human intro | `README.md` |
| Agent bootstrap | `AGENTS.md` |

If a path does not match this tree, or a new spec/skill is missing from `INDEX.md`, **stop and alert the user**. Propose the correct path; do not relocate files unless they agree.

Root Markdown is only `INDEX.md`, `AGENTS.md`, `CONTEXT.md`, `README.md`. New notes do not go at the root.

## Commit message

Describe the **actual change** (what a reader learns or what moved), not that “docs were updated.”

Format:

```text
<one-line subject>

<optional body: why, or what the spec/skill now says>
```

- Subject: sentence case, imperative, period at the end, ≤ 72 characters.
- Subject must name the topic and the change (`Add`, `Update`, `Fix`, `Move`, `Convert`).
- Body only when the subject cannot carry the why. No file laundry lists.
- No Conventional Commits prefixes (`feat:`, `docs:`).
- No Co-authored-by unless the user asks.

Read the diff. If several files change for one reason, one commit.

### Split unrelated topics

If the staged files include totally irrelevant topics, split them. Group files that are relevant to each other, then make a **separate commit per group**, each with a proper, concise message for that change only.

Do not ask whether to split when the topics are clearly unrelated. One mixed commit is wrong.

Keep together (same commit):

- A spec or skill plus the `INDEX.md` / `README.md` link that exists only for that addition
- Several files that implement one topic (skill `SKILL.md` + its `scripts/`)
- One mechanical edit applied for a single reason

Split (separate commits):

- Two different specs (e.g. OSC and hooks)
- A skill change and an unrelated spec
- A release-notes convert and an unrelated topic edit

If the mix is already staged, unstage, then stage and commit one group at a time. Report every new hash and subject.

Good:

```text
Add Lua 5.5 sparse-array notes for # on holey tables.
```

```text
Update OSC spec with DumpLog proof after /gma3/cmd.

Session master is now read from the log, not guessed from IP.
```

```text
Convert Release_Notes_v2.5.0.3 PDF to searchable Markdown.
```

Bad: `Update specs.`, `Add files.`, `docs: markdown.`, `WIP.`, `misc.`, a subject that only lists filenames.

## How to commit

After kind and placement checks pass (or the user overrode them):

1. Group paths by topic. Stage only the first group. Do not `git add -A` if that would mix unrelated topics or pick up non-Markdown or misplaced files you already flagged.
2. Commit that group with a HEREDOC (no `--no-verify`, no amend unless the user asked and amend is safe). Repeat stage + commit for each remaining group:

```bash
git commit -m "$(cat <<'EOF'
Subject line here.

Optional body here.
EOF
)"
```

3. Run `git status` and report each new hash and subject.

Never update git config. Never force-push. Never skip hooks.
