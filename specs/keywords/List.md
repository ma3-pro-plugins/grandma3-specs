---
keyword: "List"
kind: general
shortcuts: ["Li"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_list.html"
---

## Official

To enter the List keyword in the command line, use one of these options:

  * Press `List`
  * Type **List**
  * Type the shortcut **Li**

### Description

The List keyword displays show data, including objects and their properties, in the command line history.

It is possible to list any object or any property of:

  * Cues of the selected executor
  * Groups
  * Presets

If the List command does not specify any type of object, the data of the current command line destination is displayed.

The List command can also display the contents of library folders on the console, onPC station, or connected USB drives.

|  **Hint:**  
---|---  
The /Path option instructs the software to access folders other than the defaults. For more information on the default folder structure, see the [Folder Structure](https://help.malighting.com/grandMA3/2.5/HTML/fm_folder_structure.html) topic.   
  
  
The List keyword is a function keyword.

### Syntax

**List**[Object] ["Object_Name" or Object_Number]

List [Object] Library (If Drive [Drive_Number]) (/Path [FolderPath]) (/Type [FileType])

|  **Important:**  
---|---  
When specifying a type, the word "System" or "User" must be capitalized. For more information see the option keyword [/Type](https://help.malighting.com/grandMA3/2.5/HTML/ok_type.html).   
  
  
### Examples  
  

  * To list the first ten fixtures of the Fixture Edit Setup, type:

```
List Fixture Thru 10
```
---|---  
  
  * To list all existing attributes in the show file, type:

```
List Attribute
```
---|---  
  
  * To list the first 5 groups of the group pool, type:

```
List Group Thru 5
```
---|---  
  
  * To list the macros available to import from the default macro library folder on the first connected USB drive, type:

```
List Macro Library If Drive 2
```
---|---  
  
* * *

### Example - List Properties of a Parent and Their Children's Properties

|  **Important:**  
---|---  
In case the children of an object should have various properties, they will be listed using names and numbers when executing List within the parent object.  
To display the properties of a child directly, you have to specifically list the child.  
However, the steps described here can also be used in other constellations consisting of a parent and their children.   
  
  
In the following example we use StationSettings as the parent and DeskLightsCollect as one of their children. 

  1. Change the destination of the command line first:

```
ChangeDestination StationSettings
```
---|---  
  
Result: 

|  User name@StationSettings>  
---|---  
  
  2. To list the properties of the station settings, type:

|  User name@StationSettings> List  
---|---  
  
  

The children are now displayed in the command line history:

The children of the Station Settings are listed

  3. To list the properties of one child, for example DeskLightsCollect, type: 

|  User name@StationSettings> List DeskLightsCollect  
---|---  
  
  

The properties of the child DeskLightsCollect are now displayed in the command line history:

The properties of DeskLightsCollect are listed

  4. To access the folder DeskLightsCollect within Station Settings, type:

|  User name@StationSettings> ChangeDestination DeskLightsCollect  
---|---  
  
  

Result:

|  User name@StationSettings/DeskLightsCollect>  
---|---  
  
  5. To list the properties of the children of DeskLightsCollect, type:

|  User name@StationSettings/DeskLightsCollect> List  
---|---  
  
The children's properties are now displayed. 

Properties of DeskLightsCollect listed in the command line history

For information on the key and its loction see [List key](https://help.malighting.com/grandMA3/2.5/HTML/key_list.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
