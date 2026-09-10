---
keyword: "/Remove"
kind: option
shortcuts: ["/R"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_remove.html"
---

## Official

To enter the **/Remove** option keyword in the command line, use one of the options: 

  * Type **/Remove**
  * Type the shortcut**/R**

###  Description 

The /Remove option keyword is used to remove values that are stored in attributes and active programmer values. 

###  Syntax 

[Function] ["Object_Name" or Object_Number] /Remove

###  General Keywords 

General keywords that use the /Remove option keyword: 

  * [Assign keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_assign.html)
  * [Cook keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_cook.html)
  * [CopyCrashLog](https://help.malighting.com/grandMA3/2.5/HTML/keyword_copycrashlog.html)
  * [Cue keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_cue.html)
  * [Group keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_group.html)
  * [Layout keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_layout.html)
  * [MAtricks keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_matricks.html)
  * [Preset keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_preset.html)
  * [Store keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_store.html)
  * [Update keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_update.html)
  * [World keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_world.html)

###  Examples   
  

  * To remove the values that are active in the programmer and that are stored in cue 5 of sequence 1, type: 

```
Store Sequence 1 Cue 5 /Remove
```
---|---  
  
  * To remove all cooked data from sequence 1, type: 

```
Cook Sequence 1 /Remove
```
---|---  
  
  * To delete crash logs on your device after copying them to a USB drive, type: 

```
CopyCrashLog /Remove
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
