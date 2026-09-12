---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/agenda.html"
---

# Agenda (Topic Spec)

Concept map (thin): [`concepts/agenda.md`](concepts/agenda.md). Keyword: [`keywords/Agenda.md`](keywords/Agenda.md) (shortcut **Age**).

Manual hub + subtopics: [Agenda](https://help.malighting.com/grandMA3/2.5/HTML/agenda.html), [View Modes](https://help.malighting.com/grandMA3/2.5/HTML/agenda_modes.html), [Create an Agenda Entry](https://help.malighting.com/grandMA3/2.5/HTML/agenda_entry.html), [Edit an Agenda Entry](https://help.malighting.com/grandMA3/2.5/HTML/agenda_edit.html), [Agenda Toolbar](https://help.malighting.com/grandMA3/2.5/HTML/agenda_toolbar.html).

This Spec is **calendar agenda entries** and the **Agenda** CLI keyword. Startup / DMXRemote / agenda-startup automation overlap stays in **[`startup-dmxremote-agenda.md`](startup-dmxremote-agenda.md)** — link it; do not duplicate that matrix here.

## What it schedules

The agenda runs **sequences, macros, or plugins**, or a free **Command** string (e.g. Go+ Executor 101), on calendar time. Events can repeat every minute / day / week / month / year (and twilight modes).

Open the viewer: Add Window → Tools → **Agenda Viewer**. **AgendaViewMode** (Official+typings): Sheet, Year, Month, Week, Day (title-bar View Mode). Sheet is the property spreadsheet; create via New AgendaEvent (Edit + tap, or tap-hold).

## CLI (Official examples)

Assigns sequence 1 to agenda event 1:

```
Assign Sequence 1 At Agenda 1
```

Names agenda event 1 "Sunset":

```
Label Agenda 1 "Sunset"
```

Sets agenda event 2 mode to Dawn (twilight; needs location/date-time config — see manual Date and time):

```
Set Agenda 2 Property "Mode" "Dawn"
```

Option on Agenda Official: [`/Date`](keywords/options/Date.md) only. Agenda does **not** list `/NoConfirmation`. Official has **no** `Store Agenda`.

**Mode** (Official+typings): Absolute, Dawn, Sunrise, Sunset, Dusk. Sheet properties (manual labels, GUI): Name, Appearance, Note, Mode, StartDate, StartTime, Daylight Offset, Valid Duration, Enabled, Object (Plugin / Macro / Sequence), Action, Command, Repeat (Schedule + Iterations). Read-only columns: Countdown, Planned Date/Time, Repeat Count Days/Total.

**AgendaTool** (typings): Select, Store, Delete, Cut, Copy, Paste, Call, Edit.

## View modes and toolbar (GUI facts)

| Mode | Notes |
| --- | --- |
| Sheet | Filterable; New AgendaEvent; Delete Old clears past events including valid duration |
| Year / Month / Week / Day | Calendar layouts; disabled = red font; repeats show a marker |
| Toolbar (Setup on) | AgendaTool: Select / Store / Delete / Call / Edit / Cut / Copy / Paste |

Delete in calendar views: Delete key then tap the event (GUI). Confirm any `Delete Agenda …` on Keyword Specs before automation use.

## Related

- Startup / DMXRemote matrix: [`startup-dmxremote-agenda.md`](startup-dmxremote-agenda.md)
- Macros / plugins / sequences: [`concepts/macros.md`](concepts/macros.md), [`concepts/plugins.md`](concepts/plugins.md), [`concepts/cues-sequences.md`](concepts/cues-sequences.md)
- Multi-station (where Cue Command runs): [`multi-station.md`](multi-station.md)
