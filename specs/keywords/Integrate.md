---
keyword: "Integrate"
kind: general
shortcuts: ["Int"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_integrate.html"
---

## Official

To enter the Integrate keyword in the command line, use one of the options:

  * Press `MA` \+ `At`
  * Type **Integrate**
  * Type the shortcut**Int**

### Description

The Integrate keyword integrates step 1 of a preset into other steps of the programmer.

These steps can be stored into presets and cues.

### Syntax

Integrate Preset ["FeatureGroup_Name" or FeatureGroup_Number].["Preset_Name" or Preset_Number] Step [Step_Number]

### Examples

**Requirement: Example 1**

  * There are already active values in step 1 in the programmer

  * To integrate step 1 of preset 1.1 into step 2 of the programmer, type:

```
Integrate Preset 1.1 Step 2
```
---|---  
  

**Requirement: Example 2**

  * Select fixtures and create preset 4.5
  * Follow steps 1 to 4

  1. To call preset 4.5 into the programmer, type:

```
At Preset 4.5
```
---|---  
  
  2. To create the next step, type:

```
Next Step
```
---|---  
  
  

  3. To integrate step 1 of preset 4.2, type: 

```
Integrate Preset 4.2
```
---|---  
  
  4. To store the changes in the preset, type: 

```
Store Preset 4.5
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
