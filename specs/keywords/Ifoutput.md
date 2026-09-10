---
keyword: "IfOutput"
kind: general
shortcuts: ["Ifo"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_ifoutput.html"
---

## Official

To enter the IfOutput keyword in the command line, use one of the options:

  * Press `If`
  * Type **IfOutput**
  * Type the shortcut **Ifo**

### Description

IfOutput is a function keyword that selects fixtures based on their current output. This function works with presets and sequences only.

|  **Important:**  
---|---  
Executed on its own, the IfOutput keyword only selects fixtures of the current command line default.  
  
  
### Syntax

IfOutput ([Object] ["Object_Name" or Object_Number])

### Examples  
  

  * To select all fixtures of the current command line default which have output on stage, type:

```
IfOutput
```
---|---  
  
  * To select all fixtures that output the values stored in sequence 1, type:

```
IfOutput Sequence 1
```
---|---  
  
  * To select all fixtures that use the color preset "Green", type: 

```
IfOutput Preset "Color"."Green"
```
---|---  
  
**Requirement:**

Select several fixtures where the dimmer is enabled and select several groups right after.

  

  * To only select fixtures where the dimmer is open, type:

```
IfOutput Selection
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
