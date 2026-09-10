---
keyword: "MyRunningSoundFile"
kind: general
shortcuts: ["Myrunningso"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_myrunningsoundfile.html"
---

## Official

To enter the MyRunningSoundFile keyword in the command line, use one of the options: 

  * Type **MyRunningSoundFile**
  * Type the shortcut **Myrunningso**

###  Description 

The MyRunningSoundFile keyword addresses sound playbacks that were started by my user profile and are currently running.

|  **Important:**  
---|---  
The numbers of the running sound files are not equal to the numbers of sound files in the sound pool.   
  
  
###  Syntax 

**[Function]** MyRunningSoundFile ["MyRunningSoundFile_Name" or MyRunningSoundFile_Number]

###  Examples   
  

  * To disable the first sound file that is running and which you started, type: 

```
Off MyRunningSoundFile 1
```
---|---  
  
  * To list all your running sound files, change destination first and type: 

```
ChangeDestination MyRunningSoundFile
```
---|---  
  
  * Then type:

| User name@Temp/Cmdlines/Cmdline 1/RunningPlaybacks>Set MyRunningSoundFile Property "SelectedPlaybackType" "Sound" Property "SelectedMine" "Yes"  
---|---  
  
  

  * After that type:

| User name@Temp/Cmdlines/Cmdline 1/RunningPlaybacks>List  
  
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
