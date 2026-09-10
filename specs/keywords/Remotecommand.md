---
keyword: "RemoteCommand"
kind: general
shortcuts: []
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_remotecommand.html"
---

## Official

To enter the RemoteCommand keyword, use one of the options:

  * Type **RemoteCommand**
  * Type **RC**
  * Type**Remotec**

### Description

The RemoteCommand keyword remotely sends commands to other stations.

|  **Hint:**  
---|---  
The device types are: [Console](https://help.malighting.com/grandMA3/2.5/HTML/keyword_console.html), [NetworkNode](https://help.malighting.com/grandMA3/2.5/HTML/keyword_networknode.html), [onPC](https://help.malighting.com/grandMA3/2.5/HTML/keyword_onpc.html), [ProcessingUnit](https://help.malighting.com/grandMA3/2.5/HTML/keyword_processingunit.html), [Session](https://help.malighting.com/grandMA3/2.5/HTML/keyword_session.html), [Station](https://help.malighting.com/grandMA3/2.5/HTML/keyword_station.html), and [Extension](https://help.malighting.com/grandMA3/2.5/HTML/keyword_extension.html).  
  
  
### Syntax

RemoteCommand IP [IP] ["Command to be Executed"]

RemoteCommand [Device_Type] ["Device_Name" or Device_Number] ["Command to be Executed"]

### Example  
  

  * To remotely execute the command "Call ViewButton 2.1" on the station with the IP address 192.168.0.10, type:

```
RemoteCommand IP 192.168.0.10 "Call ViewButton 2.1"
```
---|---  
  
  * To remotely lock the desk on the station with the IP address 192.168.0.10, type:

```
RemoteCommand IP 192.168.0.10 'Menu "DeskLock" '
```
---|---  
  
**Alternatively type:**

```
RemoteCommand IP 192.168.0.10 "Menu 'DeskLock' "
```
---|---  
  
For more information on the usage of quotation marks see [General Syntax Rules](https://help.malighting.com/grandMA3/2.5/HTML/csk_syntax_rules.html). 

For more mutual examples see the [Station Keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_station.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
