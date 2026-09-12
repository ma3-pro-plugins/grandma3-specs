---
title: Layouts
topic_spec: ../layouts.md
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/layouts.html"
---

# Layouts

Layouts are two-dimensional drafts where you arrange fixtures, macros, groups, and other pool objects. They live in the Layouts pool (a Data Pool child) and are shown/edited in the Layout Viewer. **Max 10 000 elements** per layout.

**Topic Spec (depth — assign/clone CLI, multipatch, Setup vs operate, element tabs, encoder bar, view settings):** [`../layouts.md`](../layouts.md).

Creates **layout 5** and puts the current fixture selection on it:

```
Assign Layout 5
```

Adds **group 5** as a button on layout 4:

```
Assign Group 5 At Layout 4
```

Keyword: [`Layout`](../keywords/Layout.md), [`Assign`](../keywords/Assign.md).

## Related

- **Topic Spec:** [`../layouts.md`](../layouts.md)
- Data pools: [`datapools.md`](datapools.md)
- Groups / selection: [`groups.md`](groups.md), [`operate-fixtures.md`](operate-fixtures.md)
