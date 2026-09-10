---
keyword: "FaderCrossFadeA"
kind: general
shortcuts: ["FaderXA"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_fadercrossfadea.html"
---

## Official

To enter the FaderCrossFadeA keyword in the command line:

  * Type**FaderCrossFadeA**
  * Type the shortcut **FaderXA**

### Description

The FaderCrossFadeA keyword represents the crossfade A function of a sequence.

Crossfade A gradually fades out dimmer attributes of a current cue in a sequence in accordance with the position of the fader.

For more information see [Executors](https://help.malighting.com/grandMA3/2.5/HTML/executor_assign.html#Change Fader Function).

### Syntax

[Function] FaderCrossFadeA At [Object] ["Object_Name" or Object_Number]

FaderCrossFadeA [Object] ["Object_Name" or Object_Number] At [Value]

### Example  
  

  * To assign FaderCrossFadeA as fader function as executor 303, type:

```
Assign FaderCrossFadeA At Executor 303
```
---|---  
  
  * To set the FaderCrossFadeA value to 10% of the fader range for sequence 5, type:

```
FaderCrossFadeA Sequence 5 At 10
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
