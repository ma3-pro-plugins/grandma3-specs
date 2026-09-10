---
keyword: "MyRunningTimer"
kind: general
shortcuts: []
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_myrunningtimer.html"
---

## Official

To enter the MyRunningTimer keyword in the command line, use one of the options:

  * Type **MyRunningTimer**

### Description

The MyRunningTimer keyword addresses timer playbacks that were started by my user profile and are currently running.

|  **Important:**  
---|---  
The numbers of the running timers are not equal to the numbers of timers in the timers data pool.  
  
  
### Syntax

**[Function]** MyRunningTimer ["MyRunningTimer_Name" or MyRunningTimer_Number]

### Examples  
  

  * To disable the first timer that is running and which you started, type:

```
Off MyRunningTimer 1
```
---|---  
  
  * To list all your running timers, change destination first and type:

```
ChangeDestination RunningPlayback
```
---|---  
  
  

  * Then type:

|  User name@Temp/Cmdlines/Cmdline 1/RunningPlaybacks>Set MyRunningTimer Property "SelectedPlaybackType" "Timer" Property "SelectedMine" "Yes"  
---|---  
  
  

  * After that type:

|  User name@Temp/Cmdlines/Cmdline 1/RunningPlaybacks>List   
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
