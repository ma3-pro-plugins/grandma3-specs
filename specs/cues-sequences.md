---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/cue_sequence.html"
---

# Cues and Sequences (Topic Spec)

Concept map (thin): [`concepts/cues-sequences.md`](concepts/cues-sequences.md). Keywords: [`keywords/Sequence.md`](keywords/Sequence.md), [`keywords/Cue.md`](keywords/Cue.md).

Manual hub + subtopics (one Spec, not fifteen): [Tracking](https://help.malighting.com/grandMA3/2.5/HTML/cue_tracking.html), [Sequence Sheet](https://help.malighting.com/grandMA3/2.5/HTML/cue_sequence_sheet.html), [Content Sheet](https://help.malighting.com/grandMA3/2.5/HTML/cue_content_sheet.html), [Sequence Settings](https://help.malighting.com/grandMA3/2.5/HTML/cue_sequence_settings.html), [Store](https://help.malighting.com/grandMA3/2.5/HTML/cue_store.html), [Update](https://help.malighting.com/grandMA3/2.5/HTML/cue_update.html), [Copy](https://help.malighting.com/grandMA3/2.5/HTML/cue_copy.html), [Cue Recipes](https://help.malighting.com/grandMA3/2.5/HTML/cue_recipe.html), [Store Settings / Preferences](https://help.malighting.com/grandMA3/2.5/HTML/cue_store_settings_preferences.html), [Playback](https://help.malighting.com/grandMA3/2.5/HTML/cue_playback.html), [MIB](https://help.malighting.com/grandMA3/2.5/HTML/cue_mib.html), [Timing](https://help.malighting.com/grandMA3/2.5/HTML/cue_timing.html), [Renumber](https://help.malighting.com/grandMA3/2.5/HTML/cue_renumber.html), [Delete](https://help.malighting.com/grandMA3/2.5/HTML/cue_delete.html).

Looks (fixture values) live in **cues** inside **sequences**. A sequence is a ordered cue list with tracking, timing, MIB, and playback settings. Cue **IDs may be decimals** (`0.001`–`9999.999`); other objects use dot as **parent.child** (e.g. `Page 2.301`, `Master 1.1`).

Cue-command plugins / Cue Command lines run on the **session master** — [`multi-station.md`](multi-station.md). Do not duplicate that matrix here.

## Store cues

Default Store target is **Cue** on the **selected sequence**. Unattended macros/plugins/OSC: name the store mode and append [`/NoConfirmation`](keywords/options/Noconfirmation.md) — [`automation.md`](automation.md).

Stores active programmer values as **cue 2** of the selected sequence (no pop-up):

```
Store Cue 2 /NoConfirmation
```

Bare number is also Cue on the selected sequence:

```
Store 2 /NoConfirmation
```

Stores **cue 1.2** of **sequence 4** (two equivalent forms — separate fences):

```
Store Cue 1.2 Sequence 4 /NoConfirmation
```

```
Store Sequence 4 Cue 1.2 /NoConfirmation
```

Stores labeled cues **2** and **4** as `"BO Scene 1"`:

```
Store Cue 2 + 4 "BO Scene 1" /NoConfirmation
```

Merges into every cue whose name matches `BO*` on the selected sequence:

```
Store Cue "BO*" /Merge /NoConfirmation
```

Stores **cue 42** labeled, with CueFade in/out `6/3`, merge into existing:

```
Store Cue 42 "Al Powell arrives at the Plaze" CueFade 6/3 /Merge /NoConfirmation
```

Stores into **cue part 10** of cue 2:

```
Store Cue 2 Part 10 /NoConfirmation
```

Relative store (Official): next existing cue / offset:

```
Store Cue Next /Merge /NoConfirmation
```

```
Store Cue + 0.5 /NoConfirmation
```

```
Store Cue - 0.4 /NoConfirmation
```

Store options that matter for cues (confirm each Spec): [`/Merge`](keywords/options/Merge.md), [`/Overwrite`](keywords/options/Overwrite.md), [`/Remove`](keywords/options/Remove.md), [`/CueOnly`](keywords/options/CueOnly.md), [`/TrackingShield`](keywords/options/Trackingshield.md), plus selection/data-source options on [`Store`](keywords/Store.md). Temporary Store Settings vs Cue Preferences: manual [Store Settings and Preferences](https://help.malighting.com/grandMA3/2.5/HTML/cue_store_settings_preferences.html).

## Update

[`Update`](keywords/Update.md) writes programmer changes back into cues (Update key / dialog). **Do not** invent `/NoConfirmation` here — Official does not list Update under that option. Prefer explicit Update flows from the Keyword Spec; for silent store-style writes use `Store … /Merge` (or other mode) instead.

## Copy / delete

Copies cues **1–4** to start at **cue 11** (preserves order; desk may insert dotted numbers if needed):

```
Copy Cue 1 Thru 4 At Cue 11 /NoConfirmation
```

Copies in reverse source order to cue 11:

```
Copy Cue 4 Thru 1 At Cue 11 /NoConfirmation
```

Copies discrete cues:

```
Copy Cue 1 + 4 At Cue 11 /NoConfirmation
```

```
Copy Cue 2 At 6 /NoConfirmation
```

Deletes **cue 2** of the selected sequence:

```
Delete Cue 2 /NoConfirmation
```

Delete Values can follow Tracking vs Cue Only rules (GUI / Delete options — confirm [`Delete`](keywords/Delete.md) and Cue Only topics before scripting).

## Playback

`Go+` → [`Goplus`](keywords/Goplus.md), `Go-` → [`Gominus`](keywords/Gominus.md), [`Goto`](keywords/Goto.md). Also Load / Pause / Off / On / Call / Top / Temp / Flash / Toggle as listed in the keyword index.

Goes to the **next cue** of sequence 1:

```
Go+ Sequence 1
```

Goes to the **previous cue** of the selected sequence:

```
Go-
```

Jumps selected sequence to **cue 5**:

```
Goto Cue 5
```

Jumps sequence 6 to cue 4 (two equivalent forms):

```
Goto Cue 4 Sequence 6
```

```
Goto Sequence 6 Cue 4
```

Sends Go+ to whatever object is assigned on **executor 101**:

```
Go+ Executor 101
```

## Timing

Sets cue 3 CueFade in/out **5/8**:

```
Cue 3 CueFade 5/8
```

Sets cue 4 CueFade **7** (both directions):

```
Cue 4 CueFade 7
```

Partial CueFade / CueDelay form from the manual:

```
CueFade /3 CueDelay 1/
```

Assigns timing master Timing1 to page 1 executor 216:

```
Assign Master "Timing"."Timing1" At Page 1.216
```

Goto with fade from a timing master name / absolute fade:

```
Goto Cue 5 Fade "Timing5"
```

```
Goto Cue 5 Fade 2
```

Keywords: [`Cuefade`](keywords/Cuefade.md), [`Cuedelay`](keywords/Cuedelay.md), [`Fade`](keywords/Fade.md), [`Time`](keywords/Time.md).

## Tracking / MIB / recipes

Tracking is a **sequence setting** (On/Off). Cue Zero / Off Cue / Release / Cue Only / Tracking Distance / Tracking Shield are manual subtopics under [What is Tracking](https://help.malighting.com/grandMA3/2.5/HTML/cue_tracking.html) — do not invent CLI for GUI-only protect modes.

Unblocks tracking in **sequence 2**:

```
Unblock Sequence 2
```

MIB (Move In Black) is configured per **cue part**, sequence MIB settings, and global Preferences — largely property/GUI. No invent MIB keyword CLI here; see sequence settings MIB Mode (Early / UponGo / Late / Never / Enabled).

Cue recipes: recipe **Selection** must be a **group** — [`groups.md`](groups.md), [`concepts/recipes.md`](concepts/recipes.md), [`phaser-recipe.md`](phaser-recipe.md). Cook a cue/sequence after editing recipes ([`Cook`](keywords/Cook.md); `/NoConfirmation` listed for Cook):

```
Cook Sequence 1 /Overwrite /NoConfirmation
```

Confirm Cook options (`/Merge`, `/Overwrite`, `/Remove`, …) on the Keyword Spec before use.

## Renumber

**No CLI keyword** to renumber cues (manual: Sequence Sheet → select cue numbers → Edit). Do not invent a `Renumber` command.

## Sheets / settings (agent notes)

Sequence Sheet / Content Sheet / Sequence Settings are primarily GUI. Agent-relevant settings names from the manual (not proven `Set Sequence … Property` CLI unless a Keyword Spec shows them): Tracking, Cue Zero Mode, Cue Command, Rate/Speed Master + Scale, Use Executor Time, MIB Mode / Enabled / Never, Soft LTP, priorities, LastGo exclusion.

## Related

- Executors / handles: [`concepts/executors.md`](concepts/executors.md), [`executors.md`](executors.md)
- Masters (selected / grand / timing): [`masters.md`](masters.md)
- Programmer: [`concepts/programmer.md`](concepts/programmer.md)
- Automation: [`automation.md`](automation.md)
- Multi-station / cue commands: [`multi-station.md`](multi-station.md)
