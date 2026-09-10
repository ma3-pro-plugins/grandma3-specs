---
keyword: "SetUserVariable"
kind: general
shortcuts: ["Setu"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_setuservariable.html"
---

## Official

To enter the SetUserVariable keyword in the command line, use one of the options: 

  * Type **SetUserVariable**
  * Type the shortcut **Setu**

###  Description 

The SetUserVariable keyword is used to set user-specific variables. It also supports the use of values in properties of other objects as a value of the variable. 

###  Syntax 

SetUserVariable ["Name of Variable"] [Numeric Value]

SetUserVariable ["Name of Variable"] ["Text_Value"]

SetUserVariable [**"Name of Variable"] At [Object] ["Object_Name" or Object Number] Property ["Property_Name"] (/Look)**

###  Option Keywords 

The SetUserVariable keyword uses the following option keywords: 

  * [/Look](https://help.malighting.com/grandMA3/2.5/HTML/ok_look.html)

###  Examples 

  * To set the user variable "Green" to the value 5, type: 

```
SetUserVariable "Green" 5
```
---|---  
  

  * To set the user variable "MyVar" to the CueFade value of cue 1 of the selected sequence, type:   

```
SetUserVariable "MyVar" At Cue 1 Property "CueFade"
```
---|---  
  

  * ####  To set the user variable "mySeqPrioIdx" to the Priority index value of the selected sequence, type:

```
SetUserVariable "mySeqPrioIdx" At Sequence Property "Priority"
```
---|---  
  
  

  * To set the user variable myEncoderBar to the name of the selected encoder bar, type: 

```
SetUserVariable myEncoderBar At EncoderBar Property "Name"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
