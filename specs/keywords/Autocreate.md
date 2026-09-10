---
keyword: "AutoCreate"
kind: general
shortcuts: ["Ac", "Au"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_autocreate.html"
---

## Official

To enter the AutoCreate keyword in the command line, use one of the options:

  * Type **AutoCreate**
  * Type the shortcut **Ac** or **Au**

### Description

The AutoCreate keyword creates objects depending on predefined source objects. It can, for example, create groups in the fixture types of the patched fixtures. 

|  **Hint:**  
---|---  
If your selection is defined as source list, the active MAtricks settings will be taken into cosideration whenever executing AutoCreate.  
  
  
### Syntax

**AutoCreate [Source_Object] ["Source_Object_Name" or Source_Object_Number] At [Destination_Object] ["Destination_Object_Name" or Destination_Object_Number] (/Option)**

### Option Keywords

The AutoCreate keyword uses the following option keywords:

  * [/All](https://help.malighting.com/grandMA3/2.5/HTML/ok_all.html)
  * [/ChannelSet](https://help.malighting.com/grandMA3/2.5/HTML/ok_channelset.html)
  * [/Merge](https://help.malighting.com/grandMA3/2.5/HTML/ok_merge.html)
  * [/OddEven](https://help.malighting.com/grandMA3/2.5/HTML/ok_oddeven.html)
  * [/Overwrite](https://help.malighting.com/grandMA3/2.5/HTML/ok_overwrite.html)
  * [/Single](https://help.malighting.com/grandMA3/2.5/HTML/ok_single.html)

### Examples  
  

  * To create single fixture groups starting with group pool object 1 using all selected fixtures, type:

```
AutoCreate Selection At Group 1
```
---|---  
  

  * To create single fixture groups for fixtures 1 to 10 starting with group pool object 1, type:

```
AutoCreate Fixture 1 Thru 10 At Group 1
```
---|---  
  

**Requirement:**

  1. Insert at least ten fixture types in the show file and patch at least two fixtures of every fixture type.

  * To create a group in the group pool object 42 containing all fixtures of fixture type 10, type:

```
AutoCreate FixtureType 10 At Group 42
```
---|---  
  

**Requirement:**

  1. Create layers and classes within the patch.
  2. Set fixtures to these layers and classes.

|  **Hint:**  
---|---  
The demo show already uses these settings.  
  
  
  

  * To create a group in the group pool object 301 using all patched fixtures that are set to class "Spots" within the patch, type:

```
AutoCreate FixtureClass "Spots" At Group 301
```
---|---  
  

  * To create single fixture groups starting with group pool object 401 using all fixtures of fixture type 9 that are also set to fixture class "Spots", type:

```
AutoCreate FixtureType 9 + 10 If FixtureClass "Spots"
```
---|---  
  

  * To create universal dimmer presets with a value increment of 25%, with the first preset being the 11th dimmer preset, type:

```
AutoCreate Preset "Dimmer" At Preset 1.11 "DimmerIncrement" 25
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
