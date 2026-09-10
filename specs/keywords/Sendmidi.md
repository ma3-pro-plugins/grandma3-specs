---
keyword: "SendMIDI"
kind: general
shortcuts: []
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_sendmidi.html"
---

## Official

To enter the SendMIDI keyword in the command line, use one of the options: 

  * Type **SendMIDI**
  * Type **Sendm**

###  Description 

The SendMIDI keyword is a command keyword that is used to output MIDI notes, MIDI control change messages, and MIDI program change messages. 

###  Syntax 

**SendMIDI "Note" (Channel/)Note (Velocity) (Status)**

**SendMIDI "Program" (Channel/)Value**

**SendMIDI "Control" (Channel/)Controller (Value)**

###  Examples   
  

  * To send out the MIDI note 42 on MIDI channel 2 with a velocity of 99, type: 

```
SendMIDI "Note" 2/42 99
```
---|---  
  
  * To send out the MIDI note 37 on MIDI channel 1, type: 

```
SendMIDI "Note" 37
```
---|---  
  
  * To send out the MIDI control value 64 to MIDI channel 1 controller 8, type: 

```
SendMIDI "Control" 1/8 64
```
---|---  
  
  * To send out a MIDI program change of 12, type: 

```
SendMIDI "Program" 12
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
