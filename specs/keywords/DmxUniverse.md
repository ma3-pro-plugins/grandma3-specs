---
keyword: "DMXUniverse"
kind: general
shortcuts: ["Dmx"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_dmx_universe.html"
---

## Official

To enter the DMXUniverse in the command line, use one of the options:

  * Press `MA` \+ `X8 | DMX`
  * Type **DMXUniverse**
  * Type the shortcut **Dmx**

### Description

The DMXUniverse keyword is used to access DMX universes or all DMX channels of a universe.

### Syntax

[Function] DMXUniverse ["DMXUniverse_Name" or DMXUniverse_Number]

DMXUniverse ["DMXUniverse_Name" or DMXUniverse_Number] At ([Readout]) [Value]

### Examples  
  

  * To patch all DMX channels of universe 1 to universe 11, type:

```
​Move DMXUniverse 1 At DMXUniverse 11
```
---|---  
  
  * To select the fixture patched to universe 2.001, type:

```
SelectFixtures DMXUniverse 2.001
```
---|---  
  
  

  * To output 50% on the third DMX channel of universe 1 using the DMX testing function, type:

```
DMXUniverse 1.3 At 50
```
---|---  
  
  * To output 42% on the DMX channels 8 to 15 on universe 2 using the DMX testing function, type:

```
DMXUniverse 2.8 Thru 15 At 42
```
---|---  
  
  * To disable the DMX testing function on all DMX channels of all universes, type:

```
Off DMXUniverse Thru
```
---|---  
  
For information on the key and its location see [X8 | DMX key](https://help.malighting.com/grandMA3/2.5/HTML/key_x8.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
