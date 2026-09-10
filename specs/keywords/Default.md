---
keyword: "Default"
kind: general
shortcuts: ["Def"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_default.html"
---

## Official

To enter the Default keyword in the command line, use one of the options: 

  * Press `MA` \+ ` . `
  * Type **Default**
  * Type the shortcut **Def**

###  Description 

The Default keyword is used to reset the attributes of your fixture selection to default values. If there is no attribute list, all attributes of the selected fixtures will be set to their default values. 

###  Syntax 

**Default**

**Fixture ["Fixture_Name" or Fixture_Number] At Default (** FeatureGroup ["FeatureGroup_Name" or FeatureGroup_Number]) 

**Store Default (/Option)**

###  Examples   
  

  * To set the dimmer of fixture 1 to its default values, type: 

```
Fixture 1 At Default
```
---|---  
  
  * To set the position attribute of fixture 2 to default, type: 

```
Fixture 2 At Default FeatureGroup 2
```
---|---  
  

Example: Store Special Values

**Requirement:**

Activate values in the programmer: 

-Call a preset or turn the attribute encoders. 

  * To store the currently active values as default values, type: 

```
Store Default
```
---|---  
  
  * To reset the special values in the currently active values, type: 

```
Store Default /Remove
```
---|---  
  
For more information on the special values see [Parameter List](https://help.malighting.com/grandMA3/2.5/HTML/patch_parameter_list.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
