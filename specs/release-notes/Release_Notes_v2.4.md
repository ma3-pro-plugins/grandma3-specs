# grandMA3 Release Notes 2.4

**Version:** 2.4 | **Date:** 2026-05-18

> Text extracted from the official MA Lighting PDF (`Release_Notes_v2.4.pdf`). Layout and formatting are approximate.

## Table of Contents

- [1. Features](#1-features)
- [2. Other Enhancements](#2-other-enhancements)
- [3. Changes](#3-changes)
- [4. Bug Fixes](#4-bug-fixes)
- [5. Deprecated](#5-deprecated)
- [6. Appendix](#6-appendix)
- [7. Known Limitations](#7-known-limitations)

## Let's Get Started

Do you need help getting started in grandMA3? Perfect! Here we describe a few quick steps to get you rolling. The manual will explain functionality in detail while the MA e-Learning in the MA University offers you all kinds of training. All information can be

Let's go! Boot your console or open your onPC and find predefined views on view buttons on the right. To switch between the views, tap the corresponding view buttons.

If this is your first time starting grandMA3 software, patch some fixtures first. Or you can load one of the demo shows delivered with the software. Either way, press Menu. If you use grandMA3 onPC software, there is a symbol in the top left corner there.

Clicking the symbol is the same as pressing Menu on a console.

Tap Backup and then Load, now you are ready to load shows. Would you like to get right on it? Switch Shows to Demo Shows in the title bar first. To do so, tap Shows repeatedly until it says Demo Shows. Once Demo Shows is displayed, it is possible to select any demo show in the list. After you selected a demo show, tap Load.

In case a show was already loaded, a pop-up will appear asking if you want to save the current show first before loading the new one. It's up to you!

Here we go! Now you are ready to work with the grandMA3 software. It is as easy as that! Again - there are view buttons there, which change the screen content. At the bottom, you will find the encoder bar and the command line. Technically that is all you need to get started. For more information, see the grandMA3 help menu. To access the help in the console or the onPC, tap the view buttons named Help or visit the Online Manuals on the MA Lighting website. If you want to learn the grandMA3 software step by step, please see the Quick Start Guide and join the MA e-Learning - it's free of charge and available on the MA Lighting website.

Have fun using our grandMA3 software! Find all the improvements and changes of this software version further down.

> **Hint:** The grandMA3 software will start using the show file (or status) that was in operation before the software was shut down.

## 1. Features

- Phaser Recipes and Shapes
- Presets
- MIDI Show Control (MSC)
- Preview
- Improved MVR and Partial Show Read
- Phone Tethering via USB

### Phaser Recipes and Shapes

#### Added in this release:

Phasers can now be created as recipes.

Phaser recipes are recipes that have 2 or more steps.

To create a phaser recipe:

1. Open the recipe editor.
2. Tap Add Phaser Recipe.
3. Add a selection and values in the recipe lines.

To add steps to a phaser recipe, tap New Step below the phaser recipe.

Ifadditional steps are added to a phaser recipe, some values are inherited from previous steps.

Phaser recipes in presets are indicated with a violet .When editing a phaser preset, a temporary version of the recipe editor opens in the edit window.

To add phaser recipes to cue parts, open the sequence sheet, enable Show Recipes in the window settings, and tap on the violet

on the left side of the recipe lines.

Recipe lines of phaser recipes are indicated by a violet background in the recipe editor and can be edited like standard recipe lines, which are indicated by a green background.

The colors for both standard and phaser recipes can be changed in the color theme.

Known Limitation:

Currently phaser recipes cannot be created using the edit recipe mode. The edit recipe mode is only available in standard recipes.

Multiple new columns have been added to the phaser editor for creating phaser recipes. Additionally, a context area has been added to the recipe editor to edit recipes lines. For more information on the context area, see below.

- Step: Displays which step of the phaser the recipe linecorresponds to. The step isset automatically and cannot be
  changed manually.

- Shape: Select a shape from the shapes pool. Shapes span across the entire phaser. Selecting a shape influences
  other values. For more information on shapes, see below.

if you assign a shape to a phaser recipe, values that are set in the shape are applied to the corresponding empty cells in the phaser recipe. Values that are set manually ina phaser recipe have priority over values that are set in the shape. They are not overridden If a shape isassigned. Exception: Curves that are set manually are overridden with the curves in the shape If the shape is called a second time.

Values that are transferred from the shape are displayed in angle brackets (<>).

> **Restriction:** if you use PSR, phaser recipes willlose the link to referenced shapes.

- Attributes: Select an attribute from the list. To select a filter, tap Filters in the Sheet tab or tap the Filter tab in the
  assignment editor.

To filter the list of attributes, tap Filter next to the search bar in the context area or in the title bar of the assignment editor. The options are All, Used, Unused, and Selection. Used and Unused refer to the attributes used in the show file. Selection displays all attributes that are available for the current selection. If there is an attribute set in the selected shape object, the attribute of the shape will be automatically added if the Attributes column is empty.

- To clear the attributes cell, tap Clear Attribute in the context area or tap the Empty tab in the assignment editor.
  Attributes are set for all steps.

- Value Absolute: Set an absolute value for an attribute, for instance a dimmer value of 50%. Presets can be used as
  absolute values. Presets that cannot be used as absolute values are grayed out in the pool. Empty presets can be selected as absolute values. Select None in the Specials tab in the calculator to specify that no absolute value is applied.

- Value Relative: Set a relative value for an attribute, for instance a dimmer value of -20%. Presets can be used as
  relative values. Presets that cannot be used as relative values are grayed out in the pool. Empty presets can be selected as relative values. Select None in the Specials tab in the calculator to specify that no relative value is applied.

- Curve: Select a curve from the dropdown. The options are Linear, Ease In and Out, Ease Out, Ease In, Snap, and
  Swing. If a curve differs from the predefined curves or you manually adjust a curve in the editor, the cell displays Custom. A visual representation of the curve is displayed on the left of the cell. Curves can be edited per step. For more information on editing curves, see Edit Shapes.

To reset the curve of a single step to the shape that is set in the phaser recipe, select Reset in the dropdown. If no shape is set, the curve will be reset to the default Linear.

To reset the curves of all steps to the shape that is set in the phaser recipe, tap Reset to Shape in the encoder bar. If no shape is set, the curves will be reset to the default Linear.

- Trans X/Y/Z: Set a transition value or range of values on the X, Y, or Z axis. For more information on the transition
  layer, see step layers.

- Width X/Y/Z: Set a width or range of width values on the X, Y, or Z axis. For more information on the width layer,
  see step layers.

- Accel X/Y/Z: Set an acceleration value or range of values on the X, Y, or Z axis. "P" or "F" in front of the value in the
  cell indicates if Spline in the calculator is set to Proportional (P) or Free (F). For more information on the accel layer see step layers.

- Decel X/Y/Z: Set a deceleration value or range of values for the X, Y, or Z axis. "P" or "F" in front of the value in the cell
  indicates if Spline in the calculator is set to Proportional (P) or Free (F). For more information on the decel layer see step layers.

- Measure: Change the value of the measure layer. For more information on measure see phaser layers.
- Playback: For information on other columns in the recipe editor see Recipes.
    - NShot: Determine the number of times the phaser runs. After completing the number of cycles set in the
      cell, the phaser automatically stops. Example: To create a one shot phaser, set NShot to 1. The phaser runs a single time and then stops. NShot can be set to a number lower than 1. The phaser then stops before completing an entire cycle. Example: If you have a phaser with 4 steps and you set NShot to 0.75, only the first 3 steps of the phaser will run, the fourth step will be omitted.

To keep the values that are active at the end of the determined phaser cycles, set NShot Stay to Yes in the calculator. To run the phaser in a loop, tap Unlimited in the calculator.

To retrigger an NShot phaser, activate Sync in the encoder bar.

#### Added NShot keyword:

NShot keyword sets the number of phaser cycles using the command line.

Use this syntax:

At NShot [NShot_Number] Example:

To set the number of phaser cycles to 4, type:

Release Notes 2.4.

User name[Fixture]>At NShot 4

- Direction: Set the direction inwhich you want the phaser to run. - Forward: The phaser steps run in the order set in the phaser, for example 1 -2 -3. - Backward: The phaser steps and transitions run inreverse order, for example, 3 - 2 -1. - Alternate: The phaser continuously alternates between running forward and backward. If
  you use Alternate in combination with NShot, one cycle includes one forward and one backward run of the phaser. Example: If NShot is set to 1 in a phaser with three steps and direction is set to Alternate, the phaser runs 1 -2 - 3 -2 - 1 and then stops.

- Adaptive Measure:
  If set to Yes, the measure is adapted to the number of grid positions on an axis. By default, Adaptive Measure applies to the x-axis. Example: If you have a selection of 10 fixtures that are arranged across the x-axis and enable Adaptive Measure, the measure isset to 10. This can be used to synchronize the phaser to a beat. To apply the value that is set in the shape of the phaser recipe, select Take from Shape in the selection pop-up. The selection pop-up is only available If a shape is set in the recipe.

- Adaptive Width:
  If set to Yes, the width of the firststep is adapted to the number of grid position on an axis. By default, Adaptive Width applies to the x-axis. Example: if you have a selection of 5 fixtures that are arranged across the x-axis and enable Adaptive Width, the firststep is automatically calculated to be 20 %. This can be used to output exactly one grid position of a selection at a time. Curve, width, and transition reflect the calculated values. The transition can be edited in the firststep.

When adaptive width isset to Yes, the width cannot be changed manually. To apply the value that is set in the shape of the phaser recipe, select Take from Shape in the selection pop-up. The selection pop-up is only available If a shape is set in the recipe.

Adaptive width can only be used with phasers that have two steps. If a step is added to a recipe with Adaptive Width set to Yes, itis automatically set to No.

- Adaptive XY Rotation:
  Rotate the axis to which Adaptive Measure and Adaptive Width are applied. To apply the value that is set in the shape of the phaser recipe, tap Take from Shape in the editor pop-up.

For information on other columns in the recipe editor, see Recipe Editor.

When adding or editing a phaser recipe in the recipe editor, a dedicated encoder bar is displayed. This bar allows you to easily edit phaser recipes.

You can store phaser recipes to sequences, cues, cue parts, presets, or programmer parts. Newly created recipe presets and presets that are converted into a recipe using Turn into Recipe are stored as Selective.

#### Improved recipe editor:

#### Added a context area to the recipe editor:

- Sources of attributes for editing are displayed in the context area in the lower section of the recipe editor.
  There are three tabs:
    - Pool: The pool for the property is displayed.
    - Sheet: The available values are displayed in sheet form.
    - Editor: If an editor is available for the property, the editor is displayed.

For each property that has more than one tab available in the context area, the context area opens to the tab that was opened last.

To hide the context area, disable Context Area in the window settings.

- To pin the current view of the context area in place, enable the on the bottom left.The displayed values in the
  context area of the recipe editor now stay pinned, selecting a different attribute in the recipe linedoes not change them.

You can stillswitch between pool, sheet, and editor.

When you toggle the pin off,the values of the selected field in the phaser recipe line are displayed.

- In pools in the context area, Assign, Label, Move, and Copy are available in the swipey commands. Other swipey
  commands are not available and grayed out.

Pool settings are available in the context area. To open them, tap MA in the upper leftcorner of the pool. Pool objects in the context area can be addressed using the command line.

- Selection has three additional buttons in the context area. To clear the selection cell,tap None. To apply the
  selection that is set in the selected value preset, tap From Value. To apply the current selection in the programmer, tap Take Selection.

- Tap New with Selection in the selection drop-down listto create a new group in the groups pool that contains the
  current selection and reference itin the recipe.

- On the bottom right of the window there are seven action buttons for quick access to important functions: To hide
  the action buttons, disable Action Buttons in the settings.
    - Add Programmer Part: Add a programmer part line.This button does the same as tapping New
      Programmer Part at the bottom of the recipe lines.

    - Add Standard Recipe: Add a recipe line fora standard recipe with one step. If the new recipe is added to
      an existing recipe, the new recipe inherits the selection of the previous recipe.

    - Add Phaser Recipe: Add a recipe line for a phaser recipe with at least two steps. If the new recipe is
      added to an existing recipe, the new recipe inherits the selection of the previous recipe.

    - Insert Step: Add a step to a phaser recipe above the currently selected step. To add a step at the
      bottom, select New Step below the phaser recipe, then tap Insert Step. New steps inherit the value source from the previous step.

    - Add Value Source: Add a value source to a phaser recipe. Value sources include attributes and filters.
    - Adjust Shape: Open the shape pool in the context area of the recipe editor and select the cellin the
      shape column.

    - Adjust MAtricks: Open the MAtricks editor and select the cell in the MAtricks column.

- In presets without a recipe line, the buttons above are grayed out, and an additional button called Turn into Standard
  Recipe isdisplayed. First,tap Turn into Standard Recipe to create a recipe preset and use the buttons as described above.

Additional improvements:

- Cut ( ),copy ( ),and paste ( )buttons were added to the toolbar on the left side of the recipe editor window.

- In the recipe area in the sequence sheet, there are four additional buttons in the toolbar on the left side:
    - (green): Add a standard recipe to the cue part.

    - (violet):Add a phaser recipe to the cue part.

    - : Delete the selected step or recipe.

    - :Open a temporary recipe editor pop-up for the recipe linethat was last selected.

- To automatically set the focus to another cell after selecting a value, enable Auto Focus to Next Cell in the settings.
  Auto Focus to Next Cell is disabled by default.

- To sort the recipe lines by attributes, enable Group by Attribute in the settings. The grid layout changes. One recipe
  line now corresponds to one attribute. Properties that correspond to the same step are grouped in a numbered Step header. Tap the arrow on the leftof the header to unfold or collapse the group and display more or less columns for the step. By default, the group is collapsed.

- Properties that correspond to the same attribute are grouped in a numbered Value Source header. Tap the arrow on
  the leftof the header to unfold or collapse the group and display more or less columns for the attribute. By default, the group is collapsed. If multiple attributes are active inone phaser step, the attributes and their corresponding values are displayed next to each other.

- To unfold or collapse the MAtricks columns, tap the arrow on the left of the MAtricks header. By default, the MAtricks
  columns are collapsed.

- MAtricks with only one property can be used in the MAtricks cell in the recipe with or without a reference to the pool
  object. The same is true for MAtricks that only remove MAtricks values, for example an MAtricks object with No Group, No Width, and No Wings.

MAtricks objects with more than one property are always referenced. They are indicated by in the pool object.

To use objects from the MAtricks pool without reference, tap the cell in the recipe grid and tap a pool object in the context area of the recipe editor. The value is applied to the cell but does not have a reference to the pool object.

To reference objects in the recipe, use the dropdown in the cell or assign the object to the cell using the command line. MAtricks that are set individually in the cells of the recipe override the values of the object.

- MAtricks values without a reference to a pool object are displayed in the bottom right of the MAtricks cell. This
  includes values that override the value of an object.

The properties are indicated by a combination of the axis and the first letter of the property, for example YF for Fade Y. If only values on the x-axis are set individually, the X is omitted, for example: W for XWings.

To remove all MAtricks values without a reference to a pool object, tap Clear Individuals in the selection drop-down.

- Objects that are referenced in the recipe can be edited in the recipe. To do so, type EditSetting in the command line
  and tap the cell in the recipe grid. The changes are stored in the object in the pool.

- Recipe templates can be set as values in the Values column in standard recipes.

- When adding a standard recipe line to an existing phaser recipe, the phaser recipe can be linked in the Values
  column. Tap and hold the values cell in the standard recipe line and select the phaser recipe in the Edit Values pop up.

When adding a phaser recipe line to an existing phaser recipe, the previous phaser recipe can be linked in the Shape column. Tap and hold the shape cell in the new phaser recipe and select the phaser recipe in the Edit Shape pop-up.

- To ensure a clean overview in the recipe grid, properties are merged into appropriate cells to reduce the lines that are
  displayed, for example FadeFromX and FadeToX are merged to FadeX. For more information see Changes.

- To set a range of values for a property that can have a range of values, select the cell and type in a range of values
  using Thru in the calculator, for example 20 Thru 60.

If a single value is set to a property that can have a range of values, the value is applied to From. If the property was set to a range of values before, the To value is reset to None.

The new properties and value ranges can also be addressed via command line.

Examples:

To set a range of 0 to 5 for FadeX, type:

User name[Fixture]>Set Cue 1 Part 0.1 Property "FadeX" "0 Thru 5"

To change only the starting value and set itto 4, type:

User name[Fixture]> Set Sequence 1 Cue 1 Part 0.1 Property "FadeFromX" "4"

- Added Edit Title Bar, FontSize, PresetReadoutMode, DataPool, Edit Recipe, and Clean Up to the window settings. For
  more information, see Recipes.

#### Added shape pool:

A shape is an object containing a single recipe that defines how values are transferred between steps over time. They can be imported and exported via the show creator.

Use shape objects in phaser recipes to quickly and easily determine curves and other values.

Shapes includes Transition, Width, Acceleration, and Deceleration values.

Additionally, Attributes, Speed, Measure, Adaptive Measure, Adaptive Width, and Adaptive XY Rotation can be set in the shape.

To edit a shape, tap Edit and tap the pool object or use the swipey commands or the command line.

To open the settings of the shape editor, press in the upper left corner of the editor.

To define a minimum width for the steps in a shape, go to the settings, tap Minimum Step Width, and set a value in the calculator.

Shapes that contain information about one or more attributes can be called into the programmer and output directly. The values that are set in the shape will be applied to the attributes that are defined in the shape for the current selection.

If a shape contains attribute information, the feature group indicator bar is displayed in the bottom of the shape. White squares indicate that values of attributes of the corresponding feature group are stored in the shape.

Shapes that are generic and do not contain attribute values do not have a feature group indicator bar. If a generic shape is called into the programmer, the values that are set in the shape will be applied to active attributes in the programmer with multi-step values.

There are 22 predefined shapes in the pool. Some of them are specific to an attribute, some are generic and can be applied to multiple or all attributes.

The 1D tab in the shape editor and the editor tab in the context area provide quick and easy access to a 1D layout of the attributes in the shape and Accel X, Decel X, Trans X, Width X, Value Absolute, and Value Relative for each step.

The blue grid in the 1D layout displays the width on the x-axis with bolder separating lines at 100 %. The step numbers are displayed in the center of each step.

To modify the curves, move the handles or change the values in the buttons. The curves of all enabled attributes are modified collectively. If there are more than two steps, the two selected steps are highlighted in gray.

Attributes are displayed as toggle buttons at the top. To edit a shape of an attribute, enable the corresponding button. To change attributes, use a two finger edit to open the assignment editor and select an attribute in the list.

To display the curves of disabled attributes ina darker green color, enable Show All Attributes in the settings. To hide the curves of disabled attributes, disable Show All Attributes.

Inaddition to the attributes, there are six buttons above the 1D layout:

- : Enable or disable all attributes.
- Show Step Values: If this button is disabled, the actual value range of the shape is displayed to span across the full
  height of the 1D layout. If itisenabled, the height of the 1D layout represents the fullavailable range of values.

- Attribute: Delete allenabled attributes from the shape.

- Attribute: Add an attribute to the shape.

- Step: Delete the selected step of a shape. The number of the step that is to be deleted isdisplayed in the button.

- Step: Add a step to a shape. The step isadded at the end of the phaser.

#### Added Shape keyword:

The Shape keyword addresses the shape pool using the command line.

Use thissyntax:

[Function] Shape ["Shape_Name" or Shape_Number]

Example:

- To store shape 21, type:
  User name[Fixture]>Store Shape 21

> **Hint:** Storing a shape deactivates programmer values.

### Presets

#### Improved in this release:

Presets were enhanced and they now provide a more consistent and efficient workflow for programming. A key improvement is the introduction of a more powerful Universal call mode, and the option to mark a value as universal. Any preset, even MAgic presets, can now be called universally, regardless of the data stored. When a preset is called universally and it does not have a universally marked value, the system prioritizes global values. If there are no global values, the system will use the first selective value it finds. Fixtures without stored data automatically receive values from the first matching global or selective value source.

Values are always stored to existing channels of real fixtures and for the usage of universal and global, the data is marked as global or universal. The universal data is indicated by two yellow markers in the upper right corner of the attribute values.

> **Hint:** Values that are marked as global and universal values are applied to channels that do not have stored values.

Handle preset modes (Selective, Global, and Universal) more flexibly and individually with the new setting Preset Mode.

Regardless of how presets were stored, the mode can be adjusted in presets at any time. For example, a selective color preset that contains information of one fixture can be called universally for any other fixture that uses the same color attributes, even in fixtures that use different color systems.

To set the mode for a single preset pool object, go to the edit setting pop-up of the preset and enable Settings in the title bar.

Swipe Preset Mode. The drop-down displays the following options:

- Selective (S):
  Changes the preset to a selective preset.

- Global (G):
  Changes the preset to a global preset.

- Universal (U):
  Changes the preset to a universal preset.

To speed up the workflow, Channel Filter was added to the store pop-up. It defines which values from which fixtures and attributes are stored into the preset.

The following options are the same as below the "Use Selection" in the Store Settings pop-up:

- Active For Selected:
  Stores all active attributes but only for the fixtures selected in the programmer. This is only available in the data source of the programmer.

- All For Selected:
  Stores all attributes of the selected fixtures.

- Active:
  Stores the values that are active in the programmer. This is only available in the data source of the programmer.

- All:
  Stores all attributes for all fixtures.

When Preset Mode Default is set in your store settings, the preset mode drop-down in the store pop-up now shows the preset mode of the destination preset object in <>, such as <Universal>. It also now includes a new ForceUniversal option, which stores the preset as universal discarding any existing selective or global data. When storing values as global or universal while there are two or more fixtures with different values, a pop-up appears to warn that you are trying to store non-matching values. Non-

matching values are a contradiction in the definition of Global and Universal. For more information see Preset Mode Conflict in Create New Presets.

#### Added option keywords /ForceGlobal and /ForceUniversal:

- /ForceGlobal adds global data to the preset that already contains selective data. Subsequently, selective data will be
  removed in the preset of fixtures of the same fixture type.

- /ForceUniversal adds universal data to the preset and sets its call mode to universal. Subsequently, selective data
  will be removed in this preset.

Use this syntax:

[Function] Preset ["Preset_Name" or Preset_Number] /ForceGlobal

[Function] Preset ["Preset_Name" or Preset_Number] /ForceUniversal

Known Limitation:

When using the Universal Preset for Default, Highlight, or Lowlight, the attribute channel of the destination fixture must have a value that is marked as universal in the preset. For example, if the RGB value must be 100, then it has to be stored as 100 and marked as universal for each attribute channel.

Another useful addition is combining the option keywords /Selective, /Global, and /Universal with the At command to callpresets into the programmer. To speed up the programming experience, at any time, regardless of the data stored, you can call a preset universally and store itto a cue. When changing or adding a universally marked value to the presets, the cues willbe updated accordingly.

You can decide how you want to call the preset regardless of the preset mode. This is very handy when you need to quickly and universally call a preset that was originally stored as selective. Afterward, you can stillgo back and change the preset mode or add selective data in other fixtures.

Example:

- To call the first color preset for fixture 1 universally, type:
  User name[Fixture]>Fixture 1 At Preset 4.1 /Universal

#### Improved embedded and referenced presets:

- Improved the calculation of embedded recipes when calculating embedded presets and their maximum chain length.
  For more information, see the Embedded Presets section in the help manual.

- Added a Depth column to the ListReference pop-up, displaying the actual chain length of referenced presets. For

more information, see ListReference Keyword. A warning icon ( ) appears in the corresponding preset object when the maximum depth limit is reached. If this limit is exceeded, updating these presets, for example using a TotalReferenceUpdate, is not guaranteed to work reliably.

#### Improved the universal fixture type:

- The Universal fixture type isno longer set as the required default fixture in new show files.The existing universal
  fixture type is now a customizable "Moving Head" fixture type in the Generic folder of the fixture library can stillbe manually added via Insert New Fixtures. This fixture type isuseful when patching fixtures, providing maximum

flexibilityin programming. Additionally, this provides an opportunity to have dedicated fixtures to hold universally marked channel values for the use in universal presets, similar to the old workflow with the universal fixture type.

- As the term Universal now relates specifically to the marked data inside a preset, the IDType Universal was renamed
  Generic. Multiple fixtures can now be set to the IDType Generic. For instance, fixtures based on the generic ID type may be used as dummy fixtures during preprogramming or to store global and universal values within presets.

> **Important:** Fixtures of the IDType Generic are not automatically selected when using SelectFixtures on a preset that contains global or universal data. For example, to select fixtures on a preset, clear the selection and tap a preset or SelectFixtures Preset 1.1.

When a preset contains only selective data for such fixtures, itwill stillget selected via SelectFixtures on the preset.

> **Hint:** Show files saved in version 2.3 or prior willreplace the IDType Universal with the IDType Generic.

- All fixture types can now be used in a universal way to easily transfer data to various fixture types in different show
  files. They behave just like the universal fixture.

To define specific fixture types as the preferred data holders of universally marked values:

1. Open the Patch menu and go to the Fixture Types tab.
2. In the Special Purpose column, set the fixture type to Universal.
3. Save and exit the patch. When the fixture that was used to create the universal values is no longer available, the
   software tries to move those universal values to the fixtures whose Special Purpose is set to Universal.

Known Limitation:

You should not store global and universal data to fixtures of the same fixture type.

We recommend storing universal data to generic fixtures.

### MIDI Show Control (MSC)

#### New in this release:

MIDI Show Control (MSC) is a way to remote control the system. To read more about MSC in general and the MSC command structure, visit https://midi.org.

grandMA3 devices can be controlled by other devices via MSC, and vice versa.

> **Restriction:** MSC is transmitted via MIDI 5pin cable. MSC viaethernet is not supported.

> **Important:** MSC uses the Remote user profile for remote input and output. For more information about user profiles, see Create User.

> **Important:** To determine whether MSC can be transmitted or received, adjust the MIDI Data Mode setting in the output configuration. The default is In & Out.

The MSC menu is located in Menu – In & Out – MSC.

The menu is divided into three areas (Input, Output, and Executor Mapping) with multiple input fields and a monitor field.

Input:

- Enable Input:
  The device can receive MSC from other devices.

- Input Device:
  Set the input device ID number.

- Input Group:
  Set the input group ID number.

- Input Data Pool:
  The input data pool islinked to the selected data pool of the remote user by default. This is indicated by brackets <> around the number. To set an individual pool ID, tap and hold Input Data Pool and use the calculator. To linkitagain, tap Link Remote in the calculator.

- Input Command:
  Select the command format toreceive MSC.
    - Extensions:
      Extensions command format (hex 00).

    - General Light:
      General lights command format (hex 01).

    - Moving Light:
      Moving Light command format (hex 02).

    - All:
      Alltype command format (hex 7F).

- Display Input in System Monitor:
  The system monitor displays accepted MSC messages that match with MSC input settings.

Output:

- Enable Output:
  Ifenabled, the device can send MSC to other devices.

- Output Device:
  Set the device ID number that MSC is transmitted to.

- Output Group:
  Set the group ID number that MSC is transmitted to.

- Output Data Pool:
  The output data pool islinked to the selected data pool of the remote user by default. This is indicated by brackets <> around the number. To set an individual pool ID,tap and hold Output Data Pool and use the calculator. To link it again, tap Link Remote in the calculator.

- Output Command:
  Select the command format to transmit MSC.
    - Extensions:
      Extensions command format (hex 00).

    - General Light:
      General lights command format (hex 01).

    - Moving Light:
      Moving Light command format (hex 02).

    - All:
      Alltype command format (hex 7F). All equipment should respond to this format.

- Display Output in System Monitor:
  The system monitor displays alltransmitted MSC messages.

- Output Executor:
    - Default:
      MSC commands go to and from the selected executors on the master station only.

    - Executor.Page:
      MSC commands are sent to a specific executor. The page and executor number must be separated by a "period" character (hex = 2E)

    - Executor Page:
      MSC commands are sent to a specific executor. The page and executor number must be separated by a "NULL" character (hex = 00).

- Send To:
    - Group:
      The station transmits MSC to the specified group number (1to 15).

    - Device:
      The station transmits MSC to the specified device number (0 to 111).

    - All:
      The station transmits MSC to allconnected devices.

Executor Mapping:

- Key Row 400 Start - Key Row 100 Start:
  The start index can be separately defined for each executor row. For example, tap Key Row 100 Start to open the calculator and set a value between 0 and 1 000 to define the starting point of the corresponding executor row. If multiple rows have the same input index value, the highest executor row willbe addressed. The priority of the other rows becomes secondary.

- Fader Row 400 Start - Fader Row 100 Start:
  The start index can be separately defined for each row of fader executors. For example, tap Fader Row 100 Start to open the calculator and set a value between 0 and 127 to define the starting point of the corresponding fader row. If multiple rows have the same input index value, the highest fader row willbe addressed. The priorityof the other rows becomes secondary.

Monitor:

- The monitor fielddisplays MSC data feedback.
- The messages inside the monitor are displayed indifferent colors depending on theirstatus. Incoming commands
  are displayed in yellow, transmitted commands are displayed ingreen.

- The system monitor window also displays MSC data. Use the buttons Display Input in System Monitor and Display
  Output inSystem Monitor to determine which data to display in the system monitor.

grandMA3 supports seven different command types:

- Go (01):
  This isthe same as the Go+ command in grandMA3. Itisusually followed by a cue number.

- Stop (02):
  This isthe same as the Pause On command in grandMA3. This can be followed by a cue number.

- Resume (03):
  This isthe same as the Pause Off command ingrandMA3. This willrestart a cue that was paused. If a specific cue is paused, the number of the cue willhave to be specified with this command.

- Timed_Go (04):
  This can be used to perform a Goto with a specific fade time. Use both, the time and the cue number, exactly inthat order.

- Set (06):
  Set can be used to set the position of faders. Use fader number and page followed by position. Adding an optional time in MSC standard time format allows you to fade the fader tothe given position at the given time.

- Fire (07):
  This can be used to trigger macros. The macro number has to follow the command. Only macro 1 to127 can be triggered. Macro 1 ismapped to FIRE 01.

Known Limitation:

The command type Fire (07) is only implemented for MSC input.

- Go_Off (0B):
  This command can be used to "Off" (disable) executors. This has to be followed by a cue number.

> **Hint:** In preview mode, the device does not transmit or receive MSC.

> **Important:** Without a specific number followed by a command, the selected object of the remote user is executed If the object islinked to the data pool and assigned to an executor. Ifno page isset in the input, the MSC Monitor will display page 0 which ismapped to the selected page of the remote user.

### Preview

#### Added in this release:

Preview mode enables the operator to preview objects without affecting the live show output. When activated, the programmer's content isisolated from the actual output. For example, the operator can run through a sequence in preview while the output stays unchanged.

> **Important:** Preview is enabled for all users that share the same user profile.This means that in a session with multiple users a separate user profile must be used ifone user wants to work in the preview environment while another user stays in the liveenvironment.

To preview a sequence or cue:

- Press Prvw and tap a sequence pool object.
- Press Prvw Sequ 1 Cue 5 Please.

Ifother objects are loaded in the preview environment before, they will be removed from the preview environment.

> **Hint:** Preview of a running sequence starts the preview playback on the running cue.

Once preview is enabled, you can add or remove objects from the preview environment.

To do so:

- To add or remove objects, press and hold Prvw and tap a sequence pool object.
- To remove objects, press Prvw Off Sequ 2 Please.

Orange flashing binoculars ( )in the pool object indicate the primary previewed object. This is the object that isselected in preview.

White flashing binoculars ( )indicate objects that are not selected but that are loaded in the preview environment.

Ifmultiple objects are added to the preview environment, by default, the primary previewed object isthe object that was added last.

Storing or updating objects in preview directly stores or updates them in the live environment.

> **Important:** Storing or updating sequences or cues can affect live output, for example if you update a running cue or a previous cue while tracking is enabled.

To switch between the preview environment and the live environment, double press Prvw. To leave preview, you can also press Prvw + Off.

When you enter preview, the preview environment opens to itsprevious state.

> **Hint:** The firsttime you enter the preview mode, you have to select a sequence or cue you would like tohave inpreview. Otherwise, the preview environment will be empty.

The following windows support preview mode and are visually indicated by an orange frame while preview isenabled:

- 3D Viewer
  The 3D viewer can either display the preview or the live output. To switch between the two, tap Follow Preview in the Misc tab of the 3D viewer settings. By default, Follow Preview is enabled in the 3D viewer.

- Align Bar
- At Filter
- Content Sheet
- DMX Sheet
  The DMX sheet can either display the preview or the live output. To switch between the two, tap Follow Preview in the Display tab of the DMX sheet settings. By default, Follow Preview is disabled in the DMX sheet.

- Fixture Sheet
- Layout Viewer
- MAtricks Editor
- Off Menu
- Phaser Editor
- Recipe Editor
- Running Playbacks
- Selection Bar
- Selection Grid
- Sequence Sheet
- sMArt
- Special Dialog
- Step Bar

The preview encoder bar is displayed in the same orange color as the frames around windows interacting with preview. It has two different modes - the preview preparation bar and the preview encoder bar that is displayed in the preview environment.

To access the preview preparation bar, press Prvw once.

It has two toggle buttons that are only available in the preparation bar:

- Transfer Selection: When enabled, it copies the live selection into the preview environment when entering preview.
- Transfer Programmer: When enabled, it copies live programmer values into the preview environment when entering
  preview.

As soon as you enter the preview mode by double pressing Prvw or preview an object, the preview encoder bar has the following controls:

- Object: Selects the primary previewed object using Encoder Wheel 1. Pressing the encoder opens a drop-down to
  select a primary previewed object. In this selection drop-down, sequences that are running in preview are indicated by a green arrow ( ) on the right.

- Cue: Selects the currently previewed cue using Encoder wheel 2. Pressing the encoder opens the Goto Cue po-up to
  select a cue.

- Copy Selection: Copies the selection from the liveenvironment into the preview environment.
- Copy Programmer: Copies data from the programmer of the liveenvironment into the programmer of the preview
  environment.

- Copy Playbacks: Copies active playbacks from the live environment into the preview environment.

- Clear Preview Environment: Removes allobjects from the preview environment.

- AutoStart: Selects an auto start mechanism for sequences
    - Off: When selecting multiple sequences, none willbe started.

    - Single: When selecting multiple sequences, it starts the last one. For example, Preview Sequence 1 Thru
      3 starts sequence 3.

    - Multi: When selecting multiple sequences, allof them will be started.

- <<<: Select previous cue.
- II:Pause current cue.
- > > > : Select next cue.
- <: Trigger Go-.
- :Trigger Toggle.
- > : Trigger Go+.
- Preview Bar: Toggles the preview encoder bar.

If a cue isselected, the sequence is displayed next to the encoders in the preview encoder bar.

Preview mode uses its own data pool located in Data Pool Object 128.

Allactions performed inpreview mode are displayed in the command line history.

> **Hint:** Command line feedback isnot displayed in the system monitor.

The master section is for live output only.

Using highlight, lowlight, and solo while you are in preview only affects the preview environment, not the live output.

#### Added in this release:

Added the option keywords /AutoStart, /TransferProgrammer, and /TransferSelection.

- /AutoStart option keyword automatically starts your sequence in the preview.
- /TransferProgrammer keyword transfers data from the programmer of live environment to preview environment.
- /TransferSelection keyword transfers the selection from live environment to preview environment.

Use this syntax:

Set UserProfile ["UserProfile_Name" or UserProfile_Number] Property ["Property_Name"] ["Option_Value"]

### Improved MVR and Partial Show Read

> **Important:** MVR integration is now part of the Show Creator / Partial Show Read. For more information see the "New in this release" section below.

> **Important:** Exporting MVR fileswas integrated into the Export dialog in the patch menu. For more information see the section "Improved inthis release" further down.

In thisrelease, multiple features were added to improve the overall handling of fixture types. Especially, the import and export of fixturetypes was restructured for them to be handled, edited, integrated, and reused easily in different show files.

Additionally, multiple bugs were fixed regarding MVR import, export, and GTDF filehandling. For more information, see Bug Fixes.

#### New inthis release:

Partial Show Read supports MVR integration. To open the PSR menu, press Menu – Show Creator – Partial Show Read. Then tap MVR in the top right corner of the menu. Select between User, and Demo MVR files.

To check all boxes, tap Check All.Fixtures and Group Objects are checked by default. The following listof MVR object types can be selected individually:

- Fixtures
- Group Objects
- Scene Objects
- Focus Points
- Supports
- Trusses
- Video Screens
- Projectors

    > **Important:** MVR import via Partial Show Read clears the programmer.

- GDTF and MVR import can be canceled by pressing and holding MA + ESC or Shift + ESC for fiveseconds.
- Additionally itispossible to set an MVR object type foreach fixturetype to define the object type of a fixture when
  exporting as MVR. Open the patch menu, then go to Fixture Types. Tap and hold the cell in the MVR Object Type column of a fixture type and select a type from the drop-down.

- MVR in grandMA3 now supports multipatch fixtures.

#### Improved in this release:

- Itis now possible to exchange fixture types directly in the PSR Prepare menu. Tap and hold the cell in the Fixture
  Type (PSR Patch: Left side only) column of the fixture you want to exchange or select multiple fixtures and then tap and hold. This opens the Insert New Fixture Type pop-up of the patch menu so you can select a fixture type from the Show or Library tab. Select a fixture type and tap Select. The fixturetypes are now exchanged in your PSR patch, indicated by cyan font in the Fixture Type column. if you previously selected a fixture type in the Show tab, the column displays "Local". if you selected one in the Library tab,itdisplays "New".

- To easily detect matching fixtures where only some of the data differentiates fora single property in the PSR patch,
  the data that changed is now highlighted inorange text in the cells on the left side.

- Added GUID, Position and Rotation columns to the grid of the PSR Patch dialog.
- A separating linewas added in the listbetween matched and unmatched fixtures.

- Added and tothe PSR Prepare menu, to partially import patch data. The properties Patch, Position, and
  Rotation can be individually imported. Tap on a single property of a fixture or select multiple properties. Use and between the two patch areas to define which properties will be used:
    - : Use the selected properties in the resulting patch.
    - : Remove the selected properties from the resulting patch.

- Improved the buttons between the two patch areas that define which fixtures will be used in the resulting patch:
    - : Use the selected fixtures in the resulting patch.

    - : Use the fixtures from the opposite patch in the resulting patch.
    - : Remove the selected fixtures from the resulting patch.

- Added Use PSR Patch Column (adds data of the patch column to the resulting patch) and Use PSR Position/Rotation
  Columns (adds data of the position and rotation columns to the resulting patch) buttons on the left side of the menu.

- The matchmaking of the configuration lines has changed. The order for comparison isnow FID → CID → GUID →
  Name.

- If you want to perform a partial show read and want to keep fixtures from both sides with the same FID, CID, Name,
  and UUID, tap and hold the cell in the GUID column of the fixture in the PSR Prepare menu. in the selection pop-up, tap New to give the fixture a new UUID. You can now apply PSR.

- Added Auto Scroll to the title bar of the PSR menu. If itisenabled and you add or remove fixtures from the resulting
  patch, the focus jumps to the new position of the selected fixtures in the grid. Ifitis disabled, the focus stays in the current position. By default, Auto Scroll is enabled.

- The export settings for MVR files were integrated into the Export option within the patch menu. As a result, Export
  MVR was removed from the patch menu.

In the patch, tap Export to open the patch export pop-up. The export type is categorized into two options, grandMA3 and MVR, with MVR selected by default. The Export options are displayed on the right: Entire Patch exports all fixtures in the patch. Selected Fixtures exports only the fixtures that are currently selected. The export file name can be defined in the Name field. <Default> will automatically generate a name depending on the selected fixtures. Tap Export to initiate the export process and generate the MVR file. Tap Delete to remove the currently selected file from the list. For more information, see My Virtual Rig (MVR).

- Added the option keyword /MVR to export the patch as MVR file instead of a grandMA3 XML file. Use this syntax:

Export [Object] ["Object_Name" or Object_Number] (If Drive ["Drive_Name" or Drive_Number]) /MVR

### Phone Tethering via USB

#### New in this release:

You can now connect tothe world server on grandMA3 consoles viaUSB tethering. Enable USB Network in theStation Control settings on grandMA3 consoles. Connect a mobile device that supports phone tethering via USB or alternatively a router through aUSB ethernet adapter. Connect the device tothe console viaUSB port.With mobile devices, make sure toactivate phone tethering on your mobile device after connecting. Once enabled, the USB Network connection islisted inMy Interfaces in the network menu.

> **Restriction:** Phone tethering is only supported on devices that are compatible with Android™ and Apple®. We do not guarantee compatibility with allmobile devices.

## 2. Other Enhancements

#### Updated predefined content:

- Updated demo shows:
    - Demoshow_grandMA3
    - MA_StartShow
    - Simple_Show
- Updated the predefined MVR demo stage.
- Changed the default render qualities in the render qualities pool. The new defaults are No Beam, Line, Low, Standard,
  High, and Ultra. By default, Standard is selected in a new show.

- New predefined macros
- New predefined filters
- New predefined symbols
- Added predefined phaser recipe presets.
- Updated predefined phaser presets.
- Added predefined shapes.
- Improved the Sequence Sheet view of new shows.
- Group By ID Type is enabled by default in the fixture sheet settings.

#### Improved tags:

- The tags pool now has Pool Action. Pool actions can be set up per tags pool or individually per object.
- You can assign tags as layout elements in the layout viewer.

#### Improved pools:

- Added First Index to the pool settings of presets and the following pools: Filters, Groups, MAtricks, Sequences,
  Shapes, and Worlds.
    - Set values between 1 -9999 to define where a pool object should be stored. An individually defined first
      index is indicated by >=x in the top leftcorner of the corresponding pool. For example, setting First Index to 195 in the sequence pool and then executing Store Sequence will create a pool object at slot

195. If the slot isoccupied, the next free slot will be used instead.

- FirstIndex can be set up per user profile.

#### Improved MAtricks:

- Linked and unlinked shuffle modes now work incombination with Rx, Ry, and Rz:
    - Rx, Ry, or Rz are toggled on: Only existing grid positions on the selected axis are taken into account.
    - Rx, Ry,or Rz are toggled off: The entire range on the axis is taken into account.
    - Linked: Fixtures that are located on the same point of the selected axis are triggered at the same time.
    - Unlinked: Parallel lines are shuffled independently to each other.
- The value 0° is now available as a predefined input option for phase values.

- MAtricks objects with more than one property are indicated by in the pool object.

#### Improved presets:

- The new recipe context area isdisplayed in the lower part of the preset editor. To access the recipe editor settings,
  tap in the top left corner.

Read more about the context area and new recipe editor settings in Features.

- Removed Auto in Preset Modes of the Store Settings pop-up. Read more about presets in Features.
- If a recipe is stored into an empty preset, the preset mode automatically changes to Selective.
- Added Recipe Mode to the Store Settings pop-up, when storing recipes into presets. The options are:
    - Normal: Stores recipe presets with the selected fixtures in the programmer.
    - NoSelection: Stores recipe presets without the selection.
      To store a recipe without selection via command line, use this syntax: Store ["FeatureGroup_Name" or FeatureGroup_Number] /Recipe "NoSelection" Known Limitation:

If a preset contains a recipe, Edit and Recast Preset are not available and grayed out in the preset editor.

#### Improved patch:

- Added Same as FID in the calculator when editing a CID cell.
- Added Same as CID in the calculator when editing a FID cell.
- Added Suggestions tab with a number of suggested values in the calculator in CID and FID.
- Added Invert 3D as a column in the patch. Set the subcolumns Pan and Tilt to Inverted to visualize a pan and tilt
  inversion in the 3D viewer.

- Fixtures with Master React set to None are now indicated by a gray bar in the top left corner of the IDType column in
  the programmer.

#### Improved the fixture types editor and the DMX mode editor:

- Added Columns to the title bar of the fixture type editor and the DMX mode editor to filterthe number of columns
  that will be displayed. There are three different modes:
    - Condensed: Displays only essential columns for a better overview, DMXModes and Revisions tab.
    - Full:Displays allcolumns that can be used in the grandMA3 software, and all tabs except the Protocols
      tab.

    - Extended: Displays all columns of allsettings and features of a fixturetype, and alltabs.

- For multi instance fixture types, geometry references can link to a model which overwrites the model of the
  referenced geometry. This can be edited in the Geometries tab of the fixture type editor.

#### Improved playbacks window:

- Added Display Mode as a new setting of the Playback window, Xkeys window, and Custom Master Section window.
  The options are:
    - Text+Icon: The icon of the function is displayed in the background of the executor, the function is
      displayed in text on top of the icon.

    - Text: The function is displayed in text on the executor.
    - Icon: The icon is displayed on the executor.

- The mini encoders in the playbacks window display the icon of assigned functions, ifencoder left or encoder right,or
  MA + encoder leftor MA + encoder right is assigned.

#### Improved 3D visualization:

- 3D now visualizes continuous pan and tiltrotation when using the attributes PanRotate and TiltRotate.
- Itis now possible to assign appearances to materials of meshes.
  To do so:

1. Tap mesh object and swipe to edit it.
2. in the listof materials in the column Appearance, tap and hold the cell to select appearance.

Such appearances can either be a color, an image, or a video. These appearances are, inturn, visualized in the 3D. Ifan appearance isselected, the values of the Texture Name and Color columns willbe removed and display "Replaced by Appearance".

- The color of materials can also be edited. in the listof materials in the column Color, tap and hold the cell to open the
  color editpop-up. Tap Ok in the title bar to save the color you changed.

- Itis now possible to overwrite materials with appearances inindividual fixtures in the 3D viewer. The selected
  appearance is visually applied to the fixturein the 3D viewer instead of the material that is defined in the fixture type itself.

To set a material for an individual fixture:

1. Open the patch.
2. in the column Material Overwrite, tap and hold a cell.
3. in the dropdown, select an appearance to be used as a material in the fixture.

- Added Show Environmental Label to the settings of the 3D viewer. Show Environmental Label relates to Show Label
  on Body. When itis enabled, labels of environmental fixtures are displayed. Show Environmental Label is disabled by default.

- Added Follow Preview to the Misc tab of the 3D Viewer window settings. When Follow Preview is enabled and you
  are in preview, the output in preview isvisualized. When Follow Preview is enabled and you are not in preview, the live output is visualized. When Follow Preview is disabled, the liveoutput isalways visualized, even if you are in preview.

#### Improved the selection grid:

- The two different position modes (Perspective; Planar), which define how the selected fixtures are positioned in the
  selection grid, can now be addressed using the command line.

Known Limitation:

At the moment, these two commands will not work if subfixtures are selected.

- This is the general syntax forpositioning the selected fixtures in perspective mode: Grid "Perspective"
  Camera ["Camera_Name" or Camera_Number]

- This is the general syntax forpositioning the selected fixtures in planar mode: Grid "Planar" Camera
  ["Camera_Name" or Camera_Number]

- Small icons in the upper left corner of the Selection button in the encoder bar display the axis and the selected Move
  Grid Cursor setting in the selection grid.
    - x-axis
    - y-axis

    - z-axis

    - None
    - Append X

    - New Line

#### Improved executor configuration editor:

- The new editor allows you to customize executor configurations and is similar to the handle tab in the assign menu.
- The buttons on the left side of the menu always come in pairs and represent a fader/encoder and key executor. This

is indicated by the icons in the upper left corner of the buttons ( / ). An executor configuration can be loaded to any type of executor. Depending on for which type of executor (encoder, fader, or key) the configuration is used later, the functions set in the editor are loaded to the executor. For example, when encoder left/right are defined, and used later on an executor in row 200, the fader would have an empty assignment.

- Select a fader/encoder or key executor on the left side of the editor, to edit its trigger options and functions on the
  right side of the editor.

- Tap Recast in the title bar to recast the executor configuration. For more information, see Recast Keyword. List
  Reference opens the list reference pop-up.

- Enabling Settings in the title bar displays the following options below the title bar:
    - Name
    - Scribble
    - Appearance
    - Tags
    - Note
    - Width: Edit the width of the executor configuration.
    - Height: Edit the height of the executor configuration.

        > **Hint:** The width and height define the scale of a new executor when using the configuration. Itis possible to increase the width and height of the configuration and edit the functions for additional executor button and decrease itagain in the editor. When loaded to an executor and the executor is expanded later, allinformation of the assigned functions willbe loaded.

    - ExecConfigType: Select an ExecutorConfigType as a preference for which object type you want to use
      the executor configuration. Functions that cannot be used with the selected type are grayed out in the list below. However, itis stillpossible to assign itto executors of different object types.

- Added Learn Mode as setting to speed masters. It can be accessed in the UI via the Edit Setting tab of the assign
  menu. Itdefines how Learn and LearnSpeed react. There are three different values:
    - Default: The speed scale isnot taken into account.
    - Learn Respects Speed Scale: This takes the value set in SpeedScale into account. Example: Tapping a
      speed of 60 BPM with a speed scale of Mul2 results in a speed of 120 BPM.

    - Auto Increase Speed Scale: Tapping a high BPM value over 225 BPM automatically increases the
      SpeedScale value.

> **Hint:** Default matches the behavior in version 2.3. Learn Respects Speed Scale is enabled in show files that were saved in version 2.2 or prior. This matches the behavior in these versions.

#### Improved executor configurations:

- Added the possibility to define default executor configurations for Timing Masters and Selected Masters. With the
  separation of Selected Masters and Grand Masters, the previous Master setting was renamed GrandMaster.

- Added Selected Master, Grand Master, and Timing Master to the Masters section of the Executor Config. tab in
  Preferences and Timings.

#### Improved assign menu:

- Tapping an empty executor in the handle tab creates a new empty executor and the assign menu switches to the
  object tab.

- Executors with a custom command assigned to them are displayed with a specific icon ( ).
- Extra trigger options for executors, for example MA + release key, will only be displayed on the left side of the
  Handle tab if a function is assigned.

- When only the encoder or key trigger option is used, without the MA trigger option, then the trigger option remains
  accessible when pressing MA.

- For the 300 and 400 row executors, if no function is assigned for MA + encoder, the encoder resolution step size can
  still be adjusted separately as a second encoder resolution step size for the normal encoder. It can be triggered by turning the encoder while pressing MA. This is useful for having a coarse and fine resolution for the same encoder, for example.

- Added Fix Executor to the title bar of the handle tab. When enabled, it latches the executor to the current page, same
  as using the Fix Keyword does.

- The executor is also displayed in the resulting command, if Add Executor is enabled when using the custom
  command section.

- Secondary functions can be assigned to executors. For example, press Assign + Go- , and then press and
  hold MA and tap an executor. This is also possible via command line using the option keyword /MA, for example Assign FaderTemp Page 1.301 /MA.

#### Improved message center:

- The design of the message center was separated into two tabs, Messages and Statuses.
- The temporary message and status center opens in the tab or listof messages that was opened last.
  The message center window opens in the tab or listof messages that was stored.

- Added settings to the message center window:
    - To hide the Messages tab bar on the left side of the message center window disable Tabs.
    - Swipe Tab and select a tab (Messages or Statuses) that you want to display.

- Added Confirm All in the title bar of the messages section. Tap this button to confirm allmessages in the
  message center at the same time.

- was added to the title bar of the message center. Select a display in which you want to display the message
  center.

- The notification type is displayed as text next to the bell icon ( ) in the upper left corner of the cell.

- Messages can be confirmed by tapping in the upper right corner of the cell.The icon isonly displayed if there
  are new messages in that category.

- The notification pop-ups have a new button Confirm Message to close the pop-up and at the same time confirm the
  message in the message center.

- By default, messages of the Information column are displayed as confirmed.
- The timestamp of the latest message is displayed in the lower right corner of the cell in the main page of the
  message center. The date and time is displayed in the format dd.mm.yyyy hh:mm:ss.

- To open a list with all messages, tap All in the upper left corner.
  To open the list of messages for a category or priority, tap the header of the category or priority.

- The list of messages displays information about Time, Sender, Category, Priority, and the message itself. The
  Sender column displays the name and IP of the device that sent the message.

To filter the list of messages, use the yellow filter row below the header row. Undefined displays messages that are not part of any category or priority. For more information see Temporary Filtering.

- The width of the time, category, priority, and message column in the list of messages of a category can be adjusted.
  To do so, tap and drag the separating line in the title bar of the list.

- To display a message in full below the list of messages, enable Full Message on the upper right side below the title
  bar. To change the height of the display area for the full message, drag the separating line.

- Select All and Select None were added in the upper right corner of the messages list, below the title bar.
  To select all messages in the list, tap Select All.

To deselect all selected messages in the list, tap Select None.

- Confirm Selection, Unconfirm Selection, and Delete Selection were added to the bottom of the messages list.
  To mark all selected messages as read, tap Confirm Selection. Confirmed messages are still displayed in the list, the background changes from opaque to transparent.

To mark all select messages as unread, tap Unconfirm Selection. Unconfirmed messages are still displayed in the list, the background changes from transparent to opaque.

To delete all selected messages, tap Delete Selection. Deleted messages are no longer displayed in the list.

> **Restriction:** Itis not possible to oops these actions - confirm, unconfirm, delete.

- Messages can be confirmed using the command line.
  Call MessageCenter "Category.Priority"
    - To confirm all messages, type:
      User name[Fixture]>Call MessageCenter

    - To confirm all messages in MA-Net, type:
      User name[Fixture]>Call MessageCenter "MA-Net."

    - To confirm all messages with the priority Warning, type:
      User name[Fixture]>Call MessageCenter ".Warning"

    - To confirm all messages that have both the category Power and the priority Error, type:
      User name[Fixture]>Call MessageCenter "Power.Error"

- Information messages are already set as confirmed and do not need to be confirmed by the user.
- Enabling Local Settings in the Backup menu when loading a show filekeeps the local messages, and vice versa.
  Disabling Clear Local Settings when creating a new show keeps the local messages and vice versa.

- Message center settings are defined per user.
- USB and Chat messages are only shown on the local device.
- Messages with the priority Alert are set to notification type Notification by default.
- Incase of power loss, the message pop-up informs the user about missing power supply.
- Warning, error,and alert messages flash while they are displayed. In contrast, information messages remain static
  and do not flash.

- Messages are stored in the show filewhen saving a show fileand loaded when loading a show file.

#### Improved status center:

- The status center is now located in a separate tab called Statuses. To open it,tap or certain status icons, then
  tap Statuses on the left side of the window.

- The icon and title bar of a status light up in the corresponding color If the status isactive.
- Added an icon for the status source My:
- The preview icon is now displayed in the same orange color as windows and objects when preview isactive.
- Swiping a status in the status center offers a new category in the drop-down called "Blink".
  The options are:
    - None: The background of the status in the command linedoes not blink when the status is active.
    - Once: The background of the status blinks red once when active.
    - Always: The background of the status blinks red continuously when the status is active.
        > **Hint:** For the statuses Highlight, Blind, Solo, Grand Master, World Master, and Disk Space "Blink" is set to Always by default.

- Tap the Grand Master, World Master, or Grand Rate status icon in the command line to open the temporary Master
  Controls.

- Improved Battery status: When a device runs in battery mode, the system now clearly differentiates between the
  battery status of your own device and those of other devices in the session. Depending on the configuration, the label beneath the status icon will show either "My", "My+Ext", or "Ext" to indicate which device is affected. The tooltip provides further information.

- Added new statuses to the status center:
    - No Fixtures Patched ( ): No fixtures are patched in the current show.

    - Encoder Bar ( ): A different encoder bar and not the default encoder bar is selected.

    - Grand Master ( ): Grand master is not at full.

    - World Master ( ): World master is not at full.

    - Grand Rate ( ): Grand rate master is not at 1:1.
    - Patch Open ( ): Another user is in full patch.
    - Added the section Hardware. This section includes the status Battery and the following statuses:
    - USB Network ( ): USB network is active. This status is not available in the onPC software. For
      more information, see USB Network in Features.

    - ShowData ( ): Previously named Memory.

    - CPU ( ): Displays the CPU usage as a percentage below the status icon in the command line.
    - Memory ( ): Displays the memory usage in MB below the status icon in the command line.

    - CPU Temperature ( ): Displays the CPU temperature in °C below the status icon in the
      command line.

    - GPU Temperature ( ): Displays the GPU temperature in °C below the status icon in the
      command line.

    - Fan Speed ( ): Displays the fan speed as a percentage below the status icon in the command
      line.

    - Disk Space ( ): Displays the available free space in GB of the HDD below the status icon in
      the command line.

#### Improved timecode:

- The Note and Appearance columns are hidden by default in the Timecode Viewer and Timecode Editor.
- Timecode slots were expanded to 16 (previously 8).
- Added Toggle as a pool action to the timecode slot window settings to toggle timecode slots on and off.
- Removed Toggle Pause and Toggle Off as values of the pool action setting.

- Added Restart Option to the settings to choose a mode for Toggle.
  The options are:
    - Continue: When a stopped timecode restarts, it willcontinue to run.
    - Reset: When a stopped timecode restarts, itwillbe reset from the start.

#### Improved timecode slot pool:

- Added Restart Option to the settings to choose a mode for Toggle.
  The options are:
    - Continue: When a stopped timecode slot restarts, it willcontinue to run.
    - Reset: When a stopped timecode slot restarts, itwillbe reset to the generator start time.

#### Improved the DMX Protocol Art-Net:

- The Art-Net menu now has a tab called Timecode. In Timecode itis possible to set 16 Art-Net streams with different
  stream IDs to send and receive up to 16 timecodes in parallel.

#### Improved Lua:

- The Lua Core has been updated to Lua v5.4.8.

#### Added an Oops window:

- To open the new Oops window, open the Add Window dialog and go to the More tab. The window is similar to the
  oops menu. For more information, see Oops Menu.

#### Improved layouts:

- If you enable Setup mode in a layout in the layout viewer, the object will be locked using object ownership. This
  is indicated by a red lock icon in the pool object.

- Selecting group elements in setup and linear mode will occupy a grid position in the selection grid for better
  calculation.

#### Improved color picker:

- Added swatch books to the color picker for color inputs, for example the border color of layout elements.
  To select gels in the swatch book, click Book in the title bar of the color picker.

- The swatch book opens to the last selected gel.
- Improved color selection If the fixture has a color wheel.

#### Improved network:

- Added MSC Input and MSC Output to the Session Control menu.
- QR codes have been added to the Web Remote tab inside the Network menu. For each network interface with an
  assigned IP address, a unique QR code is generated, allowing quick access via mobile devices scanning. Network interfaces without an assigned IP address and Loopback IPs will not be generated as QR code. If an interface has no link connection, the QR Code is shown in red. For more information, see Interfaces and IP. Menu "WebremoteView" opens a resizable pop-up showing the QR Codes. The maximum height of QR codes is 480 pixels, so they perfectly fit on small screens, for example, the grandMA3 onPC rack-unit.

- The web remote Resolution Limit has been adjusted per device:
    - grandMA3 consoles: 1440p
    - grandMA3 onPC command wing XT and grandMA3 onPC rack-unit: 4k
    - grandMA3 onPC: Unlimited

#### Improved DMX Remotes

- Added Trigger On Session Change column to the DMX remotes menu.
  IfTrigger on Session Change is set to Yes, the target istriggered every time the DMX calculation of the session changes. This includes, for example, the startup of a console or adding a processing unit to the session. This is valid as long as the DMX address iswithin the range of values between Trigger On and Trigger Off. This means if Trigger On is set to 0, the target istriggered even if there isno external DMX signal.

IfTrigger On Session Change is disabled, a change in the DMX calculation willnot trigger the target.

> **Hint:** Trigger On Session Change is set to Yes in show files that were saved inversion 2.3 or prior. This matches the behavior in these versions. In new show files,Trigger on Session Change is disabled by default.

#### Improved masks:

- Executing Store on an empty mask button in the mask toolbar creates a new filterin the filterpool.

#### Improved agenda:

- Added per column filtering. For more general information, see the Temporary Filtering topic.
- Added Delete Old button in the title bar in setup mode. Tap to delete outdated agenda entries.

#### Improved attribute definitions:

- Temporary filtering is now available for all tabs in the attribute definitions.

#### Improved Add window dialog:

- Added Recipe Editor to the Common tab.

#### Improved DMX sheet:

- The setting Level Bar has a new option Programmer. IfProgrammer isselected, values in the DMX sheet are
  visualized in the same colors as in the programmer.

- Added Follow Preview to the window settings of the DMX sheet. When enabled, itdisplays the output inpreview.
  When disabled, itdisplays the liveoutput. The function is disabled by default.

#### Improved sequence sheet:

- Added Recipe Preset to the Mask tab of the sequence sheet settings. This defines how recipe presets are displayed
  in the sheet:
    - Name:
      Displays the name of the preset.

    - ID:
      Displays the ID number of the preset.

    - ID+Name:
      Displays the ID and name of the preset, for example "1. 1 Closed".

ID+Long Name:

Displays the ID and long name of the preset, for example "1 Dimmer. 1 Closed".

- Added "cmd" as an indicator in the bottom right corner of the name cell for cues and cue parts If a command isset
  and enabled in the cue or cue part.

#### Improved the resizing of info window pop-ups:

- Double-tap the title bar to resize the pop-up to the largest possible size on the screen.

#### Improved displayed text:

- Ifan object has a note with more text than can be displayed in the fieldor column, an ellipsis[...]isadded at the end
  of the displayed text.

- The text on pool objects only shrinks a littlebit,then cuts off the end of the label, and an ellipsis [...]isadded at the
  end of the displayed text.

#### Improved sheets:

- The state of expanding ( )or collapsing ( )columns in sheets, for example in the recipe editor, isnow
  remembered.

- Ifcolumns are expanded by tapping ,the firstexpanded column is scrolled into view.
- Objects and values that are referenced in a cellcan be edited directly in the corresponding sheet. To do so, type
  EditSetting in the command lineand tap the cellin the grid. The changes are stored in the source, for example the object in the pool.

Improved the speed of the total reference update mechanism due toparallel updating multiple objects.

Unified the UI of several window settings, for example for the Xkeys, MAtricks and message center window.

#### Added /Recursive option keyword tothe Lock keyword and Unlock keyword:

Using /Recursive in combination with the Lock keyword or Unlock keyword allows you to define which levels of objects you can lock or unlock.

Examples:

- To only lock data pool 1, type:

```
User name[Fixture]>Lock     Datapool   1
```

- To lock allchildren within data pool 1, type:

```
User name[Fixture]>Lock     Datapool   1 /Recursive
```

Requirement: Lock at least two levels of objects.

- To unlock sequence 1 with all itscues but to keep cue parts locked, type:

```
User name[Fixture]>Unlock      Sequence   1  /Recursive  1
```

## 3. Changes

- New keywords:
    - MessageCenter
    - MyRunningPlayback
    - NShot
    - RunningPlayback
    - Shape
- New option keywords:
    - /AutoStart
    - /ForceUniversal
    - /MA
    - /MVR
    - /Recursive
    - /TransferProgrammer
    - /TransferSelection
        > **Hint:** For more information about the new keywords, please read the corresponding sections above.

- New color theme colors:
    - ColorDefinitions:
        - PoolDefault.Shape
    - Colors:
        - Assignment.Shape
        - Assignment.Tag
        - DBObjectGrid.MergedParentSeparator
        - FixtureSheetCell.BackgroundActiveIntegratedNShot
        - FixtureSheetCell.BackgroundActivePresetNShot
        - FixtureSheetCell.BackgroundActiveValueNShot
        - FixtureSheetCell.TextProgValueNShot
        - FixtureSheetCell.TextSelectedPlaybackNShot
        - Global.Preview
        - MessageCenter.NewInformationBackground
        - PoolWindow.Shapes
        - ProgLayer.BackgroundActiveNShot
        - ProgLayer.NShot
        - PSR.DifferentText
        - RecipeEditing.ContextBackground
        - RecipeEditing.CurveBackground
        - RecipeEditing.CurveLine
        - RecipeEditing.PhaserRecipe
        - RecipeEditing.PhaserRecipeMergedBack
        - RecipeEditing.PresetRecipe
        - StatusCenter.Blink
        - StatusCenter.Button
        - StatusCenter.Preview
        - User.AFK
        - User.LoggedIn
        - User.LoggedOut
- New grandMA3 Lua Functions:
    - CmdlineIndex(light_userdata:handle): integer:index
    - CompareHandle(light_userdata:handle): bool :equal

    - CompareImages(light_userdata:image a,light_userdata:image b,light_userdata:image diff out):
      integer:differing-pixels

    - CurrentDataPool(nothing): light_userdata:handle
    - CurrentObjectSelection(nothing): light_userdata:handle
    - GetPresetDataFast(light_userdata:preset_handle[, boolean:phasers_only(default=false)[,
      boolean:by_fixtures(default=true)]]): table:phaser_data

    - GetTargetList(light_userdata:handle): {light_userdata:target_handle}
    - GridGetFirstSelectedObject(light_userdata:handle to UIGrid (or derived)): light_userdata:handle
    - IsRunningPlayback(light_userdata:handle): boolean:result
    - UndoDisable(nothing): nothing
    - UndoEnable(nothing): nothing

- Miscellaneous:
    - In Connector Configuration, the new default for MIDI Data Mode in alldevices is In & Out.
    - Renamed the values of Executor Display Mode in the sequence settings Data; Appearance; Data and
      Appearance

    - Renamed column Last 1m/5m/10m in the network menu → previously Per 1m/5m/10m
    - Renamed property KeyAddExecutor → previously KeyAddExec
    - Removed Import MVR from patch menu. The MVR import is now part of Partial Show Read menu. For
      more information, see Features.

    - Removed Export MVR from patch menu. Exporting MVR files was integrated into the Export dialog in the
      patch menu. For more information, see Features.

    - Renamed attribute definition VideoKeyColor_B → previously VideoColorKey_B
    - Renamed Standard Recipe → previously Recipe
    - Renamed property Selection instandard recipes (previously named recipes) → previously GROUP
    - Removed Toggle Pause and Toggle Off as values of the pool action property of the timecode slot pool.
    - Changed the default render qualities in the render qualities pool. The new defaults are No Beam, Line,
      Low, Standard, High, and Ultra. By default, Standard isselected ina new show.

    - Renamed priority Information in the message center → previously Spam
    - Renamed shortcut /Mat of the /MAtricks option keyword → previously /Ma
    - Renamed shortcut Act of the ActivationGroup keyword → previously Ac
    - Renamed shcortcut Cal of the Call keyword → previously Ca
    - Renamed shortcut Channelf of the ChannelFunctionDefault keyword → previously Chann
    - Renamed shortcut Scr of the Scribble keyword → previously Sc
    - Removed shortcut Se in the Set keyword. The Set keyword no longer has a shortcut.
    - Added the Recipe Editor tothe Common tab of the Add Window pop-up.
    - Renamed Generic keyword → previously Universal keyword.
    - Renamed ID Type Generic → previously Universal.
    - For standard recipes, properties that define a range were combined: - Speed → previously Speed From and Speed To - Phase → previously Phase From and Phase To - Delay→ previously Delay From and Delay To - Fade→ previously Fade From and Fade To
      For more information on setting values for properties that allow ranges, see Features.

## 4. Bug Fixes

### 3D

#### Description

Fixtures that are used with gobo position shake enabled could show artefacts on grandMA3 consoles.

if you used the Calibrate Position tool,the values would not update properly when using the calculator.

The calculators in the Edit Camera pop-up did not display a value range in the title bar.

In the 3D viewer, the 3D stage could disappear when changing attributes in the patch.

In the 3D viewer, when fixtures were rotated on the Y axis and used grandMA3 default meshes, the yoke and lens would set off tothe base and head with the greatest offset at 45°.

Reset Properties in the 3D position settings in the patch did not work.

Setting Multi LED Beam Mode to Single Beam Dynamic Gobo in the Render Qualities settings did not work as expected. Outer pixels were on, but the lightbeam would not render.

A number of show fileshad a memory leak when the 3D viewer was open.

if you deleted allrender qualities, the software would crash. Now, if you delete allrender qualities, a new render quality is created automatically.

A color wheel selection was only visualized in the beam but not on geometries. They were still visualizedin white.

if you set a value for Rot X, Rot Y, or Rot Z using the calculator with the 3D viewer insetup mode and rotation mode set to Group, the fixtures would rotate around their own axis as ifrotation mode was set to Single.

The software could crash, when you opened the 3D window with a grouping fixture as a subfixture of another fixture.

If MultiLed Beam Mode of a render quality was set to Single Beam Dynamic Gobo or Mean Color, the direction of rotated beams was wrong.

### Command Line and Macro

#### Description

EncoderBank X At Y would only apply to one attribute.

Park EncoderBank X and UnPark EncoderBank X would only park or unpark the firstencoder page of the respective encoder bank.

if you set a long custom command in the handle tab of the assign menu, the command would overlap and insome cases be unreadable. Now long commands are cut off and square brackets [...]indicatethat the command islonger than what is displayed.

if you shuffled fixtures on one axis with the shuffle mode Linked and the numbers of fixtures on another axis were different compared to each other, the shuffle would not appear as linked.

if you changed a gobo or a color value by spinning the encoder with the readout set to Natural or Physical, the value could jump unexpectedly.

The index numbers for mask buttons had a 0-1 shift.

In connector configurations that were set and locked by the user in the previously loaded show file,the user lock would be transferred to a new show.

Lines in the system monitor would sometimes overlap when echoing multi-line strings in Lua.

Clone Group X At Group Y would not work properly ifone group did not have CIDs.

if you called a preset where Recipe Template was enabled when itwas created, and then edited the preset and disabled Recipe Template again, the recipe of the preset would not be called into programmer and also not be cooked.

Lines in the system monitor would overlap when Lua Echo functions were executed, for example Lua "Echo('Test 123\n456\n789')".

Itwas not possible to store views using apostrophes in the name.

if you performed a clean start before loading and saving a show file,the onPC software would not load the previous show filebut instead perform another clean startif you restarted it.

if you stored a look using pan/tilt values, the look would be stored using XYZ values and vice versa. Additionally, the fixtures would move to the center or XYZ 0/0/0, respectively.

The software could crash when executing Lua commands with the Echo and GetObject function (Lua "Echo(GetObject("")).

if you assigned encoder bar 1 to a view button and saved and reloaded the show file,the reference of encoder bar 1 to the view button would break.

#### Description

Cloning color presets created using the color wheel resulted inincorrect RGB values being applied to the destination fixture.

Objects that were locked were not excluded when cloning was performed.

With XYZ, turning the X encoder past 10 and then back under 10 did not immediately lower the value.

Pressing Off and then an object in the running playbacks window disabled the object, but also selected it.This bug is now fixed. The object willbe disabled but not selected.

In the layout editor, the column filtersfor Custom Text Vertical and Full Resolution open a calculator instead of a dropdown menu.

Exchanging executors when the executor was greater than 1×1, and an executor other than the bottom leftone was addressed at the source and destination using the Exchange keyword, for example Exchange Page 1.106 at Page 1.107 split up the executors and changed assignments.

In layouts, when a group was selected insetup mode and then Clear was pressed, the group remained selected.

The command Cleanup _._ deleted allunreferenced objects, including those that could not be referenced. This bug isfixed. Now, only objects that are user generated and can be referenced in the software can be addressed by Cleanup.

Copying a custom mesh did not copy the material of the mesh.

Copying a default mesh created an invalid mesh.

Loading a show file ofprevious versions into 2.3, corrupted strings with handles inside macros.

Assigning an encoder function using the command line, for example Assign FaderTemp Page 1.301, assigned the function but did not remove the encoder leftand right function that was previously assigned.

Removing a fixture from a cue overwrote stored selective data from the cue If a preset with a recipe was stored in the cue.

Timing calculations of cues were wrong if you combined individual timings and timing masters.

if you executed Next without a selection and Group as the command linedefault, the software would crash.

Itwas not possible to unlock a macro and then add a new linein the editor. Instead, you had to close the editor and open itagain.

if you were in a cue that had a number with .9 and stored a new cue using Store Cue +,the cue would merge into the next cue with a whole number instead of creating a cue .91.

Commands with SelectFixtures in combination with Data Pool selected the wrong fixtures. For example, SelectFixtures DataPool 1 Group 1 -Fixture 1 Thru 2 selected all fixtures instead of fixture 1,2, and 5 to 10.

In rare cases, if you executed Block Cue Thru, a new cue part with the name "Blocked" would be added to a cue.

if you moved and then edited a cue part that had a command, an ownership conflict pop-up would appear.

if you cut a rule in a filterand tried to paste itinto a new ruleset, the rulewould be lost and could not be brought back back using Oops.

Editing and updating an embedded preset, discarded embedded references of the preset.

if you turned an encoder in one direction and then changed direction, in some cases, the second input would not work.

Disabling a recipe linein a sequence and then using the SelFix command on the sequence, did not select the fixtures of the sequence.

Selecting fixtures would lag If the selected sequence had a large number of recipes and the sequence sheet was open.

In some rare cases, the software could crash when executing an At Cue Thru command.

In a multi user session, instead of stomping only the selected fixtures with a multistep phaser, all fixtures with a multistep phaser were stomped.

Executing Copy \_FrameSelection 1 At Frame 2 after a lasso selection could cause a crash.

For attributes that were on break two or higher, the default values would be reset if you saved and loaded a show file.

if you cloned color values to a fixture of a different fixture type, in some cases, the color would not be converted correctly.

### Connections

#### Description

if you sent Art-Net from one console to another and changed the value in the Amount column of transmitted universes, the Art-Net input could get lost.

if you tried to create the firsttimecode in a session using the timecode viewer, all stations would disconnect from the session.

If a target was repeatedly triggered via MIDI input, setting the same value again, an error message would be displayed.

The RDM protocol requirement of a minimum of 176 μs of spacing was not met between any other packet and an RDM packet.

Switching an encoder bank in the encoder bar window using web remote, does not display the currently selected bank in yellow text.

If a fader wing or command wing was connected to an onPC on Mac and onPC got restarted, the grandMA3 USB devices would not reconnect automatically.

Some cue commands would not be executed when the sequence was triggered by a timecode event through a MIDI timecode source.

Ifaudio equipment connected toSound Out had more than one mixer element to control volume, the volume of the sound output would change.

In a session, and where Show Midi Data inSystem Monitor was enabled for the use of MIDI remotes, only the master station would display MIDI data in the system monitor. This bug is now fixed. Now all stations display MIDI data in the session.

The CID forsACN was saved with the show fileand then loaded with the local settings. This could result in multiple stations with the same sACN CID. This bug isfixed. Now, each station has a unique CID. Therefore, the output signals of the stations can be clearly distinguished.

Extensions could not be dismissed. They would immediately reconnect to the console.

The context sensitive help did not work via web remote.

Storing a mask button was not synchronized on connected devices in the network.

In certain show files,the OSC output stopped functioning after the filewas saved and reloaded.

To restore functionality, users had to toggle the OSC output offand back on.

For the first60 seconds after startup, the faders on the grandMA3 devices responded at different speeds when allwere assigned to the same sequence.

After setting the Connection Limit to 5 on grandMA3 onPC, saving the show file,and reopening it on a grandMA3 console, the system displayed the connection limit incorrectly.

Sending a MIDI note that set the master of a sequence to 100%, and then sending the same note again, caused an error message.

While booting a console, wings did not display the desk lock if you locked the desk before they finished booting.

The console unlocked again after itwas locked and an external display was connected.

Joining a session could lose the selection of the user profile.After merging, the default user profile was selected.

The software could crash after the session data merge pop-up when object references collided in the session.

Locking the console using Pause and then connecting an external display unlocked the console.

In a session after session data merge, SpeedMaster values could get lost and were reset to their default values.

Label Please did not label the current cue, instead itlabeled the Sequence.

The lavender marker in the ID Type column of the fixture sheet that indicate groups that have their mode set to additive was not displayed on connected stations ina session.

The indicators on the bitmap pool object, which are displayed when the bitmap isused, were not displayed on connected stations in a session.

In some cases, the software could crash if the resolution of a connected web remote was higher than the resolution limitset in the Web Remote tab.

The shutdown process of processing units was inconsistent. A confirmation pop‑up appeared depending on where the shutdown was triggered from -remotely from a console oronPC, button, or key.

if you were in a session, changes of MAtricks on a connected console would not always be applied to the layout correctly in setup mode.

Moving a fader toconfigure OSC output using the playback window and hardware fader, created two different actions in the system monitor, "......FaderMaster, 1 ,........."and"......FaderMaster,3 ,.........".Thisbughas been fixed. Both methods now ouput "......FaderMaster, 3 ,.........".

### Patch

#### Description

Filters would not be updated if you made changes concerning layers in the patch.

The software could crash while editing the DMX mode of a newly created fixture type. This crash occurred if you tapped Insert New DMX Channel while New Object Line and Merge Children were disabled and you unfolded a Logical Channel and then folded it again.

The software could crash, ifShow 3D Positions and all labels in 3D Positions Settings were enabled, and then all fixtures were removed from the patch.

Some fixture types were not imported correctly from the world server.

In a show file,allmultipatched fixtures got lost after using PSR.

GDTF fileswith "GDTF" written in caps in the filename, for example "Strobe.GDTF", could not be imported.

Itwas not possible to import compressed GTDF zip files.

Exporting MVR filesalso exported redundant xml files to the hard drive.

Exporting MVR fileslost emitter and filterdata ifthey were not linked.

Meshes of grandMA3 default environmental fixtures were not exported to an MVR file.

Meshes were not automatically updated when importing a GDTF filethat had new meshes using the same filename.

MVR export did not work with filenames containing special characters in iton consoles.

Ifmedia pools were renamed ina show fileand you imported a fixture type, in some cases, the fixture type modes would be imported to the universal fixture type instead of the imported fixture type.

if you copied a fixture type that had a DMX break index greater than 8 into the fixturetype folder and opened the fixture wizard in the patch, the software would crash.

Editing logical channels of fixturetypes sometimes resulted in the loss of assigned DMX curves.

The software could crash if you tried to import fixture types that have more than 8 DMX breaks.

This bug is fixed. Now, the fixture type willbe imported, and any breaks with an index greater than 8 willbe ignored.

In some fixture types, the incorrect DMX footprint was displayed in the user library.

In the PSR patch, Reset and Reset Filter reset everything, except the filterinput field.

In some cases, if you exchanged a fixture type or deleted something in the patch, the software would crash.

if you edited the IDType in the live patch, the software would crash. Now, the IDType cannot be edited in the livepatch.

In some cases, stored default fixture values were deleted from the local show after PSR.

The software could crash when importing a user profile where EditRecipe was enabled.

Importing certain meshes could crash the software.

Universal color presets were not consistent in the attribute conversion of the target fixtures.

Importing previously exported universal presets did not work as expected. This bug is now fixed.

Importing universal presets creates universal values on existing fixtures.

### Phaser

#### Description

Speed masters stored ina preset would be overwritten with MAtricks speed values.

### Playback

#### Description

In some circumstances, pressing Flash did not work If a cue was loaded.

When the encoder resolution in the handle tab of the assign menu was set to a value greater than 1%, the click intended to reach exactly 0% or 100% would only result ina value of 1% or 99%, requiring an additional click to reach 0 % or 100 %.

A CueFade before the last cue with an empty cue at the end was not executed and fixtures would snap off if you went through the cue listbefore and started the sequence again from the top.

After setting the speed master to "Speed1", DoubleSpeed and HalfSpeed would not be applied, unless your restarted the sequence.

Using the (Add Multiple Events At Time Cursor) in the timecode viewer could play back cues multiple times.

Timecode record mode did not playback events the same as in play mode, as events could jump too quickly.

#### Description

When new values were stored in a cue while a multi-step phaser was running and the cue was being played back, the new cue values were not output immediately. Restarting the cue was necessary for the new values to be output.

The output of fixtures was different when using special values in dimmers, for example when fading up from a dimmer value, Hold was following the outfade time instead of the infade time.

In some cases, if you stored values to a preset and then pressed Off and then the preset, all values would be knocked out instead of only the preset values.

Tracking values through a break did not work for an attribute if there was a changed relative value in the attribute in the tracking range.

Fixture data could have been lost when ‘Unblock‘ was used and did not update the content of cue zero.

Storing "0"as a relative value into a cue, could break the tracking shield.

When trying to remove active values from a cue, for example Store Cue 5 /Remove, the active values did not reset to the previously stored values. Instead, the fixtures fellback to their default values.

If a cue had preset data stored and a cue recipe that referred to the same preset, updating the preset caused the fixtures to snap back to the old values instead of the updated ones.

The two 100 mm master faders did not indicate their location with a red line in the bottom of the executor.

The output of a group with the mode set to Additive was unaffected by the Grand Master.

Importing a new video into a video pool object currently assigned to a bitmap that was played back caused the software to crash.

If a sequence had more than one break and blocked absolute values, relative values of a phaser would only be released in the last break of the sequence.

Removing data from a cue with an active tracking shield could release attributes in following cues so they were no longer protected.

In some cases, if you started a sound file,ashort sound would be audible before the sound file would play back.

In some cases with relative pan and tiltvalues, Stomp did not work as expected and running phasers did not stop.

Attributes of the main instance did not do MIB, ifonly the subfixtures had dimmers and they were allclosed.

if you were in a session and cues were played back using timecode, inrare cases, these cues would not play back as intended although the software would indicate that they were.

In some cases, when a fixture was part of two sequences — one set to HTP and the other to LTP — moving the LTP sequence fader to 100% displayed a dimmer value of 0% instead of the stored value from the HTP sequence.

In sequences with many cue parts and tracked pan and tiltvalues, sometimes a cue that had XYZ values ina cue part would not output these XYZ values when using goto.

The software could crash when an encoder had Go+ and Go- assigned and you scrolled fast through a sequence.

Fade transitions of cues could be slightly faster when using Go+.

Selecting a filterinOutput Filterfor a preset in the Edit Setting tab of the assign menu, did not filtercorrectly and created wrong output insome cases.

Removing values from layers in presets that were part of a cue kept the preset linkand set value to 0 in a cue.

A preset that contained a phaser and was assigned to an executor that had a defined executor time would sometimes snap offinstead of fading.

### Windows, Views, and Menus

#### Description

Changing the time zone on a connected station would not change the time in the clock viewer on the master station and the connected station would readjust to the time on the master station.

The range of values offered in the calculators forwidth and height in the configure display menu was too big and allowed for negative numbers. This bug isnow fixed.Now, the possible values range from 0 to 255. Additionally, itispossible to subtract a value from the current width or height.

The title bar button Page in the playbacks window displayed the text "Page X" in front of the custom name.

Timecode objects would not have an indicator bar in the off menu and running playbacks window.

The names of some columns in the fixture type editor were lowercase, and the order of the columns was improved.

#### Description

Executors of a bigger size that spanned across two executor banks were not displayed correctly and could not be resized in the assignment editor.

Instead of MasterSpeed, the title bar of the assign menu would only display Master as the category if you assigned a speed master.

Blocked values were displayed with red text in the Dimmer+ and Sheet/Filter mode in the fixture sheet.

IfMerge Cells was set to Feature in the fixture sheet settings, the PanTilt and RGB cells would not display any of the markers.

Itwas not possible to select an executor in the handle tab of the assign menu by tapping on the title bar of the executor.

The listof functions of the Key Unpress pop-up in the handle tab of the assign menu did not match the listof functions below the trigger options.

The user profilesetting Preset Readout could not be applied in the fixture sheet and sequence sheet, because the setting Preset in the Display tab did not have an Auto option.

Even If a filterreferenced by a mask button was deleted, itwo stillshown as active and not grayed out.

The software could crash, when a layout was deleted and then a new layout was created in the drop-down of Layout in the title bar of the layout viewer.

Enabling CLI in the quickey pool settings while a different data pool was selected did not enable CLI for the pool. Instead, itenabled CLI for the quickey pool of the selected data pool.

Itwas not possible to use settings of the title bar inreally small windows by tapping the overhang pop-up button ( ) in the title bar.

Changing Cue Mode in the content sheet with Show Recipes enabled from Manual to another mode, stilldisplayed the recipes of the recent cue selected in the Manual mode.

When typing a note in the Note tab of the Info window for a selected sequence, the focus and cursor would jump to the note section of the first cue after typing the firstcharacter.

The camera arrangement in the layout encoder bar did not work with subfixtures.

Ifno secondary function isassigned to an executor, the firstfunction will not be displayed in the playbacks window and playback bar by pressing MA.

Messages in the messages grid of any category in the message center were listed from bottom to top, instead of top to bottom.

On onPC with a really small software window itwas not possible to select the command linefor input.

The displayed listof objects in the object tab of the assign menu did not scroll down to the assigned object.

Special dialog for shapers did not work in some fixture types. if you then moved the blades, they would be displayed with a slight offset starting from a designated position.

Moving a selected object in the encoder bar pool could result in the software crashing or the object losing its selection.

In the fixture sheet, cells would sometimes randomly flash different merge cells states after knocking in values in the programmer.

In the assign menu, the assignable functions for button press/unpress were not displayed in the playbacks window. This bug isfixed. Also, the unpress function is shown in allexecutor displays, once the executor is pressed.

In some cases, although notes were listed,the Note tab in the Info window and the List Reference pop-up displayed a (0) or (x) in the title bar.

The heights of headers of statuses and messages were not the same in the message center.

Cloning presets from fixtures did not work ifPresets was selected in the middle of the clone menu and all the other object buttons in the middle of the clone menu were deselected.

Itwas not possible to scroll the At Filterwindow with the mouse wheel.

The turquoise arrow in the upper right corner of sequence pool objects that indicates that the sequence isassigned to an executor was not displayed.

Cloning with a dimmer filteractive, for example Call Filter2 'Only Dimmer', and then Clone Group 1 At Group 3 IfSequence 2,also cloned color information.

if you filtered a drop-down listthat can be filtered,such as the drop-down listfor Code in Quickeys or Selection in the Recipe Editor,by typing some characters into the search field,the indicators for the previous selection and your current location in the listwould not be displayed correctly.

With Add Executor enabled in the handle tab of the assign menu, custom commands were displayed in the wrong order. For example Cue 1 Page x.y,instead of Page x.y Cue 1.

When storing a help window with changed zoom as a view, the set up zoom was not stored.

In the show creator, tapping an object in the pool listof around 100 objects caused the pool listto scroll and collect the wrong object.

The fade and delay buttons, such as, FadeFrom/To X and the DelayFrom/To X buttons displayed

#### Description

incorrect formating when setting a value of 59 and then increasing the value with + or the swipe function.

Resizing an executor did not apply the new assignments to the single executors that already existed. Only the new executors inside the greater executor had the new assignments for the new size.

This bug is now fixed. Executors inside a greater executor do not apply the new assignment they willget during resize If the single executor was manually changed by the user to a different assignment (cyan colored icon). Executors inside a greater executor apply the new assignment during resize when they are stillon their default assignment (no cyan icon).

In some cases, the number displayed in the lower right corner of each tab in the running playbacks window indicating how many playbacks of itsobject type are currently running was incorrect.

Sometimes, ifan executor spanned two sections, itwould be displayed incorrectly in the Xkeys and Playbacks window.

The software could crash when loading a show filethat contained fixturetypes with invalid channel functions.

Special executors with no function assigned to them displayed "Proxy xx" on the executor in the custom master section instead of nothing.

Special executors with a secondary function, did not display the function on the executor in the custom master section.

If a locked layout was moved from the default data pool to another data pool, it was possible to enable setup in the layout viewer although itwas locked.

Enabling shortcuts on a console and pressing the leftshift key, highlighted the rightMA instead of the left MA, and vice versa.

Storing a view of the timecode viewer did not store the zoom settings.

When bar windows, such as the align bar window and the special dialog window were open on the same screen, tapping different options in the Align Bar window caused the encoder bar to react in unexpected and incorrect ways.

In some editors, oops did not cancel the last action, and closed the editor pop-up.

The software could crash ifallrender qualities were deleted in the pool and the 3D viewer was opened.

The sequence editor displayed an empty toggle button in the title bar.

Messages about power loss or a faulty battery were not displayed in the Power category in the message center.

A custom text inside a layout element was not automatically wrapping the text to the size of the layout element. This bug isfixed. The text now adjusts automatically and the element name will no longer be displayed.

Itwas not possible to copy an executor by tapping the bottom-left executor when itssize was larger than 1×1.

In the shaper special dialog, it was not possible to reset a value to0 using the calculator.

if you selected an appearance in the label pop-up and edited the name of the appearance, an infiniteamount of new label pop-ups could be opened. Now only one pop-up opens to edit the name.

if you enabled Add Alpha in the image editor,the transparency would not be displayed until you saved and loaded the show file.

Setting Empty in the object tab of the assign menu stilldisplayed the previously assigned selection in the handle tab of special executors.

Long text was not wrapped on layout elements.

Editing a layout element and changing the SelectFixtures action, then tapping Save as Default, removed the action from the Preferences and Timings menu for fixtures. This iswhy fixtures could not be selected anymore.

The layout encoder bar did not display correct values, when Setup was enabled in the layout viewer.

In some cases, the calculator of Preferred IP in the Art - Net tab of DMX protocols had no "/".

In some cases, moving views in the pool viaswipey command did not work.

When a user was logged inwith Rights set to None, titlebuttons in the 3D viewer were not grayed out. Instead empty buttons were displayed.

Sorting lines by Command column in macros did not work. The order was not alphabetically or numerically sorted.

On OnPC, changing the scaling in the Configure Display pop-up to 0.75 and double-clicking on the title bar of a window to maximize it did not work. Instead, the window became larger than the

#### Description

screen.

When not all FeatureGroups were used by the patched fixtures,the feature group indicator bar displayed wrong indicators.

Adding a "."in the calculator of IP column in network interfaces using the key .,deleted the following character.

The sequence sheet flickered when the DMX Tester encoder bar was used.

Make Handles did not convert handles with cue numeration correctly.

Layout elements were jumping around and resizing, when you tried to move them.

After loading a show filefrom version 2.2 into 2.3, some fixtures lost their appearances in the layout viewer.

Itwas not possible to filterforcue numbers in the Goto Cue and Load pop-up for sequences.

The temporary help pop-up did not respect the overlay fade set in the user profile.

Saving a show including "%" as a character could crash the software and connected stations.

EditSetting a second preset entered the Edit mode, and deleted the current programmer values.

This bug is fixed. Now, itis possible to edit only one preset ata time.

The Countdown cellof agendas displayed the wrong time between midnight and 04:47:44 a.m.

In some rare cases, If a sequence was running and you tapped the Sheet Mode button in the settings of the content sheet several times, the software would crash.

Using a mask with the filter rule"IfOutput" on a fixture and sequence sheet, switching to a different view, and then calling the view again, displayed the wrong content on the sheets as If the mask was disabled.

If the phaser editor was open in2D mode, swiping Pages in the phaser encoder bar could crash the software.

The encoder bar did not display current values of the respective encoder components if you drew new layout elements in Setup mode. Instead, it displayed 0 for all the encoder components (PosX, PosY, etc.) Some filterswould not work in the Sheet/Filter mode of the fixture sheet.

The encoders, for example At:Speed, in the Phaser Bar did not reliably open the calculator when pressing the encoder.

## 5. Deprecated

> **Hint:** The following is deprecated and willbe removed in the software in the near future. Make sure you read the sections stated below, so you can adjust your macros and plugins accordingly, if necessary.

- The Lua function HasActivePlayback() is deprecated. It was replaced by IsRunningPlayback(). For more information
  on the new Lua function IsRunningPlayback() see Release Notes 2.4.

- /Selective combined with CleanUp is deprecated. It was replaced by the /Type option keyword, which now works in
  combination with the CleanUp keyword. For more information see Release Notes 2.2.

- The command Help + Please is deprecated. It was replaced by the new HelpKeyword keyword. For more information
  see HelpKeyword in Release Notes 2.2.

- The Lua function Aquire() is deprecated. It was replaced by Acquire(). For more information on the new Lua function
  Acquire() see Release Notes 2.2.

## 6. Appendix

- We recommend you use a dedicated and a separate physical network for each grandMA3 session.
- When using DMX protocols we recommend you use a dedicated physical network for each protocol.
- The recommended workflow for executor configurations that are different, compared with the default executor
  configuration, is to create a new executor configuration, do the changes in the new configuration and save them.

- XML files with exported executor configurations from grandMA3 version 1.2 and prior cannot be properly imported to
  grandMA3 version 1.3 or later due to structural changes.

- XML files with exported analog remote setups from grandMA3 version 1.3 and prior cannot be properly imported to
  grandMA3 version 1.4 or later due to structural changes.

- XML files with exported timecode shows from grandMA3 version 1.3 and prior cannot be properly imported to
  grandMA3 version 1.4 or later due to structural changes.

## 7. Known Limitations

Software update via network to onPC stations requires confirmation during the install process at the destination system.

When multiple GlobalMasters exist on the network, each with the same session and location name, the station with the higher priority takes over automatically.

Ifallstations have the same priority,the station with the longest Online Time becomes the GlobalMaster of all stations.

Recast will only recast presets to cues if there isa preset link in the absolute layer.

Loading show filesthat were saved in previous versions deletes the programmer content.
