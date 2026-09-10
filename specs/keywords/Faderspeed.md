---
keyword: "FaderSpeed"
kind: general
shortcuts: ["Faders"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_faderspeed.html"
---

## Official

To enter the FaderSpeed keyword in the command line, use one of the options:

  * Type **FaderSpeed**
  * Type the shortcut **Faders**

### Description

The FaderSpeed keyword applies the Speed function to a number of objects such as executors, sequences, groups, masters, and other.

It controls the speed of a phaser in a cue.

For more information see [Executors](https://help.malighting.com/grandMA3/2.5/HTML/executor_assign.html#Change Fader Function), [Cues and Sequences](https://help.malighting.com/grandMA3/2.5/HTML/cue_sequence.html), [Groups](https://help.malighting.com/grandMA3/2.5/HTML/group.html), or  [Masters](https://help.malighting.com/grandMA3/2.5/HTML/masters.html).

### Syntax

Assign FaderSpeed At [Object] ["Object_Name" or Object_Number]

FaderSpeed [Object] ["Object_Name" or Object_Number] At [Speed_Readout] [Speed_Value]

### Examples  
  

  * To assign FaderSpeed to executor 206, type:

```
Assign FaderSpeed At Executor 206
```
---|---  
  
  * To set the FaderSpeed of sequence 2 to 6 BPM, type:

```
FaderSpeed Sequence 2 At BPM 6
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
