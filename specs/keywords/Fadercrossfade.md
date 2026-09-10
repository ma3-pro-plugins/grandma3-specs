---
keyword: "FaderCrossFade"
kind: general
shortcuts: ["FaderX", "Faderc"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_fadercrossfade.html"
---

## Official

To enter the FaderCrossFade keyword in the command line:

  * Type **FaderCrossFade**
  * Type the**** shortcut **FaderX** or **Faderc**

### Description

The FaderCrossFade keyword represents the crossfade function of a sequence.

Crossfade gradually activates the next cue of a sequence in accordance with the position of the fader.

For more information see [Executors](https://help.malighting.com/grandMA3/2.5/HTML/executor_assign.html#Change Fader Function).

### Syntax

[Function] FaderCrossFade At [Object] ["Object_Name" or Object_Number]

FaderCrossFade [Object] ["Object_Name or Object_Number] At [Value] 

### Example  
  

  * To assign FaderCrossFade as executor 302, type:

```
Assign FaderCrossFade At Executor 302
```
---|---  
  
  * To set the FaderCrossFade value of the fader range to 10% in sequence 5, type:

```
FaderCrossFade Sequence 5 At 10
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
