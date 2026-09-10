---
keyword: "#[Object]"
kind: general
shortcuts: []
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_hashsquarebrackets.html"
---

## Official

To enter the #[Object] character in the command line, type **#[Object]**. 

###  Description 

The #[Object] is used instead of object numbers or names in order to address an object. Using #[Object] makes it unnecessary to update macros or commands if the object was moved or the name of the object was changed.

### Syntax

[Function] #[Object "Object_Name"]

[Function] #[Object Object_Number]

###  Examples

  * To set the variable "MyHandle" to the handle of macro 1, type: 

```
SetUserVariable "MyHandle" #[Macro 1]
```
---|---  
  

or:

```
SetUserVariable "MyHandle" At Macro 1
```
---|---  
  

  * To go to the next cue in sequence 23 using the handle of the sequence, type:

```
Go+ #[Sequence 23]
```
---|---  
  
  

  * To delete macro lines 1 to 5 of macro 42 using the handle of macro 42, type:

```
Delete #[Macro 42].1 Thru 5
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
