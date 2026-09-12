---
name: write-plugin
description: >-
  Write grandMA3 pure Lua plugin XML and Lua files (UserPlugin, ComponentLua,
  Note IDs). Use when creating or updating standalone Lua plugins. Requires an
  absolute gma3_library path from the user. Not for Pro Plugins framework plugins.
---

# Write Pure Lua Plugin

Create standalone grandMA3 Lua plugin files for playgrounds, prototypes, and small utilities.

## Output path

Do not guess a machine path. Before writing files, you need an absolute **`gma3_library`** (the user’s grandMA3 shared library root).

Typical locations (examples only — do not write here unless the user confirmed this is their library):

- macOS: `~/MALightingTechnology/gma3_library`
- Windows: `%USERPROFILE%\MALightingTechnology\gma3_library`

If the user has not given an absolute `gma3_library` in this chat, **ask once** and wait.

Default output:

```text
<gma3_library>/datapools/plugins/<PluginName>.xml
<gma3_library>/datapools/plugins/<PluginName>.lua
```

Use a subfolder (and matching XML `path` attribute) only when the user asks, e.g. `datapools/plugins/generated/` with `path="generated"`.

## Workflow

1. Determine the plugin name, author, version, and Lua behavior from the user request.
2. Create or update both files under the resolved plugins folder.
3. Set **`ComponentLua` `Installed`** deliberately:
   - **`Installed="No"`** — default for **multi-station** labs: Lua is embedded in the **show** on import; other stations do not need the `.lua` under their local `gma3_library`.
   - **`Installed="Yes"`** — Lua loads from `datapools/plugins/<path>/` on **each** machine. A station without that `.lua` beside the XML will not load the plugin.
4. Keep implementation in the `.lua` file, not in documentation.
5. If the plugin **reads** show objects (`GetObject` / `ObjectList` / `:Get` / parent-children), follow [`../../../specs/plugin-access.md`](../../../specs/plugin-access.md). If it needs object hooks, also read [`references.md`](references.md).
6. Read the files back and verify the XML `FileName` matches the Lua basename exactly.
7. In the final response, state the plugin name, plugin `Note`, and full paths.

## XML format (MA3 1.8+)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<GMA3 DataVersion="2.3.2.0">
    <UserPlugin Name="My Plugin" Version="1.0.0" Author="Your Name" path="" Note="your_name@my_plugin@v1_0_0">
        <ComponentLua FileName="My Plugin.lua" Installed="No" />
    </UserPlugin>
</GMA3>
```

If the files sit directly in `datapools/plugins/`, use `path=""` or omit a subfolder path. `ComponentLua FileName` is the Lua filename only, not a full path.

## Note ID

```text
author@plugin_name@vversion
```

- Author and plugin name are lowercase.
- Spaces become underscores.
- Version dots become underscores and are prefixed with `v`.
- Example: `ada@hello_world@v1_0_0`.

## Lua format

Minimal single-component plugin:

```lua
return function ()
    Echo('Hello World')
end
```

If the plugin needs injected MA3 component values:

```lua
local pluginName    = select(1,...)
local componentName = select(2,...)
local signalTable   = select(3,...)
local compHandle    = select(4,...)
```

### Main function call arguments (runtime)

When the plugin is **called** (`Call Plugin …`, macro, or `RemoteCommand`), MA3 invokes the **returned main function** with runtime args. These are **not** the same as the load-time `select(1,…)` injected values above.

| Index | Meaning | Example |
| --- | --- | --- |
| **1** | **Display handle** | `Display 1` |
| **2** | **Plugin string argument** (if any) | `wakeup` |
| 3+ | Additional comma-separated tokens | rare |

| Command | Runtime args |
| --- | --- |
| `Call Plugin 1` | `(Display 1)` |
| `Call Plugin 1 "wakeup"` | `(Display 1, "wakeup")` |
| `Call Plugin 1 my_action` | `(Display 1, my_action)` |

- Do **not** treat arg 1 as the action string — it is always the Display.
- Read the user action from **arg 2 onward**.
- When normalizing string args, strip surrounding quotes and stray backslashes from `RemoteCommand` relay.

```lua
return function (displayHandle, actionArg, ...)
    Echo('display=' .. tostring(displayHandle) .. ' action=' .. tostring(actionArg))
    if actionArg == 'wakeup' then
        return
    end
end
```

For object hook snippets, see [`references.md`](references.md).

## Verification

- Both files are under the user-provided `gma3_library` plugins folder.
- `ComponentLua FileName` matches the Lua basename.
- `Installed` is the intended value (`No` for multi-station playground unless every seat has the `.lua`).
- Do not run workspace formatters on generated plugin XML/Lua unless the user asks.
