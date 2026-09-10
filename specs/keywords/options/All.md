---
keyword: "/All"
kind: option
shortcuts: ["/Al"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_all.html"
---

## Official

To enter the **/All** option keyword in the command line, use one of the options:

  * Type **/All**
  * Type the shortcut **/Al**

### Description

The /All option keyword stores the values of all attributes when using Data Source Output or DMX.

### Syntax

**[Function] [Object] ["Object_Name" or Object_Number] /All**

### General Keywords

General keywords that use the /All option keyword:

  * [AutoCreate keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_autocreate.html)
  * [Cue keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_cue.html)
  * [FixtureClass keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_fixture_class.html)
  * [FixtureLayer keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_fixture_layer.html)
  * [FixtureType keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_fixturetype.html)
  * [LoadShow keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_loadshow.html)
  * [NewShow keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_newshow.html)
  * [Preset keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_preset.html)
  * [Store keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_store.html)

| **Hint:** |
| --- |
| The /All option keyword also works in conjunction with the [/Look option keyword](https://help.malighting.com/grandMA3/2.5/HTML/ok_look.html). |

### Examples

  * To store all attributes in cue 1, type:

| User name[Fixture]>Store Cue 1 /All |
| --- |

  * To load the entire data of the show "Fiddler on the Roof", type:

| User name[Fixture]>LoadShow "Fiddler on the Roof" /All |
| --- |

  * To create a new show file called "Rocky Horror Picture Show" and clear all previous settings, type:

| User name[Fixture]>NewShow "Rocky Horror Picture Show" /All |
| --- |

**Requirement:**

  1. Select eight fixtures.
  2. Set MAtricks XGroup to 2.
  3. Set MAtricks X to 0.

  * To create group 21 in the group pool containing all main fixtures of the selection (odd fixtures of the current selection), type:

| User name[Fixture]>AutoCreate Selection At Group 21 /All |
| --- |

**Requirement:** Create layers and classes and set fixtures to these.

For more information and how to use fixture classes and fixture layers see Patch and [Fixture Setup - Classes and Layers](https://help.malighting.com/grandMA3/2.5/HTML/patch_classes_layers.html).

| **Hint:** |
| --- |
| The demo show runs using this setting. For more information see [Backup, Demo, and Template Show Files](https://help.malighting.com/grandMA3/2.5/HTML/sfh_backup.html). |

  * To create a group at group pool object 301 with all fixtures that are set to class "Spots" within the patch, type:

| User name[Fixture]>AutoCreate FixtureClass "Spots" At Group 301 /All |
| --- |

  * To create a group at group pool object 201 with all fixtures that are set to layer "Backtruss" within the patch, type:

| User name[Fixture]>AutoCreate FixtureLayer "Backtruss" At Group 201 /All |
| --- |

  * To create a group at group pool object 42 with all patched fixtures of fixture type 9, type:

| User name[Fixture]>AutoCreate FixtureType 10 At Group 42 /All |
| --- |

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
