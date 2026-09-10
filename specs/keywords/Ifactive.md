---
keyword: "IfActive"
kind: general
shortcuts: ["Ifa"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_ifactive.html"
---

## Official

To enter the IfActive keyword in the command line, use one of the options:

  * Press `If` `If`
  * Type **IfActive**
  * Type the shortcut **Ifa**

### Description

IfActive is a function keyword that selects fixtures with active values in the programmer.

|  **Important:**  
---|---  
Executed on its own, the IfActive keyword only selects fixtures of the current command line default.  
  
|  **Important:**  
---|---  
IfActive only works with dimmer values.  
  
  
If no filter is entered, IfActive will select all fixtures with active values.

If a filter is entered, IfActive will select all fixtures which have this filter and also fixtures that have active values in the programmer.

### Syntax

IfActive ([Object] ["Object_Name" or Object_Number])

### Examples  
  

  * To select all fixtures with active values in the programmer, type:

```
IfActive
```
---|---  
  
  * To select fixtures within group 5 which also have active values in the programmer, type: 

```
IfActive Group 5
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
