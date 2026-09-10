---
keyword: "FixtureClass"
kind: general
shortcuts: ["FC", "Fixturec"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_fixture_class.html"
---

## Official

To enter the FixtureClass keyword in the command line, use one of the options: 

  * Press `MA` \+ `Fixture` \+ `Fixture` \+ `Fixture`
  * Type **FixtureClass**
  * Type the shortcuts **FC** or **Fixturec**

###  Description 

FixtureClass is an object keyword which addresses the fixture classes of a show file. 

###  Syntax 

[Function] FixtureClass ["FixtureClass_Name" or FixtureClass_Number]

###  Option Keywords 

The FixtureClass keyword uses the following option keywords: 

  * [/All](https://help.malighting.com/grandMA3/2.5/HTML/ok_all.html)
  * [/OddEven](https://help.malighting.com/grandMA3/2.5/HTML/ok_oddeven.html)
  * [/Single](https://help.malighting.com/grandMA3/2.5/HTML/ok_single.html)

###  Examples 

**Requirement:** Create the class "Spots" in the patch and link fixtures to it. 

  * To create a group in the group pool object 301 that contains all patched fixtures that are set to class "Spots" in the patch, type: 

```
AutoCreate FixtureClass "Spots" At Group 301
```
---|---  
  
  * To select all fixtures that are set to the class "Spots" in the patch, type: 

```
SelectFixture FixtureClass "Spots"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
