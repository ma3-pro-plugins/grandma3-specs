---
keyword: "AutoStore"
kind: general
shortcuts: ["Autos"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_autostore.html"
---

## Official

To enter the AutoStore keyword in the command line, use one of the options: 

  * Type **AutoStore**
  * Type the shortcut **Autos**

###  Description 

The AutoStore keyword is used to directly store presets in a fixture type. This can be useful, for example, when you have to use a fixture type in a different show file, and want to save time by creating your own standard set of presets. 

Syntax

AutoStore FixtureType ["FixtureType_Name" or FixtureType_Number]

AutoStore Fixture ["Fixture_Name" or Fixture_Number]

AutoStore Preset ["FeatureGroup_Name" or FeatureGroup_Number].["Preset_Name" or Preset_Number] At FixtureType ["FixtureType_Name" or FixtureType_Number]

###  Option Keywords 

The AutoStore keyword uses the following option keywords: 

  * [/Merge](https://help.malighting.com/grandMA3/2.5/HTML/ok_merge.html)
  * [/NoConfirmation](https://help.malighting.com/grandMA3/2.5/HTML/ok_noconfirmation.html)
  * [/Overwrite](https://help.malighting.com/grandMA3/2.5/HTML/ok_overwrite.html)

###  Examples   
  

  * To store your presets into the fixture type Mac Aura XB, type:

```
AutoStore FixtureType "Mac Aura XB"
```
---|---  
  
  

  * To store all possible presets to fixture type 9, type: 

```
AutoStore Preset *.* At FixtureType 9
```
---|---  
  
  

  * To store possible color presets to the fixture type of fixture 1, merging existing fixture type presets, type

```
AutoStore Preset 4.1 Thru At Fixture 1 /Merge /NoConfirmation
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
