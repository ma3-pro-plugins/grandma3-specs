---
keyword: "MyRunningMacro"
kind: general
shortcuts: ["Myrunningm"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_myrunningmacro.html"
---

## Official

To enter the MyRunningMacro keyword in the command line, use one of the options: 

  * Type **MyRunningMacro**
  * Type the shortcut**My runningm**

###  Description 

The MyRunningMacro keyword addresses macro playbacks that were started by my user profile and are currently running.

|  **Important:**  
---|---  
The numbers of the running macros are not equal to the numbers of the macro in the macros data pool.   
  
  
###  Syntax 

**[Function]** MyRunningMacro ["MyRunningMacro_Name" or MyRunningMacro_Number]

###  Examples   
  

  * To disable the first macro that you started and that is currently running, type: 

```
Off MyRunningMacro 1
```
---|---  
  
  * To list all your running macros, change destination first and type: 

```
ChangeDestination MyRunningMacro
```
---|---  
  
  * Then type: 

|  User name@Temp/Cmdlines/Cmdline 1/RunningPlaybacks>Set MyRunningMacro Property "SelectedPlaybackType" "Macro" Property "SelectedMine" "Yes"  
---|---  
  
  

  * After that: 

|  User name@Temp/Cmdlines/Cmdline 1/RunningPlaybacks>List   
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
