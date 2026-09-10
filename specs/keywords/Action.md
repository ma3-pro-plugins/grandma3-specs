---
keyword: "Action"
kind: general
shortcuts: ["Actio"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_action.html"
---

## Official

To enter the Action keyword in the command line, use one of the options:

  * Type **Action**
  * Type the shortcut **Actio**

### Description

The Action keyword is used to call functions that do not have a designated keyword. 

### Syntax

**Action ["Function"]**

### Examples  
  

  * To store the pan/tilt position to calibration point 1 of the currently selected fixtures, type:

```
Action "StoreCalibrationPoint1"
```
---|---  
  

  * To call the pan/tilt position of the currently selected fixture of calibration point 2 into the programmer, type:

```
Action "CallCalibrationPoint2"
```
---|---  
  
  * To solve the stage calibration, type: 

```
Action "SolveCalibration"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
