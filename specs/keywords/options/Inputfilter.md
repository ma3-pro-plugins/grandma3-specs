---
keyword: "/InputFilter"
kind: option
shortcuts: ["/I"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_inputfilter.html"
---

## Official

To enter the **/InputFilter** option keyword in the command line, use one of the options:

  * Type **/InputFilter**
  * Type the shortcut**/I**

### Description

The /InputFilter option keyword is used to enable or disable the filter of a feature group when storing or updating presets. 

### Syntax

[Function] Preset ["FeatureGroup_Name" or FeatureGroup_Number].["Preset_Name" or Preset_Number] /InputFilter ["Option_Value"]

### General Keywords

General keywords that use the /InputFilter option keyword:

  * [Preset keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_preset.html)
  * [Store keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_store.html)
  * [Update keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_update.html)

### Example  
  

  * To disable the input filter when storing the third dimmer preset, type:

```
Store Preset 1.3 /InputFilter "No"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
