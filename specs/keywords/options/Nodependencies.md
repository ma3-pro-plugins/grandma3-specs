---
keyword: "/NoDependencies"
kind: option
shortcuts: ["/Nod"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_nodependencies.html"
---

## Official

To enter the **/NoDependencies** option keyword in the command line, use one of the options:

  * Type **/NoDependencies**
  * Type the shortcuts**/Nod**

### Description

The /NoDependencies option keyword is used to import or export data without the dependent objects.

### Syntax

[Function] ["Object_Name" or Object_Number] /NoDependencies

### General Keywords

General keywords that use the /NoDependencies option keyword:

  * [Clone keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_clone.html)
  * [Export keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_export.html)
  * [Import keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_import.html)

### Examples  
  

  * To import the sequence in the file "Mimas.xml" to sequence 4 without dependent objects, type:

```
Import Sequence Library "Mimas.xml" At Sequence 4 /NoDependencies
```
---|---  
  
**Requirement:** Fixture 1, which uses a selective preset, is stored in a cue of sequence 1. Only fixture 1 is part of this preset.

  * To clone the data of fixture 1 to fixture 2 and use hard values in sequence 1 in fixture 2 where fixture 1 uses the selective preset, type:

```
Clone Fixture 1 At Fixture 2 If Sequence 1 /NoDependencies
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
