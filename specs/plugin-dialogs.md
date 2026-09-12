# Plugin Dialogs

**Source**: `mixed` (Help Dump MA 2.5.0.3, forum observed examples, grandma3-ts-types)

How a plugin presents UI: stock `MessageBox` vs building a custom dialog tree with `DialogFrame`, layout grids, and interactive controls.

## When to use MessageBox

`MessageBox` is an **official API** (Help Dump `grandMA3_lua_functions 2.5.0.3.txt`) for standard prompts with buttons, text inputs, checkboxes, and selectors. Use it when:

- The dialog fits a prompt + action buttons + a few inputs
- You want MA3's native styling automatically
- Multi-language handling is done by MA3
- The complexity stays within MessageBox's parameter structure

### MessageBox signature (official)

From `specs/lua-functions/grandMA3_lua_functions 2.5.0.3.txt`:

```lua
MessageBox({
  title: string,
  [backColor: string],
  [timeout: integer (ms)],
  [timeoutResultCancel: boolean],
  [timeoutResultID: integer],
  [icon: string],
  [titleTextColor: string],
  [messageTextColor: string],
  [autoCloseOnInput: boolean],
  message: string,
  [message_align_h: integer (Enums.AlignmentH)],
  [message_align_v: integer (Enums.AlignmentV)],
  [display: integer|lightuserdata],
  commands: {array of {value: integer, name: string, [order: integer]}},
  inputs: {array of {
    name: string,
    value: string,
    blackFilter: string,
    whiteFilter: string,
    vkPlugin: string,
    maxTextLength: integer,
    [order: integer]
  }},
  states: {array of {name: string, state: boolean, [order: integer]}},
  selectors: {array of {
    name: string,
    selectedValue: integer,
    values: table,
    [type: integer], -- 0=swipe, 1=radio
    [order: integer]
  }}
}): {
  success: boolean,
  result: integer,
  inputs: {array of [name] = value},
  states: {array of [name] = state},
  selectors: {array of [name] = selected-value}
}
```

`MessageBox` **blocks** the plugin thread until the user responds or the timeout expires. Returns a table with `success`, `result` (which command button was pressed), and the final values of all `inputs`, `states`, and `selectors`.

### MessageBox example

```lua
return function()
  local response = MessageBox({
    title = "Backup Settings",
    message = "Configure the backup",
    commands = {
      {value = 1, name = "OK"},
      {value = 0, name = "Cancel"}
    },
    inputs = {
      {name = "filename", value = "show_backup", blackFilter = "", whiteFilter = "", vkPlugin = "", maxTextLength = 64}
    },
    states = {
      {name = "include_presets", state = true}
    }
  })
  
  if response.success and response.result == 1 then
    Echo("File: " .. response.inputs.filename)
    Echo("Presets: " .. tostring(response.states.include_presets))
  end
end
```

## When to build a custom UI tree

Build a custom dialog when:

- The layout needs more structure than MessageBox supports (e.g. multi-row grids, tabs, scrollable lists)
- You need custom sizing, colors, or styling beyond MessageBox's optional parameters
- The dialog must respond to events without closing (live updates, multi-step wizards)
- You want finer control over widget placement and behavior

### How custom dialogs work

A plugin creates a UI tree under the **Display's ScreenOverlay**:

1. Get the Display handle (arg 1 when plugin is called, or `GetFocusDisplay()` / `GetDisplayByIndex(index)` — official Help Dump)
2. Append a root container to `display.ScreenOverlay` (or `display:Append(...)`)
3. Build the tree: `DialogFrame` with rows/columns, then child widgets (`Button`, `LineEdit`, `CheckBox`, `ScrollBox`, etc.)
4. The overlay is modal if you create a blocking container (e.g. `BaseInput`) — the dialog captures input until closed
5. Tear down the dialog manually (set to `nil` and Lua GC, or call a close callback if registered)

**Multi-station**: the dialog appears on the **station that runs the plugin call**. CmdLine / Macro run **local**; Cue Command runs **master** — same rules as plugin execution (see [`multi-station.md`](multi-station.md) / [`plugins.md`](plugins.md)).

The plugin function **does not automatically block** while the dialog is open. If you build a non-modal overlay and return immediately, the dialog stays visible but your plugin code ends. Use `coroutine.yield()`, a callback, or a MessageQueue to resume plugin logic when the user interacts.

### Proven UI classes (observed)

From **forum observed** (MA forum thread [UI Element List](https://forum.malighting.com/forum/thread/69718-ui-element-list/), user BakaCowpoke, Feb 2026) plus examples in public plugins:

**Commonly used containers and widgets** (observed in multiple working plugins):

- `BaseInput` — root modal container (shaded overlay, captures focus)
- `DialogFrame` — structured grid container with `Columns` / `Rows` properties and column/row sizing policy
- `TitleBar` — title bar with text (add `CloseButton` as a child)
- `CloseButton` — close button widget (append to `TitleBar`; appending directly to `DialogFrame` raises an error per forum)
- `UILayoutGrid` — general layout grid, same column/row API as `DialogFrame`
- `ScrollBox` — scrollable container (holds content larger than the visible area)
- `ScrollBarV` / `ScrollBarH` — vertical / horizontal scrollbar (set `ScrollTarget` to the `ScrollBox` handle)
- `Button` — clickable button with `Text` property
- `LineEdit` — single-line text input
- `CheckBox` — boolean checkbox
- `UIObject` — generic UI element (can hold properties like `Text`, `Anchors`, `H`, `W`, `Transparent`)
- `UiFader` — fader widget (observed)
- `ResizeCorner` — corner resize handle (observed)
- `TitleButton` — button in title bar (observed)

**Additional observed classes** (from forum code scan; may require specific parents or properties):

- `CmdlineEdit`, `ColorPickXYZ`, `ColorTestView`, `DialogHelp`, `EncoderBarSlot`, `EncoderControl`, `FilebrowserView`, `FixtureSheet`, `HardwareMiniEncoder`, `NetworkTestView`, `NormedTitleBar`, `ObjectView`, `PSRTreeViewFrame`, `ReferencesGrid`, `RotationButton`, `ScreenEncoderControl`, `SelectionView`, `ShaperPovFader`, `ShowHistoryGrid`, `SoundWaveView`, `SplitView`, `TexPageDebugView`, `TrackpadPanTiltControl`, `UiScreen`, `UiStationGrid`, `ViewBar`, `WindowMeshStatistics`

**Note**: MA3 has many internal UI classes. The lists above are observed from public examples. Do not invent class names — test or reference existing working plugin code when adding new widget types.

### Common properties (observed)

From forum examples and public plugins:

- **Sizing**: `H` (height), `W` (width) — integers (pixels) or strings (`"100%"` for stretch)
- **Anchors**: `Anchors = "col,row"` or `Anchors = {left = c1, right = c2, top = r1, bottom = r2}` — zero-indexed grid position
- **Text**: `Text = "Label"` — button/label text
- **Layout**: `Columns`, `Rows` — integer count for `DialogFrame` / `UILayoutGrid`
- **Column/row policy**: `dialogFrame[columnIndex][rowIndex].SizePolicy = "Fixed"|"Stretch"|"Content"` and `.Size = pixels` (for Fixed)
- **Transparency**: `Transparent = true|false`
- **Scroll target**: `scrollbar.ScrollTarget = scrollBoxHandle` (not a string path, a handle)
- **Expand content**: `ExpandContent = "Yes"|"No"` — whether container expands to fit children
- **Name**: `Name = "myWidget"` — internal name (for targeting or debugging)

### Display and Overlay API (official)

From `specs/lua-functions/grandMA3_lua_functions 2.5.0.3.txt`:

```lua
GetDisplayByIndex(integer:display_index): light_userdata:display_handle
GetFocusDisplay(nothing): light_userdata:display_handle
GetDisplayCollect(nothing): light_userdata:handle to DisplayCollect
GetDisplay(light_userdata:handle to UIObject): light_userdata:display_handle
GetDisplayIndex(light_userdata:handle to UIObject): integer:display_index

GetOverlay(light_userdata:handle to UIObject): light_userdata:overlay_handle
GetTopModal(nothing): light_userdata:handle to top modal overlay
GetTopOverlay(integer:display_index): light_userdata:handle to top overlay on the display
CloseAllOverlays(nothing): nothing
OverlaySetCloseCallback(light_userdata:handle to Overlay, callbackName:string[, ctx:anything]): nothing

WaitModal([number:seconds to wait]): handle to modal overlay or nil on failure(timeout)
```

Most plugins use `GetFocusDisplay()` or the Display arg 1 when called.

### Creating a dialog: basic pattern (observed)

From forum examples ([Scrolling UI](https://forum.malighting.com/forum/thread/8942-scrolling-ui/), [PopupInput](https://forum.malighting.com/forum/thread/69960-popupinput-and-custom-popups-custom-group-picker-and-more/)):

```lua
return function(displayHandle)
  local display = displayHandle or GetFocusDisplay()
  
  -- Root modal container
  local baseInput = display.ScreenOverlay:Append("BaseInput")
  baseInput.H, baseInput.W = 600, 800
  baseInput.Anchors = {left = 0, right = 0, top = 0, bottom = 0}
  
  -- Main layout frame
  local dlgFrame = baseInput:Append("DialogFrame")
  dlgFrame.Columns, dlgFrame.Rows = 2, 3
  dlgFrame.H, dlgFrame.W = "100%", "100%"
  
  -- Column/row sizing
  dlgFrame[1][1].SizePolicy = "Fixed"
  dlgFrame[1][1].Size = 60
  dlgFrame[1][2].SizePolicy = "Stretch"
  dlgFrame[2][1].SizePolicy = "Content"
  
  -- Title bar with close button
  local titleBar = dlgFrame:Append("TitleBar")
  titleBar.Anchors = "0,0"
  titleBar.Text = "My Plugin Settings"
  
  local closeBtn = titleBar:Append("CloseButton")
  -- CloseButton auto-closes the overlay on click
  
  -- Content row: add buttons, edits, checkboxes
  local okButton = dlgFrame:Append("Button")
  okButton.Anchors = "0,2"
  okButton.Text = "OK"
  okButton.H, okButton.W = 50, 120
  
  -- The dialog stays open until closed by user or plugin
  -- Return immediately (non-blocking) or use a callback/queue
end
```

### Scrollable content (observed)

From forum example ([Scrolling UI](https://forum.malighting.com/forum/thread/8942-scrolling-ui/)):

```lua
-- Scrollbar requires its own column
local dlgFrame = baseInput:Append("DialogFrame")
dlgFrame.Columns, dlgFrame.Rows = 2, 3
dlgFrame[2][2].SizePolicy = "Content"  -- scrollbar column

-- ScrollBox in one column
local boxHolder = dlgFrame:Append("UIObject")
boxHolder.Anchors = {left = 0, right = 0, top = 2, bottom = 2}

local scrollBox = boxHolder:Append("ScrollBox")

-- Scrollbar in adjacent column
local scrollBar = dlgFrame:Append("ScrollBarV")
scrollBar.Anchors = "1,2"
scrollBar.ScrollTarget = scrollBox  -- handle, not string

-- Content grid inside ScrollBox (size defines scrollable area)
local contentGrid = scrollBox:Append("UILayoutGrid")
contentGrid.H, contentGrid.W = 1200, 800
contentGrid.Columns, contentGrid.Rows = 2, 20
```

**Important**: `ScrollTarget` expects a **handle** (the `ScrollBox` variable), not a string path or `Name`. Defining the **content grid's size** (not the `ScrollBox`'s) controls the scrollable region.

### Tearing down a dialog

- **Automatic**: `CloseButton` appended to a `TitleBar` closes the overlay on click
- **Manual**: set the root container variable to `nil` (Lua GC cleans up MA references)
- **Callback**: `OverlaySetCloseCallback(overlayHandle, "callbackFunctionName", context)` (official Help Dump) — plugin function named `callbackFunctionName` is invoked when the overlay closes

When a plugin returns, the dialog remains visible until explicitly closed or MA3 tears down the overlay (e.g. on ReloadUI).

### Input and callbacks

**Blocking approach** (same station, one step):

- Use `MessageBox` — it blocks and returns all input values

**Non-blocking approach** (custom UI):

- Plugin returns immediately after creating the dialog
- Use a **Lua message queue** (`OpenMessageQueue` / `SendLuaMessage` — [`message-queue.md`](message-queue.md)) or a global callback to process button clicks asynchronously
- Set button/widget properties to invoke plugin functions via `Cmd()` or `RemoteCommand`
- Example: `button.Cmd = "Call Plugin 'MyPlugin' 'action=save'"` (observed pattern; property name may vary by widget)

**Coroutine yield**: some plugins use `coroutine.yield()` to pause execution while a dialog is open, then resume on callback. Not documented in Help Dump; observed in public plugin examples.

### Multi-station behavior

A dialog appears on the **station that runs the plugin call**:

- **CmdLine** → local station shows the dialog
- **Macro** → local station shows the dialog
- **Cue Command** → master station shows the dialog

Follower stations do **not** see the dialog unless the plugin explicitly sends commands to each station (e.g. via `RemoteCommand` — see [`remote-command.md`](remote-command.md)).

For cross-station UI, consider:

- Calling the plugin separately on each station via Macros or CmdLine
- Using `SendLuaMessage` to notify a background plugin on each station
- Storing shared state in show objects (`AddonVars`, global variables under the Root) and polling

See [`multi-station.md`](multi-station.md) for session / master / follower command routing.

## Related

- Plugin lifecycle, where calls run: [`plugins.md`](plugins.md)
- Multi-station / master / follower: [`multi-station.md`](multi-station.md)
- Plugin access (read objects): [`plugin-access.md`](plugin-access.md)
- Lua message queues: [`message-queue.md`](message-queue.md)
- Official Help Dump functions: [`object-api.md`](object-api.md)
- Lua enums for alignment, etc.: [`enums.md`](enums.md)
- Write-plugin skill: [`.agents/skills/write-plugin/SKILL.md`](.agents/skills/write-plugin/SKILL.md)
