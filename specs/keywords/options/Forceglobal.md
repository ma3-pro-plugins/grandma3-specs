---
keyword: "/ForceGlobal"
kind: option
shortcuts: ["/Forceg"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_forceglobal.html"
---

## Official

To enter the **/ForceGlobal** option keyword in the command line, use one of the options: 

  * Type **/ForceGlobal**
  * Type the shortcut**/Forceg**

###  Description 

The /ForceGlobal option keyword adds global data to a preset already containing selective data. Selective data which is not used will be removed in the preset of fixtures of the same fixture type. /ForceGlobal removes selective data when updating or storing using the merge option. 

###  Syntax 

[Function] Preset ["FeatureGroup_Name" or FeatureGroup_Number].["Preset_Name" or Preset_Number] /ForceGlobal

###  General Keywords 

General keywords that use the /ForceGlobal option keyword: 

  * [Preset keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_preset.html)
  * [Store keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_store.html)
  * [Update keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_update.html)

###  Example   
  

  * To replace the selective data by global data in all fixtures of the same fixture type in the second dimmer preset, type: 

```
Store Preset 1.2 /ForceGlobal
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
