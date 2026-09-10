---
keyword: "CleanUp"
kind: general
shortcuts: ["Clean"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_cleanup.html"
---

## Official

To enter the CleanUp keyword in the command line, use one of the options:

  * Type **CleanUp**
  * Or type the shortcut**Clean**

### Description

The CleanUp keyword is a command keyword that is used to delete objects that are not used and do not contain references in the show file. For example, you can clean up sequences that are not assigned to an executor.

### Syntax

CleanUp [Object] ["Object_Name" or Object_Number] (/Option)

### Option Keywords

The CleanUp keyword uses the following option keywords:

  * [/Recipe](https://help.malighting.com/grandMA3/2.5/HTML/ok_recipe.html)
  * [/Selective](https://help.malighting.com/grandMA3/2.5/HTML/ok_selective.html)
  * [/Type](https://help.malighting.com/grandMA3/2.5/HTML/ok_type.html)

### Examples  
  

  * To delete all unassigned sequences, type:

```
CleanUp Sequence Thru
```
---|---  
  

  * To delete all unused color presets in preset pool 4, type:

```
CleanUp Preset 4.*
```
---|---  
  

  * To delete all images without reference, type:

```
CleanUp Image 3.1 Thru
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
