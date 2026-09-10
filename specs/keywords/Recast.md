---
keyword: "Recast"
kind: general
shortcuts: ["Reca"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_recast.html"
---

## Official

To enter the Recast keyword in the command line, use one of the options:

  * Press `MA` \+ `X1 | Clone` \+ `X1 | Clone`
  * Type **Recast**
  * Type the shortcut **Reca**

### Description

The Recast keyword is a command keyword which is used to update attributes that were added or removed in the presets. It will add or remove these values in cues where the preset is used. 

Furthermore, recast can be used when configuring executors. When an executor configuration is used on several executors, and the assignment of handle for one of these executors changes, the changes will not automatically be transmitted to other executors using this configuration. When storing the changes into the executor configuration, it is possible to recast the executor configuration. All other executors using this configuration will then get the new handle assignment. For more information on executor configurations see the [Executor Configurations](https://help.malighting.com/grandMA3/2.5/HTML/executor_configurations.html).

|  **Known Limitation:**  
---|---  
Recast will only recast presets to cues where a preset link exists in the absolute layer.  
  
  
### Syntax

Recast Preset ["FeatureGroup_Name" or FeatureGroup_Number].["Preset_Name" or Preset_Number]

Recast Configuration ["ExecutorConfiguration_Name" or ExecutorConfiguration_Number]

Example

  * The dimmer is open and the color is red in ten fixtures in the All preset 21.1. This preset is used in sequence 1. We now add position to the preset. To recast preset 21.1, type: 

```
Recast Preset 21.1
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
