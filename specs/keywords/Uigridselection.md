---
keyword: "UIGridSelection"
kind: general
shortcuts: ["Uig"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_uigridselection.html"
---

## Official

To enter the UIGridSelection keyword in the command line, use one of the options:

  * Type **UIGridSelection**
  * Type the shortcut **Uig**

### Description

UIGridSelection keyword is used by the system to hold information about which objects are selected in a grid window. Grid windows include sheets. It **does****not include** the Selection Grid window.

The keyword is primarily used internally by the system, but the selection can be used for normal operations that are executed on the selected objects.

|  **Important:**  
---|---  
The grid with the selection must have a focus so the UIGridSelection command can actually work.  
  
  
### Syntax

[Function] UIGridSelection

### Example

**Requirement:**

  * Several cues in a sequence.
  * A macro containing a Copy UIGridSelection command. This is important so you can execute the command without moving the focus.

  * To copy a selection of the cues to cue 41 using the UIGridCommand, follow these steps:

  1. Select the desired cues in the sequence sheet.
  2. Run the macro using the command keys (Important to use the keys to keep the focus in the cue selection).
  3. Now the following command can be entered and executed in the command line:

```
Paste Cue 41
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
