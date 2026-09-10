---
keyword: "Clone"
kind: general
shortcuts: []
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_clone.html"
---

## Official

To enter the Clone keyword in the command line, use one of the options: 

  * Press `MA` \+ `X1 | Clone`
  * Type **Clone**
  * Type **Clo**

###  Description 

Clone replicates data from one fixture or selection to another throughtout the show file. For more information on applying values live in the programmer only, see the [At keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_at.html). 

Syntax

Clone [Object] ["Object_Name" or Object_Number] At [Object] ["Object_Name" or Object_Number] (If [Object] ["Object_Name" or Object_Number] /Option)

###  Option Keywords 

The Clone keyword uses the following option keywords: 

  * [/MergeLowPriority](https://help.malighting.com/grandMA3/2.5/HTML/ok_mergelowpriority.html)
  * [/MergeHighPriority](https://help.malighting.com/grandMA3/2.5/HTML/ok_mergehightpriority.html)
  * [/NoDependencies](https://help.malighting.com/grandMA3/2.5/HTML/ok_nodependencies.html)
  * [/Overwrite](https://help.malighting.com/grandMA3/2.5/HTML/ok_overwrite.html)

###  Examples   
  

  * To clone the entire show data from fixture 1 to fixture 2, type: 

```
Clone Fixture 1 At Fixture 2
```
---|---  
  

The Clone window opens.

  

Clone Window

For more information on cloning in the general user interface see [Clone](https://help.malighting.com/grandMA3/2.5/HTML/operate_clone.html). 

  * To clone data from fixtures 1 and 2 to fixtures in group 10 within sequence 1 thru 10C only, type: 

```
Clone Fixture 1 + 2 At Group 10 If Sequence 1 Thru 10
```
---|---  
  

  * To clone all objects within data pool 1 from fixtures 1 thru 12 to fixtures 101 thru 112, type: 

```
Clone Fixture 1 Thru 12 At Fixture 101 Thru 112 If DataPool 1
```
---|---  
  

For more information on data pools, see the [Data Pools](https://help.malighting.com/grandMA3/2.5/HTML/datapool.html). 

  * To clone the pan attribute of fixture 1 to the tilt attribute of fixture 2, type:

```
Clone Fixture 1 Attribute "Pan" At Fixture 2 Attribute "Tilt"
```
---|---  
  

|  **Hint:**  
---|---  
When cloning presets and cue data, all presets referenced by the destination objects are automatically cloned in addition.   
  
|  **Hint:**  
---|---  
The syntax:   
Clone [Source_Object] ["Object_Name" or Object_Number] At [Destination_Object] ["Object_Name" or Object_Number] (/Option)   
produces the same results as:   
[Destination_Object] ["Object_Name" or Object_Number] At [Source_Object] ["Object_Name" or Object_Number] (/Option)   
All options described above work the same for both syntax structures. When cloning without the **Clone** keyword, keep in mind that the source and destination change places within the syntax.   
For more information on the **At** keyword, see the [At keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_at.html).   
  
  
For information on the key and its location see [X1 | Clone key](https://help.malighting.com/grandMA3/2.5/HTML/key_x1.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
