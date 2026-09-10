---
keyword: "/Recursive"
kind: option
shortcuts: ["/Recu"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_recursive.html"
---

## Official

To enter the **/Recursive** option keyword in the command line, use one of the options: 

  * Type **/Recursive**
  * Type the shortcut**/Recu**

###  Description 

The /Recursive option keyword is used to define which levels of objects you can lock or unlock. 

###  Syntax 

[Function][Object]["Object_Name" or Object_Number] /Recursive

###  General Keywords 

General keywords that use the /Recursive option keyword: 

  * [Lock keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_lock.html)
  * [Unlock keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_unlock.html)

###  Examples  
  

  * To lock all levels within data pool 1, type: 

```
Lock Datapool 1 /Recursive
```
---|---  
  
  

**Requirement:** Lock at least two levels of objects.  

  * To unlock sequence 1 with all its cues but to keep cue parts locked, type:

```
Unlock Sequence 1 /Recursive 1
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
