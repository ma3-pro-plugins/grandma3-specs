---
keyword: "CueFade"
kind: general
shortcuts: []
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_cuefade.html"
---

## Official

To enter the CueFade keyword in the command line, use one of the options:

  * Press `Time` (If the Time Key Target is set to Cue. For more information see [User Settings](https://help.malighting.com/grandMA3/2.5/HTML/users_and_profiles_configuration.html) and [Time Key](https://help.malighting.com/grandMA3/2.5/HTML/key_time.html).)
  * Type **CueFade**
  * Type **Cuef**

### Description

CueFade can set both the infade and the outfade time of a cue. To do so, use a /. See examples further down. 

As a helping keyword for programming functions (for example Store), this keyword sets the fade time of a cue or a cue part.

### Syntax

(Cue ["Cue_Name" or Cue_Number]) CueFade [CueFade_Time]

(Cue ["Cue_Name" or Cue_Number]) CueFade [CueInFade_Time]/[CueOutFade_Time]

### Examples  
  

  * To enter a fade of 5 seconds in a cue, type:

```
CueFade 5
```
---|---  
  

  * To set an infade of 6 seconds and an outfade of 12 seconds in the current cue of the selected sequence, type:

```
CueFade 6/12
```
---|---  
  

  * To adjust the CueInFade to 3 seconds, but leave the CueOutFade as it was, type:

```
CueFade 3/
```
---|---  
  

  * To enter a fade of 5 seconds in cues 1 to 4, type:

```
Cue 1 Thru 4 CueFade 5
```
---|---  
  

  * To enter a fade time of 1 hour 22 minutes 56.3 seconds in cue 1 of the selected sequence, type:

```
Cue 1 CueFade 1h22m56.3
```
---|---  
  

Or press:

`Time` `1` `.` `.` `.` `2` `2` `.` `.` `5` `6` `.` `3`

  * To double the CueFade time, type:

```
CueFade * 2
```
---|---  
  

  * To subtract 3 seconds from the CueFade time, type:

```
CueFade - 3
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
