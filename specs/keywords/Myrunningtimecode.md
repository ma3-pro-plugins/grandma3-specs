---
keyword: "MyRunningTimecode"
kind: general
shortcuts: ["Myrunningt"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_myrunningtimecode.html"
---

## Official

To enter the MyRunningTimecode keyword in the command line, use one of the options: 

  * Type **MyRunningTimecode**
  * Type the shortcut **Myrunningt**

###  Description 

The MyRunningTimecode keyword addresses timecode playbacks that were started by my user profile and are currently running.

|  **Important:**  
---|---  
The numbers of the running timecodes are not equal to the numbers of timecodes in the timecode data pool.   
  
  
###  Syntax 

**[Function]** MyRunningTimecode ["MyRunningTimecode_Name" or MyRunningTimecode_Number]

###  Examples   
  

  * To disable the first timecode that is running and which you started, type: 

```
Off MyRunningTimecode 1
```
---|---  
  
  * To list all your running timecodes, change destination first and type: 

```
ChangeDestination RunningPlayback
```
---|---  
  
  * Then type:

|  User name@Temp/Cmdlines/Cmdline 1/RunningPlaybacks>Set MyRunningTimecode Property "SelectedPlaybackType" "Timecode" Property "SelectedMine" "Yes"  
---|---  
  
  

  * After that type:

| User name@Temp/Cmdlines/Cmdline 1/RunningPlaybacks>List  
  
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
