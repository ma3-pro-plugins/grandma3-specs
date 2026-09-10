---
keyword: "Export"
kind: general
shortcuts: ["Exp"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_export.html"
---

## Official

To enter the Export keyword in the command line, use one of the options:

  * Type **Export**
  * Type the shortcut**Exp**

### Description

Export is a function keyword which is used to save objects from the current show file as a smaller file.

If no file name is used in the command, the file name will use the name of the object.

By default, files will be exported to the relevant folder within the library folder structure, either on the local drive of the console or onPC station, or on a selected USB drive. For more information on grandMA3 folders see [Folder Structure](https://help.malighting.com/grandMA3/2.5/HTML/fm_folder_structure.html).

|  **Important:**  
---|---  
When exporting several objects at a time without indicating a file name for each pool object, a separate XML file will be exported.   
When exporting several objects at a time indicating a file name, all pool objects will be exported into a shared XML file.   
  
|  **Hint:**  
---|---  
The Import and Export buttons offer a graphical user interface for import and export functions within the Show Creator Menu. For more information, see [Import/Export](https://help.malighting.com/grandMA3/2.5/HTML/import-export.html).   
  
  
### Syntax

Export [Object] ["Object_Name" or Object_Number] (If Drive [Drive_Number]) (/Option) ("Option_Value")

### Option Keywords

The Export keyword uses the following option keywords:

  * [/Gaps](https://help.malighting.com/grandMA3/2.5/HTML/ok_gaps.html)
  * [/GDTF](https://help.malighting.com/grandMA3/2.5/HTML/ok_gdtf.html)
  * [/HighPrecision](https://help.malighting.com/grandMA3/2.5/HTML/ok_highprecision.html)
  * [/NoDependencies](https://help.malighting.com/grandMA3/2.5/HTML/ok_nodependencies.html)
  * [/Path ](https://help.malighting.com/grandMA3/2.5/HTML/ok_path.html)
  * [/Type](https://help.malighting.com/grandMA3/2.5/HTML/ok_type.html)

### Examples  
  

  * To export macro 1 as the XML file "test", type: 

```
Export Macro 1 "test"
```
---|---  
  
  * To export macro 1 using the macro name, type:

```
Export Macro 1
```
---|---  
  
  * To export several macros to single XML files at a time, type:

```
Export Macro 1 Thru 42
```
---|---  
  
  * To export macro 1 "test" to the first connected USB drive, type:

```
Export Macro 1 "test" If Drive 2
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
