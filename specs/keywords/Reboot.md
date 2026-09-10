---
keyword: "Reboot"
kind: general
shortcuts: ["R"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_reboot.html"
---

## Official

To enter the Reboot keyword in the command line, use one of the following options:

  * Type **Reboot**
  * Type the shortcut **R**

### Description

The Reboot keyword is a function keyword that is used to shut down the station in use and boot it up again.

A confirmation pop-up opens on the station in use.

|  **Hint:**  
---|---  
The device types are: [Console](https://help.malighting.com/grandMA3/2.5/HTML/keyword_console.html), [NetworkNode](https://help.malighting.com/grandMA3/2.5/HTML/keyword_networknode.html), [onPC](https://help.malighting.com/grandMA3/2.5/HTML/keyword_onpc.html), [ProcessingUnit](https://help.malighting.com/grandMA3/2.5/HTML/keyword_processingunit.html), [Session](https://help.malighting.com/grandMA3/2.5/HTML/keyword_session.html), [Station](https://help.malighting.com/grandMA3/2.5/HTML/keyword_station.html), and [Extension](https://help.malighting.com/grandMA3/2.5/HTML/keyword_extension.html).  
  
  
### Syntax

Reboot (/Option)

Reboot IP [IP_Address] (/Option)

Reboot [Device_Type] ["Device_Name" or Device_Number] (/Option)

Option Keywords

The Reboot keyword uses the following option keywords:

  * [/NoConfirmation](https://help.malighting.com/grandMA3/2.5/HTML/ok_noconfirmation.html)
  * [/NoSave](https://help.malighting.com/grandMA3/2.5/HTML/ok_nosave.html)
  * [/Save](https://help.malighting.com/grandMA3/2.5/HTML/ok_save.html)
  * [/Wait](https://help.malighting.com/grandMA3/2.5/HTML/ok_wait.html)

### Examples  
  

  * To reboot the connected grandMA3 processing unit 1, type:

```
Reboot ProcessingUnit 1
```
---|---  
  
  * To reboot the connected grandMA3 processing unit called "Stage Right", type:

```
Reboot ProcessingUnit "Stage Right"
```
---|---  
  
  * To reboot the console that uses the IP address 192.168.0.4, type:

```
Reboot IP 192.168.0.4
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
