---
keyword: "Import"
kind: general
shortcuts: ["Im"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_import.html"
---

## Official

To enter the Import keyword in the command line, use one of the options:

  * Type **Import**
  * Type the shortcut **Im**

### Description

Import is a function keyword that incorporates small portions of exported show file data, available as XML files, into the current show file.

The Import command loads data into the specified destination occupying the first free pool object when no certain pool object is given. 

By default, files will be imported from the relevant folder within the library folder structure, either on the local drive of the console or onPC station, or on a selected USB flash drive. For more information on this folder structure see [Folder Structure](https://help.malighting.com/grandMA3/2.5/HTML/fm_folder_structure.html).

### Syntax

Import [Object] Library "File Name.xml" (If Drive [Drive_Number]) (At ["Object_Name" or Object_Number]) (/Option) ("Option_Value")

### Option Keywords

The Import keyword uses the following option keywords:

  * [/Path](https://help.malighting.com/grandMA3/2.5/HTML/ok_path.html)
  * [/Gaps](https://help.malighting.com/grandMA3/2.5/HTML/ok_gaps.html)
  * [/NoDependencies](https://help.malighting.com/grandMA3/2.5/HTML/ok_nodependencies.html)
  * [/NoRefresh](https://help.malighting.com/grandMA3/2.5/HTML/ok_norefresh.html)
  * [/Type](https://help.malighting.com/grandMA3/2.5/HTML/ok_type.html)

### Examples

**Requirements:** Destination is changed to fixture types.

  * To import a MAC Aura XB as a new fixture type in the show file, type:

|  User name@ShowData/Patch/FixtureTypes> Import Library "MAC Aura XB"  
---|---  
  
**Requirements:** Destination is changed to macros.

  * To import the macro color.xml to the first free pool object, type:

|  User name@ShowData/DataPools/Default/Macros> Import Library "color.xml"  
---|---  
  
  * To import the same macro to macro 42 in the macro pool without changing the command line destination, type:

```
Import Macro Library "color.xml" At Macro 42
```
---|---  
  
**Requirements:** Destination is changed to macros.

  * To import all macros from the library into the show file, type:

|  User name@ShowData/DataPools/Default/Macros> Import Library "*.xml"  
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
