---
keyword: "EncoderBank"
kind: general
shortcuts: ["Encoderban"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_encoderbank.html"
---

## Official

To enter the EncoderBank keyword in the command line, use one of the options:

  * Press `MA` \+ `X15 | Page` \+ `X15 | Page` \+ `X15 | Page`
  * Type **EncoderBank**
  * Type the shortcut **Encoderban**

|  **Hint:**  
---|---  
You can define commands for each encoder bank. The command will be executed once you select the encoder bank. To do so, edit the command cell in the Encoder Bar editor first.  
  
  
### Description

The EncoderBank keyword is an object keyword which addresses encoder banks.

Syntax

[Function] EncoderBank ["EncoderBank_Name" or EncoderBank_Number].(["EncoderPage_Name" or EncoderPage_Number])

### Examples

  

  * To select the encoder bank "Fancy Stuff", type:

```
Select EncoderBank "Fancy Stuff"
```
---|---  
  

  * To switch to the encoder page "Song 2" of the encoder bank "Show", type:

```
Select EncoderBank "Show"."Song 2"
```
---|---  
  
  * To only consider the attributes of filter 5 while knocking in the encoder bank 2, type:

```
On EncoderBank2 If Filter 5
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
