---
keyword: "/ChannelSet"
kind: option
shortcuts: ["/Ch"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_channelset.html"
---

## Official

To enter the **/ChannelSet** option keyword in the command line, use one of the options: 

  * Type **/ChannelSet**
  * Type the shortcut**/Ch**

###  Description 

The /ChannelSet option keyword is used in conjuction with the AutoCreate keyword – whereby the AutoCreate command creates objects out of channel sets.

###  Syntax

AutoCreate [Source_Object] ["Source_Object_Name" or Source_Object_Number] At [Destination_Object] ["Destination_Object_Name" or Destination_Object_Number] /ChannelSet

General Keywords

General keywords that use the /ChannelSet option keyword: 

  * [AutoCreate keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_autocreate.html)

###  Example   
  

  * To create global beam presets out of channel sets of fixture type 9, type: 

```
AutoCreate FixtureType 9 At Preset * If FeatureGroup "Beam" /ChannelSet
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
