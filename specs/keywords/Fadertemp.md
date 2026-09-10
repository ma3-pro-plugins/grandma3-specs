---
keyword: "FaderTemp"
kind: general
shortcuts: ["Fadert"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_fadertemp.html"
---

## Official

To enter the FaderTemp keyword in the command line, use one of the options:

  * Type **FaderTemp**
  * Type the shortcut **Fadert**

### Description

The FaderTemp keyword applies the Temp function to a number of objects such as executors, sequences, groups, masters, and other.

Temp crossfades the first cue on when pulled up, and off when pulled down.

For more information see [Executors](https://help.malighting.com/grandMA3/2.5/HTML/executor_assign.html#Change Fader Function), [Cues and Sequences](https://help.malighting.com/grandMA3/2.5/HTML/cue_sequence.html), [Groups](https://help.malighting.com/grandMA3/2.5/HTML/group.html), or  [Masters](https://help.malighting.com/grandMA3/2.5/HTML/masters.html).

### Syntax

Assign FaderTemp At [Object] ["Object_Name" or Object_Number]

FaderTemp [Object] ["Object_Name" or Object_Number] At [Value]

### Examples  
  

  * To assign FaderTemp to executor 301, type:

```
Assign FaderTemp At Executor 301
```
---|---  
  
  * To set the temp fader of sequence 2 to 42%, type: 

```
FaderTemp Sequence 2 At 42
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
