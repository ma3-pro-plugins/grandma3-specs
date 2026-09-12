---
title: DMX In and Out
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/dmx.html"
---

# DMX In and Out

There are several ways to get DMX in and out of grandMA3. Physical ports on devices can be inputs or outputs; DMX can also travel as Ethernet protocols (Art-Net / sACN). Behavior depends on whether it is a physical port or a network protocol, configured in Output Configuration.

**Topic Spec (depth — menus, refresh rates, Ethernet, priorities, park/tester pointers):** [`../dmx.md`](../dmx.md).

Opens Connector Configuration:

```
Menu "ConnectorConfig"
```

Opens the Art-Net protocols menu:

```
Menu "ArtNet"
```

## Related

- **Topic Spec:** [`../dmx.md`](../dmx.md)
- Patch / universes / DMX sheet: [`patch.md`](patch.md)
- Session Master outputs network DMX: [`networking.md`](networking.md), [`../multi-station.md`](../multi-station.md)
- DMX Remotes: [`remote-in-out.md`](remote-in-out.md)

Related keywords: [`DMXUniverse`](../keywords/DmxUniverse.md), [`Park`](../keywords/Park.md), menus above. Merge Mode / Input Priority enums and sACN \| Art-Net only: [`../dmx.md`](../dmx.md).
