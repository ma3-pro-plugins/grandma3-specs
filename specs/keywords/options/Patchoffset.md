---
keyword: "/PatchOffset"
kind: option
shortcuts: ["/Patc"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_patchoffset.html"
---

## Official

To enter the **/PatchOffset** option keyword in the command line, use one of the options:

  * Type **/PatchOffset**
  * Type the shortcut**/Patc**

### Description

When patching the /PatchOffset option keyword sets the offset of DMX addresses in fixtures. The DMX address has to be specified using breaks of the fixture type.

### Syntax

Set (Object) [Object_Number] Property "Break[Number]" **["DMXAddress"] /PatchOffset [PatchOffset_Value]**

### General Keywords

General keywords that use the /PatchOffset option keyword:

  * [Set keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_set.html)

### Example

**Requirement:** Go to the Live Patch

For information on the Live Patch and how to use it in the grandMA3, see [Live Patch](https://help.malighting.com/grandMA3/2.5/HTML/patch_live.html). 

  * To set an offset of 50 starting at DMX address 10.1 in the first 13 fixtures in the patch, type:

```
Set 2 Thru 14 Property "Break1" "10.1" /PatchOffset 50
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
