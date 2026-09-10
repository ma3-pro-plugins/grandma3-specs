---
keyword: "Session"
kind: general
shortcuts: ["Ses"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_session.html"
---

## Official

To enter the Session keyword in the command line, use one of the options:

  * Type **Session**
  * Type the shortcut **Ses**

### Description

The Session keyword is an object keyword which is used to address all sessions in the network. If the name and number of session is not specified, your own session will be addressed.

The name of the session consists of the network properties "Session" and "Location" which are connected by @ – "Session@Location".

### Syntax

[Function] Session ["Session_Name" or Session_Number] 

### Examples  
  

  * To restart all devices that have the same session credentials as your station, type:

```
Restart Session
```
---|---  
  
  

  * To shut down all devices that use the session name "Athena" with location "Caledonia", type:

```
ShutDown Session "Athena@Caledonia"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
