---
keyword: "Unblock"
kind: general
shortcuts: ["UB", "Unb"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_unblock.html"
---

## Official

To enter the Unblock keyword in the command line, use one of the options:

  * Type **Unblock**
  * Type the shortcut **UB** or **Unb**

### Description

Unblock is a function that converts blocked values into tracking values in cues.

If the object list does not contain any references to any cues, the unblock function is applied to the selected sequence.

If unblock does not contain any selection list filters, all fixtures will be used.

If unblock does not contain any attribute list filters, all attributes will be used.

### Syntax

**Unblock (Sequence ["Sequence_Name" or Sequence_Number]) Cue ["Cue_Name" or Cue_Number] (If Fixture ["Fixture_Name" or Fixture_Number] FeatureGroup ["FeatureGroup_Name" or FeatureGroup_Number] or Attribute ["Attribute_Name" or Attribute_Number] EndIf)**

### Examples  
  

  * To unblock all parameters of the selected sequence, type:

```
Unblock
```
---|---  
  
  * To unblock pan and tilt of fixture 4 in cue 5 of the selected sequence, type:

```
Unblock Cue 5 If Fixture 4 Attribute "Position" EndIf
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
