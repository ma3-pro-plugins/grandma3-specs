---
keyword: "SendMVR"
kind: general
shortcuts: ["Sendmv"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_sendmvr.html"
---

## Official

To enter the SendMVR keyword in the command line, use one of the options:

  * Type **SendMVR**
  * Type the shortcut **Sendmv**

###  Description 

The keyword SendMVR can be used to commit and request MVR files, or to join and leave the connection to other devices during MVR-xchange.

###  Syntax 

**SendMVR ["Connection_Type"] ["Number]**

SendMVR "Commit" ["Path_to_Folder/Name"] ["Name"]

###  Examples   
  

  * To establish a connection to the third service device, type: 

```
SendMVR "Join" "3"
```
---|---  
  
  * To end connection to the the first service device, type: 

```
SendMVR "Leave" "1"
```
---|---  
  
  

  * To commit the MVR file "BestShow.mvr" (which is located on C:\ProgramData\MA Lighting Technology\gma3_library\mvr) to the MVR-xchange group, type:

```
SendMVR "Commit" "C:\ProgramData\MA Lighting Technology\gma3_library\mvr\BestShow" "BestShow"
```
---|---  
  
  

  * To request the second file, type:

```
SendMVR "Request" "2"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
