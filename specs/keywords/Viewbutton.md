---
keyword: "ViewButton"
kind: general
shortcuts: ["ViewB"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_viewbutton.html"
---

## Official

To enter the ViewButton keyword in the command line, use one of the options:

  * Press `MA` \+ `X7|View` \+ `X7|View`
  * Type **ViewButton**
  * Type the shortcut**ViewB**
  * Type **VB**

### Description

The ViewButton keyword is an object keyword which is used to call or store the object assigned on the view button.

Calling a view button only works if the object assigned to it supports it.

For more information see the [Call Keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_call.html).

### Syntax

ViewButton [Screen_Number].["ViewButton_Name" or ViewButton_Number] (/Option "[Option_Value]")

[Function] ViewButton [Screen_Number].["ViewButton_Name" or ViewButton_Number] (/Option "[Option_Value]")

### Option Keywords

The ViewButton keyword uses the following option keywords:

  * [/Screen](https://help.malighting.com/grandMA3/2.5/HTML/ok_screen.html)

### Examples  
  

  * To call the view assigned to ViewButton 4 on screen 2, type:

```
ViewButton 2.4
```
---|---  
|  **Important:**  
---|---  
If you do not specify the screen location using the /Screen option keyword, the view will be called to the screen that currently has focus.  
  
  
  

  * To assign the user pool object "Guest" to ViewButton 1.1, type:

```
Assign User "Guest" At ViewButton 1.1
```
---|---  
  
  * To remove the object assigned to ViewButton 4, screen 1, type:

```
Delete ViewButton 1.4
```
---|---  
  
  * To label the view that is assigned to ViewButton 5 on screen 2 "Layout", type:

```
Label ViewButton 2.5 "Layout"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
