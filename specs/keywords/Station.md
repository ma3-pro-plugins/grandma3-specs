---
keyword: "Station"
kind: general
shortcuts: ["Stat"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_station.html"
---

## Official

To enter the Station keyword in the command line, use one of the options:

  * Type **Station**
  * Type the shortcut **Stat**

### Description

The Station keyword is an object keyword which is used to address all stations in the network. You can also [invite](https://help.malighting.com/grandMA3/2.5/HTML/keyword_invite.html) stations to your session or [dismiss](https://help.malighting.com/grandMA3/2.5/HTML/keyword_dismiss.html) them.

|  **Hint:**  
---|---  
A station is a physical device in the grandMA3 system that can participate in a session and exchange data with other devices in the network.  
  
Stations include:

  * [Console](https://help.malighting.com/grandMA3/2.5/HTML/keyword_console.html)
  * [NetworkNode](https://help.malighting.com/grandMA3/2.5/HTML/keyword_networknode.html)
  * [onPC](https://help.malighting.com/grandMA3/2.5/HTML/keyword_onpc.html)
  * [ProcessingUnit](https://help.malighting.com/grandMA3/2.5/HTML/keyword_processingunit.html)
  * [Extension](https://help.malighting.com/grandMA3/2.5/HTML/keyword_extension.html)

  
  

### Syntax

[Function] Station ["DeviceType_Name" or DeviceType_Number].["Device_Name" or Device_Number]

### Examples  
  

  * To list all existing stations types in the same network, type:

```
List Station
```
---|---  
  
  * To invite console "FOH3" to your session, type:

```
Invite Station "Console"."FOH3"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
