---
keyword: "/Path"
kind: option
shortcuts: ["/Pa"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_path.html"
---

## Official

To enter the **/Path** option keyword in the command line, use one of the options:

  * Type **/Path**
  * Type the shortcut**/Pa**

### Description

The /Path option keyword defines the folder path where an imported or exported file is saved. 

|  **Hint:**  
---|---  
-Enter a path beginning with a letter or number if the path is incorporated with the default folder structure.-Enter a path beginning with the forward-slash (/) character if the path begins at the root of the device.-Entering a path that does not already exist creates the necessary folders.  
  
### Syntax

[Function] [Object] ["Object_Name" or Object_Number] (If Drive [Drive_Number]) /Path "The/Path/To/My/Files"

### General Keywords

General keywords that use the /Path option keyword:

  * [Export keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_export.html)
  * [Import keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_import.html)
  * [LoadShow keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_loadshow.html)
  * [SaveShow keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_saveshow.html)

### Examples  
  

  * To export macro 1, with the name "test," to a folder labeled "myfavorites" at the root of the first connected USB drive, type:

```
Export Macro 1 "test" If Drive 2 /Path "/myfavorites"
```
---|---  
  
  * To load the show file with the name "Fabulous" which was placed in the subfolder structure "/test" on the USB drive, type:

```
LoadShow "Fabulous" If Drive 2 /Path "/test"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
