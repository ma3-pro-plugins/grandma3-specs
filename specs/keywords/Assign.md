---
keyword: "Assign"
kind: general
shortcuts: ["As"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_assign.html"
---

## Official

To enter the Assign keyword in the command line, use one of the options:

  * Press `Assign`
  * Type **Assign**
  * Type the shortcut **As**

### Description

The Assign keyword is a function which is used to assign objects to other objects.

To unassign objects in other objects, use the **Assign Off** command.

To set parameters for objects, use the [Set keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_set.html).

For more information see:

  * [Assign macros to keys and buttons](https://help.malighting.com/grandMA3/2.5/HTML/macro_assign.html)
  * [Create new presets](https://help.malighting.com/grandMA3/2.5/HTML/presets_create.html)
  * [Use appearances](https://help.malighting.com/grandMA3/2.5/HTML/appear_use.html)
  * [Store and recall views](https://help.malighting.com/grandMA3/2.5/HTML/wvm_store_recall.html)

### Syntax

Assign [Object] ["Object_Name" or Object_Number] At [Object] ["Object_Name" or Object_Number]

Assign Off [Object] ["Object_Name" or Object_Number] At [Object] ["Object_Name" or Object_Number]

### Option Keywords

The Assign keyword uses the following option keywords:

  * [/Tab](https://help.malighting.com/grandMA3/2.5/HTML/ok_tab.html)

### Examples

  * To assign macro 2 to executor page 1 executor 402, type:

| User name[Fixture]>Assign Macro 2 At Page 1.402 |
| --- |

  * To assign view 2 to display 2 and view button 3, type:

| User name[Fixture]>Assign View 2 At ViewButton 2.3 |
| --- |

  * To assign appearance 3 to group 5, type:

| User name[Fixture]>Assign Appearance 3 At Group 5 |
| --- |

  * To assign appearance 1 to the sequences 2, 3 and 4, type:

| User name[Fixture]>Assign Appearance 1 At Sequence 2 + 3 + 4 |
| --- |

  * To unassign tag "ArgleBargle" in sequence 3, type:

| User name[Fixture]>Assign Off Tag "ArgleBargle" At Sequence 3 |
| --- |

  * To share data of sequence 1 with sequence 2, type:

| User name[Fixture]>Assign Sequence 1 At Sequence 2 |
| --- |

  * To revert sharing data of sequence 2 in sequence 1 and keep all settings of sequence 2:

    1. Type:

| User name[Fixture]>Copy Sequence 2 At Sequence 3 |
| --- |

    2. After that, type:

| User name[Fixture]>Delete Sequence 2 |
| --- |

For more information on sharing data in sequences see [Cues and Sequences](https://help.malighting.com/grandMA3/2.5/HTML/cue_sequence.html).

| **Hint:** |
| --- |
| In terms of playback, mirrored sequences are independent from one another. However, their content is linked. |

**Requirements:**

  1. Open the grandMA3 demo showfile.
  2. Tap view button 1 "Fixture" on screen 1. The Fixture Sheet opens on screen 1.

  * To assign the filter "Only Dimmer" to the Fixture Sheet on screen 1, type:

| User name[Fixture]>Assign Filter "Only Dimmer" At ScreenContent 1.1.1 |
| --- |

  * To assign the world 1 to the Fixture Sheet on screen 1, type:

| User name[Fixture]>Assign World 1 At ScreenContent 1.1.1 |
| --- |

For information on the key and its location see [Assign key](https://help.malighting.com/grandMA3/2.5/HTML/key_assign.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
