---
keyword: "Load"
kind: general
shortcuts: []
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_load.html"
---

## Official

To enter the Load keyword in the command line, use one of the options:

  * Press `Goto` `Goto`
  * Type **Load**

### Description

The Load keyword is a playback keyword which is used to prepare an executor to jump to another cue rather than jumping to the next cue when a [Go+](https://help.malighting.com/grandMA3/2.5/HTML/keyword_goplus.html) is performed on the executor.

For more information on how to assign executors see [Assign Objects to an Executor](https://help.malighting.com/grandMA3/2.5/HTML/executor_assign.html). 

### Syntax

****Load [Object] ["Object_Name" or Object_Number]****

### Examples  
  

  * To load cue 3 on the [selected](https://help.malighting.com/grandMA3/2.5/HTML/keyword_select.html) executor, type:

```
Load Cue 3
```
---|---  
  
Cue 3 is loaded. To indicate that a cue is loaded, the display toggles between Cue 3 and Cue "Name".

  * To load cue 5 on executor 114, type:

```
Load Executor 114 Cue 5
```
---|---  
  
  * To load cue +2 on executor 114, type:

```
Load +2 Executor 114
```
---|---  
  
  * To load the previous cue on executor 114, type:

```
Load Previous Executor 114
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
