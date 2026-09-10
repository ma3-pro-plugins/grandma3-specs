---
keyword: "SelectFixtures"
kind: general
shortcuts: ["Selectf"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_selectfixtures.html"
---

## Official

To enter the **SelectFixtures** keyword in the command line, use one of the options:

  * Press `SelFix`
  * Type**SelectFixtures**
  * Type the shortcut **Selectf**

### Description

The SelectFixtures keyword is a function keyword that is used to create selections of fixtures in the programmer.

If only fixtures are selected, the SelectFixtures keyword adds additional fixtures to the selection.

If fixtures are selected and activated in the programmer, the SelectFixtures keyword replaces the selection by the SelectFixtures selection.

If the exact same SelectFixtures command is successively used:

  * using it the second time activates all attributes of the selected fixtures in the programmer 
  * using it the third time deactivates all attributes of the selected fixtures in the programmer

SelectFixtures is the default function of most objects, for example, fixture or group or preset.

To clear the selection, press `Clear`.

### Syntax

SelectFixtures**[Object] ["Object_Name" or Object_Number]**

### Examples  
  

  * To select all fixtures or channels stored in a sequence of the executor 101, type:

```
SelectFixtures Executor 101
```
---|---  
  
  * To select all fixtures stored in dimmer preset 1.1, type:

```
SelectFixtures Preset 1.1
```
---|---  
  
For information on the key and its location see [SelFix [SelectFixtures] key](https://help.malighting.com/grandMA3/2.5/HTML/key_selfix.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
