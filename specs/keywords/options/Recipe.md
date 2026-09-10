---
keyword: "/Recipe"
kind: option
shortcuts: ["/Rec"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/ok_recipe.html"
---

## Official

To enter the **/Recipe** option keyword in the command line, use one of the options: 

  * Type **/Recipe**
  * Type the shortcut**/Rec**

###  Description 

The /Recipe option keyword can only be used together with the [CleanUp keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_cleanup.html) and only if the [/Type option keyword](https://help.malighting.com/grandMA3/2.5/HTML/ok_type.html) is set to **Recipe**.

Using /Recipe allows you to define more precisely which recipes are to be deleted.

###  Syntax 

[Function] [Object] ["Object_Name" or Object_Number] (/Type "Recipe")(/Recipe "Recipe_Value")

### General Keywords and Option Keywords

General keywords and option keywords that use the /Recipe option keyword.

  * [CleanUp keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_cleanup.html)
  * [Store keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_store.html)
  * [/Type option keyword](https://help.malighting.com/grandMA3/2.5/HTML/ok_type.html)

### Values

The /Recipe option keyword uses these values:

  * **NoOutput****:**  
Recipes that do not generate output are deleted. This combines the following values – NotCooked and CookedButOverwritten. When specifying /Type "Recipe" and not using /Recipe in addition, NoOutput will be applied.
  * **NotCooked:**  
If the assigned preset cannot be used by the selection or if the assigned group is empty, **NotCooked** will remove such non-functional recipes. 
  * **CookedButOverwritten:**  
If a later recipe uses a preset with the values of the same attributes in the same selection, **CookedButOverwritten** will delete all recipes that could have been cooked successfully, but which do not generate output.
  * **Normal:**  
Is only used in combination with the Store keyword. When storing recipes into a preset **Normal** keeps the selection of recipes of the programmer. 
  * **NoSelection:  
** Is only used in combination with the Store keyword. **NoSelection** stores recipe presets without selection.

### Examples  
  

  * To clean up all recipes that do not generate output in cue 2 part 0 of sequence 1, type: 

```
CleanUp Sequence 1 Cue 2 Part 0 /Type "Recipe"
```
---|---  
  
or:

```
CleanUp Sequence 1 Cue 2 Part 0 /Type "Recipe" /Recipe "NoOutput"
```
---|---  
  

  * To clean up the recipes in the second position preset that could not be cooked, type:

```
CleanUp Preset 2.2 /Type "Recipe" /Recipe "NotCooked"
```
---|---  
  
  

### Store a Recipe Preset without Selection

**Requirement:** There are several recipes in the programmer.  
  

  * First type:

```
Store /Recipe "NoSelection"
```
---|---  
  
  * Then tap a preset you would like to store this recipe to.

Result:

You can now generically apply this recipe preset to other fixtures.

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
