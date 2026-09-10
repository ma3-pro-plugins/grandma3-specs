---
keyword: "/Sort"
kind: option
shortcuts: ["/So"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_sort.html"
---

## Official

To enter the **/Sort** option keyword in the command line, use one of the options: 

  * Type **/Sort**
  * Type the shortcut**/So**

###  Description 

The /Sort option keyword defines how to sort results in the command line history.

|  **Hint:**  
---|---  
You can use**/Sort** together with the [/Limit option keyword](https://help.malighting.com/grandMA3/2.5/HTML/ok_limit.html).   
  
Use the following sort names to define the order you are using /Sort with:  
Sort Name  
|  Description  
---|---  
Asc| Sorts results in an ascending order.  
  
Desc  
| Sorts results in an descending order.   
  
None  
| Sorts results in the order of destination.  
  
### Syntax 

MemoryInfo /Sort ["Sort_Name"] 

###  General Keywords 

General keywords that use the /Sort option keyword: 

  * [MemoryInfo keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_memoryinfo.html)   

###  Example   
  

  * To display the 5 objects that are occupying the most of memory, type: 

```
MemoryInfo /Sort "Desc" /Limit 5
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
