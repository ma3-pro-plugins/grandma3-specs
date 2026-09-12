# Pure Lua Plugin References

Small snippets for specific pure-Lua plugin features. Runtime vs load-time args: see **Main function call arguments** in [`SKILL.md`](SKILL.md). Resolving handles and reading properties: [`../../../specs/plugin-access.md`](../../../specs/plugin-access.md).

## Object Hooks

Use object hooks when the plugin needs to react to changes on a grandMA3 object such as a group, sequence, macro, preset, or layout object.

```text
HookObjectChange(function:callback, light_userdata:handle, light_userdata:plugin_handle[, light_userdata:target]): integer:hook_id
```

Parameters inside `[...]` are optional.

Rules:

- Put injected plugin variables at the top of the Lua file.
- Define the hook callback as a root-scope function, not inside the returned main function.
- Register hooks with `HookObjectChange(callback, objectHandle, compHandle:Parent())`.
- Keep the returned main function focused on resolving the object handle and registering the hook.
- Store the hook ID in root scope if the plugin may need to unhook later.

```lua
local pluginName    = select(1,...)
local componentName = select(2,...)
local signalTable   = select(3,...)
local compHandle    = select(4,...)

local hookId = nil

local function onWatchedObjectChanged(obj, changeLevel)
    Echo('Object changed: ' .. tostring(obj) .. ', changeLevel=' .. tostring(changeLevel))
end

return function ()
    local watchedObject = GetObject('Group 1')

    if watchedObject == nil then
        Echo('Could not find object to hook')
        return
    end

    if hookId ~= nil then
        Unhook(hookId)
    end

    hookId = HookObjectChange(onWatchedObjectChanged, watchedObject, compHandle:Parent())
    Echo('Registered object hook for ' .. tostring(watchedObject))
end
```

- `compHandle` is the injected component handle from `select(4,...)`.
- `compHandle:Parent()` is the plugin handle required by `HookObjectChange`.
- `GetObject('Group 1')` is only an example.
