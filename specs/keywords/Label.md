---
keyword: "Label"
kind: general
shortcuts: ["L"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_label.html"
---

## Official

To enter the Label keyword in the command line, use one of the options:

  * Press `Assign` `Assign`
  * Type **Label**
  * Type the shortcut **L**

### Description

The Label keyword is used to give objects a name.

If multiple objects are labeled, and the name contains a free-standing number, the number will be enumerated for each object.

If you do not label an object, a pop-up appears.

If no object is specified when using the Label keyword, the cue in the selected sequence will be addressed. If the selected sequence is disabled, the sequence will be addressed.

### Syntax

**Label [Object] ["Object_Name" or Object_Number] ["Name"]**

|  **Important:**  
---|---  
The name must not contain the following characters: \ " $ & * ? , . ; ^ { | } ~   
  
### Examples  
  

  * To label group 3 "Higgs Boson", type:

```
Label Group 3 "Higgs Boson"
```
---|---  
  
  * To label fixtures 1 to 10 as "Mac700 1", "Mac700 2" and so on, type:

```
Label Fixture 1 Thru 10 "Mac700 1"
```
---|---  
  
  * To rename the color preset "Red" to "Dark Red", type:

```
Label Preset "Color"."Red" "Dark Red"
```
---|---  
  
  * To label group 1 using the name of the selected attribute, type:

```
Label Group 1 At Attribute
```
---|---  
  
  

  * To label cue 1 "Insomnia", type:

```
Label 1 "Insomnia"
```
---|---  
  
  

  * To address the current cue of the selected sequence, type:

```
Label
```
---|---  
  
  

  * To label cue 42 in the selected sequence given that the sequence is running, type:

```
Label 42
```
---|---  
  

  * To label sequence 42 given that the selected sequence is disabled, type:

```
Label 42
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
