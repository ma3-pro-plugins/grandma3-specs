---
keyword: "Remote"
kind: general
shortcuts: ["Rem"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_remote.html"
---

## Official

To enter the Remote keyword in the command line, use one of the options:

  * Type **Remote**
  * Type the shortcut **Rem**

### Description

The Remote keyword is an object keyword that is used to access the remote input types.

You can store or delete remote input types and set parameters.

### Syntax

[Function] Remote ["RemoteInputType_Name" or RemoteInputType_Number].["Remote_Name" or Remote_Number] (Property ["Property_Name"] ["Property_Value"])

Assign [Object] ["Object_Name" or Object_Number] At Remote **["RemoteInputType_Name" or RemoteInputType_Number].["Remote_Name" or Remote_Number] (Property ["Property_Name"] ["Property_Value"])**

The following table displays the available remote input types and their remote input type IDs.

Remote Input Type | Remote Input Type ID  
---|---  
DC Remote | 1  
MIDI Remote | 2  
DMX Remote | 3  
  
The IDs in the input type have to be in an order and have to start with 1.

### Properties

The following table displays the properties you can set using the command line with the help of the [Set Keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_set.html).

|  **Hint:**  
---|---  
If an option or any other part of the keyword command requires two quotation marks, the outer quotation marks are "+" and the inner quotation marks are '+'.  
  
Property | Property Value | Description  
---|---|---  
Lock | "Yes", "No" | Sets the lock status.  
Name | "This is the name of the remote" | Sets the name of the remote.  
Target | "World", "Sequence", "Macro", "Group", "Plugin", "View", "Master" | Sets the target of the action when the contact is active.  
Fader | "Master", "X", "Temp", and all the fader functions. | Sets the fader the console should activate.  
Key | "Fix", "Select", "SelFix", and all the key functions. | Sets the key the console should activate.  
TriggerOn | "0%...100%" | Sets the value at which the trigger will be set to on.  
TriggerOff | "0%...100%" | Sets the value at which the trigger will be set to off.  
InFrom | "0%...100%" | Sets the starting point of the range of the incoming signal in use.  
InTo | "0%...100%" | Sets the end point of the range of the incoming signal in use.  
OutFrom | "0%...100%" | Sets the starting point of the range of the outgoing signal in use.  
OutTo | "0%...100%" | Sets the end point of the range of the outgoing signal in use.  
Enabled | "Yes", "No" | Sets the status to enabled or not enabled.  
**Only for DMX remotes:**  
Address | 1.001...1024.512 [universe].[dmx address] | Sets the DMX universe and address.  
**Only for DMX remotes:**  
Resolution | "8bit", "16bit", "24bit" | Sets the DMX resolution. For 16 bit and 24 bit, the DMX channels have to be consecutive.  
**Only for MIDI remotes:**  
MIDIChannel | "1, 2, 3, ..., 16" | Sets the MIDI channel.  
**Only for MIDI remotes:**  
MIDIIndex | "1, 2, 3, ..., 128" | Sets the MIDI index.  
**Only for MIDI remotes:**  
MIDIType | "Note", "NoteAttack", "NoteAttackDecay", "Control" |  Sets the MIDI type.  
Note = MIDI note only  
NoteAttack = MIDI note and uses the velocity to regulate the master except note off  
NoteAttackDecay = MIDI note and uses the velocity to regulate the master with note off  
Control = Control change (CC) messages.  
**Only for DC remotes:**  
DC start signal | "1, 2, 3, ..., 64" | Sets the DC start signal.  
  
The start signal and the MIDI offset of the desired input console for [DC Remotes](https://help.malighting.com/grandMA3/2.5/HTML/remote_inputs_dc.html) and [MIDI Remotes](https://help.malighting.com/grandMA3/2.5/HTML/remote_inputs_midi.html) have to be set in the [Output Configuration Menu](https://help.malighting.com/grandMA3/2.5/HTML/dmx_port_config.html).

Examples

  * To set the key of the first DMX remote to Go+, type:

```
Set Remote 3.1 "Key" "Go+"
```
---|---  
  
  * To store a new MIDI remote, type:

```
Store Remote 2.1
```
---|---  
  
  * To assign sequence 2 to the second DMX remote, type:

```
Assign Sequence 2 At Remote "DMXRemotes".2
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
