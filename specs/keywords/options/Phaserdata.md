---
keyword: "/PhaserData"
kind: option
shortcuts: ["/Ph"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_phaserdata.html"
---

## Official

To enter the **/PhaserData** option keyword in the command line, use one of the options:

  * Type **/PhaserData**
  * Type the shortcut**/Ph**

### Description

The /PhaserData option keyword is used to define if attribute data will be stored in presets. 

### Syntax

Store Preset ["FeatureGroup_Name" or FeatureGroup_Number].["Preset_Name" or Preset_Number] /PhaserData ["Option_Value"]

### General Keywords

General keywords that use the /PhaserData option keyword:

  * [Preset keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_preset.html)
  * [Store keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_store.html)

### Example

**Requirement:**

  1. Select 10 fixtures.
  2. Set XWings to 2.
  3. Type in the command line:

```
At 0 Thru 100
```
---|---  
  
  * To store all data, except the active programmer data, into the first preset of the third All preset pool, type:

```
Store Preset 23.1 /PhaserData "No"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
