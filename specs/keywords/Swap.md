---
keyword: "Swap"
kind: general
shortcuts: ["Swa"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_swap.html"
---

## Official

To enter the Swap keyword in the command line, use one of the options:

  * Type **Swap**
  * Type the shortcut **Swa**

### Description

The Swap keyword is a playback keyword that starts the playback of a sequence and pulls down the dimmer of all other fixtures that are not part of the sequence or that are protected against Swap.

For more information on how to assign executors see [Assign Objects to an Executor](https://help.malighting.com/grandMA3/2.5/HTML/executor_assign.html). 

  * To disable the executor, release the executor key.

Pressing the executor button plays back the sequence using the swap functionality.  
If you swap sequences that have the same playback master, one will go to zero should it not be swap-protected. 

For more information on Swap Protect see [Sequence Settings](https://help.malighting.com/grandMA3/2.5/HTML/cue_sequence_settings.html). 

|  **Hint:**  
---|---  
If you press and hold an executor, this playback keyword will directly interact with a sequence or preset. Additionally, it can also be used with pool objects:

  1. Enter the keyword in the command line. 
  2. Tap and hold the pool object.
  3. The action will be applied as long as you keep holding the pool object.

  
  
### Syntax

Swap (On/Off) [Object] ["Object_Name" or Object_Number]

### Example  
  

  * To playback sequence 5 and pull down the dimmers of all other running playbacks to 0, type:

```
Swap Sequence 5
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
