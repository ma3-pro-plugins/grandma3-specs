---
keyword: "Master"
kind: general
shortcuts: ["Mas"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_master.html"
---

## Official

To enter the **Master** keyword in the command line, use one of the options: 

  * Type **Master**
  * Type the shortcut **Mas**

###  Description 

The Master keyword is an object keyword that is used to address the different master functions, e.g., for the selected sequence, grand masters, speed masters and playback masters. 

###  Syntax 

**[Function] Master**["MasterCategory_Name" or MasterCategory_Number].["Master_Name" or Master_Number]

Master [MasterCategory_Number].["Master_Name" or Master_Number] At [SpeedReadout] [SpeedReadout_Value]

###  Examples   
  

  * To assign the master to the selected sequence on executor 206, type: 

```
Assign Master 1.1 At Executor 206
```
---|---  
  
  * To assign the grand master to executor 207, type: 

```
Assign Master 2.1 At Executor 207
```
---|---  
  
  * To label the second speed master "Great Speed", type: 

```
Label Master 3.2 "Great Speed"
```
---|---  
  
  * To assign the playback master 3 to executor 209 on page 6, type: 

```
Assign Master 4.3 At Page 6.209
```
---|---  
  
For more information on how to assign objects to executors see [Assign Object to an Executor](https://help.malighting.com/grandMA3/2.5/HTML/executor_assign.html). 

  * To set the first speed master to a speed of 42 BPM, type: 

```
Master 3.1 At BPM 42
```
---|---  
  
  

  * To set the first speed master to a speed of 2 hertz, type: 

```
Master 3."Speed1" At Hz 2
```
---|---  
  
  

  * To set the first speed master to a speed of 0.69 seconds, type: 

```
Master 3."Speed1" At Seconds 0.69
```
---|---  
  
  

|  **Hint:**  
---|---  
You can also set the speed readout of other objects such as sequences and presets.

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
