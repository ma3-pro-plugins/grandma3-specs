---
keyword: "If"
kind: general
shortcuts: ["I"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_if.html"
---

## Official

To enter the If keyword in the command line, use one of the options: 

  * Press `If`
  * Type If
  * Type the shortcut**I**

###  Description 

The **If** keyword is a function keyword which is used to deselect fixtures in a selection. 

As a helping keyword If sets a filter for the operation. 

As a helping keyword for the Clone function If sets the scope of cloning. 

For more information see the [Clone Keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_clone.html). 

###  Syntax 

([Function] [Object] ["Object_Name" or Object_Number]) If [Object] ["Object_Name" or Object_Number]

Clone [Object] ["Object_Name" or Object_Number] At [Object] ["Object_Name" or Object_Number] If [Object] ["Object_Name" or Object_Number]

###  Examples   
  

  * To deselect fixtures which are not in group 5, type:

```
If Group 5
```
---|---  
  
  * To deselect fixtures which are not in group 3 and group 5, type:

```
Group 3 If Group 5
```
---|---  
  
  * To delete channel 4 in cue 3, type:

```
Delete Cue 3 If Channel 4
```
---|---  
  
  

  

  * To delete attibute "Pan" of fixture 4 in cue 3, type:

```
Delete Cue 3 If Fixture 4 Attribute "Pan"
```
---|---  
  
  * To clone fixture 1 to fixture 2 only in sequence 1, type:

```
Clone Fixture 1 At Fixture 2 If Sequence 1
```
---|---  
  
  * To activate only the attributes of filter 42 when knocking in feature group 2, type:

```
On FeatureGroup 2 If Filter 42
```
---|---  
  
  

  * To open the label editor for all groups where appearance 20 is assigned, type:

```
Label Group Thru If Appearance 20
```
---|---  
  
For information on the key and its location see [If key](https://help.malighting.com/grandMA3/2.5/HTML/key_if.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
