---
keyword: "FaderMaster"
kind: general
shortcuts: ["Faderm"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_fadermaster.html"
---

## Official

To enter the FaderMaster keyword in the command line, use one of the options:

  * Type **FaderMaster**
  * Type the shortcut **Faderm**
  * Press `MA` \+ `X16 | Exec` \+ `X16 | Exec` \+ `X16 | Exec`

### Description

The FaderMaster keyword applies the Master function to a number of objects such as executors, sequences, groups, masters, and other.

The master function controls the intensity of the assigned object.

For more information see [Executors](https://help.malighting.com/grandMA3/2.5/HTML/executor_assign.html#Change Fader Function), [Cues and Sequences](https://help.malighting.com/grandMA3/2.5/HTML/cue_sequence.html), [Groups](https://help.malighting.com/grandMA3/2.5/HTML/group.html), or  [Masters](https://help.malighting.com/grandMA3/2.5/HTML/masters.html).

### Syntax

Assign FaderMaster At [Object] ["Object_Name" or Object_Number]

FaderMaster [Object] ["Object_Name" or Object_Number] At [Value] (Fade [Time])

Only sequences and presets can move the master using a fade time. Other objects snap to the value.

### Option Keywords

The FaderMaster keyword uses the following option keywords: 

  * [/Type](https://help.malighting.com/grandMA3/2.5/HTML/ok_type.html)

### Examples  
  

  * To assign FaderMaster to executor 204, type:

```
Assign FaderMaster At Executor 204
```
---|---  
  
  * To move FaderMaster 205 at position 50% in a 5 seconds fade:

```
FaderMaster 205 At 50 Fade 5
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
