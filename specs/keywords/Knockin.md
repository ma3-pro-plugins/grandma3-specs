---
keyword: "KnockIn"
kind: general
shortcuts: ["Kn"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_knockin.html"
---

## Official

To enter the KnockIn keyword in the command line, use one of the options:

  * Type **KnockIn**
  * Type the shortcut **Kn**

### Description

KnockIn is used to take values that are located for example in sequences or presets actively into the programmer. 

This is useful to the effect that you can actively take values that have already been stored into the programmer. 

### Syntax

Fixture ["Fixture_Name" or Fixture_Number] KnockIn****["Attribute_Name" or Attribute_Number]/["FeatureGroup_Name" or FeatureGroup_Number]

KnockIn Fixture ["Fixture_Name" or Fixture_Number]

**Attribute ["Attribute_Name" or Attribute_Number] At KnockIn**

### Examples  
  

  * To knock in the attribute Color RGB_R in fixture 1, type:

```
Fixture 1 KnockIn Attribute "ColorRGB_R"
```
---|---  
  
  * To knock in all attributes of fixture 2, type:

```
KnockIn Fixture 2
```
---|---  
  
  * To knock in only the dimmer values of fixtures 11 through 15, type:

```
Fixture 11 Thru 15 At KnockIn
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
