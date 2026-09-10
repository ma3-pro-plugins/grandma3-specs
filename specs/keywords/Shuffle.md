---
keyword: "Shuffle"
kind: general
shortcuts: ["Shuf"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_shuffle.html"
---

## Official

To enter the Shuffle keyword in the command line, use one of the options:

  * Press `SelFix` `SelFix`
  * Type **Shuffle**
  * Type the shortcut **Shuf**

### Description

Shuffle is a command keyword which is used to shuffle the order of the fixture selection. Shuffle is part of the MAtricks toolset.

For more information, see [MAtricks and Shuffle](https://help.malighting.com/grandMA3/2.5/HTML/matricks.html).

### Syntax

MAtricks **[ Axis]** **[Value]** text

MAtricks **[ Axis]** +

|  **Hint:**  
---|---  
The plus is a replacement of the value. You can either use plus/minus or a value.  
  
  
### Examples  
  

  * To shuffle the current selection on the y-axis, type:

```
MAtricks "YShuffle" +
```
---|---  
  
  

  * To shuffle the current selection on the z-axis, type:

```
MAtricks "ZShuffle" +
```
---|---  
  
  

  * It is also possible to set a certain value to any of the three shuffle settings. To set the shuffle to 4 for the x-axis, type:

```
MAtricks "XShuffle" 4
```
---|---  
  
|  **Hint:**  
---|---  
When deactivating or resetting the MAtricks, the original selection order will be restored.

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
