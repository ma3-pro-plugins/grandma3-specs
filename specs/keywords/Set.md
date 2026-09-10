---
keyword: "Set"
kind: general
shortcuts: []
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_set.html"
---

## Official

To enter the Set keyword in the command line, use one of the options: 

  * Press `MA` \+ `Assign`
  * Type **Set**

###  Description 

The Set keyword sets values to properties of objects. It is also used to transfer values of properties to other properties, to other objects, and to different properties of other objects.

It is used in conjunction with the [Property keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_property.html) or the [= [Equal] keyword.](https://help.malighting.com/grandMA3/2.5/HTML/keyword_equal.html)

###  Syntax

Set [Object_Type] ["Object_Name" or Object_Number] Property ["Property_Name"] ["Property_Value"]

Set [Object_Type] ["Target_Object_Name" or Target_Object_Number] Property ["Property_Name"] At [Object_Type] (["Source_Object_Name" or Source_Object_Number]) (Property ["Property_Name"])

###  Option Keywords 

The Set keyword uses the following option keywords: 

  * [/PatchOffset](https://help.malighting.com/grandMA3/2.5/HTML/ok_patchoffset.html)
  * [/Look](https://help.malighting.com/grandMA3/2.5/HTML/ok_look.html)

###  Examples   
  

  * To set sequence 8 to priority HTP, type: 

```
Set Sequence 8 "Priority" 3
```
---|---  
  
  

  * To transfer the value of the Priority setting of sequence 1 to sequence 42, type: 

```
Set Sequence 42 Property "Priority" At Sequence 1
```
---|---  
  
  

  * To transfer the name of the selected sequence to the name of group 5, type:

```
Set Group 5 Property "Name" At Sequence Property "Name"
```
---|---  
  
  

  * To transfer the value of the CueFade property of cue 9 to the CueDelay property of cue 6, type: 

```
Set Cue 6 Property "CueDelay" At Cue 9 Property "CueFade"
```
---|---  
  
  

  * To set CueFade and CueDelay of cue 1 to three seconds, type: 

```
Set Cue 1 Property "CueFade" + "CueDelay" 3
```
---|---  
  
  

  * To transfer CueFade and CueDelay of cue 3 to cue 1, type: 

```
Set Cue 1 Property "CueFade" + "CueDelay" At Cue 3
```
---|---  
  
  

  * To set a range of values for FadeX in the first recipe of cue 1, part 0 of the selected sequence, type:

```
Set Cue 1 Part 0.1 Property "FadeX" "0 Thru 5"
```
---|---  
  
For information on the key and its location see [Set key](https://help.malighting.com/grandMA3/2.5/HTML/key_set.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
