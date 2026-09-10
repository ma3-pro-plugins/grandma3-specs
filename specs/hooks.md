# Hooks

- A Plugin can register a hook, which is a listener on some change in an Object which is exposed by MA Object API.
- Hooks are always fired LOCALLY (on the station where the hook was registered).

## Object hooks (`HookObjectChange`)

Typical registration:

```lua
HookObjectChange(callback, objectHandle, pluginHandle)
-- callback(obj, changeLevel)
```

`changeLevel` is an `Enums.ChangeLevel` value. In Lua logs, Structural often appears as the numeric value `8`.

## Patch changes and Group hooks

Group object hooks do **not** fire for every patch edit that changes output distribution.

Observed on grandMA3 **2.4.2.2** (playground isolation with `HookObjectChange` on many Groups):

| Patch action | Output distribution | Group hooks (`changeLevel` Structural / `8`) |
| --- | --- | --- |
| Create / delete FixtureType (non-event for groups) | often unchanged | no |
| Create / delete empty Stage | often unchanged | no |
| Add / delete a normal (non-Universal) fixture | may change | **no** (TRU can still run) |
| Add / delete a fixture whose FixtureType has **`SpecialPurpose="Universal"`** (typically patched as **Generic** ID type) | changes | **yes — all hooked Groups**, even Groups that do not contain that fixture |

### Universal SpecialPurpose fixture types

FixtureTypes with **Special Purpose = Universal** (LiveFX example: `pro_plugins@live_fx@…@GeneratorUniversalFixture`, XML `SpecialPurpose="Universal"`) are special in the patch:

- Adding or removing such a fixture (e.g. via `AddFixtures` with `idtype="Generic"`, or the same FT from the Patch UI) triggers a Content TRU that **Structural-notifies hooked Group objects**.
- A manual add of a conventional Fixture-ID library type can still log `Output: distribution changed` and finish TRU **without** calling Group hooks.
- CID value alone is not the distinguishing factor; the Universal SpecialPurpose fixture type (and the Generic/Universal fixture path) is.

### Practical implication

Plugins that create/destroy Universal SpecialPurpose fixtures (LiveFX generator universal fixture, similar assets) should expect **broadcast Structural Group hooks** after leaving patch edit-setup / TRU — not only hooks on Groups that reference the new fixture. Filter or debounce accordingly if Group content did not actually change.
