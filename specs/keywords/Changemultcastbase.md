---
keyword: "ChangeMulticastBase"
kind: general
shortcuts: ["Changem"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_changemultcastbase.html"
---

## Official

To enter the ChangeMulitcastBase keyword in the command line, use one of the options: 

  * Type **ChangeMulticastBase**
  * Type the shortcut ****Changem****

###  Description 

The ChangeMulticastBase keyword is a function keyword used to change the current address of the Multicast Base. 

For more information see [Session](https://help.malighting.com/grandMA3/2.5/HTML/network_session.html).

###  Syntax

ChangeMulticastBase [Device_Type] ["Device_Name" or Device_Number] /Type "Type_Value"

ChangeMulticastBase IP [IP] /Type "Type_Value"

### Option Keywords

The ChangeMulticastBase keyword uses the following option keywords:

  * [/Type](https://help.malighting.com/grandMA3/2.5/HTML/ok_type.html)

###  Examples

  * To change the address of multicast base to **Alternative** , type: 

```
ChangeMulticastBase Processing Unit Thru /Type "Alternative"
```
---|---  
  
  * To change the address of multicast base to **Default** on the device with the IP 192.168.0.4, type:

```
ChangeMulticastBase IP 192.168.0.4 Thru /Type "Default"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
