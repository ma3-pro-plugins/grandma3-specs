---
keyword: "FixtureLayer"
kind: general
shortcuts: ["FL", "Fixturel"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_fixture_layer.html"
---

## Official

To enter the FixtureLayer keyword in the command line, use one of the options: 

  * Press `MA` \+ `Fixture` \+ `Fixture`
  * Type **FixtureLayer**
  * Type the shortcuts **FL** or **Fixturel**

###  Description 

FixtureLayer is an object keyword which addresses the layers of fixtures in a show file. 

###  Syntax 

[Function] FixtureLayer ["FixtureLayer_Name" or FixtureLayer_Number]

###  Option Keywords 

The FixtureLayer keyword uses the following option keywords: 

  * [ /All](https://help.malighting.com/grandMA3/2.5/HTML/ok_all.html)
  * [/OddEven](https://help.malighting.com/grandMA3/2.5/HTML/ok_oddeven.html)
  * [/](https://help.malighting.com/grandMA3/2.5/HTML/ok_single.html)[Single](https://help.malighting.com/grandMA3/2.5/HTML/ok_single.html)

Example

**Requirement:** Create the layer "Backtruss" in the patch and link fixtures to it. 

  

  * To select all fixtures that are set to layer "Backtruss" within the patch, type: 

```
SelectFixtures FixtureLayer "Backtruss"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
