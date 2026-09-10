---
keyword: "Block"
kind: general
shortcuts: ["Blo"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_block.html"
---

## Official

To enter the Block keyword in the command line, use one of the options:

  * Type **Block**
  * Type the shortcut **Blo**

### Description

Block is a function used to add data and prevent them from tracking. Tracked values are converted to stored values.

If the object list does not contain any references to any cues, the Block function is applied to the selected sequence.

If syntax does not contain any selection list filter, all fixtures will be used.

If syntax does not contain any attribute list filter, all attributes will be used.

### Syntax

Block (Sequence ["Sequence_Name" or Sequence_Number]) Cue ["Cue_Name" or Cue_Number] (If Fixture ["Fixture_Name" or Fixture_Number] FeatureGroup ["FeatureGroup_Name" or FeatureGroup_Number] or Attribute ["Attribute_Name" or Attribute_Number] EndIf)

### Examples  
  

  * To block all parameters in cue 2 of the selected sequence, type:

```
Block Cue 2
```
---|---  
  

To unblock parameters, use the [Unblock keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_unblock.html). 

  * To block pan and tilt of fixture 4 in cue 5 of the selected sequence, type:

```
Block Cue 5 If Fixture 4 FeatureGroup "Position" EndIf
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
