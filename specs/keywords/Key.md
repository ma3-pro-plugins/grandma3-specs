---
keyword: "Key"
kind: general
shortcuts: ["K"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_key.html"
---

## Official

To enter the Key keyword in the command line, use one of the options:

  * Type **Key**
  * Type the shortcut**K**

### Description

The Key keyword is used to address the network keys.

For more information on what network keys are see [Create a Custom Key](https://help.malighting.com/grandMA3/2.5/HTML/network_session_key.html). 

### Syntax

[Function] Key ["Key_Name" or Key_Number] (Property ["Property_Name" ] ["Value"])

### Examples  
  

  * To store a new key, type:

```
Store Key 2
```
---|---  
  
  * To list all keys, type:

```
List Key
```
---|---  
  
  * To set a different password for a newly created key, type:

```
Set Key 2 Property "Seed" "Concord Dawn"
```
---|---  
  
  * To not use key 2 for MAnet, type:

```
Set Key 2 Property "MANET" "No"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
