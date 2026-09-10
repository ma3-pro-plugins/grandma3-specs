---
keyword: "/AutoStart"
kind: option
shortcuts: ["/Autos"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_autostart.html"
---

## Official

To enter the **/AutoStart** option keyword in the command line, use one of the options: 

  * Type **/AutoStart**
  * Type the shortcut**/Autos**

###  Description 

The /AutoStart option keyword is used to define which sequences will start if you enter the preview mode. 

Syntax

Preview Sequence ["Sequence_Name" or Sequence_Number] /AutoStart ("Option Value")

###  General Keywords 

General keywords that use the /AutoStart option keyword: 

  * [Preview keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_preview.html)
  * [Sequence keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_sequence.html)

###  Values 

The /AutoStart option keyword uses these values: 

  * Off – if several sequences are selected, using "Off"**** starts none of the sequences. 
  * Single – if several sequences are selected, using "Single" starts the last sequence. 
  * Multi – If several sequences are selected, all of them will be started. 

###  Example   
  

  * To load sequences 1 to 3 into preview mode and start the last sequence, type: 

```
Preview Sequence 1 Thru 3 /AutoStart "Single"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
