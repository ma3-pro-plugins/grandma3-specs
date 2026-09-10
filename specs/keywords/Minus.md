---
keyword: "- (Minus)"
kind: general
shortcuts: []
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_minus.html"
---

## Official

To enter the - [Minus] keyword in the command line, use one of the options: 

  * Press `-`
  * Type **-**[Minus] 

###  Description 

The - [Minus] keyword is used to remove objects from a list or to indicate negative values. 

If the - [Minus] keyword is used in order to indicate values, it will indicate absolute or relative values: 

  * A space between the - [Minus] and the value is automatically added. The space makes the value relative 
  * To obtain an absolute value, remove the space between the - [Minus] 

###  Syntax 

([Attribute] ["Attribute_Name" or Attribute_Number]) At - [Value]

[Object] ["Object_Name or Object_Number] - [Object] ["Object_Name" or Object_Number] [Number]

###  Examples   
  

  * To reduce the percentage readout of pan by 10 percent, type: 

```
Attribute "Pan" At - 10
```
---|---  
  

  * To reduce 10 % from the current dimmer value in the selected fixtures, type: 

```
At - 10
```
---|---  
  

  * To select the entire group 5 without selecting fixture 2, type: 

```
Group 5 - Fixture 2
```
---|---  
  
  * To remove fixtures 5, 6, and 7 in the current selection of fixtures, type: 

```
\- Fixture 5 Thru 7
```
---|---  
  
For information on the key and its location see [\- [Minus] key](https://help.malighting.com/grandMA3/2.5/HTML/key_minus.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
