---
keyword: "Fade"
kind: general
shortcuts: []
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_fade.html"
---

## Official

To enter the **Fade** keyword in the command line, use one of the options:

  * Press `Time` (If the Time Key Target is set to Fixture. For more information see [User Settings](https://help.malighting.com/grandMA3/2.5/HTML/users_and_profiles_configuration.html) and [Time Key](https://help.malighting.com/grandMA3/2.5/HTML/key_time.html).)
  * Press `MA` `Time` `Time`
  * Type **Fade**

### Description

The Fade keyword is a helping keyword which is used to indicate fade times.

As a helping keyword for playback functions (for example Goto), this keyword sets the time which is used to execute the function.

If it is used as a starting keyword, Fade will apply individual timing in the programmer for the current selection and attributes.

|  **Hint:**  
---|---  
As long as the command starts with a function, the Fade keyword and the fade value can be randomly used within the command.  
  
  
To set the fade times for cues, read more in the [CueFade keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_cuefade.html).

### Syntax

**([Function] [Object] ["Object_Name" or Object_Number]) Fade [Fade_Value]**

### Examples  
  

  * To crossfade to cue 3 in the selected sequence in 4 seconds, type:

```
Goto Cue 3 Fade 4
```
---|---  
  
  * To set the individual fade time of 2 seconds to the dimmer of the current selection, type:

```
Fade 2
```
---|---  
  
  * To set the dimmer value of the current fixture selection to 50 % and apply an individual fade time of 2 seconds to the dimmer of the current selection, type:

```
At 50 Fade 2
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
