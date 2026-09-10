---
keyword: "Plugin"
kind: general
shortcuts: ["Pl"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_plugin.html"
---

## Official

To enter the Plugin keyword in the command line, use one of the options:

  * Press `MA` \+ `X14 | Macro` \+ `X14 | Macro`
  * Type **Plugin**
  * Type the shortcut **Pl**

### Description

The Plugin keyword is an object keyword which is used to access plugins. 

The default function of the Plugin keyword is [Go+](https://help.malighting.com/grandMA3/2.5/HTML/keyword_goplus.html).

### Syntax

([Function]) Plugin ["Plugin_Name" or Plugin_Number](.["LuaComponent_Name" or LuaComponent_Number]) ("Argument_Value")

### Examples  
  

  * To edit plugin 2, type:

```
Edit Plugin 2
```
---|---  
  
  * To label plugin 1 "Weakon," type:

```
Label Plugin 1 "Weakon"
```
---|---  
  
  

* * *

### Call a Plugin and Specify an Argument

**Requirement:**

  * Create a plugin that uses an argument when calling a function.

In this example our plugin is plugin 1 of the plugin pool and the argument is called name in the definition of the function. 

[Copy Code](<javascript:void\(0\)>)Lua  
---  
      
    
    return function(display_handle, name)
    	Printf("My name is "..name)
    end  
  
  * To generate the sentence "My name is Richard Roe" in the command line history, type:

```
Plugin 1 "Richard Roe"
```
---|---  
  
Result:

OK :| Plugin 1 "Richard Roe"  
---|---  
My name is Richard Roe  
Response in the command line history

"My name is Richard Roe" is now displayed in the command line history. 

* * *

### Call a Dedicated LuaComponent

**Requirement:**

  * Create at least two lua components in the plugin.

For more information on how to create lua components see [Plugins](https://help.malighting.com/grandMA3/2.5/HTML/plugins.html). 

  * To call the second LuaComponent of plugin 1, type:

```
Plugin 1.2
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
