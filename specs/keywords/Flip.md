---
keyword: "Flip"
kind: general
shortcuts: ["Fli"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_flip.html"
---

## Official

To enter the Flip keyword in the command line, use one of the options:

  * Type **Flip**
  * Type the shortcut **Fli**

### Description

The Flip keyword is used to access the different pan/tilt combinations that direct a moving head in the same direction. 

Flip adds 180 degrees to the pan value of the fixtures and inverts the tilt angle. If the fixtures reach their physical breakpoint, the pan and tilt values will be set to the smallest possible value.  
That is, Flip directs the fixture in the same direction using a different pan/tilt combinations. 

|  **Hint:**  
---|---  
-If no selection list is entered, Flip is applied to the fixture selection.  
-If no number is entered, the function toggles through the different possible combinations.  
-The number of combinations depends on the possible degree value the fixture can pan in.   
  
  
### Syntax

Flip ([Flip_Number] [Object] ["Object_Name" or Object_Number])

### Examples  
  

  * To set the pan and tilt of the fixture selection to the next pan/tilt combination, type:

```
Flip
```
---|---  
  
  * To set the pan and tilt of group 7 to the second pan/tilt combination that directs the fixtures in the same direction, type:

```
Flip 2 Group 7
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
