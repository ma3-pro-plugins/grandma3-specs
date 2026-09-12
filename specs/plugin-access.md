---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/plugins.html"
---

# Plugin access (read objects)

Concept (thin): [`concepts/plugin-access.md`](concepts/plugin-access.md). Help Dump (Target): [`lua-functions/`](lua-functions/) — open the file that matches [`versions.md`](versions.md). Per-object trees (recipe, layout, group, …): that object’s Topic Spec **Plugin access** section.

This Spec is **read** (resolve a handle, read properties, walk parent/children). Write stays CLI (`Cmd` / `Store` / `Assign`) unless a Help Dump function is documented on the object Spec.

Signatures below are from the **2.5.0.3 Help Dump** (`HelpLua`). Colon form `obj:Get("name")` is `Get(handle, "name")`.

## Resolve a handle

| Function (Help Dump) | Returns |
| --- | --- |
| `GetObject(string:address)` | one handle |
| `ObjectList(string:address[, {selected_as_default, reverse_order}])` | table of handles |
| `FromAddr(string:address[, handle:base])` | one handle |
| `DataPool()` | selected data pool |
| `ShowData()` | show root |
| `ToAddr(handle, boolean:with_name[, boolean:use_visible_addr])` | address string |

Always nil-check. `GetObject` / `FromAddr` fail closed (no handle). `ObjectList` can be empty.

**`GetObject` first.** Use it when the address names one object and has no wildcard. Do not write `ObjectList("…")[1]` for a concrete address. `ObjectList` only when you need every matching handle. `GetObject` exists since MA **2.1.1.2** (**observed** `SupportedFeatures.ts`). Target examples use `GetObject`.

Resolves **Group 1** (one handle):

```lua
local g = GetObject("Group 1")
if g == nil then
  Echo("no Group 1")
  return
end
```

Resolves **one** recipe by concrete address (`GetObject`, not `ObjectList`):

```lua
local rec = GetObject("Sequence 1 Cue 2 Part 0.1")
```

Selected data pool vs numbered pool:

```lua
local dp = DataPool()
local pools = ShowData().DataPools
```

`DataPool().Sequences` / `.Groups` / `.Layouts` / `.PresetPools` are **observed** child names (see each object Spec). Confirm with `GetClass()` / `Count()`.

## Read properties

```text
Get(handle, string:property_name[, integer:role(Enums.Roles)]): handle or string
GetClass(handle): string:class_name
Index(handle): integer:index
Dump(handle): string:information
```

Reads the **name** property of Group 1:

```lua
local g = GetObject("Group 1")
if g ~= nil then
  Echo(g:Get("name"))
end
```

Prints the class (use this before assuming a child is `StandardRecipe` / `Layout` / …):

```lua
Echo(g:GetClass())
```

`Dump(obj)` is a debug string of the handle. Do not invent property names — Official / Help Dump / grandma3-ts-types (**typings**) / the object Spec.

## Traverse parent and children

```text
Parent(handle): handle
Count(handle): integer:child_count
Ptr(handle, integer:index(1-based)): handle
Children(handle): {handles}
GetChildClass(handle): string
HasParent(handle, handle:object_to_check)
```

Walks children of the selected data pool’s Groups (1-based `Ptr`):

```lua
local groups = DataPool().Groups
for i = 1, groups:Count() do
  local child = groups:Ptr(i)
  Echo(string.format("%d %s %s", i, child:GetClass(), tostring(child:Get("name"))))
end
```

Goes to the parent of Group 1:

```lua
local g = GetObject("Group 1")
local parent = g:Parent()
Echo(parent:GetClass())
```

`Children()` returns the whole child table. `CmdlineChildren` / `CmdlinePtr` exist in the Help Dump when command-line child order differs from object-tree order — confirm on Target before using them.

## Related

- Object API / which Help Dump to open: [`object-api.md`](object-api.md)
- Hooks (`HookObjectChange` needs a handle): [`hooks.md`](hooks.md)
- Per-object trees: [`recipes.md`](recipes.md), [`layouts.md`](layouts.md), [`groups.md`](groups.md), [`phaser-recipe.md`](phaser-recipe.md)
- Plugin lifecycle / `Cmd` limits: [`plugins.md`](plugins.md)
- Write skill (file layout only): [`.agents/skills/write-plugin/SKILL.md`](../.agents/skills/write-plugin/SKILL.md)
