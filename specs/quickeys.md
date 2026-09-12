---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/quickeys.html"
---

# Quickeys (Topic Spec)

Concept map (thin): [`concepts/quickeys.md`](concepts/quickeys.md). Keyword: [`keywords/Quickey.md`](keywords/Quickey.md) (shortcut **Q**).

Manual hub + subtopics: [Quickeys](https://help.malighting.com/grandMA3/2.5/HTML/quickeys.html), [Quickey Editor](https://help.malighting.com/grandMA3/2.5/HTML/quickeys_editor.html), [Use Quickey Pool Objects](https://help.malighting.com/grandMA3/2.5/HTML/quickeys_pool_objects.html), [Create Quickey](https://help.malighting.com/grandMA3/2.5/HTML/quickeys_example.html).

Quickeys are **soft versions of hardkeys and functions**. They live in the **Quickeys pool** (Data Pools). Assignable to Xkeys, layouts, and executors, or used directly from the pool.

## Address / edit

Opens the editor for Quickey 1 (Official + editor topic; enable **CLI** in pool settings for pool-tap edit):

```
Edit Quickey 1
```

General form (Official): `[Function] Quickey ["Quickey_Name" or Quickey_Number]`.

Official CLI example is **`Edit Quickey 1` only** ([`Quickey`](keywords/Quickey.md)). AssignmentButtonFunctionsQuickey (typings): `Empty` \| `Go+`. Prefer [`Assign`](keywords/Assign.md) Official forms when assigning a Quickey to Xkeys / layouts / executors.

## Pool object behavior (manual facts)

| LED (pool object) | Meaning |
| --- | --- |
| Black | Off (some codes never light, e.g. MENU / NUM1) |
| White | Active |
| Grey | Keyword entered into the command line |

Tap a pool object to activate/deactivate. **MA1** / **MA2** Quickeys can be latched (see Command area / Keys manual).

## Editor settings (GUI)

Pool object fields: Name, Scribble, Appearance, Tags, Note, Lock, **Code**. **Code** opens the hardkey/function list (filterable). Selecting a code first takes precedence over the function name for the pool label. Individual codes are documented under **Keys** in the manual (list codes from that chapter when needed).

Creating a Quickey is primarily **GUI** (Swipey → Edit on an empty pool object → Code → pick function). Example workflow uses `Fixture 9 Thru 13` then taps FULL / BLIND Quickeys — fixture selection is ordinary CLI:

```
Fixture 9 Thru 13
```

## Pool window settings (GUI)

Show Empty, Appearance, Pool Columns, Font Size, DataPool, Pool Color, Empty Color, Reset Colors, **CLI** (Command Line Interaction). Same pool-window pattern as other Data Pool windows — [`concepts/datapools.md`](concepts/datapools.md).

## Related

- Data pools: [`concepts/datapools.md`](concepts/datapools.md)
- Layouts (assign targets): [`layouts.md`](layouts.md), [`concepts/layouts.md`](concepts/layouts.md)
- Executors: [`concepts/executors.md`](concepts/executors.md)
- Keys / hardkey codes: manual Keys chapter (GUI reference)
