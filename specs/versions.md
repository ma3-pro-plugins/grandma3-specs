# GrandMA3 versions

- Latest version tracked here: 2.5.0.x (Lua 5.5.0). 2.4.2.2 remains the last 2.4 line.

## Lua engine

Each station runs plugin code in its own Lua VM (see [`plugins.md`](plugins.md)).

| grandMA3 release | Lua version                                            |
| ---------------- | ------------------------------------------------------ |
| **2.5.x**        | **5.5.0** (MA: “Lua Core has been updated to Lua v5.5.0”) |
| **2.4.x**        | **5.4.8**                                              |
| Before 2.4.x     | Earlier Lua 5.4.x (exact patch level not tracked here) |

Plugin TypeScript is still transpiled with TSTL’s Lua **5.4** emit, but it **runs** on the engine above. Breaking 5.4 → 5.5 behavior (immutable `for` control variables, `#` on sparse arrays): [`lua-5.4-to-5.5.md`](lua-5.4-to-5.5.md).
