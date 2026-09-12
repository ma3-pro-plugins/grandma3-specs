---
title: Timecode Show
topic_spec: ../timecode.md
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/timecode.html"
---

# Timecode Show

A timecode show executes events and can move faders against a running time counter (internal timecode from the session master, or an external source). Shows are organized as **Tracks** inside a **Track Group**, stored in the Timecode pool.

**Topic Spec (depth — store/set/play CLI, slots, track groups, viewer/markers/events facts):** [`../timecode.md`](../timecode.md).

Keywords: [`Timecode`](../keywords/Timecode.md), [`Timecodeslot`](../keywords/Timecodeslot.md). Prefer Object API for track edits. Session master for internal timecode: [`../multi-station.md`](../multi-station.md).

Stores a new timecode show named **Napalm Skies**:

```
Store Timecode "Napalm Skies" /NoConfirmation
```

Starts show **Prelude**:

```
Go Timecode "Prelude"
```

Part of Data Pools: [`datapools.md`](datapools.md).

## Related

- **Topic Spec:** [`../timecode.md`](../timecode.md)
- Data pools: [`datapools.md`](datapools.md)
- Multi-station: [`../multi-station.md`](../multi-station.md)
