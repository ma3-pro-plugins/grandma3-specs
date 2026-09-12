---
title: Worlds and Filters
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/worldfilter.html"
---

# Worlds and Filters

Worlds and filters are programming / playback tools (both are pool windows). The selected world and the selected or called filter always dictate what the programmer can touch.

- **Worlds** limit access to fixtures and attributes (especially useful in multi-user so each user works in a designated world).
- **Filters** block attributes from passing (typically store, update, recall, or sheet masking).

Worlds and filters can be assigned to objects (sequence, preset) and to sheets for masking.

**Depth:** [`../worlds-filters.md`](../worlds-filters.md).

Stores **world 5** from the current programmer selection / active attributes:

```
Store World 5 /NoConfirmation
```

Calls **world 5** (limits programmer access):

```
World 5
```

Calls **filter 4**:

```
Filter 4
```

Keywords: [`World`](../keywords/World.md), [`Filter`](../keywords/Filter.md). Do not invent filter syntax.

Part of Data Pools: [`datapools.md`](datapools.md). Multi-user session: [`users.md`](users.md), [`../multi-station.md`](../multi-station.md).
