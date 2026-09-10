---
keyword: "FaderCrossFadeB"
kind: general
shortcuts: ["FaderXB"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_fadercrossfadeb.html"
---

## Official

To enter the FaderCrossFadeB keyword in the command line:

  * Type **FaderCrossFadeB**
  * Type the shortcut **FaderXB**

### Description

The FaderCrossFadeB keyword represents the crossfade B function of a sequence.

Crossfade B gradually fades in dimmer attributes of the next cue in a sequence in accordance with the position of the fader.

For more information see [Executors](https://help.malighting.com/grandMA3/2.5/HTML/executor_assign.html#Change Fader Function).

### Syntax

[Function] FaderCrossFadeB At ["Object_Name" or Object_Number]

FaderCrossFadeB [Object] ["Object_Name" or Object_Number] At [Value] 

### Example  
  

  * To assign FaderCrossFadeB as fader function to executor 304, type:

```
Assign FaderCrossFadeB At Executor 304
```
---|---  
  
  * To set the FaderCrossFadeB value of the fader range to 10% in sequence 5, type:

```
FaderCrossFadeB Sequence 5 At 10
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
