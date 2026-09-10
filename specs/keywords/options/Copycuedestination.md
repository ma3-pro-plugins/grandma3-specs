---
keyword: "/CopyCueDestination"
kind: option
shortcuts: ["/CopyCued", "/CCD"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_copycuedestination.html"
---

## Official

To enter the **/CopyCueDestination** option keyword in the command line, use one of the options:

  * Type **/CopyCueDestination**
  * Type the shortcut**/CopyCued** or /**CCD**

### Description

The /CopyCueDestination option keyword defines how the copied data is used in the destination cue when copying cues. 

For more information see [Copy Cues](https://help.malighting.com/grandMA3/2.5/HTML/cue_copy.html). 

### Syntax

Copy (Sequence ["Source_Sequence_Name" or Source_Sequence_ID]) Cue ["Source_Cue_Name" or Source_Cue_ID] At (Sequence ["Destination_Sequence_Name" or Destination_Sequence_ID]) Cue ["Destination_Cue_Name" or Destination_Cue_ID] /CopyCueDestination "Value"

### General Keywords

General keywords that use the /CopyCueDestination option keyword:

  * [Cue keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_cue.html)
  * [Copy keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_copy.html)

### Values

The /CopyCueDestination option keyword uses these values:

  * Merge
  * Overwrite

### Example

**Requirement:** Create cues 1 and 2

  * To copy cue 1 to cue 2 and merge the data of cue 1 with cue 2, type:

```
Copy Cue 1 At Cue 2 /CopyCueDestination "Merge"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
