---
keyword: "/Screen"
kind: option
shortcuts: ["/S"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_screen.html"
---

## Official

To enter the **/Screen** option keyword in the command line, use one of the options: 

  * Type **/Screen**
  * Type the shortcut**/S**

###  Description 

The /Screen option keyword addresses screens when storing or calling views. It can be used in conjunction with the [/ScreenOnly option keyword](https://help.malighting.com/grandMA3/2.5/HTML/ok_screenonly.html). 

###  Syntax 

[Function] [Object] ["Object_Name" or Object_Number] /Screen

###  General Keywords 

General keywords that use the /Screen option keyword: 

  * [Call keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_call.html)
  * [Store keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_store.html)
  * [View keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_view.html)
  * [ViewButton keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_viewbutton.html)

###  Examples   
  

  * To store screen 1 on the view button 1, type: 

```
Store View 1 /Screen "1"
```
---|---  
  

  * To call view 5 on screen 2, type: 

```
View 5 /Screen "2"
```
---|---  
  
  

  * To call the view which is assigned to view button 1, screen 2 on screen 3, type: 

```
ViewButton 2.1 /Screen "3"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
