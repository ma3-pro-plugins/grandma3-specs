# Ingest (contributors)

External sources **elaborate existing Topic Specs**. They do **not** create new topics or new concept hubs.

Agents that want to contribute: read this folder first so you do not re-ingest the same thread, file, or plugin. If you use a smarter extract than a previous run, log that (logic + date) — do not silently overwrite the log.

## Rules

1. Target only. Verify facts against [`specs/versions.md`](../../specs/versions.md), Help Dumps, and Keyword Specs. Do not invent keywords or UI class names.
2. Forum: take **high-reliability answers only**. Prefer users in [`forum-users.md`](forum-users.md). Skip questions, speculation, and “try this” without confirmation.
3. Private `ma3-pro-plugins` `lib/ui/`: facts only, no vendoring. **Skip** any `*react*` folder (`components-react`, `dialogs-react`, `react`, `react-dom`).
4. Open-source plugins: treat as **working examples** if they pass the reliability bar in [`sources.md`](sources.md) (stars + last commit, or a trusted forum author). grandMA3 only.
5. One short reviewable PR per run. Record the chunk in [`log.md`](log.md).
6. Version facts stay on the page that uses them. No SupportedFeatures matrix.

Daily Grok Bot routine: **Daily specs ingest PR**.
