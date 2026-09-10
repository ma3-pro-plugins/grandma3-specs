---
keyword: "SendOSC"
kind: general
shortcuts: ["Sen"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_sendosc.html"
---

## Official

To enter the **SendOSC** keyword in the command line, use one of the options:

  * Type **SendOSC**
  * Type the shortcut **Sen**

### Description

The SendOSC keyword is a command keyword that is used to send an OSC command.

For more information see [Remote In and Out](https://help.malighting.com/grandMA3/2.5/HTML/remote_inputs.html#OSC).

### Syntax

**SendOSC [ID] "/[OSCAddress],[OSC Type],[Value]"**

The supported types are:

  * Int(i)
  * Float(f)
  * Blob(b)
  * String(s)
  * True(T)
  * False(F)
  * Null(N)
  * Impulse(I)
  * Timetag(t)

It is not necessary to set a value (Payload) for:

  * True
  * False
  * Null
  * Impulse
  * Timetag

|  **Hint:**  
---|---  
When using the OSC types True, False, Nil/Null, Impulse and Timetag it is not necessary to enter a value.  
|  **Hint:**  
---|---  
Several values can be sent at once when separated by commas.  
  
|  **Important:**  
---|---  
When addressing an executor, a page must be specified as well.  
  
  
Instead of using page and executor numbers, it is also possible to address them by name.

When addressing executor keys, a value of 0 will be interpreted as not pressed. Values greater 0 will be interpreted as button press.

If a prefix is specified for an OSCData entry, then this very prefix will be added to the sent string when using the OSCSend command.

|  **Hint:**  
---|---  
The supported OSC types to control faders, executor knobs, and buttons are: Integer32, Float32, True, False and Nil/Null.A True will be interpreted as 1, while a False will be interpreted as 0.  
  
|  **Hint:**  
---|---  
The addresses defined for Page, Fader, ExecutorKnob, and Key are case-sensitive.   
  
  
### Examples  
  

  * To send an OSC command using the first configuration in the OSC menu with integer value 50 to fader 201 on page 1, type:

```
SendOSC 1 "/Page1/Fader201,i,50"
```
---|---  
  
  * To send an OSC command using the first configuration in the OSC menu with integer value 100 to fader 201 on page 1 and a fade time of 5s, type:

```
SendOSC 1 "/Page1/Fader201,ii,100,5"
```
---|---  
  
  * To send commands via OSC to the second grandMA3 station, the OSC address /cmd can be used. To store cue 1 via OSC, type: 

```
SendOSC 1 "/cmd,s,Store Cue 1"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
