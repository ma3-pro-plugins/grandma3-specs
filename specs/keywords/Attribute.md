---
keyword: "Attribute"
kind: general
shortcuts: ["Att"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_attribute.html"
---

## Official

To enter the Attribute keyword in the command line, use one of the options:

  * Press `Preset` `Preset`
  * Type **Attribute**
  * Type the shortcut **Att**

### Description

The Attribute keyword is an object keyword which is used to set attributes of a fixture.

The default function of attributes is Call. If you call an attribute, you can use the encoders to modify the values. Calling attributes also selects the attributes in the fixture sheet.

|  **Important:**  
---|---  
The number of an attribute may vary if new fixtures and attributes are added to the show file. We recommend you use the unique library name of attributes.   
  
|  **Hint:**  
---|---  
  
  * Attributes are organized by subattributes;
  * Subattributes are organized by features;
  * Features are organized by feature groups.

  
  
### Syntax

[Function] Attribute ["Attribute_Name" or Attribute_Number]

### Examples  
  

  * To view the list of attributes along with their corresponding names and numbers in the command line history, type:

```
List Attribute
```
---|---  
  

  * To set the attribute "Pan" to 120 degrees in the selected fixtures, type:

```
Attribute "Pan" At 120
```
---|---  
  

  * To knock out the first attribute, which is Dimmer, in the current selection, type:

```
Off Attribute 1
```
---|---  
  

**Requirement:** Load the demo show and select fixture 1.

  * To set the random strobe (channel function 4) of the selected fixture to a value of 4 Hz, type:

```
Attribute "Shutter1StrobeRandom" At 4
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
