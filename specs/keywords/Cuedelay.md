---
keyword: "CueDelay"
kind: general
shortcuts: ["Cued"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_cuedelay.html"
---

## Official

To enter the CueDelay keyword in the command line, use one of the options:

  * Press `Time` `Time` (If the Time Key Target is set to Cue. For more information see [User Settings](https://help.malighting.com/grandMA3/2.5/HTML/users_and_profiles_configuration.html) and [Time Key](https://help.malighting.com/grandMA3/2.5/HTML/key_time.html).)
  * Type **CueDelay**
  * Type the shortcut **Cued**

### Description

CueDelay can set both the indelay and the outdelay time of a cue. To do so, use a /. See examples further down.

For more information on how to set the delay times in objects see the [Delay Keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_delay.html).

### Syntax

(Cue ["Cue_Name" or Cue_Number]) CueDelay [CueDelay_Time]

(Cue ["Cue_Name" or Cue_Number])**** CueDelay [CueInDelay_Time]/[CueOutDelay_Time]

### Examples  
  

  * To enter a delay of 5 seconds in the current cue of the selected sequence, type:

```
CueDelay 5
```
---|---  
  

  * To set an indelay of 6 seconds and an outdelay of 12 seconds in the current cue of the selected sequence, type:

```
CueDelay 6/12
```
---|---  
  

  * To adjust the CueInDelay to 3 seconds, but leave the CueOutDelay as it was, type:

```
CueDelay 3/
```
---|---  
  

  * To enter a delay of 5 seconds in cues 1 to 4 of the selected sequence, type:

```
Cue 1 Thru 4 CueDelay 5
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
