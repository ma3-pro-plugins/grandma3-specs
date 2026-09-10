---
keyword: "MyRunningPreset"
kind: general
shortcuts: ["Myrunningp"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_myrunningpreset.html"
---

## Official

To enter the MyRunningPreset keyword in the command line, use one of the options:

  * Type **MyRunningPreset**
  * Type the shortcut **Myrunningp**

### Description

The MyRunningPreset keyword addresses preset playbacks that were started by my user profile and are currently running.

|  **Important:**  
---|---  
The numbers of the running presets are not equal to the numbers in the preset pool.  
  
  
### Syntax

**[Function]** MyRunningPreset ["MyRunningPreset_Name" or MyRunningPreset_Number]

### Examples  
  

  * To disable the second and currently running preset started by my user profile, type:

```
Off MyRunningPreset 2
```
---|---  
  
  * To list my running presets, change destination first and type:

```
ChangeDestination MyRunningPreset
```
---|---  
  
  

  * Then type:

|  User name@Temp/Cmdlines/Cmdline 1/RunningPlaybacks>Set MyRunningPreset Property "SelectedPlaybackType" "Preset" Property "SelectedMine" "Yes"  
---|---  
  
  

  * Ater that type:

|  User name@Temp/Cmdlines/Cmdline 1/RunningPlaybacks>List  
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
