---
keyword: "ListOwnership"
kind: general
shortcuts: ["Listo"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_listownership.html"
---

## Official

To enter the ListOwnership keyword in the command line, use one of the options:

  * Type **ListOwnership**
  * Type the shortcut **Listo**

### Description

ListOwnership is used as a troubleshooting keyword in case of a multi-user access conflict.

If a multi-user access conflict occurs, use the ListOwnership keyword. It lists the objects that are currently locked for all users in the session, hence causing the conflict. 

### Syntax

ListOwnership ([Object] ["Object_Name" or Object_Number])

### Examples  
  

  * To display all objects that are locked for all users and that might cause a multi-user conflict, type:

```
ListOwnership
```
---|---  
  
  * To display the ownership in macro 1 line 1, type:

```
ListOwnership Macro 1
```
---|---  
  
or type:

```
ListOwnership Macro 1.1
```
---|---  
  
or:

```
ListOwnership Macro 1.*
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
