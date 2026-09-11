---
title: Networking
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/network.html"
---

# Networking

Networking expands a standalone station into a system: sessions, Ethernet DMX (Art-Net / sACN), MVR-xchange, World Server / internet, and station control.

Open the Network menu:

```
Menu "Network"
```

## Session (summary)

From the manual Session topic:

- Controlling devices are **Stations**.
- A session always has a **Master**, a unique **Session Index** (not user-set), matching **Session Name**, **Location**, and **Key**.
- Members need the same **Streaming Version** (first three version numbers).
- All **DMX network protocols output from the Master** only.
- Same user on consoles → Full-Tracking Mode; different users → Multi-User Mode.
- Devices may Join / Leave / Invite / Dismiss (Network menu).

## Multi-station depth (do not duplicate here)

Master/follower, **where CmdLine / Macro / Cue Command / plugins run**, and OSC relay in a session: **[`../multi-station.md`](../multi-station.md)**.

Network object API: [`../api-objects-network.md`](../api-objects-network.md).

## Subtopics (manual)

Interfaces and IP · Session · Web Remote · Network Design · Network Tests · Regulations · Station Control.
