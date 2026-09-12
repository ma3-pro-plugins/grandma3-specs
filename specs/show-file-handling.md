---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/show_file_management.html"
---

# Show File Handling (Topic Spec)

Concept map (thin): [`concepts/show-file-handling.md`](concepts/show-file-handling.md).

Manual hub + subtopics: [Show File Handling](https://help.malighting.com/grandMA3/2.5/HTML/show_file_management.html), [Load](https://help.malighting.com/grandMA3/2.5/HTML/sfh_load.html), [Save](https://help.malighting.com/grandMA3/2.5/HTML/sfh_save.html), [New](https://help.malighting.com/grandMA3/2.5/HTML/sfh_new.html), [Backup and Template](https://help.malighting.com/grandMA3/2.5/HTML/sfh_backup.html), [Organize](https://help.malighting.com/grandMA3/2.5/HTML/shf_organize.html), [Demo Shows](https://help.malighting.com/grandMA3/2.5/HTML/sfh_demo.html). Folder layout: [File Management](https://help.malighting.com/grandMA3/2.5/HTML/file_management.html) / [Folder Structure](https://help.malighting.com/grandMA3/2.5/HTML/fm_folder_structure.html).

Show files hold patch, fixture types, cues, timings, 3D, users/profiles, …. Software version only moves **forward**. Max show size **10 GB**. Folders: Shows, Backup Shows, Demo Shows, Template Shows. Management UI is the **Backup** menu; CLI keywords below cover load/save/new/drive.

**None of LoadShow / SaveShow / NewShow / Menu / Select / Drive list `/NoConfirmation`** — do not append it.

## Backup menu and drive

Opens the Backup menu:

```
Menu "Backup"
```

Selects the first USB stick (internal = Drive 1; first USB = Drive 2; later sticks get higher numbers by plug order):

```
Select Drive 2
```

Lists drives:

```
List Drive
```

Keywords: [`Menu`](keywords/Menu.md), [`Select`](keywords/Select.md), [`Drive`](keywords/Drive.md).

## Load / Save / New

Loads show file named MacBeth (from Shows on the current drive unless options say otherwise):

```
LoadShow "MacBeth"
```

Loads from internal drive explicitly:

```
LoadShow "Timecode" If Drive 1
```

Loads the demo show from the Demo Shows folder:

```
LoadShow "Demoshow_grandMA3.show" /Type "Demo"
```

Saves under a new name (overwrites same name if it exists — Official warning):

```
SaveShow "Rhapsody"
```

Saves under the current show name:

```
SaveShow
```

Creates a new show named La Bohème:

```
NewShow "La Bohème"
```

Keywords: [`LoadShow`](keywords/Loadshow.md), [`SaveShow`](keywords/Saveshow.md), [`NewShow`](keywords/Newshow.md).

Useful options (confirm on option Specs): LoadShow — `/All`, `/DMXProtocols`, `/LocalSettings`, `/NoSave`, `/NoShowData`, `/OutputStations`, `/Path`, `/Save`, `/Type` (`Demo` / `Template` per [`/Type`](keywords/options/Type.md)); SaveShow — `/Enumerate`, `/Path`; NewShow — `/All`, `/DMXProtocols`, `/LocalSettings`, `/NoShowData`, `/OutputStations`, `/Path`.

`LoadShow "Henrietta"` with a **new** name creates that show; save afterward so it can be reloaded (Official note on LoadShow).

## Backup / demo / template (facts)

- Up to **10** backup files per show; cannot save/create new shows **into** Backup / Demo / Template folders.
- Demo Shows = MA-supplied; Template Shows = user-predefined templates.
- Free disk space warnings in Backup menu: orange < 15 GB, red < 5 GB.
- Delete show files: Backup menu Delete (GUI). Do not invent a DeleteShow keyword.

## Related

- Local settings (what survives show load): [`concepts/local-settings.md`](concepts/local-settings.md)
- System / station: [`system.md`](system.md)
- Automation: [`automation.md`](automation.md)
