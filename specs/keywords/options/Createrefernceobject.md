---
keyword: "/CreateReferenceObject"
kind: option
shortcuts: ["/Creater"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_createrefernceobject.html"
---

## Official

To enter the **/CreateReferenceObject** option keyword in the command line, use one of the options:

  * Type **/CreateReferenceObject**
  * Type the shortcut**/Creater**

### Description

The /CreateReferenceObject option keyword creates a referenced object when an object is imported. For example, an appearance which uses the imported image. 

For more information on importing references see [Import/Export Menu](https://help.malighting.com/grandMA3/2.5/HTML/import-export.html). 

### Syntax

Import [Object Type] Library "File Name.file_type" At [Object Type] ([Object_Number] [Object_ID]) /CreateReferenceObject

### General Keywords

General keywords that use the /CreateReferenceObject option keyword:

  * [Import keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_import.html)
  * [Image keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_image.html)

### Example  
  

  * To import an image and automatically create an appearance which references to the imported image, type:

```
Import Image Library "Cloud.png" At Image 3.11 /CreateReferenceObject
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
