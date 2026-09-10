---
keyword: "SetGlobalVariable"
kind: general
shortcuts: ["Setg"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_setglobalvariable.html"
---

## Official

To enter the SetGlobalVariable keyword in the command line, use one of the options:

  * Type **SetGlobalVariable**
  * Type the shortcut **Setg**

### Description

The SetGlobalVariable keyword is used to set global variables in a show. It also supports the use of values in properties of other objects as a value of the variable. 

### Syntax

SetGlobalVariable ["Name of Variable"] [Numeric Value]

SetGlobalVariable ["Name of Variable"] ["Text_Value"]

SetGlobalVariable [**"Name of Variable"] At [Object] ["Object Name" or Object Number] Property ["Property_Name"] (/Look)**

### Examples  
  

  * To set the global variable "Urban Blues" to the value of 3, type:

```
SetGlobalVariable "Urban Blues" "3"
```
---|---  
  
  

  * To set the global variable "Hook" to the CueFade value of cue 2 of the selected sequence, type:

```
SetGlobalVariable "Hook" At Cue 2 Property "CueFade"
```
---|---  
  
  

  

  * To set the global variable "PositionX" to the 3D X coordinate of fixture 1, type:

```
SetGlobalVariable "PositionX" At Fixture 1 Property "PosX"
```
---|---  
  
  

  

  * To set the global variable "myShow" to the name of the show file that was loaded, type:

```
SetGlobalVariable myShow At Root "MANetSocket" Property "ShowFile"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
