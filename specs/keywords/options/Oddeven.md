---
keyword: "/OddEven"
kind: option
shortcuts: ["/Od"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_oddeven.html"
---

## Official

To enter the **/OddEven** option keyword in the command line, use one of the options: 

  * Type **/OddEven**
  * Type the shortcut**/Od**

###  Description 

The /OddEven option keyword is used to form two groups – odd and even – out of fixtures of a specific fixture type, class or layer, and range of fixtures and selection.

###  Syntax 

AutoCreate [SourceObject] ["SourceObject_Name" or SourceObject_Number] At [DestinationObject] ["DestinationObject_Name" or Destination_Object_Number] /OddEven  

###  General Keywords 

General keywords that use the /OddEven option keyword: 

  * [AutoCreate keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_autocreate.html)
  * [Fixture keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_fixture.html)
  * [FixtureClass keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_fixture_class.html)
  * [FixtureLayer keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_fixture_layer.html)
  * [FixtureType keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_fixturetype.html)
  * [Selection keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_selection.html)
  * [Store keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_store.html)

###  Example  
  
  

  * To auto create odd and even groups out of all patched fixtures using fixture type 13 starting in group 21, type:

```
AutoCreate FixtureType 13 At Group 21 /OddEven
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
