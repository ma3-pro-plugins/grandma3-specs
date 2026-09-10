---
keyword: "ScreenContent"
kind: general
shortcuts: ["Scre"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_screencontent.html"
---

## Official

To enter the ScreenContent keyword in the command line, use one of the options:

  * Type **ScreenContent**
  * Type the shortcut **Scre**

### Description

The ScreeContent keyword is used to represent the windows of a display.

### Syntax

[Function] ScreenContent

[Function] ScreenContent [Screen_Number].["Window_Name" or Window_Number]

### Option Keywords

The ScreenContent keyword uses the following option keywords:

  * [/AutoFit](https://help.malighting.com/grandMA3/2.5/HTML/ok_autofit.html)

### Examples  
  

  * To delete all windows on all screens, type:

```
Delete ScreenContent *.*
```
---|---  
  
  * To delete all windows on screen 1, type:

```
Delete ScreenContent 1.*
```
---|---  
  
  * To set the width of the first window you created to 12 half columns in screen 1, type:

```
Set ScreenContent 1.1 "W" "12"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
