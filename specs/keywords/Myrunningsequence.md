---
keyword: "MyRunningSequence"
kind: general
shortcuts: ["My"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_myrunningsequence.html"
---

## Official

To enter the MyRunningSequence keyword in the command line, use one of the options: 

  * Type **MyRunningSequence**
  * Type the shortcut **My**

###  Description 

The MyRunningSequence keyword addresses sequence playbacks that were started by my user profile and are currently running.

| **Important:**  
---|---  
The numbers of the running sequences are not equal to the numbers of sequences in the sequences data pool.   
  
  
###  Syntax 

**[Function]** MyRunningSequence ["MyRunningSequence_Name" or MyRunningSequence_Number]

###  Examples   
  

  * To disable the first sequence that is running and which you started, type: 

```
Off MyRunningSequence 1
```
---|---  
  
  * To list all your running sequences, change destination first and type:

```
ChangeDestination RunningPlayback
```
---|---  
  
  

  * Then type:

| User name@Temp/Cmdlines/Cmdline 1/RunningPlaybacks>Set MyRunningSequence Property "SelectedPlaybackType" "Sequence" Property "SelectedMine" "Yes"  
---|---  
  
  

  * After that:

|  User name@Temp/Cmdlines/Cmdline 1/RunningPlaybacks>List   
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
