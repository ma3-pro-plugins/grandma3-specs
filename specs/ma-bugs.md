# MA Bugs

Known grandMA3 console issues that still matter for **Target** (see [`versions.md`](versions.md)). One file for open bugs; when a bug is fixed in a release we have adopted, add **Fixed in** and move the entry to `bugs/fixed/` (create that folder on first archive).

Each entry should say the version where it was **encountered**, the version it was **introduced** when known, and **Fixed in** when resolved.

---

## Cue commands “Not allowed” when Auto Start / Auto Stop is fired by DMX Remote

- **Encountered in:** 2.5.x
- **Introduced in:** 2.5 (works in 2.4; same show file fails in 2.5)
- **Fixed in:** (open on Target)

Cue / Off Cue **command syntax** that runs because a sequence’s **Auto Start** / **Auto Stop** was triggered by a **DMX Remote** writing that sequence’s master is rejected with **“Not allowed”**.

Typical chain: a source sequence’s fixture DMX drives a DMX Remote → target sequence **FaderMaster** → Auto Start / Auto Stop → Cue or Off Cue commands.

**Workaround:** put the commands on a **macro** and have the cue **call the macro**. Those macro commands are allowed.

**Scope:** Confirmed with `Store Layout`. Other command-syntax operations may be blocked in the same context; full set not mapped.

**Executor vs DMX Remote:** Moving the **target sequence’s own master** on an executor (no DMX Remote) does not reproduce this on its own.

**Lingering state (one extra toggle):** After a DMX Remote toggle that fails, the next toggle via the sequence’s **own** master still fails once; the toggle after that works again. After a successful own-master toggle, the **next** DMX Remote toggle succeeds; following DMX Remote toggles fail again.

**Impact:** Breaking behavior in existing 2.4 show files opened on 2.5. Breaks plugins that rely on those cue commands. Users with the same DMX Remote + Auto Start / Auto Stop + cue-command setup (no plugin) get “Not allowed” and missing objects, with no obvious workaround.

---

## DMXRemote / Agenda startup “Not allowed” after master loads a show

- **Encountered in:** 2.3.2
- **Introduced in:** unknown (seen on 2.3.2)
- **Fixed in:** unknown (still listed until confirmed fixed on Target)

There is a bug in MA3 v2.3.2 where both DMXRemote and Agenda Startup event solutions don't reliably work when a master station loads a new show file. We sometimes get a “Not Allowed” error for the triggering of the startup Macro/Plugin.

See also [`startup-dmxremote-agenda.md`](startup-dmxremote-agenda.md).
