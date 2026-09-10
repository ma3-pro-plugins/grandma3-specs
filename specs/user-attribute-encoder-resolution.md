# Handoff: UserAttributePreferences EncoderResolution (Default)

**Audience:** next agent working on encoder resolution / user attribute preferences.  
**Status:** Confirmed on console via playground Lua (2026-08-10).  
**Playground plugins used in the lab:**

- `Toggle Encoder Resolutions Fine` — snapshot → Fine → revert (handles Default)
- `Print Encoder Resolutions` / `Set Encoder Resolutions Fine|Coarse` — related labs

---

## Object path

Per-attribute **user** encoder resolution lives under the current user profile:

```lua
local prefs = CurrentProfile().UserAttributePreferences
```

- Class path shape: `ShowData.UserProfiles.<profile>.UserAttributePreferences.<AttributeName>`
- This is **not** the patch Attribute definition at  
  `ShowData.LivePatch.AttributeDefinitions.Attributes.*`

Typings: `UserAttribute.EncoderResolution` → `Enums.AttriebuteEncoderResolution`  
(also `AttriebuteEncoderResolutionDefault` which includes **Default = 0** — note MA’s spelling `Attriebute`).

---

## Enum values (raw)

From `Enums.AttriebuteEncoderResolutionDefault`:

| Name        | Raw number   |
| ----------- | ------------ |
| Native      | -16777216    |
| **Default** | **0**        |
| Increment   | 167772       |
| Fine        | 1677721      |
| Coarse      | 16777216     |

`Enums.AttriebuteEncoderResolution` is the same without `Default`.

---

## How to identify Default (inherited)

When the profile has **Default** selected, `Get` does **not** return `0`. It returns the **effective** resolution from the attribute definition (often Coarse), and `tostring` wraps it in angle brackets:

| Stored state | Typical `tostring(Get(...))` | Meaning                                      |
| ------------ | ---------------------------- | -------------------------------------------- |
| Default      | `<Coarse>` / `<Fine>` / …    | Inherited from patch attr def — **Default**  |
| Explicit     | `Coarse` / `Fine` / number   | Profile override — **not** Default           |

### Detection rule (use this)

```lua
local function isInheritedDefault(value)
    if value == nil then return false end
    local s = tostring(value)
    return string.sub(s, 1, 1) == '<' and string.sub(s, -1) == '>'
end
```

Do **not** treat a read of `Coarse` / `16777216` / `<Coarse>` as “store Coarse for later restore” when the brackets are present — restoring that value makes an **explicit** Coarse and loses Default.

Optional roles (display vs raw-ish):

```lua
attr:Get('EncoderResolution')                           -- often shows <Coarse> when Default
attr:Get('EncoderResolution', Enums.Roles.Display)
attr:Get('EncoderResolution', Enums.Roles.Edit)
attr:Get('EncoderResolution', Enums.Roles.Default)       -- Roles.Default = 0; still may show <> form
```

There is **no** `Enums.Roles.Raw`.

---

## How to set Default

Write **`0`** (or the enum constant), not the effective `<Coarse>` handle:

```lua
attr.EncoderResolution = 0
-- or
attr.EncoderResolution = Enums.AttriebuteEncoderResolutionDefault.Default
-- or
attr:Set('EncoderResolution', 'Default')  -- also works in lab; prefer enum/0 in plugins
```

After a successful Default write, a subsequent Get/`tostring` typically shows `<Coarse>` (or whatever the attr def’s default is) again.

Set Fine / Coarse explicitly:

```lua
attr.EncoderResolution = Enums.AttriebuteEncoderResolution.Fine
attr.EncoderResolution = Enums.AttriebuteEncoderResolution.Coarse
```

Property assign (`attr.EncoderResolution = …`) is the reliable write path used by playground code. `:Set('encoderResolution', …)` with wrong casing can fail silently; prefer `'EncoderResolution'`.

---

## Iterating attributes (important)

`prefs[1]` may work (often Dimmer), but **`prefs[2]` is often nil** even when hundreds of children exist.

Always use:

```lua
local attrs = prefs:CmdlineChildren()  -- dense 1..N, names like Dimmer, Pan, …
-- fallbacks: prefs:Children() or prefs:Count() with care
```

Lab confirmation: `Count=390`, `CmdlineChildren=390`, `c[1]=Dimmer`, `c[2]=Pan`, while `prefs[2]` was nil.

Named access also works: `prefs.Dimmer`, `prefs.Pan`.

---

## Snapshot / toggle pattern

When temporarily forcing Fine and later restoring:

1. **Read** with `attr:Get('EncoderResolution')` (or `.EncoderResolution`).
2. If `isInheritedDefault(value)` → **save `0`**.
3. Else → save the explicit value (Fine / Coarse / number / enum).
4. Set all to Fine.
5. On revert, write the saved values (so Defaults become `0` again).

Reference implementation:  
`generated/Toggle Encoder Resolutions Fine.lua`  
(`[ToggleEncoderResFine]` log prefix).

---

## Quick cmdline probes

```text
Lua "Echo(tostring(Enums.AttriebuteEncoderResolutionDefault.Default))"
```

```text
Lua "local a=CurrentProfile().UserAttributePreferences:CmdlineChildren()[1]; Echo(tostring(a.name)..'='..tostring(a:Get('EncoderResolution')))"
```

```text
Lua "local a=CurrentProfile().UserAttributePreferences:CmdlineChildren()[1]; a.EncoderResolution=Enums.AttriebuteEncoderResolution.Fine; Echo('fine='..tostring(a:Get('EncoderResolution'))); a.EncoderResolution=0; Echo('after0='..tostring(a:Get('EncoderResolution')))"
```

---

## Pitfalls

- Restoring the tostring/`Get` value when it is `<Coarse>` **breaks** Default (becomes explicit Coarse).
- Numeric index on `UserAttributePreferences` is unsafe past `[1]`.
- Patch `Attribute.EncoderResolution` (fixture type / attr def) is a different object from user preferences.
- Plugin-scope locals survive across `Call Plugin` until component reload / show reload — toggle “active” state can be stale after editing the `.lua` if `Installed="No"` embedded content wasn’t refreshed.
