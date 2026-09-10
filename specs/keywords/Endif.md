---
keyword: "EndIf"
kind: general
shortcuts: ["End"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_endif.html"
---

## Official

To enter the EndIf keyword in the command line, use one of the options:

    * Type **EndIf**
    * Type the shortcut **End**

###  Description 

EndIf is a helping keyword that indicates the end of an If statement. 

It enables If statements to be entered in the middle of a syntax. Upon processing, the If statement is moved to the end of the syntax, and is used as a filter or condition. This enables If syntax to be used in conjunction with pool items. 

For more information see [If Keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_if.html). 

###  Syntax 

[Function] If [Object] ["Object_Name" or Object_Number] EndIf [Object] ["Object_Name" or Object_Number]

###  Example   
  

    * To create preset 1.1 using fixtures of group 5 type:

```
Store If Group 5 EndIf Preset 1.1
```
---|---  
  
Result in the command line history:

OK : |  Store If Group 5  EndIf Preset 1 .1  
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
