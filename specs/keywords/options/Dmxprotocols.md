---
keyword: "/DMXProtocols"
kind: option
shortcuts: ["/Dmxp"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_dmxprotocols.html"
---

## Official

To enter the **/DMXProtocols** option keyword in the command line, use one of the options:

  * Type **/DMXProtocols**
  * Type the shortcut **/Dmxp**

### Description

The /DMXProtocols option keyword is used to load the DMX protocol settings (Art-Net and sACN) of the show file. 

### Syntax

[Function] ["Show_Name"] /DMXProtocols

### General Keywords

General keywords that use the /DMXProtocols option keyword:

  * [LoadShow](https://help.malighting.com/grandMA3/2.5/HTML/keyword_loadshow.html)
  * [NewShow](https://help.malighting.com/grandMA3/2.5/HTML/keyword_newshow.html)

### Examples  
  

  * To load the DMX protocols of the show file "A Midsummer Night's Dream" and its show data, type:

```
LoadShow "A Midsummer Night's Dream" /DMXProtocols
```
---|---  
  
  * To create a new show and clear all DMX protocols, type:

```
NewShow "Phobos" /DMXProtocols
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
