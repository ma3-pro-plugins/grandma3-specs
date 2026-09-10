---
keyword: "/GridMergeMode"
kind: option
shortcuts: ["/Gr", "/GMM"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_gridmergemode.html"
---

## Official

To enter the **/GridMergeMode** option keyword in the command line, use one of the options: 

  * Type **/GridMergeMode**
  * Type the shortcut**/Gr** or **GMM**

### Description

The /GridMergeMode option keyword is used when storing fixtures with their selection grid data into objects using the merge mode.

For more information see [Store Settings and Preferences](https://help.malighting.com/grandMA3/2.5/HTML/cue_store_settings_preferences.html).

### Syntax

Store [Object] ["Object_Name" or Object_Number] /Merge /GridMergeMode "Value"

### General Keywords

General keywords that use the /GridMergeMode option keyword:

  * [Cue keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_cue.html)
  * [Group keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_group.html)
  * [Preset keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_preset.html)
  * [Store keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_store.html)
  * [World keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_world.html)

### Values

The /GridMergeMode option keyword uses these values:

  * AppendX
  * Off

### Examples  
  

  * To merge the currently selected fixtures in group 27 and append the new fixtures in the selection grid on the x-axis following the fixtures that were alrady stored, type:

```
Store Group 27 /GridMergeMode "AppendX"
```
---|---  
  
  * To merge the currently selected fixtures in group 28 and place them on their original position in the selection grid, type:

```
Store Group 28 /GridMergeMode "Off"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
