---
keyword: "ScreenConfiguration"
kind: general
shortcuts: ["Screenconf"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_screenconfiguration.html"
---

## Official

To enter the ScreenConfiguration keyword in the command line, use one of the options: 

  * Type **ScreenConfiguration**
  * Type the shortcut **Screenconf**

###  Description 

The ScreeConfiguration keyword is an object keyword that addresses the different screen configurations of a user profile. For example, one setup for the operation of a console, and a second setup for the operation of a dedicated onPC station. 

###  Syntax 

[Function] ScreenConfiguration ["ScreenConfiguration_Name" or ScreenConfiguration_Number]

###  Examples   
  

  * To store a new screen configuration called "Average Joe", type: 

```
Store ScreenConfiguration 3 "Average Joe"
```
---|---  
  
  * To enter screen configuration 2, type: 

```
ScreenConfiguration 2
```
---|---  
  
  * To assign the screen configuration "Average Joe" to ViewButton 1.6, type: 

```
Assign ScreenConfiguration "Average Joe" At ViewButton 1.6.
```
---|---  
  
For more information on ViewButtons see [Store and Recall Views](https://help.malighting.com/grandMA3/2.5/HTML/wvm_store_recall.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
