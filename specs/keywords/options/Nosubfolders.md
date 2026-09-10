---
keyword: "/NoSubfolders"
kind: option
shortcuts: ["/Nos"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_nosubfolders.html"
---

## Official

To enter the **/NoSubfolders** option keyword in the command line, use one of the options:

  * Type **/NoSubfolders**
  * Type the shortcut**/Nos**

### Description

The /NoSubfolders option keyword is used to exclude subfolders when importing library files or listing libraries. 

|  **Hint:**  
---|---  
Subfolders are created by the users.   
  
  
### Syntax

[Function] [Object] ["Object_Name" or Object_Number] /NoSubfolders

### General Keywords

General keywords that use the /NoSubfolders option keyword:

  * [List keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_list.html)
  * [Import keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_import.html)

### Examples  
  

  * To only show color themes in the main folders when listing, type:

```
List ColorTheme /NoSubfolders
```
---|---  
  
It might as well happen that there are two files with the same name located in the main folder and a subfolder. 

  * To import the macro library file "bestmacro.xml" located in the main folder, type:

```
Import Macro Library "bestmacro.xml" At Macro 5 If Drive 2 /NoSubfolders
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
