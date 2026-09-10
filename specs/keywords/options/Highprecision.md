---
keyword: "/HighPrecision"
kind: option
shortcuts: ["/H"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_highprecision.html"
---

## Official

To enter the **/HighPrecision** option keyword in the command line, use one of the options: 

  * Type **/HighPrecision**
  * Type the shortcut**/H**

###  Description 

The /HighPrecision option keyword is used to increase the precision of metrics in fixture types during their export.

Beam exported **without using** /HighPrecision:

<Beam Name="H1_ColorPixel1" Model="CenterPixel" PosZ="-0.0730"[...]

Same beam exported **using /HighPrecision** :

<Beam Name="H1_ColorPixel1" Model="CenterPixel" PosZ="-0.072999998927116"[...]  

###  Syntax 

Export ["FixtureType_Name" or FixtureType_Number] /HighPrecision

###  General Keywords 

General keywords that use the /HighPrecision option keyword: 

  * [Export keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_export.html)

###  Example  
  

  * To export fixture type 3 with a higher precision, type: 

```
Export FixtureType 3 /HighPrecision
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
