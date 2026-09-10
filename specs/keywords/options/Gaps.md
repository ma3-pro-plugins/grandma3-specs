---
keyword: "/Gaps"
kind: option
shortcuts: ["/Ga"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_gaps.html"
---

## Official

To enter the **/Gaps** option keyword in the command line, use one of the options:

  * Type **/Gaps**
  * Type the shortcut**/Ga**

### Description

The /Gaps option keyword retains or suppresses empty spaces when importing or exporting a range of pool objects.

|  **Hint:**  
---|---  
**/Gaps** or **/Gaps "Yes"** retains empty spaces when importing or exporting a range of pool objects.**/Gaps "No"** suppresses empty spaces when importing or exporting a range of pool objects.  
  
### Syntax

[Function] [Object] ["Object_Name" or Object_Number] /Gaps ("Yes" or "No")

### General Keywords

General keywords that use the /Gaps option keyword:

  * [Import keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_import.html)
  * [Export keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_export.html)

### Example  
  

  * To import all macros from the library "mymacros.xml," starting with macro 11, while suppressing any empty spaces included in the library, type:

```
Import Macro Library "mymacros.xml" At Macro 11 /Gaps "No"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
