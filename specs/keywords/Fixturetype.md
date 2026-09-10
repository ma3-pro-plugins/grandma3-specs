---
keyword: "FixtureType"
kind: general
shortcuts: ["FT", "Fixturet"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_fixturetype.html"
---

## Official

To enter the FixtureType keyword in the command line, use one of the options: 

  * Press `MA` \+ `Fixture`
  * Type **FixtureType**
  * Type the shortcuts **FT** or **Fixturet**

###  Description 

FixtureType is an object keyword which addresses the fixture types of a show file. 

|  **Important:**  
---|---  
Most edits and command line actions with the keyword FixtureType has to be done while in the Edit Setup mode. For more information, see [ChangeDestination keyword](https://help.malighting.com/grandMA3/2.5/HTML/release_notes.html).   
  
  
###  Syntax 

[Function] FixtureType ["FixtureType_Name" or FixtureType_Number]

###  Option Keywords 

The FixtureType keyword uses the following option keywords: 

  * [/All](https://help.malighting.com/grandMA3/2.5/HTML/ok_all.html)
  * [/OddEven](https://help.malighting.com/grandMA3/2.5/HTML/ok_oddeven.html)
  * [/Single](https://help.malighting.com/grandMA3/2.5/HTML/ok_single.html)

###  Examples 

**Requirement:**

  * Enter the Patch menu first.   
For more information see [Patch and Fixture Setup](https://help.malighting.com/grandMA3/2.5/HTML/patch.html). 

  * To assign fixture type 2 to fixtures 1 through 4, type: 

|  User name@ShowData/Patch/Stages/Stage 1> Assign FixtureType 2 At 1 Thru 4  
---|---  
  
  * To select all patched fixtures of fixture type 3, type: 

```
SelectFixtures FixtureType 3
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
