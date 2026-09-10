---
keyword: "SoftwareUpdate"
kind: general
shortcuts: ["Softwareu"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_softwareupdate.html"
---

## Official

To enter the SoftwareUpdate keyword in the command line, use one of the options:

  * Type **SoftwareUpdate**
  * Type the shortcut **Softwareu**

### Description

The SoftwareUpdate keyword is a function keyword which is used to update the software of every MA device or program in the network.

For more information on how to update the software and requirements see [Update grandMA3 Consoles](https://help.malighting.com/grandMA3/2.5/HTML/update_consoles.html).

### Syntax

SoftwareUpdate [StationType] [ID/"Name"] "release_type_x.y.z.a.xml;/Path/to/MALightingTechnology/installation_packages"

### Example

**Requirement:**

  1. The grandMA3 onPC runs on Windows®
  2. Copy the files of the ma folder of the grandMA3_stick_v1.6.3.7.zip file to C:\ProgramData\MALightingTechnology\installation_packages

  * To update the first console within your network to grandMA3 v1.6.3.7, type:

```
SoftwareUpdate Console 1 "release_stick_1.6.3.7.xml;C:/ProgramData/MAlightingTechnology/installation_packages"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
