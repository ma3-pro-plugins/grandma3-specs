---
keyword: "Store"
kind: general
shortcuts: ["S"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_store.html"
---

## Official

To enter the **Store** keyword in the command line, use one of the options:

  * Press `Store`
  * Type **Store**
  * Type the shortcut **S**

### Description

The Store keyword is a function keyword which is used to store objects in the show file. 

If no object type or destination is given, the object type **Cue** will be used in the selected sequence.

If you do not specify a target during storing, the new object will occupy the first free spot in the pool.

However, you can store an object at a certain spot or later in a pool. To do so, use the Window Settings and set First Index. For more information see [Common Window Settings](https://help.malighting.com/grandMA3/2.5/HTML/wvm_settings.html#h2__522911071).

### Syntax

Store [Object] ["Object_Name" or Object_Number or Next/Previous](/Option)

### Option Keywords

The Store keyword uses the following option keywords:

  * [/Active](https://help.malighting.com/grandMA3/2.5/HTML/ok_active.html)
  * [/ActiveForSelected](https://help.malighting.com/grandMA3/2.5/HTML/ok_activeforselected.html)
  * [/All](https://help.malighting.com/grandMA3/2.5/HTML/ok_all.html)
  * [/AllForSelected](https://help.malighting.com/grandMA3/2.5/HTML/ok_allforselected.html)
  * [/Ask](https://help.malighting.com/grandMA3/2.5/HTML/ok_ask.html)
  * [/Auto](https://help.malighting.com/grandMA3/2.5/HTML/ok_auto.html)
  * [/AutoFit](https://help.malighting.com/grandMA3/2.5/HTML/ok_autofit.html)
  * [/CreateSecondCue](https://help.malighting.com/grandMA3/2.5/HTML/ok_createsecondcue.html)
  * [/CueOnly](https://help.malighting.com/grandMA3/2.5/HTML/ok_cueonly.html)
  * [/DMX](https://help.malighting.com/grandMA3/2.5/HTML/ok_dmx.html)
  * [/Embed](https://help.malighting.com/grandMA3/2.5/HTML/ok_embed.html)
  * [/ForceGlobal](https://help.malighting.com/grandMA3/2.5/HTML/ok_forceglobal.html)
  * [/Global](https://help.malighting.com/grandMA3/2.5/HTML/ok_global.html)
  * [/GridMergeMode](https://help.malighting.com/grandMA3/2.5/HTML/ok_gridmergemode.html)
  * [/InputFilter](https://help.malighting.com/grandMA3/2.5/HTML/ok_inputfilter.html)
  * [/KeepActivation](https://help.malighting.com/grandMA3/2.5/HTML/ok_keepactivation.html)
  * [/Look](https://help.malighting.com/grandMA3/2.5/HTML/ok_look.html)
  * [/MAtricks](https://help.malighting.com/grandMA3/2.5/HTML/ok_matricks.html)
  * [/Merge](https://help.malighting.com/grandMA3/2.5/HTML/ok_merge.html)
  * [/NoConfirmation](https://help.malighting.com/grandMA3/2.5/HTML/ok_noconfirmation.html)
  * [/OddEven](https://help.malighting.com/grandMA3/2.5/HTML/ok_oddeven.html)
  * [/Output](https://help.malighting.com/grandMA3/2.5/HTML/ok_output.html)
  * [/Overwrite](https://help.malighting.com/grandMA3/2.5/HTML/ok_overwrite.html)
  * [/PhaserData](https://help.malighting.com/grandMA3/2.5/HTML/ok_phaserdata.html)
  * [/Programmer](https://help.malighting.com/grandMA3/2.5/HTML/ok_programmer.html)
  * [/Recipe](https://help.malighting.com/grandMA3/2.5/HTML/ok_recipe.html)
  * [/Remove](https://help.malighting.com/grandMA3/2.5/HTML/ok_remove.html)
  * [/Screen](https://help.malighting.com/grandMA3/2.5/HTML/ok_screen.html)
  * [/ScreenOnly](https://help.malighting.com/grandMA3/2.5/HTML/ok_screenonly.html)
  * [/Selective](https://help.malighting.com/grandMA3/2.5/HTML/ok_selective.html)
  * [/TrackingShield](https://help.malighting.com/grandMA3/2.5/HTML/ok_trackingshield.html)
  * [/Universal](https://help.malighting.com/grandMA3/2.5/HTML/ok_universal.html)
  * [/Wait](https://help.malighting.com/grandMA3/2.5/HTML/ok_wait.html)

For more information see [Store Options and Store Preferences](https://help.malighting.com/grandMA3/2.5/HTML/cue_store_settings_preferences.html).

### Examples  
  

  * To store cue 2 in the selected sequence, type: 

```
Store 2
```
---|---  
  
For more information see [Store Cues](https://help.malighting.com/grandMA3/2.5/HTML/cue_store.html).

  * To store the programmer values as cue 1 through cue 10 and cue 20 through cue 30, type:

```
Store Cue 1 Thru 10 + 20 Thru 30
```
---|---  
  
  * To store the programmer values as cue 42 of the selected sequence and directly label it, type:

```
Store Cue 42 "Return of the Paranoid Android"
```
---|---  
  
  * To store a new group to the first free spot in the groups pool, type:

```
Store Group
```
---|---  
  
  

  * To store new values to the already existing cue 5 in the selected sequence, whlile cue 4 is active, type:

```
Store Cue Next
```
---|---  
  
The Store Cue pop-up opens and you can now define how the values will be stored into the cue.

  

  * To store values to the second next existing cue, type:

```
Store Cue Next 2
```
---|---  
  
  

|  **Important:**  
---|---  
The examples that use **Next** can use **Previous** to **do the opposite**.  
  
  
  * To store vaues to the cue that is one digit apart from the curent cue in the selected sequence, type:

```
Store Cue + 1
```
---|---  
  
  * To store values to the cue that is 0.1 digits from the current cue in the selected sequence, type:

```
Store Cue + 0.1
```
---|---  
  

  * To store a new cue in the cue list while the focus is in cue 4, type:

```
Store Cue +
```
---|---  
  
  

|  **Important:**  
---|---  
The examples that use **+** can use **-** to **do the opposite**.  
  
  
For information on the key and its location see [Store key](https://help.malighting.com/grandMA3/2.5/HTML/key_store.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
