---
keyword: "/Wait"
kind: option
shortcuts: ["/Wa"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_wait.html"
---

## Official

To enter the **/Wait** option keyword in the command line, use one of the options: 

  * Type **/Wait**
  * Type the shortcut**/Wa**

###  Description 

In conjunction with the Store keyword /Wait option keyword defines the latency time in milli seconds after which your command will be executed. When used with remote calls such as reboot, restart or shut down, the /Wait option keyword defines the time in the countdown of the the pop-up that consequently appears after executing the command.

Syntax

[Function] /Wait [LatencyTime]

###  General Keywords 

General keywords that use the /Wait option keyword: 

  * [Store keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_store.html)
  * [Reboot keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_reboot.html)
  * [Restart keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_restart.html)
  * [ShutDown keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_shutdown.html)

|  **Hint:**  
---|---  
/Wait currently works with the keyword Store and remote calls such as ShutDown or Restart and other. The defined wait time in remote calls specifies the countdown time of the pop-up.  
  
  
###  Examples  
  

  * To delay the Replace this syntax text Store Cue 5 command by 3 seconds, type:

```
Store Cue 5 /Wait 3000
```
---|---  
  
  

  * To set the countdown of the ShutDown pop-up to 20 seconds, type:

```
ShutDown /Wait 20000
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
