---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/dmx.html"
---

# DMX (Topic Spec)

Concept map (thin): [`concepts/dmx.md`](concepts/dmx.md). Related keywords: [`DMXUniverse`](keywords/DmxUniverse.md), [`DMXAddress`](keywords/DmxAddress.md), [`Park`](keywords/Park.md), [`Menu`](keywords/Menu.md), [`Off`](keywords/Off.md). Patch-side universe list / DMX sheet / tester examples: [`patch.md`](patch.md).

Manual hub + subtopics (one object): [DMX Port Configuration](https://help.malighting.com/grandMA3/2.5/HTML/dmx_port_config.html), [Ethernet DMX](https://help.malighting.com/grandMA3/2.5/HTML/dmx_ethernet.html), [DMX Priorities](https://help.malighting.com/grandMA3/2.5/HTML/dmx_priorities.html).

Physical XLR ports and Ethernet protocols (Art-Net / sACN) get DMX in or out of the system. Port/protocol tables are mostly **GUI** in Output Configuration / DMX Protocols — do not invent `Set` property names for port rows.

**Session Master outputs network DMX** (Art-Net / sACN): one-line depth in [`multi-station.md`](multi-station.md) / [`concepts/networking.md`](concepts/networking.md). Visual send/receive feedback can differ per station — judge real I/O on the master.

## Refresh rate (hub)

ANSI E1.11 allows a wide range; grandMA3 rules:

- Entire universe each send
- Max **30 Hz**, min **1 Hz**, default **30 Hz**
- Rate can drop (not below min) on quiet universes for XLR ports in **RDM** mode and for Art-Net / sACN
- XLR ports set to **Out** do not slow the rate
- Universes may run at different rates

## Open configuration menus (CLI)

Opens **Connector Configuration** (Output Configuration — XLR ports, and columns for SMPTE / MIDI / DC / Ethernet):

```
Menu "ConnectorConfig"
```

Opens **Connector View**:

```
Menu "ConnectorView"
```

Opens **Art-Net** DMX Protocols menu:

```
Menu "ArtNet"
```

Opens **sACN** DMX Protocols menu:

```
Menu "sACN"
```

Port list: devices matched by IP; prefer **device name** over the changing No index. Title-bar **Session** filter: All vs In Session. Column modes: Full / Condensed / XLR Only. Merge Mode and Input Priority for incoming DMX are set per universe/port in this GUI (see priorities below).

## Ethernet DMX

Supported protocols: **sACN** and **Art-Net**. Configure in DMX Protocols (menus above). Protocol-specific transmit/receive rows and multicast/unicast choices are **GUI** — confirm any CLI against Keyword Specs before inventing.

## DMX priorities (resolve competing sources)

Common stack (highest → lower), from the manual:

1. External input (sACN / Art-Net / DMX In / PSN) — behavior depends on Merge Mode (**Prio**, **HTP**, **LowTP**, **Off**) and Input Priority (**Super**, **Prog**, **Highest**, **High**, **LTP**, **Low**, **Lowest**)
2. **DMX Tester**
3. **Parked** values
4. Playbacks with **Super** priority
5. Programmer with **Freeze** enabled
6. Standard playback priorities: Swap → HTP → Highest → High → LTP → Low → Lowest
7. Programmer with Freeze disabled

Merge behaviors: **HTP** (highest dimmer) / **LTP** (latest attribute). Output modifiers after that: Grand Master → World Masters → Group Masters. Selection overrides: Highlight / Lowlight / Solo (do **not** affect parked values).

## Park / tester CLI

Parks all attributes of fixture **1**:

```
Park Fixture 1
```

Parks the current selection:

```
Park
```

Tester / clear-tester forms live with universe addressing in [`patch.md`](patch.md) (`DMXUniverse … At …`, `Off DMXUniverse Thru`).

## Related

- Patch universes / sheet: [`patch.md`](patch.md), [`concepts/patch.md`](concepts/patch.md)
- Session Master / network DMX: [`multi-station.md`](multi-station.md), [`concepts/networking.md`](concepts/networking.md)
- DMX Remotes: [`concepts/remote-in-out.md`](concepts/remote-in-out.md)
- Timecode SMPTE/MIDI columns on ConnectorConfig: [`timecode.md`](timecode.md)
