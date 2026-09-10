---
keyword: "Locate"
kind: general
shortcuts: ["Loca"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_locate.html"
---

## Official

To enter the Locate keyword in the command line, use one of the options: 

  * Press and hold `List`
  * Type **Locate**
  * Type the shortcut **Loca**

###  Description 

The Locate keyword is a function keyword that is used to locate objects that are assigned to executors and also locate ojects in pools. Repeatedly executing Locate on the same object cycles through all pages the pool object is assigned to. Other pool windows of the same object type will jump to the located object. If the object is located in numerous pages, a cycle count will be shown as long as you keep the object pressed.

Furthermore, the page can follow the located object. That is, the object that is assigned to an executor can be located in its pool. Once the object is located, it will start pulsating in red and the pool of the object will display a red and dotted frame. 

If Locate is active, the executor starts to blink. 

|  **Important:**  
---|---  
To cancel locate, press `ESC`.   
  
|  **Hint:**  
---|---  
To execute Locate in the temporary command controls, latch List.   
  
### Syntax 

Locate **[Object] ["Object_Name" or Object_Number]**

**Locate Page (["Page_Name" or Page_Number]) Executor ["Executor_Name" or Executor_Number]**

****Locate Page ["Page_Name" or Page_Number].["Executor_Name" or Executor_Number]****

****Locate Reset (/KeepPage)  

### Option Keywords

The Locate keyword uses the following option keywords: 

  * [/KeepPage](https://help.malighting.com/grandMA3/2.5/HTML/keeppage.html)

### Examples  
  

  * To locate the group "FireWorks", type: 

```
Locate Group "FireWorks"
```
---|---  
  
  

  * To cancel locate, type:

```
Locate Reset
```
---|---  
  
  

For information on the key and its location see [List key](https://help.malighting.com/grandMA3/2.5/HTML/key_list.html). 

For information on Locate in the Masters see [Masters Window](https://help.malighting.com/grandMA3/2.5/HTML/ws_masters_window.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
