---
keyword: "/Async"
kind: option
shortcuts: ["/Asy"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_async.html"
---

## Official

To enter the **/Async** option keyword in the command line, use one of the options: 

  * Type **/Async**
  * Type the shortcut**/Asy**

###  Description 

The /Async option keyword is used to asynchronously execute remote commands. 

###  Syntax 

RemoteCommand IP [IP_Address] ["Command to be Executed"] /Async

RemoteCommand [DeviceType] ["Device_Name" or Device_Number] ["Command to be Executed"] /Async

###  Example  
  

  * To asynchronously execute the command "Delete Macro 1" on the console named "DimmerBeach", type: 

```
RemoteCommand Console "DimmerBeach" "Delete Macro 1 /NoConfirmation" /Async
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
