---
keyword: "/Look"
kind: option
shortcuts: ["/L"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_look.html"
---

## Official

To enter the **/Look** option keyword in the command line, use one of the options:

  * Type **/Look**
  * Type the shortcut**/L**

### Description

The /Look option keyword stores all dimmer values of all fixtures in the show. 

If the dimmer value of a fixture is zero, the /Look option keyword only stores dimmer values of the fixture as there is no visible output onstage. 

If the dimmer value of a fixture is above zero, the /Look option keyword stores the values of all attributes of the fixture.

### Syntax

[Function] [Object] ["Object_Name" or Object_Number] /Look

### General Keywords

General keywords that use the /Look option keyword:

[](https://help.malighting.com/grandMA3/2.5/HTML/keyword_copy.html)

  * [Cue keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_cue.html)
  * [Preset keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_preset.html)
  * [Store keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_store.html)
  * [SetUserVariable keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_setuservariable.html)
  * [SetGlobalVariable keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_setglobalvariable.html)

|  **Hint:**  
---|---  
The /Look option keyword can be used together with the [/All option keyword](https://help.malighting.com/grandMA3/2.5/HTML/ok_all.html) or the [/AllForSelected option keyword](https://help.malighting.com/grandMA3/2.5/HTML/ok_allforselected.html).   
  
  
### Examples  
  

  * To store all dimmer values and all attributes in fixtures, with dimmer open in cue 1, type:

```
Store Cue 1 /Look
```
---|---  
  
  * To store the dimmer values and all active attributes of the selected fixtures in the programmer to the second preset in the first All preset pool, type:

```
Store Preset 21.2 /AllForSelected /Look
```
---|---  
​​  

|  **Hint:**  
---|---  
If you use SetUserVariable or SetGlobalVariable in combiniation with /Look, the proper value of the UI will be used in the variable. Whereas, using SetUserVariable and SetGlobalVariable without /Look, will use the internal represantion of the value, for example in form of numbers.   
  
  
### Example with and without /Look  
  

  * To set the user variable "mySeqPrioName" to the priority LTP of sequence 42, type:

```
SetUserVariable "mySeqPrioName" At Sequence 42 Property "Priority" /Look
```
---|---  
  
  

  * To set user variable "mySeqPrioNumber" to priority 6, which is LTP, of sequence 42, type:

```
SetUserVariable "mySeqPrioName" At Sequence 42 Property "Priority"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
