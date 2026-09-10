---
keyword: "At"
kind: general
shortcuts: ["A"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_at.html"
---

## Official

To enter the At keyword in the command line, use one of the options:

  * Press `At`
  * Type **At**
  * Type the shortcut **A**

### Description

The At keyword is a function keyword and a helping keyword at once.

  * As a function keyword it is used to apply values.
  * As a helping keyword it is used along with other function keywords to indicate destination.

| **Hint:** |
| --- |
| At applies values live in the programmer. For information on how to apply values throughout the show file see the [Clone keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_clone.html). |

At is "the exception that proves the rule". At is one of the few functional keywords which accept objects before the function.

As a starting keyword, At is a function that applies values in the programmer to the current selection.

If value type Fade or Delay is used, the value list will be applied as individual fade/delay times.

Following an object list, At is a function that applies values to the object list. If the object list does not support the At function, the object list is resolved into a selection list and At applies values in the programmer.

Following an object list that follows a function, At is a helping keyword for the starting function.

### General Syntax

At ([Value_Type]) [Value]

At [Object] ["Object_Name" or Object_Number]

[Object] ["Object_Name" or Object_Number] At ([Value_Type]) [Value]

[Object] ["Object_Name" or Object_Number] At [Object] ["Object_Name" or Object_Number]

[Destination] At [Source] (If [Object] ["Object_Name" or Object_Number]) (/Option)

#### Syntax as a Helping Keyword

[Function] [Object] ["Object_Name" or Object_Number] At [Object] ["Object_Name" or Object_Number]

### Examples

  * To set the MasterFader of the sequence 1 to 30 %, type:

| User name[Fixture]>FaderMaster Sequence 1 At 30 |
| --- |

  * To set the dimmer attributes of the current selection to 75%, type:

| User name[Fixture]>At 75 |
| --- |

  * To set the fixture selection to the values of cue 3 in the selected sequence, type:

| User name[Fixture]>At Cue 3 |
| --- |

  * To set the pan attribute of the selected fixtures to 20, type:

| User name[Fixture]>Attribute "Pan" At 20 |
| --- |

  * To set an individual delay time of 2 seconds to attribute 2, type:

| User name[Fixture]>Attribute 2 At Delay 2 |
| --- |

  * To copy group 4 to group 10, type:

| User name[Fixture]>Copy Group 4 At 10 |
| --- |

  * To set a speed to 60 using the speed readout specified in the user profile (for example, BPM), type:

| User name[Fixture]>At Speed 60 |
| --- |

| **Hint:** |
| --- |
| If you use the At command without specifying additional attributes, the natural readout of the dimmer of the user profile will be used. |

**Requirement:** Enable single digit input first.

For more information on single digit input and how to enable it see [User Settings](https://help.malighting.com/grandMA3/2.5/HTML/users_and_profiles_configuration.html).

  * To apply a dimmer value of 50 to the currently selected fixtures as single digit input, type:

| User name[Fixture]>At 5 |
| --- |

  * To apply a dimmer value of 40 to fixtures 1 to 4, type:

| User name[Fixture]>Fixture 1 Thru 4 At 4 |
| --- |

For information on the key and its location see [At key](https://help.malighting.com/grandMA3/2.5/HTML/key_at.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
