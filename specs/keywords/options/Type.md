---
keyword: "/Type"
kind: option
shortcuts: ["/Ty"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_type.html"
---

## Official

To enter the **/Type** option keyword in the command line, use one of the options: 

  * Type **/Type**
  * Type the shortcut**/Ty**

###  Description 

The /Type option keyword can have different values depending on the keyword it is combined with. 

The Import keyword and the Export keyword can be both used with the /Type "User" and "System".   
The LoadShow keyword can be used with the /Type "Demo".   
In a nutshell – the Import and the Export keyword both use library files and the LoadShow keyword uses show files.   
The ChangeMulticastBase keyword uses the /Type "Default" and "Alternative". 

When importing the desired file may be either a "User" file, which has been previously exported, or a "System" file, which is predefined and included with the system software. If this option is not defined within the import syntax, the console will first search the user library for the specified file name. If the file does not exist within the user library, the console will then search within the system files. 

  * **/Type "User"** restricts the console to only search within the user library of the selected drive. 
  * **/Type "System"** restricts the console to only search within the system files, ignoring the user library. 
  * **/Type "Demo"** restricts the console to only search within demo shows folder. 
  * **/Type "Template"** restricts the console to only search within the template shows folder. 
  * **/Type "NoReference"** deletes all objects that do not have any reference in the specified range. For example, "NoReference" will delete presets that are not used in cues or recipes. 
  * **/Type "Recipe"** deletes recipes in the specified object that do not generate output. 
  * **/Type "Default"** uses the default address of multicast base. 
  * **/Type "Alternative"** uses a different address should the default address cause any problems within the network environment. For more information see [Protocol Details](https://help.malighting.com/grandMA3/2.5/HTML/network_design_protocols.html). 
  * **/Type "GridPosition"** removes gaps in grid positions and resets the offset to origin in groups. It can only be used with the [CleanUp keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_cleanup.html). 
  * **/Type "Positive"** addresses goup masters with mode **Positive**.
  * **/Type "Negative"** addresses group masters with mode **Negative**. 
  * **/Type "Scaling"** addresses group masters with mode **Scaling**. 
  * **/Type "Additive"** addresses group masters with mode **Additive**. 

|  **Important:**  
---|---  
When no type is specified, the type "User" has priority.   
  
  
Syntax

[Function] [Object] ["Object_Name" or Object_Number] (If Drive [Drive_Number]) /Type "Value" 

###  General Keywords 

General keywords that use the /Type option keyword: 

  * [ChangeMulticastBase keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_changemultcastbase.html)
  * [CleanUp keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_cleanup.html)
  * [Console keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_console.html)
  * [Cue keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_cue.html)
  * [Export keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_export.html)
  * [Extension keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_extension.html)
  * [FaderMaster keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_fadermaster.html)
  * [Group keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_group.html)
  * [Import keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_import.html)
  * [IP keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_ip.html)
  * [LoadShow keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_loadshow.html)
  * [Master keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_master.html)
  * [NetworkNode keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_networknode.html)
  * [onPC keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_onpc.html)
  * [Part keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_part.html)
  * [Preset keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_preset.html)
  * [ProcessingUnit keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_processingunit.html)
  * [Session keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_session.html)
  * [Sequence keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_sequence.html)
  * [Station keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_station.html)

[](https://help.malighting.com/grandMA3/2.5/HTML/ok_recipe.html)

###  Examples   
  

  * To import the save_show macro from the system library instead of the user library to macro 21, type: 

```
Import Macro Library "save_show.xml" At Macro 21 /Type "System"
```
---|---  
  
  * To load the demo show from the demo shows folder, type: 

```
LoadShow "Demoshow_grandMA3.show" /Type "Demo"
```
---|---  
  
  

  

  * To clean up all recipes that do not generate output in cue 2 part 0 of sequence 1, type: 

```
CleanUp Sequence 1 Cue 2 Part 0 /Type "Recipe"
```
---|---  
  
  

  * To clean up all presets that are not used in any other object, type: 

```
CleanUp Preset *.* /Type "NoReference"
```
---|---  
  
or type: 

```
CleanUp Preset *.*
```
---|---  
  
  

  * To clean up the gaps in the grid positions of group 1 and move the whole selection toward the origin of the selection grid, type: 

```
CleanUp Group 1 /Type "GridPosition"
```
---|---  
  
  

  * To set all group masters that are in mode Additive to zero, type: 

```
FaderMaster Group * At 0 /Type "Additive"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
