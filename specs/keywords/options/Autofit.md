---
keyword: "/AutoFit"
kind: option
shortcuts: ["/Autof"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_autofit.html"
---

## Official

To enter the **/AutoFit** option keyword in the command line, use one of the options: 

  * Type **/AutoFit**
  * Type the shortcut**/Autof**

###  Description 

The /AutoFit option keyword is used to position any window in the next unoccupied area of a specified screen respecting the minimum requirements of the window. If you are in a help topic, use the Command Bot which opens the corresponding UI window using this logic. For more information on our bot see [Navigate in the Help](https://help.malighting.com/grandMA3/2.5/HTML/atm_navigate_in_the_help.html). 

Syntax

Store ScreenContent [Display_Number or Default] ["Window_Name"] /AutoFit

###  General Keywords 

General keywords that use the /AutoFit option keyword: 

  * [ScreenContent keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_screencontent.html)
  * [Store keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_store.html)

###  Example   
  

  * To open the fixture sheet in a free area of the screen you have currently the focus in, type: 

```
Store ScreenContent Default "WindowFixtureSheet" /AutoFit
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
