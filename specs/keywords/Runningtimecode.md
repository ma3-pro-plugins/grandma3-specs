---
keyword: "RunningTimecode"
kind: general
shortcuts: ["Runningt"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_runningtimecode.html"
---

## Official

To enter the RunningTimecode keyword in the command line, use one of the options:

  * Type **RunningTimecode**
  * Type the shortcut **Runningt**

### Description

The RunningTimecode keyword addresses timecodes that are playing back. 

|  **Important:**  
---|---  
The numbers of the running timcodes are not equal to the numbers of timecodes in the timecodes data pool.  
  
  
### Syntax

[Function] RunningTimcode ["RunningTimecode_Name" or RunningTimecode_Number]

### Examples  
  

  * To disable the first timecode that is currently running, type:

```
Off RunningTimecode 1
```
---|---  
  
  * To list all running timecodes, change destination first and type:

```
ChangeDestination RunningTimecode
```
---|---  
  
  * Then type:

| User name@Temp/Cmdlines/Cmdline 1/RunningPlaybacks>Set RunningPlayback Property "SelectedPlaybackType" "Timecode"  
---|---  
  
  

  * After that type:

|  User name@Temp/Cmdlines/Cmdline 1/RunningPlaybacks>List   
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
