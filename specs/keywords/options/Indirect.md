---
keyword: "/Indirect"
kind: option
shortcuts: ["/Ind"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_indirect.html"
---

## Official

To enter the **/Indirect** option keyword in the command line, use one of the options:

  * Type **/Indirect**
  * Type the shortcut**/Ind**

### Description

|  **Hint:**  
---|---  
The /Indirect Option keyword can be used with all object types to which you can assign other objects.   
  
  
The /Indirect option keyword is used to directly edit an assigned object. Executing a command containing this option keyword opens the editor for the object to be modified. 

### Syntax

Edit [Object] ["Object_Name" or Object_Number] Property ["Property_Name"] /Indirect

### General Keywords

General keywords that use the /Indirect option keyword:

  * [Edit keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_edit.html)
  * [Property keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_property.html)

### Examples  
  

  * To open the appearance editor and edit the appearance that is assigned to group 8, type:

```
Edit Group 8 Property "Appearance" /Indirect
```
---|---  
  
  * To edit the object that is triggered by the first agenda entry, type:

```
Edit Agenda 1 Property "Object" /Indirect
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
