---
keyword: "DMXAddress"
kind: general
shortcuts: ["Dmxa"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_dmx_address.html"
---

## Official

To enter the DMXAddress in the command line, use one of the options:

  * Press `MA` \+ `X8 | DMX` \+ `X8 | DMX`
  * Type **DMXAddress**
  * Type the shortcut **Dmxa**

### Description

The DMXAddress keyword is used to access DMX addresses directly using an absolute numbering method.

### Syntax

[Function] DMXAddress [DMXAddress_Number]

**DMXAddress [DMXAddress_Number] At**([Readout]) [Value]

### Examples  
  

  * To select the fixture patched to universe 2, address 1, type:

```
SelectFixtures DMXAddress 513
```
---|---  
  
  * To output 50% on the third DMX channel of universe 1 using the DMX testing function, type:

```
DMXAddress 3 At 50
```
---|---  
  
  * To output 42% on the DMX channels 8 to 15 on universe 2 using the DMX testing function, type:

```
DMXAddress 520 Thru 527 At 42
```
---|---  
  
  * To disable the DMX testing function on all DMX channels of all universes, type:

```
Off DMXAddress Thru
```
---|---  
  
For information on the key and its location see [X8 | DMX key](https://help.malighting.com/grandMA3/2.5/HTML/key_x8.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
