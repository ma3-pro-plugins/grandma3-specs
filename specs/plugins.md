# Plugins

- A plugin is installed in a showfile, as a `Plugin` object. In the `Plugins` Pool.
- The `Plugins` pool is within a `DataPool`
- Plugins can use Hooks to listen on MA object changes.
- A plugin would usually want to register hooks when the system start-up or when a show is loaded.
- Each station runs the plugin in its own separate LUA engine. All stations see the same MA objects.

## LUA Engine

- grandMA3 **2.4.x**: **Lua 5.4.8**. **2.5.x**: **Lua 5.5.0** (see [`versions.md`](versions.md#lua-engine)). Plugin migration notes: [`lua-5.4-to-5.5.md`](lua-5.4-to-5.5.md).

## Calling a plugin directly (observations)

When calling a plugin directly (example: running the command `Plugin 1`), where it runs depends on how it is invoked:

- CmdLine: Local station
- Macro: Local station
- Cue Command: Master station

### Command string length limit (~16K)

Empirical testing (playground plugins **Plugin Call Arg Length Caller** / **Plugin Call Arg Length Callee**, MA 2.3.2) shows that the **entire command string** passed to `Cmd()` — not just the plugin argument — is capped at roughly **16 KB**:

| Observation                                 | Value                                   |
| ------------------------------------------- | --------------------------------------- |
| Approx. max total command length            | **~16382 characters** (16384 − 2)       |
| Last confirmed working payload (quoted arg) | **16335** characters                    |
| First confirmed failure (doubling sweep)    | **16384** payload (total well over 16K) |

The limit applies to the full text of commands such as:

```text
Call Plugin "Plugin Call Arg Length Callee" "<payload>"
```

Fixed overhead (plugin name, quotes, keywords) reduces the usable argument size. With the callee name above, overhead is **46 characters**, so the argument tops out at roughly **16336 characters** (16382 − 46).

**Practical rule:** treat plugin string arguments as limited to **~16K**, but budget a few dozen characters for the rest of the command. Shorter plugin names allow slightly longer arguments; longer names reduce the budget.

This limit likely applies to any path that parses a full MA command string the same way — including **`RemoteCommand`** (see [`remote-command.md`](remote-command.md)). For payloads near the limit, prefer **`SendLuaMessage`** or other APIs not constrained by the command-line buffer.

### String argument quoting (JSON and escaped content)

Empirical testing with playground plugins **JSON Sender** / **JSON Receiver** (MA 2.3.2) shows how the **command-line quote wrapper** around a plugin string argument interacts with JSON payloads produced by `json.encode`. The same single-quote rules apply to **`RemoteCommand`** — see [`remote-command.md`](remote-command.md).

| Wrapper around plugin arg | JSON in arg | Result (local `Cmd()`)                                              |
| ------------------------- | ----------- | ------------------------------------------------------------------- |
| Double quotes `"..."`     | Yes         | **Fails at command parse** — `Illegal name:` before the callee runs |
| Single quotes `'...'`     | Yes         | **Works** — full `json.decode` roundtrip on arg 2                   |

**Double-quote wrapper breaks on JSON.** A command such as:

```text
Call Plugin "JSON Receiver" "{"caseId":"simple",...}"
```

does not reach the callee. The inner `"` characters from JSON string delimiters terminate the quoted argument early and the command parser rejects the remainder.

**Single-quote wrapper carries JSON reliably.** Because JSON uses double quotes for strings, wrapping the encoded payload in single quotes avoids that collision:

```text
Call Plugin "JSON Receiver" '{"caseId":"quotes","payload":{"msg":"He said \"hello\""}}'
```

Confirmed roundtrips (local `Cmd()`, arg received on **arg 2**):

- embedded double quotes in string values (`\"` in JSON)
- backslashes in string values (`\\` in JSON, e.g. `C:\Users\test`)
- nested objects, arrays, spaces, empty strings, and mixed payloads

**Receiver rule:** decode the **raw** plugin arg. Do **not** strip backslashes before `json.decode`. A receiver that applies `string.gsub(s, '\\', '')` (sometimes used for `RemoteCommand` relay normalization) corrupts JSON escapes and produces false failures or silently wrong values.

**Apostrophe edge case:** single-quote wrapping is unsafe when a JSON **string value** contains a literal `'` (apostrophe), because it terminates the outer command argument:

```text
Call Plugin "JSON Receiver" '{"msg":"it's fine"}'   -- breaks at it's
```

For arbitrary string content, either escape `'` in the command-layer wrapper, avoid single-quote wrapping for that payload, or use a non-JSON wire format (e.g. pipe-delimited prefix such as `__cprpc__|...`).

**Runtime args:** when a call succeeds, the plugin main function receives the string argument as **arg 2** (arg 1 is always the Display handle). See the write-plugin skill for arg parsing patterns.

## ReloadUI

This is a command the resets the LUA engine of a station.
A user can choose to run it anytime on a station.

## Plugin Initialization

When a plugin is initialized:
The root scope of a plugin can access the signalTable and other injected variables:

```lua
local pluginName    = select(1,...);
local componentName = select(2,...);
local signalTable   = select(3,...);
local my_handle     = select(4,...);
```

- signalTable: The plugin is provisioned a new signalTable on initialization
- pluginName: The name of the Plugin object
- componentName: The name of the lua component within the plugin
- my_handle: the handle of the lua component

A Plugin is initialized in the following cases:

- ReloadUI command is performed
- A new show is loaded
- Station is restarted

## SignalTable Lifecycle

Each plugin receives a **signalTable** from the MA3 platform. SignalTables have three key lifecycle properties:

1. **Per show**: when a show file is loaded, all signalTables from the previous show are deleted and new ones are provisioned for the plugins in the new show file.
2. **Per LUA engine**: if "ReloadUI" is triggered, the Lua engine restarts, all `_G` globals are cleared, and fresh signalTables are provisioned for each plugin.
3. **Per plugin**: a plugin cannot access another plugin's signalTable.

The signalTable ID therefore acts as a **show-scoped identity token** — if the signalTable has changed, the current show context has changed.

## Show Load & LUA Globals

When a new show is loaded:

- All global remain.
- The LUA engine itself does not not reset.
- Old plugins are cleaned.
- Old plugins' hooks die.
- New show's plugins gets reloaded (new signalTable)
