---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/masters.html"
---

# Masters (Topic Spec)

Concept map (thin): [`concepts/masters.md`](concepts/masters.md). Keyword: [`keywords/Master.md`](keywords/Master.md).

Manual hub + subtopics (one Spec): [Selected](https://help.malighting.com/grandMA3/2.5/HTML/masters_selected.html), [Grand](https://help.malighting.com/grandMA3/2.5/HTML/masters_grand.html), [Highlight / Lowlight / Solo](https://help.malighting.com/grandMA3/2.5/HTML/highlight_lowlight_solo.html), [Time Control](https://help.malighting.com/grandMA3/2.5/HTML/masters_grand_time.html), [Speed](https://help.malighting.com/grandMA3/2.5/HTML/masters_speed.html), [Playback](https://help.malighting.com/grandMA3/2.5/HTML/masters_playback.html), [Timing](https://help.malighting.com/grandMA3/2.5/HTML/masters_timing.html).

Masters are **level / rate / speed / timing overrides**. Address with `Master Category.Index` (dot = parent.child). Assign them onto executors like any other object.

**Group Masters stay in** [`groups.md`](groups.md) (manual [Group Masters](https://help.malighting.com/grandMA3/2.5/HTML/group_master.html)) — one-line link only; do not fork that family here.

## Categories (manual indexes)

| Category | Role | Examples (manual names) |
| --- | --- | --- |
| **1.x Selected** | Masters for the **selected sequence** | 1.1 Master (intensity), 1.2 XFade, 1.3 XFadeA, 1.4 XFadeB, 1.5 Temp, 1.6 Rate, 1.7 Speed, 1.8–1.10 Highlight/Lowlight/Solo (selected — **not** the functional grand H/L/S), 1.11 Time |
| **2.x Grand** | Show-wide | 2.1 Grand Master, 2.2 World, 2.3 Highlight, 2.4 Lowlight, 2.5 Solo, 2.6 Rate, 2.8 ProgramTime, 2.9 ProgramXFade, 2.10 ExecutorTime, 2.11 ExecutorXFade, 2.12 Blind, 2.13–2.15 Sound* |
| **3.x Speed** | Global speed masters (0–225 BPM) | `Master 3.1`, `Master 3."Speed1"` |
| **4.x Playback** | Playback masters | `Master 4.3` |
| **Timing** | Named timing masters | `Master "Timing"."Timing1"` |

Confirm indexes/names on [`Master`](keywords/Master.md) before inventing categories.

## Assign masters to executors

Assigns **selected-sequence master** (1.1) to executor 206:

```
Assign Master 1.1 At Executor 206
```

Assigns **grand master** (2.1) to executor 207:

```
Assign Master 2.1 At Executor 207
```

Assigns **playback master 3** to page 6 executor 209:

```
Assign Master 4.3 At Page 6.209
```

Assigns **timing master Timing1** to page 1 executor 216:

```
Assign Master "Timing"."Timing1" At Page 1.216
```

[`Assign`](keywords/Assign.md) lists [`/NoConfirmation`](keywords/options/Noconfirmation.md) — use it for unattended assign when a pop-up would appear ([`automation.md`](automation.md)):

```
Assign Master 2.1 At Executor 207 /NoConfirmation
```

## Speed masters

Sets speed master 3.1 to **42 BPM**:

```
Master 3.1 At BPM 42
```

Same master by name, **2 Hz** / **0.69 s** (separate fences):

```
Master 3."Speed1" At Hz 2
```

```
Master 3."Speed1" At Seconds 0.69
```

Labels speed master 3.2:

```
Label Master 3.2 "Great Speed"
```

SpeedScale / LearnMode are speed-master properties (GUI / Assign menu) — confirm before inventing `Set Master … Property` CLI. Related: [`Speed`](keywords/Speed.md), [`Doublespeed`](keywords/Doublespeed.md), [`Halfspeed`](keywords/Halfspeed.md), [`Learnspeed`](keywords/Learnspeed.md), [`Faderspeed`](keywords/Faderspeed.md).

## Highlight / Lowlight / Solo

Functional H/L/S are the **grand** masters (2.3–2.5), not the selected-sequence 1.8–1.10 placeholders. Keywords: [`Highlight`](keywords/Highlight.md), [`Lowlight`](keywords/Lowlight.md), [`Solo`](keywords/Solo.md).

Toggles highlight on the current selection:

```
Highlight
```

Turns highlight off:

```
Highlight Off
```

```
Solo On
```

```
Solo Off
```

```
Lowlight
```

Store / At highlight or lowlight values (Official):

```
Store Highlight
```

```
At Highlight
```

```
Store Lowlight
```

```
At Lowlight
```

Manual walk-through uses selection then Highlight/Lowlight/Solo keys — e.g. select then Highlight Off:

```
Fixture 1 Thru 10; Highlight Off
```

## Time control / timing masters

Program Time / Executor Time / ProgramXFade / ExecutorXFade live under grand masters (2.8–2.11) and the Time Control topic. Sequence setting **Use Executor Time** ties cue playback to ExecutorTime.

Goto using a timing master name as fade:

```
Goto Cue 5 Fade "Timing5"
```

## Related

- Group Masters: [`groups.md`](groups.md)
- Executors: [`executors.md`](executors.md)
- Sequences / cue timing: [`cues-sequences.md`](cues-sequences.md)
- Worlds (World grand master): [`concepts/worlds-filters.md`](concepts/worlds-filters.md)
