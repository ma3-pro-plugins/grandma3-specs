---
keyword: "/ScreenOnly"
kind: option
shortcuts: ["/Screeno"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_screenonly.html"
---

## Official

To enter the **/ScreenOnly** option keyword in the command line, use one of the options: 

  * Type **/Screen**
  * Type the shortcut**/Screeno**

###  Description 

The /ScreenOny option keyword defines which parts of the screen will be used when taking screenshots. It is used in conjunction with the [/Screen option keyword](https://help.malighting.com/grandMA3/2.5/HTML/ok_screen.html), the [/XResolution option keyword](https://help.malighting.com/grandMA3/2.5/HTML/ok_xresolution.html) and the [/YResolution option keyword](https://help.malighting.com/grandMA3/2.5/HTML/ok_yresolution.html).

###  Syntax

Store Image ["MediaPool_Name" or MediaPool_Number].["Image_Name" or Image_Number] /ScreenOnly ["Value"]

###  General Keywords 

General keywords that use the /ScreenOnly option keyword:

  * [Image keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_image.html)
  * [Store keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_store.html)

### Values

The /ScreenOnly option keyword uses these values:

  * Yes - This is the default if /ScreenOnly is not defined. The screenshot only includes the area that can be defined by the user. 
  * No - The entire screen will be used, including view bar, encoder bar and other.

###  Example  
  

  * To store a screenshot of the entire screen 1 as image 6, including view bar, encoder bar, and other, type: 

```
Store Image 3.6 /Screen "1" /ScreenOnly "No"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
