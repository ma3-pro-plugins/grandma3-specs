---
keyword: "/MergeLowPriority"
kind: option
shortcuts: ["/Mergel"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_mergelowpriority.html"
---

## Official

To enter the **/MergeLowPriority** option keyword in the command line, use one of these options:

  * Type /**MergeLowPriority**
  * Type the shortcut **/Mergel**

### Description

The /MergeLowPriority option keyword adds data that is in the source to the destination only where it does not contain data. This option keyword preserves existing data at destination and is the least extreme form of merging. 

### Syntax

[Function] [Object] ["Object_Name" or Object_Number] /MergeLowPriority

### General Keywords

General keywords that use the /MergeLowPriority option keyword:

  * [Clone keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_clone.html)
  * [Cook keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_cook.html)

### Examples  
  

  * To clone data from fixture 1 to fixture 2 as a low priority merge in the programmer, type:

```
Clone Fixture 1 At Fixture 2 /MergeLowPriority
```
---|---  
  
  

  * To cook recipes in the cue parts of sequence 5 using low priority merge, type:

```
Cook Sequence 5 /MergeLowPriority
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
