---
keyword: "Park"
kind: general
shortcuts: []
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_park.html"
---

## Official

To enter the Park keyword in the command line, use one of the options:

  * Press `Pause` `Pause`
  * Type **Park**

### Description

The Park keyword is a command keyword which is used to prevent DMX channels of fixtures to change their value.

### Syntax

Park [Object] ["Object_Name" or Object_Number]

### Examples  
  

  * To park fixture 1 with all its attributes, type:

```
Park Fixture 1
```
---|---  
  
  * To park the current selection, type:

```
Park
```
---|---  
  
It is also possible to enter Park into the command line and tap a cell in the fixture sheet to park a certain attribute.

To unpark fixtures and/or attributes, see the [Unpark Keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_unpark.html).

|  **Important:**  
---|---  
When parking a fixture and/or attribute it will park the corresponding DMX channel.  
  
  
  

  * To park all DMX channels of fixture 1 at 50%, type:

```
Park Fixture 1 At 50
```
---|---  
  
|  **Hint:**  
---|---  
The command Park Fixture At will park all DMX channels of the fixture to the value that is set.  
  
  
  

  * To park only DMX channels for FeatureGroup 1 at 50, type:

```
Park Fixture 1 At 50 If FeatureGroup 1
```
---|---  
  
  * To park DMX universe 2, type:

```
Park DMXUniverse 2
```
---|---  
  
To specify the universe:

  1. Enter the Park keyword in the command line.
  2. Tap the universe in the universe pool.

  * To park DMX channel 20 on the first universe, type:

```
Park DMXUniverse 1.20
```
---|---  
  
To specify the DMX channel:

  1. Enter the Park keyword in the command line.
  2. Tap the channel in the DMX sheet.

|  **Hint:**  
---|---  
If there are parked channels in a universe, they will be indicated by a blue **P** icon in the universe pool.

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
