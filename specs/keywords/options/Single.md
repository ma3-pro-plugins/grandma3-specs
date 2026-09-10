---
keyword: "/Single"
kind: option
shortcuts: ["/Si"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_single.html"
---

## Official

To enter the **/Single** option keyword in the command line, use one of the options:

  * Type **/Single**
  * Type the shortcut**/Si**

### Description

The /Single option keyword is used when extracting presets or when autocreating single fixture groups. 

When extracting embedded presets or phaser presets where presets are integrated in the steps, Extract will call directly the values of the source presets.

Using the **/Single** option keyword together with the Extract keyword makes it possible to extract one level down in the hierarchy of presets.

|  **Important:**  
---|---  
The combination of the Extract keyword together with the /Single option keyword currently works with presets that are active in the programmer.   
  
  
### Syntax

**[Function] [Object] ["Object_Name" or Object_Number] /Single**

### General Keywords

General keywords that use the /Single option keyword:

  * [AutoCreate keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_autocreate.html)
  * [Extract keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_extract.html)
  * [FixtureClass keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_fixture_class.html)
  * [FixtureLayer keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_fixture_layer.html)
  * [FixtureType keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_fixturetype.html)

### Examples

#### Extract Example

**Requirement:**

  1. Create 2 color presets.
  2. Embed these color presets into a different color preset:  
Embed the second color preset into the All preset 21.1.
  3. Select fixtures and apply the All preset on them.

  * To call the embedded color preset into the programmer, type once:

```
Extract Selection /Single
```
---|---  
  
  

  * To activate hard values, type a second time:

```
Extract Selection /Single
```
---|---  
  
or:

```
Extract Selection
```
---|---  
  
#### AutoCreate and FixtureType Example

**Requirement:** Insert at least ten fixture types in the show file and patch at least two fixtures of every fixture type.

  * To create single fixture groups starting with group pool object 42 that contain all patched fixtures of the fixture type 9, type:

```
AutoCreate FixtureType 9 At Group 42 /Single
```
---|---  
  
  * To create single fixture groups that contain all patched fixtures of fixture types 9 and 10 starting with group pool object 101, type:

```
AutoCreate FixtureType 9 + 10 At Group 101 /Single
```
---|---  
  
  

#### AutoCreate FixtureLayer and FixtureClass Example

**Requirement:**

  1. Create layers and classes within the patch.
  2. Set fixtures to these layers and classes.

  * To create single fixture groups starting with group pool object 201 using all patched fixtures that are set to the layer "Backtruss" within the patch, type:

```
AutoCreate FixtureLayer "Backtruss" At Group 201 /Single
```
---|---  
  
  * To create single fixture groups starting at pool object 301 with all fixtures that are set to class "Spots" within the patch, type:

```
AutoCreate FixtureClass "Spots" At Group 301/Single
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
