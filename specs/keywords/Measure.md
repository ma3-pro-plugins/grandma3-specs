---
keyword: "Measure"
kind: general
shortcuts: ["Mea"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_measure.html"
---

## Official

To enter the Measure keyword in the command line, use one of the options:

  * Type **Measure**
  * Type the shortcut **Mea**

###  Description 

The Measure keyword is used together with the phaser speed (speed layer) to define the length of time of a phaser. Knocking in the measure layer without specifying a value, will take the number of steps of the running phaser as the value. 

For more information see [Phasers](https://help.malighting.com/grandMA3/2.5/HTML/phaser.html). 

|  **Hint:**  
---|---  
The measure layer also affects how the width of each step is calculated.   
  
|  **Important:**  
---|---  
When using the measure layer, multiple width value combinations can produce identical results. To ensure predictable timing, we recommended you consider the width value of a step as the percentage of a beat and ensure that the total width of all steps in the phaser equals the number of beats specified in the measure layer.   
  
  
###  Syntax 

**Measure**

[At] Measure [Value]

###  Examples 

**Requirement:**

To set values in the measure layer, create at least 2 steps in the programmer. 

  * To set the selected layer to measure, type: 

```
Measure
```
---|---  
  
  * To set the measure of the selected feature group to 4 beats, type: 

```
At Measure 4
```
---|---  
  
**Result:**

The phaser cycle now lasts 4 beats.

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
