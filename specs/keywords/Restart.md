---
keyword: "Restart"
kind: general
shortcuts: ["Res"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_restart.html"
---

## Official

To enter the Restart keyword in the command line, use one of the options:

  * Type **Restart**
  * Type the shortcut **Res**

### Description

The Restart keyword is a function keyword that is used to restart the application. Restart behaves the same as closing the program and reopening it without shutting down the console.

|  **Hint:**  
---|---  
The device types are: [Console](https://help.malighting.com/grandMA3/2.5/HTML/keyword_console.html), [NetworkNode](https://help.malighting.com/grandMA3/2.5/HTML/keyword_networknode.html), [onPC](https://help.malighting.com/grandMA3/2.5/HTML/keyword_onpc.html), [ProcessingUnit](https://help.malighting.com/grandMA3/2.5/HTML/keyword_processingunit.html), [Session](https://help.malighting.com/grandMA3/2.5/HTML/keyword_session.html), [Station](https://help.malighting.com/grandMA3/2.5/HTML/keyword_station.html), and [Extension](https://help.malighting.com/grandMA3/2.5/HTML/keyword_extension.html).  
  
  
### Syntax

Restart (/Option)

Restart [Device_Type] ["Device_Name" or Device_Number] (/Option)

Restart IP [IP_Address] (/Option)

### Option Keywords

The Restart keyword uses the following option keywords:

  * [/NoConfirmation](https://help.malighting.com/grandMA3/2.5/HTML/ok_noconfirmation.html)
  * [/NoSave](https://help.malighting.com/grandMA3/2.5/HTML/ok_nosave.html)
  * [/Save](https://help.malighting.com/grandMA3/2.5/HTML/ok_save.html)
  * [/Wait](https://help.malighting.com/grandMA3/2.5/HTML/ok_wait.html)

### Examples  
  

  * To restart the application of the console, type:

```
Restart
```
---|---  
  
  * To restart the application of the station using the IP address 192.168.0.32, type:

```
Restart IP 192.168.0.32
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
