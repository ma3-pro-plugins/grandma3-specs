---
keyword: "Executor"
kind: general
shortcuts: ["Ex"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_executor.html"
---

## Official

To enter the **Executor** keyword in the command line, use one of the options:

  * Press `MA` \+ `X16 | Exec`
  * Type **Executor**
  * Type the shortcut **Ex**

### Description

The Executor keyword is an object keyword used as a control handle for other objects.

The default function for Executor objects is **Select**. This means that calling executors without any function specified selects the object assigned to the executor. This selection is now also controllable with the 100 mm fader section.

If you apply a function or reference a property not supported by the Executor object, the command will be passed on to its child: key, fader, or the object assigned to the executor.

### Syntax

**Executor [Executor_ID]**

Select Page [Page_ID] Executor [**Executor_** ID]

**Set Executor [Executor_ID] [Setting] = [Setting_Option****]**

For more information on setting the executor assignments using the interface, see the [Assign Object to an Executor](https://help.malighting.com/grandMA3/2.5/HTML/executor_assign.html) and the [Executor Configurations](https://help.malighting.com/grandMA3/2.5/HTML/executor_configurations.html).

### Examples  
  

  * To remove executor 205 on the current page, type:

```
Delete Executor 205
```
---|---  
  
It does not delete the object assigned to the executor. It just deletes the assignment.

  * To delete cue 3 of the sequence assigned to executor 205, type:

```
Delete Executor 205 Cue 3
```
---|---  
  
  * To select executor 102 on page 4, type:

```
Select Page 4.102
```
---|---  
  
  * To change the setting "Key" of executor 201 to "Flash", type:

```
Set Executor 201 "Key" = "Flash"
```
---|---  
  
For more information see [Executors](https://help.malighting.com/grandMA3/2.5/HTML/executor.html).

For information on the key and its location see [X16 | Exec key](https://help.malighting.com/grandMA3/2.5/HTML/key_x16.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
