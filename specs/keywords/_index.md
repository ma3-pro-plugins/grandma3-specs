# Keyword Specs

Sample crawl: **10 general** + **10 option** keywords from the grandMA3 **2.5** HTML manual.
Target: [`../versions.md`](../versions.md). Layout: [`CONTEXT.md`](../../CONTEXT.md).

## General (sample)

| Keyword | File | Shortcuts |
| --- | --- | --- |
| `Assign` | [`Assign.md`](Assign.md) | `As` |
| `At` | [`At.md`](At.md) | `A` |
| `Blind` | [`Blind.md`](Blind.md) | `B` |
| `Call` | [`Call.md`](Call.md) | `Cal` |
| `Copy` | [`Copy.md`](Copy.md) | `Co` |
| `Cue` | [`Cue.md`](Cue.md) | `C` |
| `Delete` | [`Delete.md`](Delete.md) | `D` |
| `Fixture` | [`Fixture.md`](Fixture.md) | `F`, `Fi` |
| `Group` | [`Group.md`](Group.md) | `G` |
| `Store` | [`Store.md`](Store.md) | `S` |

## Option keywords

See [`options/_index.md`](options/_index.md).

## Archive

[`archive/`](archive/) — empty until lifecycle applies.

Each file: frontmatter (`keyword`, `kind`, `shortcuts`, `manual_url`, optional `introduced` / `deprecated`) + `## Official` + `## Extra`.
Crawler replaces **Official** only; never blanks Extra or `introduced`.

**Examples:** bare commands only (strip `User name[Fixture]>`). Crawler: [`.agents/skills/crawl-keywords/`](../../.agents/skills/crawl-keywords/).
