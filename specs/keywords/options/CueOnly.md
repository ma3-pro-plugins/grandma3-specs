---
keyword: "/CueOnly"
kind: option
shortcuts: ["/CO", "/Cu"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_cueonly.html"
---

## Official

To enter the **/CueOnly** option keyword in the command line, use one of the options:

  * Type **/CueOnly**
  * Type the shortcuts**/CO** or**/Cu**

### Description

The /CueOnly option keyword blocks tracked values in the next cue or cue part to preserve the previous look on stage. 

For more information see [Store Cues](https://help.malighting.com/grandMA3/2.5/HTML/cue_store.html) and [Store Settings and Store Preferences](https://help.malighting.com/grandMA3/2.5/HTML/cue_store_settings_preferences.html). 

### Syntax

[Function] (Sequence [**"** Sequence_Name" or**** Sequence_Number]) Cue ["Cue_Name" or Cue_Number] /CueOnly ["Value"]

### General Keywords

General keywords that use the /CueOnly option keyword:

  * [Cue keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_cue.html)
  * [Delete keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_delete.html)
  * [Store keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_store.html)
  * [Update keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_update.html)

### Values

The /CueOnly option keyword uses these values:

  * DimmerOnly – uses the Dimmer Cue Only and releases the recently stored dimmer attributes in the next cue. 
  * DimmerOnlyDefaultNew – uses the Dimmer Cue Only and sets recently stored dimmer attributes to the default value in the next cue.
  * Off – does not use CueOnly 
  * On – uses CueOnly 
  * OnDefaultNew – uses Cue Only and sets new attributes within the sequence to the default value in the next cue. 

### Examples  
  

  * To store the current programmer values in cue 8 and to preserve the previous look in the following cue after cue 8, type:

```
Store Cue 8 /CueOnly
```
---|---  
  
  

  * To store the current programmer values in cue 6 and release the recently stored dimmer values in the next cue, type:

```
Store Cue 6 /CueOnly "DimmerOnly"
```
---|---  
  
  

  * To store the current programmer values in cue 5 and set the dimmer attributes to default values in the next cue, type:

```
Store Cue 5 /CueOnly "DimmerOnlyDefaultNew"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
