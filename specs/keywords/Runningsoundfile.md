---
keyword: "RunningSoundFile"
kind: general
shortcuts: ["Runningso"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_runningsoundfile.html"
---

## Official

To enter the RunningSoundFile keyword in the command line, use one of the options: 

  * Type **RunningSoundFile**
  * Type the shortcut **Runningso**

###  Description 

The RunningSoundFile keyword addresses sounds that are playing back. 

It allows you to disable all running sounds in a show file. 

| **Important:**  
---|---  
The numbers of the running sounds are not equal to the numbers of sounds in the sound pool.   
  
  
###  Syntax

**[Function]** RunningSoundFile ["RunningSoundFile_Name" or RunningSoundFile_Number]

###  Examples   
  

  * To disable the first sound that is currently running, type: 

```
Off RunningSoundFile 1
```
---|---  
  
  * To list all running sounds, change destination first and type: 

```
ChangeDestination RunningSoundFile
```
---|---  
  
  

  * Then type:

| User name@Temp/Cmdlines/Cmdline 1/RunningPlaybacks>Set RunningPlayback Property "SelectedPlaybackType" "Sound"   
---|---  
  
  * After that type:

|  User name@Temp/Cmdlines/Cmdline 1/RunningPlaybacks>List   
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
