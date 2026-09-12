---
title: Patch and Fixture Setup
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/patch.html"
---

# Patch and Fixture Setup

Fixtures must be added to the show file before they can be controlled. That happens in **Patch** (fixture types, attribute definitions, parameter list, DMX universes, stages, DMX curves, 3D placement, live patch, MVR, classes/layers).

**Depth** (patch address CLI, multipatch, universe/tester, live vs full patch, stages/layers, short 3D/camera facts): [`../patch.md`](../patch.md).

## Syntax pointers

After fixtures exist, address them with [`Fixture`](../keywords/Fixture.md) (and store selections as [`Group`](../keywords/Group.md) — [`groups.md`](groups.md)). Patch CLI, FixtureClass/Camera Official examples, and typings CameraType/CameraMode: Topic Spec [`../patch.md`](../patch.md); keywords [`../keywords/_index.md`](../keywords/_index.md).

Patches **fixture 2** to universe **3**, address **123**:

```
Patch Fixture 2 3.123
```

Selects multipatch **2** of fixture **4**:

```
Fixture 4 Multipatch 2
```

## Related

- Topic Spec: [`../patch.md`](../patch.md)
- Operating fixtures / selection: [`operate-fixtures.md`](operate-fixtures.md)
- Groups: [`groups.md`](groups.md)
- DMX in/out: [`dmx.md`](dmx.md)
