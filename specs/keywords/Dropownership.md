---
keyword: "DropOwnership"
kind: general
shortcuts: ["Dro"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_dropownership.html"
---

## Official

To enter the **DropOwnership** keyword in the command line, use one of the options:

  * Type **DropOwnership**
  * Type the shortcut **Dro**

### Description

The DropOwnership keyword is used when a user wants to edit an object that is currently owned by a different user. DropOwnership sends a request to release the ownership of an object. 

|  **Important:**  
---|---  
If a running process owns the object to protect data integrity, DropOwnwership might not work right away. If this should be the case, we recommend you use the command again.   
  
  
### Syntax

DropOwnership [Object] ["Object_Name" or Object_Number]

### Examples  
  

  * To request dropping ownership of group 1, type: 

```
DropOwnership Group 1
```
---|---  
  
  * To request dropping ownership of macro 1, line 1, type:

```
DropOwnership Macro 1
```
---|---  
  
or type:

```
DropOwnership Macro 1.1
```
---|---  
```
DropOwnership Macro 1.*
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
