---
keyword: "RunningTimer"
kind: general
shortcuts: []
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_runningtimer.html"
---

## Official

To enter the RunningTimer keyword in the command line, type **RunningTimer**.

### Description

The RunningTimer keyword addresses running timers.

|  **Important:**  
---|---  
The numbers of the running timers are not equal to the numbers of timers in the timers data pool.  
  
  
### Syntax

[Function] RunningTimer ["RunningTimer_Name" or RunningTimer_Number]

### Examples  
  

  * To disable the first timer that is currently running, type:

```
Off RunningTimer 1
```
---|---  
  
  

  * To list all running timers, change destination first and type:

```
ChangeDestination RunningTimer
```
---|---  
  
  

  * Then type:

|  User name@Temp/Cmdlines/Cmdline 1/RunningPlaybacks>Set RunningPlayback Property "SelectedPlaybackType" "Timer"  
---|---  
  
  * After that type:

|  User name@Temp/Cmdlines/Cmdline 1/RunningPlaybacks>List   
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
