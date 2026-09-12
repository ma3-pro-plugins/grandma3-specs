# Ingest queues

Check [`log.md`](log.md) before taking a chunk. First campaign: **elaborate [`specs/plugin-dialogs.md`](../../specs/plugin-dialogs.md)**. Later runs may elaborate other existing Specs (plugin-access, recipes, …) from the same sources.

## 1. MA forum (LUA Plugins)

- Board: https://forum.malighting.com/forum/board/27-lua-plugins/
- Prefer answers from [`forum-users.md`](forum-users.md). Andreas first.
- Threads already cited by `plugin-dialogs.md` (e.g. “UI Element List”) are first. Then search the board for DialogFrame / MessageBox / Overlay / ScrollBox.

## 2. Private ma3-pro-plugins `lib/ui/`

Checkout: `~/lighting_dev/ma3-pro-plugins/lib/ui/` (or the private `ma3-pro-plugins/ma3-pro-plugins` repo).

**Use:** `Alert.ts`, `ConfirmDialog.ts`, `DialogStack.ts`, `MessageBoxHelper.ts`, `MessageBoxHelperV2.ts`, `PopupInputHelper.ts`, `UIUtils.ts`, `index.ts`, `types.ts`, `components/`, `dialogs/`.

**Skip:** `components-react/`, `dialogs-react/`, `react/`, `react-dom/`, and any other `*react*` path. Opinionated TS/TSTL library — extract **behavior facts** (how a dialog is parented, overlays, MessageBox vs custom tree), not the framework.

Issue #5 still covers `lib/ma_obj` (facts only). This queue is `lib/ui` only.

## 3. Open-source plugins (working examples)

Reliability bar (from [`specs/external-github-sources.md`](../../specs/external-github-sources.md) + forum links):

| Source | Why try | First topic |
| --- | --- | --- |
| [patopesto/GrandMA3-Plugins](https://github.com/patopesto/GrandMA3-Plugins) | 20★, commit 2025-10; real plugins + APIDump | plugin-dialogs / plugin-access |
| [PeramatoG/gma3-lua-snippets](https://github.com/PeramatoG/gma3-lua-snippets) | 4★, 2025-12; UI/PIN keypad | plugin-dialogs |
| Forum attachments by **Andreas** (MULE, GridTools, MyBounce, …) | Trusted author; treat as working examples | matching Spec, not new topics |
| [hossimo/GMA3Plugins](https://github.com/hossimo/GMA3Plugins) | 111★ but last commit 2024-05 — **low confidence / dated** | only if a fact is still true on Target |

Skip stale/empty rows already marked **No** on the external-sources inventory. grandMA3 only.

## Not a source

- New concept hubs or Topic Specs (unless Erez asks).
- MA2 boards or MA2 repos.
- Invented UI class names.
