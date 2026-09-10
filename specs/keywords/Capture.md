---
keyword: "Capture"
kind: general
shortcuts: ["Cap"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_capture.html"
---

## Official

To enter the Capture keyword in the command line, use one of the following options:

  * Press `Stomp` `Stomp`
  * Type **Capture**
  * Type the shortcut **Cap**

### Description

The Capture keyword is a command keyword which is used to activate the current output values of specified parameters. 

Capturing parameters during a running phaser or cue fade activates the actual values at the moment the command is executed. The result is a single step of static values resembling a freeze frame of the output.

|  **Important:**  
---|---  
The capture command produces only numeric values, losing any existing preset references.  
  
|  **Important:**  
---|---  
The capture command translates the output of each parameter into the appropriate value on the absolute layer while activating a 0 value on the relative layer. For any parameter where the output was previously composed of a combination of absolute and relative values, the output will appear the same while relying only on the absolute layer with no relative offset.  
  
  
### Syntax

**Capture [Object] ["Object_Name" or Object_Number]**

### Examples  
  

  * To capture all attributes of the selected fixtures, type:

```
Capture
```
---|---  
  

  * To capture only the position attributes of the selected fixtures, type:

```
Capture FeatureGroup "Position"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
