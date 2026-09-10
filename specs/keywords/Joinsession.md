---
keyword: "JoinSession"
kind: general
shortcuts: ["J"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_joinsession.html"
---

## Official

To enter the JoinSession keyword in the command line, use one of the options:

  * Type **JoinSession**
  * Type the shortcut **J**

### Description

JoinSession is a function keyword which is used to join a session.

### Syntax

JoinSession IP [Device_IP]

**JoinSession [DeviceType] ["Device_Name" or Device_Number]**

|  **Hint:**  
---|---  
The device types are: [Console](https://help.malighting.com/grandMA3/2.5/HTML/keyword_console.html), [Node](https://help.malighting.com/grandMA3/2.5/HTML/keyword_networknode.html), [onPC](https://help.malighting.com/grandMA3/2.5/HTML/keyword_onpc.html), [ProcessingUnit](https://help.malighting.com/grandMA3/2.5/HTML/keyword_processingunit.html), [Station](https://help.malighting.com/grandMA3/2.5/HTML/keyword_station.html), [Extension](https://help.malighting.com/grandMA3/2.5/HTML/keyword_extension.html).  
  
  
### Examples  
  

  * To join the session of console 6, type:

```
JoinSession Console 6
```
---|---  
  
  * To join the session on the station with the IP address 192.168.10.21, type:

```
JoinSession IP 192.168.10.21
```
---|---  
  
  * To join the session of the node "Truss", type:

```
JoinSession Node "Truss"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
