---
keyword: "Goto"
kind: general
shortcuts: ["Got"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_goto.html"
---

## Official

To enter the **Goto** keyword in the command line, use one of the options:

  * Press `Goto`
  * Type **Goto**
  * Type the shortcut **Got**

### Description

Goto is a function keyword that is used to jump in a list using the original cue timing of the cue where the values were initially stored. Setting fade times using the Goto keyword overrides the original cue timing. For more information see [Relevant Playback Commands](https://help.malighting.com/grandMA3/2.5/HTML/cue_playback.html#h2__483879150). 

|  **Important:**  
---|---  
A set fade time overrides the original cue timing.  
  
  
### Syntax

Goto [Object]["Object_Name" or Object_Number or Next/Previous] (Fade [Fade_Time])

### Examples  
  

  * To go to cue 103 of the selected executor, type:

```
Goto Cue 103
```
---|---  
  
  * To go to cue 105 of executor 104, type:

```
Goto Cue 105 Executor 104
```
---|---  
  
  * To go to cue 10 of executor 201 using a fade time of 2 seconds, type:

```
Goto Cue 10 Executor 201 Fade 2
```
---|---  
  
  

  * To go to the next cue in the selected sequence, type:

```
Goto Cue Next
```
---|---  
  
  

  * To go to the previous cue in sequence 42, type:

```
Goto Sequence 42 Cue Previous
```
---|---  
  
For information on the key and its location see [Goto key](https://help.malighting.com/grandMA3/2.5/HTML/key_goto.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
