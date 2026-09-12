---
title: Plugin access (read objects)
topic_spec: ../plugin-access.md
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/plugins.html"
---

# Plugin access (read objects)

Lua plugins resolve show objects by **address**, read properties, and walk **parent / children**. This is the read path. Creating or filling objects stays on CLI (`Store` / `Assign` / `Cmd`) unless an object Spec documents a Help Dump write.

**Topic Spec (depth):** [`../plugin-access.md`](../plugin-access.md).

Resolves Group 1 and Echoes its name:

```lua
local g = GetObject("Group 1")
if g ~= nil then
  Echo(g:Get("name"))
end
```

Use `GetObject` for one concrete address. `ObjectList` only when you need a table of matches. Traverse: `obj:Parent()`, `obj:Count()`, `obj:Ptr(i)` (1-based), `obj:Children()`.

## Related

- **Topic Spec:** [`../plugin-access.md`](../plugin-access.md)
- Plugins hub: [`plugins.md`](plugins.md)
- Object API / Help Dumps: [`../object-api.md`](../object-api.md)
