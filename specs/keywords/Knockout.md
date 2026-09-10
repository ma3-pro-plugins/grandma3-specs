---
keyword: "KnockOut"
kind: general
shortcuts: ["Knocko"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_knockout.html"
---

## Official

To enter the Off keyword in the command line, use one of the options:

  * Type **KnockOut**
  * Type the shortcut **Knocko**

|  **Hint:**  
---|---  
The KnockOut keyword is used as a synonym of the Off keyword.  
  
  
### Description

The KnockOut keyword is used as a function and value keyword to:

  * Knock out selections in the programmer
  * Knock out active attributes in the programmer

### Syntax

Fixture ["Fixture_Name" or Fixture_Number] KnockOut ["Attribute_Name" or Attribute_Number]/["FeatureGroup_Name" or FeatureGroup_Number]

KnockOut Fixture ["Fixture_Name" or Fixture_Number]

Attribute ["Attribute_Name" or Attribute_Number] At KnockOut

### Examples  
  

  * To knock out the parameters of fixture 2 and 4 in the programmer, type:

```
KnockOut Fixture 2 + 4
```
---|---  
  
  * To knock out the attribute Color RGB_R in the selected fixtures, type:

```
Attribute "ColorRGB_R" At KnockOut
```
---|---  
  
  * To knock out the dimmer attribute in fixture 5, type:

```
Fixture 5 At KnockOut
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
