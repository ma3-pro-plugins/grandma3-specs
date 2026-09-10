---
keyword: "Physical"
kind: general
shortcuts: ["Phy"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_physical.html"
---

## Official

To enter the Physical keyword in the command line, use one of the options:

  * Type **Physical**
  * Type the shortcut **Phy**

### Description

The Physical keyword is used to set the physical values of a fixture selection using the Physical notation. It comprises RPM (rounds per minute), Hz (Hertz), degrees, or intensity.

### Syntax

**(Attribute ["Attribute_Name" or Attribute_Number]) At ([Layer]) Physical [Value]**

### Examples  
  

  * To set the dimmer value to 1.0 in the absolute layer using Physical, type:

```
At Absolute Physical 1.0
```
---|---  
  
  * To set the pan value in the absolute layer to 75.60 degrees using Physical, type:

```
Attribute "Pan" At Absolute Physical 75.60
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
