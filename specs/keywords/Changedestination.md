---
keyword: "ChangeDestination"
kind: general
shortcuts: ["CD", "Chang"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_changedestination.html"
---

## Official

To enter the ChangeDestination keyword in the command line, use one of the options: 

  * Type **ChangeDestination**
  * Type the shortcut **CD** or ****Chang****

###  Description 

The ChangeDestination keyword is a function keyword used to change the current destination of the command line. 

###  Syntax 

ChangeDestination ["Element_Name" or Element_Number]

ChangeDestination Root

ChangeDestination .. 

###  Examples   
  

  * To enter the first element of the current destination, type: 

```
ChangeDestination 1
```
---|---  
  

Result: 

|  User name@MessageCenter>  
---|---  
  
  

  * To enter the element of the current destination called Sequence, type: 

```
ChangeDestination Sequence
```
---|---  
  

  * To leave the destination "Sequence", type: 

|  User name@ShowData/DataPools/Default/Sequences> ChangeDestination Root  
---|---  
  

Result: 

```

```
---|---  
  
  * To go one level back in the tree structure, type: 

|  User name@MessageCenter/Undefined> ChangeDestination ..  
---|---  
  

Result: 

|  User name@MessageCenter>  
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
