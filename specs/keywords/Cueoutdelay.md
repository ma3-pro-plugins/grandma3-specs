---
keyword: "CueOutDelay"
kind: general
shortcuts: ["Cueoutd"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_cueoutdelay.html"
---

## Official

To enter the CueOutDelay keyword in the command line, use one of the options:

  * Type **CueOutDelay**
  * Type the shortcut **Cueoutd**

### Description

CueOutDelay sets the outdelay time of a cue. 

|  **Hint:**  
---|---  
CueOutDelay is only used by dimmer parameters that go to a lower value in the cue.  
  
  
### Syntax

(Cue ["Cue_Name" or Cue_Number]) CueOutDelay [CueOutDelay_Time]

### Examples  
  

  * To enter an outdelay of 5 seconds in the current cue of the selected sequence, type:

```
CueOutDelay 5
```
---|---  
  

  * To enter an outdelay of 5 seconds in cues 1 to 4 of the selected sequence, type:

```
Cue 1 Thru 4 CueOutDelay 5
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
