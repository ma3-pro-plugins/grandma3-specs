---
keyword: "Copy"
kind: general
shortcuts: ["Co"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_copy.html"
---

## Official

To enter the Copy keyword in the command line, use one of these options:

  * Press `Copy`
  * Type **Copy**
  * Type the shortcut **Co**

### Description

The Copy keyword**** is a function keyword which is used to create copies of an object.

If no object type is given and the command line destination is root (no destination), the default object type **–** **Cue –** is used for this function.

### Syntax

Copy [Object] ["Source_Name" or Source_Number] At ["Destination_Name" or Destination_Number] (/Option)

**Copy [Object] ["Source_Name" or Source_Number] (/Option)**

### Option Keywords

The Copy keyword uses the following option keywords:

  * [/CopyCueDestination](https://help.malighting.com/grandMA3/2.5/HTML/ok_copycuedestination.html)
  * [/CopyCueSource](https://help.malighting.com/grandMA3/2.5/HTML/ok_copycuesource.html)
  * [/Default](https://help.malighting.com/grandMA3/2.5/HTML/ok_default.html)
  * [/Look](https://help.malighting.com/grandMA3/2.5/HTML/ok_look.html)
  * [/Merge](https://help.malighting.com/grandMA3/2.5/HTML/ok_mergehightpriority.html)
  * [/NoConfirmation](https://help.malighting.com/grandMA3/2.5/HTML/ok_noconfirmation.html)
  * [/Overwrite ](https://help.malighting.com/grandMA3/2.5/HTML/ok_overwrite.html)
  * [/Release](https://help.malighting.com/grandMA3/2.5/HTML/ok_release.html)

### Examples  
  

  * To copy group 1 to group 5, type:

```
Copy Group 1 At 5
```
---|---  
  

  * To copy group 1 to group 11; group 2 to group 12; and group 3 to group 13, type:

```
Copy Group 1 Thru 3 At 11
```
---|---  
  

  * To copy group 2 to group 6, 7, and 8, type:

```
Copy Group 2 At 6 Thru 8
```
---|---  
  

  * To copy cue 2 to cue 6 of the selected sequence, type:

```
Copy Cue 2 At 6
```
---|---  
  

  * To copy macro 2 to macro 6, type:

```
Copy Macro 2 At 6
```
---|---  
  

For information on the key and its location see [Copy key](https://help.malighting.com/grandMA3/2.5/HTML/key_copy.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
