---
title: The Programmer
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/operate_programmer.html"
---

# The Programmer

Manual: the programmer is a **temporary memory** where edited values sit until stored or released. **Every user profile has a programmer.**

**Depth (layers):** [`../programmer.md`](../programmer.md).

## Layers

Each **attribute** can hold **different values on different layers at the same time** — in the programmer and after those values are stored into cues or presets. Selecting a layer chooses which slot you edit; the other slots stay.

Sets **ColorRGB_R** to 10 on the **Absolute** layer (other layers on that attribute are unchanged):

```
Attribute "ColorRGB_R" At Absolute 10
```

Full catalog (value / timing / step / phaser / sheet-view): [`../programmer.md`](../programmer.md). Phaser layers: [`../phasers.md`](../phasers.md).

## Three levels

1. **Selected fixture** — affected by encoder / command-line entries  
2. **Active** programmer values — can affect output; **only active values are stored**  
3. **Deactivated** programmer values — may still affect output, but Store will not keep them  

Selected fixtures show with yellow name/ID in the Fixture Sheet (manual System Colors).

## Blind

[`Blind`](../keywords/Blind.md) hides programmer values from output. Toggle with the Blind keyword. Entering Blind with values removes them from output; leaving Blind with values adds them. Program Time is **not** respected when entering/exiting Blind.

## Please / activate

To activate all attributes for the selected fixture: **Please twice** loads current values into the programmer; Please again deactivates. (See Please / related keys in the manual; prefer Keyword Specs for automation.)

## Off / KnockOut

Remove a value: [`Off`](../keywords/Off.md) then target the value. Feature groups can be released via Off + encoder bank (GUI). See also [`Knockout`](../keywords/Knockout.md).

## Clear levels

[`Clear`](../keywords/Clear.md) has three presses (manual):

1. **Deselect** fixtures — output unchanged; active values still storeable  
2. Values remain but become **deactivated** — storing now yields an empty cue  
3. **Clear all** — release values  

Hold Clear >1s also clears completely. Associated keywords: [`Clear`](../keywords/Clear.md), [`ClearSelection`](../keywords/ClearSelection.md), [`ClearActive`](../keywords/ClearActive.md), [`ClearAll`](../keywords/ClearAll.md).

## Freeze / Preview / Program Time

- Default: running sequences can override programmer priority. [`Freeze`](../keywords/Freeze.md) keeps programmer above playback for adjusted values.  
- [`Preview`](../keywords/Preview.md): separate programmer without stage output; **one shared preview programmer per session** (multi-user warning).  
- Program Time can time programmer fades (manual).

## Syntax-first examples

These commands select fixtures 1 through 5, set dimmer to 50 in the programmer, and store that look as Cue 2 of the selected sequence:

```
Fixture 1 Thru 5; At 50; Store Cue 2
```

Applies **preset 2.1** to fixture 1 in the programmer:

```
Fixture 1 At Preset 2.1
```

Toggles **Blind** (programmer values hidden from output while Blind is on):

```
Blind
```

**Off** with no object knocks out / stops the current target (programmer values or playback — confirm [`Off`](../keywords/Off.md) before automating a bare Off):

```
Off
```

**Clear** — first press deselects fixtures (three-press stack; see Clear levels above):

```
Clear
```

**ClearAll** releases the programmer in one step (selection and values):

```
ClearAll
```

- [`At`](../keywords/At.md) applies values live in the programmer. Relative `At` with `+`/`-`: see [`Plus`](../keywords/Plus.md).  
- [`Store`](../keywords/Store.md) / [`Update`](../keywords/Update.md) write show data (only **active** programmer values store).  
- Store options: full Official list on [`Store`](../keywords/Store.md) Option Keywords (e.g. `/Merge`, `/Overwrite`, `/CueOnly`, `/Look`, `/Selective`, `/NoConfirmation`, …) — also [`../keywords/options/`](../keywords/options/).

## Curated

- Layers (full list): [`../programmer.md`](../programmer.md).
- Selection helpers: [`Thru`](../keywords/Thru.md), [`Plus`](../keywords/Plus.md), [`Minus`](../keywords/Minus.md), [`If`](../keywords/If.md), [`Park`](../keywords/Park.md).  
- Grammar: [`../command-line.md`](../command-line.md).  
- Cue-command vs CmdLine multi-station: [`../multi-station.md`](../multi-station.md).
