---
title: Show File Handling
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/show_file_management.html"
---

# Show File Handling

The show file holds patch, fixture types, cues, timings, 3D data, users/profiles, and related show objects. Software version of a show only moves **forward** (save on a newer build → cannot restore that file on older software).

Show files are limited to **10 GB**. Management is via the Backup menu.

**Depth** (LoadShow / SaveShow / NewShow, drives, `/Type "Demo"`, backup/demo/template folders): [`../show-file-handling.md`](../show-file-handling.md).

## Syntax (from manual)

Open Backup menu:

```
Menu "Backup"
```

Select a drive (internal = Drive 1; first USB = Drive 2):

```
Select Drive 2
```

Load / save / new (see Topic Spec for options):

```
LoadShow "MacBeth"
```

```
SaveShow
```

```
NewShow "La Bohème"
```

Keywords: [`LoadShow`](../keywords/Loadshow.md), [`SaveShow`](../keywords/Saveshow.md), [`NewShow`](../keywords/Newshow.md). There is no `DeleteShow` keyword (Backup menu Delete GUI). BackupBrowserFilter / options: [`../show-file-handling.md`](../show-file-handling.md).

## Subtopics (manual)

Load / Save / New / Backup & Template / Organize / Demo Shows.

## Related

- Topic Spec: [`../show-file-handling.md`](../show-file-handling.md)
- Local settings: [`local-settings.md`](local-settings.md)
- System: [`system.md`](system.md)
