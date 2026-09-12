---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/executor.html"
---

# Executors (Topic Spec)

Concept map (thin): [`concepts/executors.md`](concepts/executors.md). Keywords: [`keywords/Executor.md`](keywords/Executor.md), [`keywords/Page.md`](keywords/Page.md), [`keywords/Assign.md`](keywords/Assign.md), [`keywords/Specialexecutor.md`](keywords/Specialexecutor.md).

Manual hub + subtopics (one Spec): [Configurations](https://help.malighting.com/grandMA3/2.5/HTML/executor_configurations.html), [Assign](https://help.malighting.com/grandMA3/2.5/HTML/executor_assign.html), [Running Playbacks](https://help.malighting.com/grandMA3/2.5/HTML/executor_running_playbacks.html), [Special Executors](https://help.malighting.com/grandMA3/2.5/HTML/executor_special.html).

Executors are **handles** (physical keys / faders / encoders or virtual Playback Window) that send playback functions to an assigned pool object (often a sequence). Several executors may control the same object.

## Physical rows (lab — do not fork)

Canonical lab numbers live in [`hardware-layout.md`](hardware-layout.md) (`source: lab`). Short pointer:

| Range | Row (bottom→top) | Controls |
| --- | --- | --- |
| 101–190 | 1st | Key only |
| 201–290 | 2nd | Fader + key |
| 301–390 | 3rd | Encoder + key |
| 401–490 | 4th | Encoder + key |

Grouped in sets of 5 with a physical gap. Xkeys: X1–X8 ≈ executors **291–298**; X9–X16 ≈ **191–198** (manual What are Executors). If this disagrees with [`hardware-layout.md`](hardware-layout.md), trust that file.

## Pages

Stores executor **page 2** (optional name):

```
Store Page 2 /NoConfirmation
```

Syntax template from the manual: `Store Page [Page_Number] (["Page_Name"])`.

Page.executor addressing uses **dot as parent.child** (not cue decimals), e.g. `Page 2.301`.

## Assign objects and functions

Assigns **sequence 4** to executor **301** on page 2:

```
Assign Sequence 4 At Page 2.301
```

Assigns sequence 1 to executor **201** (fader row):

```
Assign Sequence 1 At Executor 201
```

Assigns **Go+** as the key function on executor 201:

```
Assign Go+ At Executor 201
```

Assigns **Pause** to page 8 executor 405:

```
Assign Pause At Page 8.405
```

Same with **MA+** key layer (`/MA`):

```
Assign Pause At Page 8.405 /MA
```

Assigns **FaderRate** to executor 209:

```
Assign FaderRate At Executor 209
```

Clears the fader assignment on page 1 executor 201 (Official Set example):

```
Set Page 1.201 Property "Fader" "Empty"
```

Unattended Assign: [`/NoConfirmation`](keywords/options/Noconfirmation.md) when Official lists it ([`automation.md`](automation.md)):

```
Assign Sequence 1 At Executor 201 /NoConfirmation
```

Handle functions from the Assign menu (confirm each Keyword Spec before use): Go+, Go-, Goto, Pause, Off, On, Toggle, Select, Top, Temp, Flash, Call, HalfSpeed, DoubleSpeed, Master / Rate / Speed fader keywords, custom commands, etc.

## Configurations / running playbacks / special

Executor Configurations are pool objects edited from the Assign menu (GUI) — save/load configs there; do not invent config CLI.

Running Playbacks / Off Menu are GUI for seeing and killing playbacks (`Off` family — [`Off`](keywords/Off.md)).

Special Executors / Custom Master Section: grand master on special executor 5, default playback buttons, page area — see [`Specialexecutor`](keywords/Specialexecutor.md) and the manual Special Executors topic. Prefer `Assign Master 2.1 At …` patterns from [`masters.md`](masters.md) over inventing special-executor-only syntax.

## Playback via executor

Sends Go+ to the object on executor 101:

```
Go+ Executor 101
```

Bare sequence playback without an executor: [`cues-sequences.md`](cues-sequences.md).

## Related

- Lab layout (canonical rows): [`hardware-layout.md`](hardware-layout.md)
- Masters: [`masters.md`](masters.md)
- Sequences / cues: [`cues-sequences.md`](cues-sequences.md)
- Data pools / pages: [`concepts/datapools.md`](concepts/datapools.md)
- Group masters on executors: [`groups.md`](groups.md)
