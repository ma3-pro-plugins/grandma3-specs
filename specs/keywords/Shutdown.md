---
keyword: "ShutDown"
kind: general
shortcuts: ["Sh"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_shutdown.html"
---

## Official

To enter the ShutDown keyword in the command line, use one of these options:

  * Type **ShutDown**
  * Type the shortcut **Sh**

### Description

The ShutDown keyword powers down the grandMA3 console or closes the grandMA3 onPC.

It requires a confirmation in the local station and can be canceled within 10 seconds using a remote station.

|  **Hint:**  
---|---  
The device types are: [Console](https://help.malighting.com/grandMA3/2.5/HTML/keyword_console.html), [NetworkNode](https://help.malighting.com/grandMA3/2.5/HTML/keyword_networknode.html), [onPC](https://help.malighting.com/grandMA3/2.5/HTML/keyword_onpc.html), [ProcessingUnit](https://help.malighting.com/grandMA3/2.5/HTML/keyword_processingunit.html), [Session](https://help.malighting.com/grandMA3/2.5/HTML/keyword_session.html), [Station](https://help.malighting.com/grandMA3/2.5/HTML/keyword_station.html), and [Extension](https://help.malighting.com/grandMA3/2.5/HTML/keyword_extension.html).  
  
  
### Syntax

ShutDown (/Option)

ShutDown [Device_Type] ["Device_Name" or Device_Number] (/Option)

ShutDown IP [IP_Address] (/Option)

#### Option Keywords

The ShutDown keyword uses the following option keywords:

  * [/NoAutoClose](https://help.malighting.com/grandMA3/2.5/HTML/ok_noautoclose.html)
  * [/NoConfirmation](https://help.malighting.com/grandMA3/2.5/HTML/ok_noconfirmation.html)
  * [/NoSave](https://help.malighting.com/grandMA3/2.5/HTML/ok_nosave.html)
  * [/Save](https://help.malighting.com/grandMA3/2.5/HTML/ok_save.html)
  * [/Wait](https://help.malighting.com/grandMA3/2.5/HTML/ok_wait.html)

### Examples  
  

  * To shut down the current station and provoke a countdown pop-up, type:

```
ShutDown
```
---|---  
  
  * To shut down the station with the IP address 192.168.0.4, type:

```
ShutDown IP 192.168.0.4
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
