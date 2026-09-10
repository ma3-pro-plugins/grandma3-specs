---
keyword: "Index"
kind: general
shortcuts: ["Ind"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_index.html"
---

## Official

To enter the Index keyword in the command line, use one of the options:

  * Type **Index**
  * Type the shortcut **Ind**

### Description

Index keyword is a command keyword that addresses values where a property can have more than one value. For example, a fixture with at least two DMX breaks. The patch property has 2 values for this fixture.

|  **Hint:**  
---|---  
The values of the Index keyword are zero nominated.  
  
### Syntax

Set [Object] ["Object_Name" or Object_Number] ["Property"] Index [Index_Number] ["Value"]

### Examples

**Requirement:**

  * Fixture 1 has to have at least two DMX breaks.  
For example, the fixture type LED Wall 20x20

  * To set the patch address of the second break to universe 2 address 1 without affecting the first address, type:

```
Set Fixture 1 "Patch" Index 1 "2.1"
```
---|---  
  
  * To disable the dimmer attribute in filter 6, type:

```
Set Filter 6 Property "Attributes" Index 0 "0"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
