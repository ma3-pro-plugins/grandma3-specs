---
keyword: "FaderTime"
kind: general
shortcuts: ["Faderti"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_fadertime.html"
---

## Official

To enter the FaderTime keyword in the command line, use one of the options:

  * Type **FaderTime**
  * Type the shortcut **Faderti**

### Description

The FaderTime keyword applies the Time function to a number of objects such as executors, sequences, groups, masters, and other. It is used to overwrite the stored cue part times by setting a time value and activating the time function. 

For more information about cue time overwriting see [Cue Timing](https://help.malighting.com/grandMA3/2.5/HTML/cue_timing.html).

For more information on how to activate and deactivate the function see [Time](https://help.malighting.com/grandMA3/2.5/HTML/keyword_time.html).

### Syntax

Assign FaderTime At [Object] ["Object_Name" or Object_Number]

FaderTime [Object] ["Object_Name" or Object_Number] At [Value]

### Examples  
  

  * To assign FaderTime function to executor 207 on the selected page, type:

```
Assign FaderTime At Executor 207
```
---|---  
  
  * To set the FaderTime value to 50% of the time range for the selected sequence, type:

```
FaderTime At 50
```
---|---  
  
  * To set the FaderTime value to 10% of the time range for sequence 5, type:

```
FaderTime Sequence 5 At 10
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
