---
keyword: "/Embed"
kind: option
shortcuts: ["/E", "/EB"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_embed.html"
---

## Official

To enter the **/Embed** option keyword in the command line, use one of the options:

  * Type **/Embed**
  * Type the shortcut**/E** or **/EB**

### Description

The /Embed option keyword is used to store presets that are active in the programmer into a preset. The values in the new preset reference the preset that was active in the programmer. 

### Syntax

Store Preset ["FeatureGroup_Name" or FeatureGroup_Number].["Preset_Name" or Preset_Number] /Embed

### General Keywords

General keywords that use the /Embed option keyword:

  * [Preset keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_preset.html)
  * [Store keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_store.html)

### Example

**Requirement:** Presets are activated in the programmer. 

  * To store the preset values that are currently active in the programmer together with the reference of these values into the second dimmer preset, type:

```
Store Preset 1.2 /Embed
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
