---
keyword: "MessageCenter"
kind: general
shortcuts: ["Mes"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_messagecenter.html"
---

## Official

To enter the MessageCenter keyword in the command line, use one of the options:

  * Type **MessageCenter**
  * Type the shortcut **Mes**

### Description

The MessgeCenter keyword is an object keyword which is used to address the message center.

Syntax

Call MessageCenter (["Category.Priority"])

### Examples  
  

  * To confirm all messages in the message center, type:

```
Call MessageCenter
```
---|---  
  
  * To confirm all messages of the priority Error in MA-Net, type:

```
Call MessageCenter "MA-Net.Errors"
```
---|---  
  
  

  * To confirm all messages of the category Warning, type:

```
Call MessageCenter ".Warning"
```
---|---  
  
  

  * To confirm all messges of the category Power and of the priority Error, type:

```
Call MessageCenter "Power.Error"
```
---|---  
  
  

  * To confirm all messages of the category Power, type:

```
Call MessageCenter "Power."
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
