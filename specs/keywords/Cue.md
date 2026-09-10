---
keyword: "Cue"
kind: general
shortcuts: ["C"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_cue.html"
---

## Official

To enter the Cue keyword in the command line, use one of the options:

  * Press `Cue`
  * Type **Cue**
  * Type the shortcut **C**

### Description

| **Important:** |
| --- |
| Cue is the only object type that accepts numerical IDs as decimal fractions. The ID which is allowed for cues ranges from 0.001 to 9999.999. In all other objects, a dot indicates the ID of a parent or a child object. |

**Cue** is an object type holding a look on stage.

Cues are arranged in sequences and are divided into parts.

For more information see the [Cue and Sequence section](https://help.malighting.com/grandMA3/2.5/HTML/cue_sequence.html).

The **Cue** keyword is an object keyword. Object keywords must have a function keyword in front of them to create a complete command. For more information on how to use the command syntax, see [General Syntax Rules](https://help.malighting.com/grandMA3/2.5/HTML/csk_syntax_rules.html).

Cue has a default function called [SelFix](https://help.malighting.com/grandMA3/2.5/HTML/keyword_selectfixtures.html). This selects all the fixtures that have stored values in the cue.

If a sequence is not specified, then the selected sequence is used in the command.

### Syntax

[Function] Cue ["Cue_Name" or Cue_Number]

[Function] Sequence ["Sequence_Name" or Sequence_Number] Cue ["Cue_Name" or Cue_Number] ([Setting] ["Setting_Value"] (/Option)

Assign [Object] ["Object_Name" or Object_Number] At (Sequence ["Sequence_Name" or Sequence_Number]) Cue ["Cue_Name" or Cue_Number]

### Settings

In some settings you have to assign an object. These can be assigned using the [Assign keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_assign.html).

Other settings may contain a text option or a value. Use the [Set keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_set.html) for these settings.

Cues can also contain settings for MAtricks and recipe values. These can be changed using the [Set Keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_set.html).

### Option Keywords

The Cue keyword uses the following option keywords:

  * [/Active](https://help.malighting.com/grandMA3/2.5/HTML/ok_active.html)
  * [/ActiveForSelected](https://help.malighting.com/grandMA3/2.5/HTML/ok_activeforselected.html)
  * [/AddNewContent](https://help.malighting.com/grandMA3/2.5/HTML/ok_addnewcontent.html)
  * [/All](https://help.malighting.com/grandMA3/2.5/HTML/ok_all.html)
  * [/AllForSelected](https://help.malighting.com/grandMA3/2.5/HTML/ok_allforselected.html)
  * [/Ask](https://help.malighting.com/grandMA3/2.5/HTML/ok_ask.html)
  * [/CopyCueDestiation](https://help.malighting.com/grandMA3/2.5/HTML/ok_copycuedestination.html)
  * [/CopyCueSource](https://help.malighting.com/grandMA3/2.5/HTML/ok_copycuesource.html)
  * [/CreateSecondCue](https://help.malighting.com/grandMA3/2.5/HTML/ok_createsecondcue.html)
  * [/CueOnly](https://help.malighting.com/grandMA3/2.5/HTML/ok_cueonly.html)
  * [/Default](https://help.malighting.com/grandMA3/2.5/HTML/ok_default.html)
  * [/DMX](https://help.malighting.com/grandMA3/2.5/HTML/ok_dmx.html)
  * [/GridMergeMode](https://help.malighting.com/grandMA3/2.5/HTML/ok_gridmergemode.html)
  * [/Look](https://help.malighting.com/grandMA3/2.5/HTML/ok_look.html)
  * [/Merge](https://help.malighting.com/grandMA3/2.5/HTML/ok_merge.html)
  * [/NoConfirmation](https://help.malighting.com/grandMA3/2.5/HTML/ok_noconfirmation.html)
  * [/Output](https://help.malighting.com/grandMA3/2.5/HTML/ok_output.html)
  * [/Overwrite](https://help.malighting.com/grandMA3/2.5/HTML/ok_overwrite.html)
  * [/Programmer](https://help.malighting.com/grandMA3/2.5/HTML/ok_programmer.html)
  * [/Release](https://help.malighting.com/grandMA3/2.5/HTML/ok_release.html)
  * [/Remove](https://help.malighting.com/grandMA3/2.5/HTML/ok_remove.html)

### Examples

  * To select the fixtures with values stored in cue 3 of a selected sequence, type:

| User name[Fixture]>Cue 3 |
| --- |

The default function for **Cue** is **SelFix** so Cue 3 is the same as SelFix Cue 3.

  * To delete cue 2.5 in the selected sequence, type:

| User name[Fixture]>Delete Cue 2.5 |
| --- |

  * To store cue 2 in sequence 5, type:

| User name[Fixture]>Store Sequence 5 Cue 2 |
| --- |

  * To store cue 3 in sequence 5 with a cue fade time of 7 seconds and an outfade of 11, type:

| User name[Fixture]>Store Sequence 5 Cue 3 CueFade 7/11 |
| --- |

For information on the key and its location see [Cue key](https://help.malighting.com/grandMA3/2.5/HTML/key_cue.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
