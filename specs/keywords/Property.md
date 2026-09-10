---
keyword: "Property"
kind: general
shortcuts: ["Prop"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_property.html"
---

## Official

To enter the Property keyword in the command line, use one of the options:

  * Type **Property**
  * Type the shortcut **Prop**

### Description

​The Property keyword is an object keyword which is used to communicate with the console for you to set a specific property.

It is used in conjunction with the [Set keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_set.html), the [SetUserVariable keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_setuservariable.html), or the [SetGlobalVariable keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_setglobalvariable.html). 

Syntax

[Function] [Object] ["Object_Name" or Object_Number] Property ["Property_Name"](At + [Object] ["Object_Name" or Object_Number]) ["Value"]

### Examples  
  

  * To set the ValueReadout to Hex8 in the current user profile, type:

```
Set CurrentUserProfile Property "ValueReadout" "Hex8"
```
---|---  
  
  * To assign the filter "Only Dimmer" of cue 5 to "Break", type:

```
Set Cue 5 Property "Break" At + Filter "Dimmer Only"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
