---
keyword: "FaderRate"
kind: general
shortcuts: ["Faderr"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_faderrate.html"
---

## Official

To enter the FaderRate keyword in the command line, use one of the options:

  * Type **FaderRate**
  * Type the shortcut **Faderr**

### Description

The FaderRate keyword applies the Rate function to a number of objects such as executors, sequences, groups, masters, presets, and other.

Rate divides or multiplies the fade and delay time in a sequence by the value of the fader. If Speed from Rate is enabled, it is then also valid for the speed stored in cues.

For more information see [Executors](https://help.malighting.com/grandMA3/2.5/HTML/executor_assign.html#Change Fader Function), [Cues and Sequences](https://help.malighting.com/grandMA3/2.5/HTML/cue_sequence.html), [Presets](https://help.malighting.com/grandMA3/2.5/HTML/presets.html), [Groups](https://help.malighting.com/grandMA3/2.5/HTML/group.html), or [Masters](https://help.malighting.com/grandMA3/2.5/HTML/masters.html).

### Syntax

Assign FaderRate At [Object] ["Object_Name " or Object_Number]

FaderRate [Object] ["Object_Name" or Object_Number] At [Value]

### Examples  
  

  * To assign FaderRate to executor 205, type:

```
Assign FaderRate At Executor 205
```
---|---  
  
  * To move the rate fader of sequence 1 to 1:1, type:

```
FaderRate Sequence 1 At 100
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
