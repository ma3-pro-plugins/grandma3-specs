---
keyword: "/NoRefresh"
kind: option
shortcuts: ["/Nor"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_norefresh.html"
---

## Official

To enter the **/NoRefresh** option keyword in the command line, use one of the options:

  * Type **/NoRefresh**
  * Type the shortcut**/Nor**

### Description

The /NoRefresh option keyword is used to suppress the refresh of libraries during import or export of objects.

|  **Hint:**  
---|---  
When listing the library files of a certain type and/or path, it may take a while to type the path and the options into the command line. When a file is to be imported after a type and/or path has been specified during a previous command, the type and/or path will typically need to be entered again as part of the import command. Using the **/NoRefresh** option, it is not necessary to reenter [/Type](https://help.malighting.com/grandMA3/2.5/HTML/ok_type.html) and/or [/Path](https://help.malighting.com/grandMA3/2.5/HTML/ok_path.html) as part of the import command.  
  
  
### Syntax

[Function] Object ["Object_Name" or Object_Number] (If Drive [Drive_Number]) (/Option) ("/Option_Value")

### General Keywords

General keywords that use the /NoRefresh option keyword:

  * [Export keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_export.html)
  * [Import keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_import.html)

### Examples

To use the /NoRefresh option to avoid reentering drive and path specifications:

  * List all macro libraries within a specific path on a specific drive:

```
List Library If Drive 2 /Path "/My_grandMA3_files/macro/archive"
```
---|---  
  
  * To import the second library from the list without reentering the drive and path, type:

```
Import Library 2 /NoRefresh
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
