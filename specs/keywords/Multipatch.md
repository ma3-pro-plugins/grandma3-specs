---
keyword: "Multipatch"
kind: general
shortcuts: ["Mu"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_multipatch.html"
---

## Official

To enter the Multipatch keyword in the command line, use one of the options:

  * Press `Channel` until Multipatch appears in the command line
  * Type **F + 10**
  * Type **Multipatch**
  * Type the shortcut**Mu**

|  **Hint:**  
---|---  
To use the Multipatch keyword, make sure you create a Multipatch in an existing fixture first.  
  
  
### Description

The Multipatch keyword is a keyword which is used to address the multipatch fixtures of a fixture.

### Syntax

Multipatch****[Absolute_Multipatch_ID] 

Fixture ["Fixture_Name" or Fixture_Number] Multipatch [Multipatch_ID] 

### Examples  
  

  * To select the second multipatch fixture of fixture 4, type:

```
Fixture 4 Multipatch 2
```
---|---  
  
  * To patch the third multipatch fixture of fixture 2 to DMX address 6 in DMX universe 42, type:

```
Patch Fixture 2 Multipatch 3 42.6
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
