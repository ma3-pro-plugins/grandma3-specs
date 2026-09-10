# Lua engine 5.4 → 5.5 (grandMA3 2.4 → 2.5)

grandMA3 **2.4.x** runs plugin Lua as **Lua 5.4.8**. grandMA3 **2.5.x** updated the Lua core to **Lua 5.5.0** (see MA release notes for 2.5.0.2: “The Lua Core has been updated to Lua v5.5.0”).

This file records **runtime** differences that affect plugins (including TypeScript-to-Lua output that still *emits* 5.4 syntax but *executes* on whichever engine MA ships). Official language text: [Lua 5.5 Reference Manual](https://www.lua.org/manual/5.5/manual.html), especially [§3.3.5 For Statement](https://www.lua.org/manual/5.5/manual.html#3.3.5), [§3.4.7 The Length Operator](https://www.lua.org/manual/5.5/manual.html#3.4.7), and [§8 Incompatibilities with the Previous Version](https://www.lua.org/manual/5.5/manual.html#8).

Version mapping: [`versions.md`](versions.md). TypeScript-to-Lua (TSTL) still *emits* Lua 5.4 syntax; the console *executes* whichever engine MA ships.

---

## For-loop control variables are read-only

**Official 5.5 incompatibility** ([§8.1](https://www.lua.org/manual/5.5/manual.html#8)):

> The control variable in for loops is read only. If you need to change it, declare a local variable with the same name in the loop body.

In 5.5, the control variable of a **numerical** `for` and the **first** (control) variable of a **generic** `for` are local **`const`** ([§3.3.5](https://www.lua.org/manual/5.5/manual.html#3.3.5)). Assigning to them raises an error, typically:

```text
attempt to assign to const variable 'i'
```

In **5.4**, those assignments were allowed. They never advanced or skipped the hidden iterator; they only mutated the loop body’s binding. Code that used `i = i + 1` / `k = nil` inside `for` to “skip” or rewrite the index was always a lie on 5.4 and is a hard error on 5.5.

### Lua

```lua
-- 5.4: runs (does not skip iterations). 5.5: error.
for i = 1, 10 do
    i = i + 1
end

-- 5.5: shadow with a mutable local (official workaround).
for i = 1, 10 do
    local i = i
    i = i + 1  -- mutates the inner local only
end
```

Generic `for`: only the **first** name is `const`. Later names (`v` in `for k, v in pairs(t)`) remain assignable.

### TypeScript / TSTL

TSTL still emits Lua 5.4. Prefer `for (const x of …)` and do **not** reassign the loop index or `for…of` binding. If a mutable working value is needed, introduce a new local:

```typescript
for (const item of items) {
    let work = item
    work = transform(work)
}

for (let i = 0; i < n; i++) {
    let j = i
    j = j + 1  // do not assign to i if the emit is a Lua numerical for
}
```

---

## Sparse arrays / table length (`#`) with holes

**Not listed** as a 5.5 language incompatibility. The **documented contract** for `#` is the same in 5.4 and 5.5 ([§3.4.7](https://www.lua.org/manual/5.5/manual.html#3.4.7)):

- `#t` returns a **border**: a non-negative integer `i` such that `t[i]` is present (or `i == 0`) and `t[i + 1]` is absent.
- A table with exactly one border is a **sequence**; `#t` is that length.
- A table with **holes** (`nil` in the middle of integer keys) is **not** a sequence. `#t` **may return any border**. Which border depends on internal table representation.

### Implementation change (observed 5.4 vs 5.5)

Lua 5.5 rewrote `luaH_getn` (length hint between array and hash parts). For many constructor tables with holes, **5.5 picks a different border than 5.4**.

Reported on lua-l ([Semantic change of table length in Lua 5.5](https://groups.google.com/g/lua-l/c/pOH68GYtDgw/m/BFAORSs5DAAJ), [Table length evaluations → Lua 5.5 vs. Lua 5.4](https://groups.google.com/g/lua-l/c/9CK0KhdeJRY)):

```lua
t = { nil, 2 }
print(#t)  -- Lua 5.4: 2    Lua 5.5: 0
```

PUC-Rio’s position: this is **not** an incompatibility, because `#` was never defined for non-sequences. In practice, code that relied on 5.4’s usual “last key / constructor length” for holey tables **breaks on 5.5**.

`ipairs` and TSTL `Array` helpers (`filter`, `map`, `length`, `join`, `for…of`) all use `#`. If `#` stops at the first hole, later keys exist in the table but are never visited.

### How it shows up in TSTL

TypeScript `undefined` / `null` in an array slot emit Lua `nil` (the key is absent). A literal like:

```typescript
const cueOrdinals = [
    prevActive,   // number
    prevPending,  // undefined
    newPending,   // undefined
    newActive,    // number
]
cueOrdinals.filter((o) => o !== undefined)
```

becomes a Lua table `{ prev, nil, nil, new }` with borders **1** and **4**. On MA **2.4 / Lua 5.4**, `#` often returned **4**, so `filter` still saw `new`. On MA **2.5 / Lua 5.5**, `#` often returns **1**, so `filter` only sees `prev`.

Live Sequence (2026-09-02, MA 2.5.0.3): `onActiveCueChanged` computed `newOrd=7` and `newVis=true` but `cueIndicesToUpdate` had `n=1` (previous cue only). Layout selection frames stopped updating after the first cell. Fix: **push only defined values** into a dense array; never use `undefined` as a placeholder to keep slots aligned.

### Rules

- Keep arrays **dense**. Build with `push` of defined values, not a fixed-length literal with optional slots.
- Do not use `undefined` as an index placeholder.
- Do not use `#`, `ipairs`, or TSTL `Array.*` to iterate a table that may contain `nil` holes. Use an explicit count, or `pairs` if key set (not order) is enough.

```typescript
// Bad — holes after TSTL emit
const xs = [a, b === undefined ? undefined : b, c]

// Good — dense
const xs: number[] = []
if (a !== undefined) xs.push(a)
if (b !== undefined) xs.push(b)
if (c !== undefined) xs.push(c)
```

---

## Other official 5.5 language incompatibilities (§8.1)

Not yet exercised as plugin bugs in this repo, but they apply to any Lua that MA 2.5 runs:

- `global` is a reserved word (unless `LUA_COMPAT_GLOBAL`).
- A chain of `__call` metamethods can have at most 15 objects.
- A `nil` error object is replaced by a string message.

Library/API incompatibilities (GC params, `lua_newstate` seed, `nresults` max 250, deprecated `lua_resetthread` / `lua_setcstacklimit`, etc.) matter mainly to MA’s C host, not typical plugin TypeScript.
