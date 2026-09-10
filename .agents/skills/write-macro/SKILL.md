---
name: write-macro
description: >-
  Write grandMA3 macro XML files (Macro, MacroLine, waits, quoting). Use when
  creating or updating macros. Requires an absolute gma3_library path from the
  user. Not for Pro Plugins refresh macros or project-specific pool paths.
---

# Write Macro

Create grandMA3 macro XML files under the user’s shared library.

## Output path

Do not guess a machine path. Before writing files, you need an absolute **`gma3_library`**.

Typical locations (examples only — do not write here unless the user confirmed this is their library):

- macOS: `~/MALightingTechnology/gma3_library`
- Windows: `%USERPROFILE%\MALightingTechnology\gma3_library`

If the user has not given an absolute `gma3_library` in this chat, **ask once** and wait.

Default output:

```text
<gma3_library>/datapools/macros/<Macro Name>.xml
```

Use another folder only when the user asks.

## Workflow

1. Determine the macro name and ordered macro lines from the user request.
2. If a similar macro exists in that folder, read it first and follow its naming, command, and wait conventions.
3. Create or update one XML file named `<Macro Name>.xml`.
4. Indent with 4 spaces.
5. Verify every `Command` attribute is XML-escaped.

## XML format

```xml
<?xml version="1.0" encoding="UTF-8"?>
<GMA3 DataVersion="2.3.2.0">
    <Macro Name="Macro Name" Guid="AA BB CC DD EE FF 00 11 22 33 44 55 66 77 88 99">
        <MacroLine Name="Optional Line Name" Command="Command text"/>
        <MacroLine Command="Command with &quot;quoted&quot; values" Wait="1.000"/>
    </Macro>
</GMA3>
```

## MacroLine rules

- Preserve the requested command order.
- Include `Name="..."` only when the user asked for a line name or a label is useful.
- Include `Wait="N.NNN"` only when a delay is requested or needed. Use three decimal places (`Wait="2.000"`).
- Escape XML attribute values: `"` → `&quot;`, `&` → `&amp;`, `<` → `&lt;`, `>` → `&gt;`.
- Do not escape normal spaces inside grandMA3 commands.

## GUID rules

- Keep a `Guid` on the `Macro` element when matching the export format.
- Do not add `Guid` attributes to generated `MacroLine` elements.
- Preserve an existing `MacroLine` `Guid` only when editing an existing macro and that line identity matters.
- Format GUIDs as 16 uppercase hex byte pairs separated by spaces:

```text
6C 7E 67 C2 0B EC 7A 07 26 7A D8 C0 38 2A 94 E7
```

## Example

For lines:

```text
Unlock Plugin 1
Set Plugin 1 path "My Plugins/Demo"
ReloadUI
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<GMA3 DataVersion="2.3.2.0">
    <Macro Name="Example Refresh" Guid="AA BB CC DD EE FF 00 11 22 33 44 55 66 77 88 99">
        <MacroLine Command="Unlock Plugin 1"/>
        <MacroLine Command="Set Plugin 1 path &quot;My Plugins/Demo&quot;"/>
        <MacroLine Name="RefreshAll" Command="ReloadUI"/>
    </Macro>
</GMA3>
```

## Verification

- Read the file back: XML declaration, `GMA3` root, `Macro`, and every requested `MacroLine`.
- Confirm the path is under the user-provided `gma3_library` macros folder.
- Do not run workspace formatters on generated macro XML unless the user asks.
