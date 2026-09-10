---
keyword: "/CopyCueSource"
kind: option
shortcuts: ["/Cop", "/CCS"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_copycuesource.html"
---

## Official

To enter the **/CopyCueSource** option keyword in the command line, use one of the options:

  * Type **/CopyCueSource**
  * Type the shortcut**/Cop** or **/CCS**

### Description

The /CopyCueSource option keyword defines how data is extracted in the source cue when copying cues. 

For more information see [Copy Cues](https://help.malighting.com/grandMA3/2.5/HTML/cue_copy.html). 

### Syntax

Copy (Sequence ["Source_Sequence_Name" or Source_Sequence_ID]) Cue ["Source_Cue_Name" or Source_Cue_ID] At (Sequence ["Destination_Sequence_Name" or Destination_Sequence_ID]) Cue ["Destination_Cue_Name" or Destination_Cue_ID] /CopyCueSource "Value"

### General Keywords

General keywords that use the /CopyCueSource option keyword:

  * [Cue keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_cue.html)
  * [Copy keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_copy.html)

### Values

The /CopyCueSource option keyword uses these values:

  * Content
  * Status
  * Look

### Example  
  

  * To copy the status of cue 1 to cue 2, type:

```
Copy Cue 1 At Cue 2 /CopyCueSource "Status"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
