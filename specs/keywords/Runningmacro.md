---
keyword: "RunningMacro"
kind: general
shortcuts: ["Runningm"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_runningmacro.html"
---

## Official

To enter the RunningMacro keyword in the command line, use one of the options:

  * Type **RunningMacro**
  * Type the shortcut **Runningm**

### Description

The RunningMacro keyword addresses macros that are playing back. 

It allows you to list or disable all running macros in a show file.

|  **Important:**  
---|---  
The numbers of the running macros are not equal to the numbers of macros in the macros data pool.  
  
  
### Syntax

[Function] RunningMacro ["RunningMacro_Name" or RunningMacro_Number]

### Example  
  

  * To disable the first macro that is currently running, type:

```
Off RunningMacro 1
```
---|---  
  
  * To list all running macros, change destination first and type:

```
ChangeDestination RunningMacro
```
---|---  
  
  

  * Then type:

|  User name@Temp/Cmdlines/Cmdline 1/RunningPlaybacks>Set RunningPlayback Property "SelectedPlaybackType" "Macro"  
---|---  
  

  

  * After that type:

| User name@Temp/Cmdlines/Cmdline 1/RunningPlaybacks>List  
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
