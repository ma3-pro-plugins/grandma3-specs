---
keyword: "Preset"
kind: general
shortcuts: ["Pr"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_preset.html"
---

## Official

To enter the Preset keyword in the command line, use one of the options:

  * Press `Preset`
  * Type **Preset**
  * Type the shortcut **Pr**

### Description

With the Preset keyword, it is possible to:

  * Select the fixtures stored in a preset;
  * Apply the At function on the preset within the fixture or channel selection;
  * Set a property in a preset.

A command containing only the Preset keyword and the preset ID performs the default function SelectFixtures. For more information see [SelectFixtures keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_selectfixtures.html).

To give the fixture attributes a link to the preset, the At keyword needs to be added in front of the Preset keyword and the preset ID. For more information see [At Keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_at.html).

### Syntax

Preset ["FeatureGroup_Name" or FeatureGroup_Number].["Preset_Name" or Preset_Number]

[Function] Preset ["FeatureGroup_Name" or FeatureGroup_Number].["Preset_Name" or Preset_Number] ([Setting] ["Setting_Value"] [/OptionKeyword])

Assign [Object] ["Object_Name" or Object_Number] At Preset ["FeatureGroup_Name" or FeatureGroup_Number].["Preset_Name" or Preset_Number]

### Settings

Some settings need an object assigned. These can be assigned using the [Assign Keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_assign.html).

Other settings contain a text option or a value. The [Set keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_set.html) is used for these settings.

The following table displays the settings that need an object:

Setting | Object | Description  
---|---|---  
Appearance | "Appearance 1" | Assigns the appearance to the pool object.  
InputFilter | "Filter 12" | Assigns a filter or world as an input filter to the pool object.  
Scribble | "Scribble 1" | Assigns the scribble to the preset pool object.  
  
The following table displays the settings that need an option or value:

Setting | Option/Value | Description  
---|---|---  
Name | "Preset Name" | Sets the name of the preset pool object.  
MoveGridCursor | "Yes" or "No" | This defines if the grid cursor is moved after calling the preset.  
CuePart | "Default" or a specific part number | This is the programmer cue part the preset will be called into.  
MAgic | "Yes" or "No" | This defines if the preset is a magic preset or not.  
PresetMode | Read only | This is information only about the preset mode.  
StoredData | Read only | This is information only about the stored data.  
  
Presets can also contain settings for MAtricks and recipe values. These can be changed using the [Set keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_set.html).

### Option Keywords

The Preset keyword uses the following option keywords:

  * [/Active](https://help.malighting.com/grandMA3/2.5/HTML/ok_active.html)
  * [/ActiveForSelected](https://help.malighting.com/grandMA3/2.5/HTML/ok_activeforselected.html)
  * [/AddNewContent](https://help.malighting.com/grandMA3/2.5/HTML/ok_addnewcontent.html)
  * [/All](https://help.malighting.com/grandMA3/2.5/HTML/ok_all.html)
  * [/AllForSelected](https://help.malighting.com/grandMA3/2.5/HTML/ok_allforselected.html)
  * [/Ask](https://help.malighting.com/grandMA3/2.5/HTML/ok_ask.html)
  * [/Auto](https://help.malighting.com/grandMA3/2.5/HTML/ok_auto.html)
  * [/DMX](https://help.malighting.com/grandMA3/2.5/HTML/ok_dmx.html)
  * [/Embed](https://help.malighting.com/grandMA3/2.5/HTML/ok_embed.html)
  * [/ForceGlobal](https://help.malighting.com/grandMA3/2.5/HTML/ok_forceglobal.html)
  * [/Global](https://help.malighting.com/grandMA3/2.5/HTML/ok_global.html)
  * [/GridMergeMode](https://help.malighting.com/grandMA3/2.5/HTML/ok_gridmergemode.html)
  * [/InputFilter](https://help.malighting.com/grandMA3/2.5/HTML/ok_inputfilter.html)
  * [/KeepActivation](https://help.malighting.com/grandMA3/2.5/HTML/ok_keepactivation.html)
  * [/Look](https://help.malighting.com/grandMA3/2.5/HTML/ok_look.html)
  * [/MAtricks](https://help.malighting.com/grandMA3/2.5/HTML/ok_matricks.html)
  * [/Output](https://help.malighting.com/grandMA3/2.5/HTML/ok_output.html)
  * [/Overwrite](https://help.malighting.com/grandMA3/2.5/HTML/ok_overwrite.html)
  * [/PhaserData](https://help.malighting.com/grandMA3/2.5/HTML/ok_phaserdata.html)
  * [/Programmer](https://help.malighting.com/grandMA3/2.5/HTML/ok_programmer.html)
  * [/Selective](https://help.malighting.com/grandMA3/2.5/HTML/ok_selective.html)
  * [/Universal](https://help.malighting.com/grandMA3/2.5/HTML/ok_universal.html)

### Examples  
  

  * To select the fixtures that can use preset 5 of the dimmer feature group, type:

```
SelFix Preset 1.5
```
---|---  
  
  * To select the fixtures stored in any preset with the name "DarkRed", type:

```
SelFix Preset *."DarkRed"
```
---|---  
  
  * To call a reference to preset 21.45 ("All 1" preset number 45) to the attributes of the selected fixtures, type:

```
At Preset 21.45
```
---|---  
  
  * To set the name of the position preset 3 to be "Stage Left", type:

```
Set Preset 2.3 Name "Stage Left"
```
---|---  
  
  * To assign world 5 as an input filter on position preset 4, type:

```
Assign World 5 At Preset 2.4
```
---|---  
  
For information on the key and its location see [Preset key](https://help.malighting.com/grandMA3/2.5/HTML/key_preset.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
