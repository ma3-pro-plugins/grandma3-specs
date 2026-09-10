---
keyword: "ReloadAllPlugins"
kind: general
shortcuts: ["RP"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_reloadallplugins.html"
---

## Official

To enter the ReloadAllPlugins keyword in the command line, use one of the options:

  * Type **ReloadAllPlugins**
  * Type **Reloada**
  * Type the shortcut **RP**

### Description

The ReloadAllPlugins keyword is a function keyword that is used to reload the content of the external Lua files.

It is necesssary to reload the external Lua files after you edited them, as the edits can influence how Lua behaves.

You may want to test the integrity of the Lua system to make sure that it behaves as expected next time you load the show. This is important as the show file saved does not contain a snapshot of the Lua memory. It only contains the integrated functions and the code in the defined plugins.

When the show file is loaded, the external Lua files and the code of the plugins are reloaded. That is, the code of the Lua file on the harddrive is reread and loaded into the show file again. This then may result in a different state than that after you powered down the console or saved the show file. 

|  **Hint:**  
---|---  
Double-check the executed command in the system monitor.  
  
  
### Syntax

**ReloadAllPlugins**

### Example  
  

  * To restart the content of the external Lua files after programming using Lua, type:

```
ReloadAllPlugins
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
