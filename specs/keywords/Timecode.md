---
keyword: "Timecode"
kind: general
shortcuts: ["Ti", "TC"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_timecode.html"
---

## Official

To enter the Timecode keyword in the command line, use one of the options:

  * Press `MA` \+ `X6 | TC`
  * Type **Timecode**
  * Type the shortcut **Ti** or **TC**

### Description

The Timecode keyword is an object keyword used to select the timecode by default.

Using the Timecode keyword you can:

  * store
  * play (go)
  * record
  * edit
  * label
  * set properties of
  * rewind (top)

timecode shows.

For more information see [Timecode](https://help.malighting.com/grandMA3/2.5/HTML/timecode.html).

### Syntax

[Function] Timecode ["Timecode_Name" or Timecode_Number] (Property **["Property_Name" or "Property_Value"])**

### Property

The following table displays the properties that can be assigned using the [Set Keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_set.html).

Property | Property Value | Description  
---|---|---  
Name | "Timecode show name" | Set the name of timecode show.  
Time |  | Set position of the time cursor.  
Duration | 0s to 255h59m58.96s | Set the entire length of timecode show.  
Offset | 0s to 255h59m58.96s | To move the entire timecode show forward, set an offset in the timecode show.  
Loop Mode | Loop  
Pause  
Off | Basic settings for Loop and how to pause or stop.  
Loop Count | "Endless Repeat" (0),  
"No Repeat" (1),  
2..1000 |  **Only for timecode shows syncing to the internal clock.**  
Set if the timecode show runs:  
Endless (Endless Repeat)  
Once and stop (No Repeat)  
A specific number of times (number between 2 and 1000)  
TimeMarkers |  | Time markers are used to select the track. They will be stored.  
TCSlot | "Internal" (-2), "Link Selected" (-1), "Slot1" (0), "Slot2" (1), "Slot3" (2), etc. | Set the timecode show to a timecode slot.  
AutoStart (only available with external timecode slot) | "Yes", "No" | **Only available when syncing to an external source.**  
If a timecode signal is received, the timecode show switches from the off mode to the play mode.  
AutoStop | "Yes", "No" | **Only available when syncing to an external source.**  
If a timecode signal is received, the timecode show switches from the play mode to the off mode.  
User Bits | 0 .. FFFFFFFF, 0 .. 4294967296 | **Only available when syncing to an external source.**  
To transmit several kinds of information, for example, a second Timecode Stream, set user bits in hex or decimal. So several incoming Timecode Streams can be discerned.  
  
### Examples  
  

  * To set timecode show "Intro" to a duration of 55 seconds, type:

```
Set Timecode "Intro" "Duration" "55"
```
---|---  
  
  * To store a new timecode show called "Napalm Skies" in the timecode pool, type:

```
Store Timecode "Napalm Skies"
```
---|---  
  
  * To rename timecode show "Intro" "Prelude", type:

```
Set Timecode "Intro" "Name" "Prelude"
```
---|---  
  
  * To start the timecode show "Prelude", type:

```
Go Timecode "Prelude"
```
---|---  
  
  * To rewind the timecode show "Prelude", type:

```
Top Timecode "Prelude"
```
---|---  
  
  * To label timecode show 3 in the timecode pool, type:

```
Label Timecode 3
```
---|---  
  
The label pop-up opens and you can now label the timecode show.

For information on the key and its location see [X6 | TC key](https://help.malighting.com/grandMA3/2.5/HTML/key_x6.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
