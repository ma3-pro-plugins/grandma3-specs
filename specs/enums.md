---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/plugins.html"
---

# Enums (Lua)

The console exposes a global **`Enums`** table. Each child is one enum; each member is a **string key** (the name MA shows) mapped to an integer. Catalog (all names + values): [`enums/grandMA3_lua_enums 2.5.0.2.md`](enums/grandMA3_lua_enums%202.5.0.2.md).

**typings** dump from `grandma3-ts-types` (generated from the live `Enums` table on MA **2.5.0.2**). Target is **2.5.0.3**. Prefer this catalog over TypeScript `.d.ts`. External HTML/JSON of the same table: [bambinito enums](https://grandma3.bambinito.net/reference/v23/enums/) (from [APIDump](https://github.com/patopesto/GrandMA3-Plugins) `grandMA3_lua_enums.json`).

## Write it in a plugin

Identifier members (most cases):

```lua
local mode = Enums.ShuffleMode.Linked
```

`Linked` is `1`. Prefer the `Enums.…` form over the raw number.

Names that are not Lua identifiers (spaces, symbols, leading digits) use brackets:

```lua
local move = Enums.GridCursorMovement["Append X"]
```

```lua
local n = Enums["100_1000"]["100"]
```

`:Get` can take a role from `Enums.Roles` (Help Dump `Get(handle, property[, role])`):

```lua
local rec = GetObject("Sequence 1 Cue 2 Part 0.1")
if rec ~= nil then
  Printf("%s", tostring(rec:Get("shuffleMode", Enums.Roles.Default)))
end
```

`Set` / `Cmd` property values usually want the **member string** (`"Linked"`, `"Append X"`), not the integer. Confirm on the object Spec.

Do not invent enum or member names — grep the catalog. Topic Specs that already list a finite set (ShuffleMode, RecipeStoreMode, …) stay the place for **which** enum a property uses; this catalog is the full member list.

## Related

- Plugin access (`Get` / `GetObject`): [`plugin-access.md`](plugin-access.md)
- Object API / Help Dump: [`object-api.md`](object-api.md)
- Target / which dump: [`versions.md`](versions.md)
