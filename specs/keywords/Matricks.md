---
keyword: "MAtricks"
kind: general
shortcuts: ["Mat"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_matricks.html"
---

## Official

To enter the MAtricks keyword in the command line, use one of the following options:

  * Type **MAtricks**
  * Type the shortcut **Mat**

### Description

The MAtricks keyword behaves as an object type.

Used with an ID, MAtricks represents MAtricks objects stored in the MAtricks pool.

With the helping keywords On, Off, and Toggle, the MAtricks of the two selections may temporarily be enabled or disabled.

Furthermore, you can set the values of the MAtricks of the two selections.

### Syntax

Set Selection (Selection_Number) MAtricks (Property) ["Property_Name" or Property_Value]

[Function] MAtricks ["MAtricks_Name" or MAtricks_Number]

### Properties

X | Y | Z  
---|---|---  
XBlock | YBlock | ZBlock  
XGroup | YGroup | ZGroup  
XWings | YWings | ZWings  
XWidth | YWidth | ZWidth  
XShuffle | YShuffle | ZShuffle  
XShift | YShift | ZShift  
  
### Examples  
  

  * To set the MAtricks X to 2 in the active selection, type:

```
Set Selection MAtricks "X" 2
```
---|---  
  
  * To set the MAtricks XBlock to 4 in selection 2, type:

```
Set Selection 2 MAtricks "XBlock" 4
```
---|---  
  
  * To disable MAtricks in the active selection, type:

```
Off Selection MAtricks
```
---|---  
  
  * Toggle to activate MAtricks in the active selection, press `Set` or type:

```
Toggle Selection MAtricks
```
---|---  
  
  * To reset the MAtricks in the first selection, type:

```
Reset Selection 1 MAtricks
```
---|---  
  

  * To call the first MAtricks object in the MAtricks pool, type:

```
Call MAtricks 1
```
---|---  
  
  * To label MAtricks 2 "Great", type:

```
Label MAtricks 2 "Great"
```
---|---  
  
  * To assign the fourth MAtricks object of the pool to the first recipe in cue 1 part 0 of the selected sequence, type:

```
Assign MAtricks 4 At Cue 1 Part 0.1
```
---|---  
  
  * To apply the speed value of 10 Hz to the speed of the X property of the MAtricks selection, type:

```
Set Selection MAtricks "SpeedFromX" "Hz 10"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
