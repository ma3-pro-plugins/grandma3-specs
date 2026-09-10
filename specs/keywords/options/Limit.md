---
keyword: "/Limit"
kind: option
shortcuts: ["/Li"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_limit.html"
---

## Official

To enter the **/Limit** option keyword in the command line, use one of the options: 

  * Type **/Limit**
  * Type the shortcut**/Li**

###  Description 

The /Limit option keyword defines how many entries will be displayed in the command line history. 

|  **Hint:**  
---|---  
You can use**/Limit** together with the [/Sort option keyword](https://help.malighting.com/grandMA3/2.5/HTML/ok_sort.html).   
  
Syntax

MemoryInfo /Limit [Limit_Number] 

###  General Keywords 

General keywords that use the /Limit option keyword:

  * [DumpLog keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_dumplog.html)

  * [MemoryInfo keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_memoryinfo.html)   

###  Examples  
  

  * To limit the number of entries to 3 in the MemoryInfo, type: 

```
MemoryInfo /Limit 3
```
---|---  
  
  

  * To store the last 10 lines of the log file, shown in the system monitor, onto a connected USB drive, type:

```
DumpLog /Limit 10
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
