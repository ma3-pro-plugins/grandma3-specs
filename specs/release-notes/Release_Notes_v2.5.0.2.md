# grandMA3 Release Notes

> Text extracted from the official MA Lighting PDF (`Release_Notes_v2.5.0.2.pdf`). Layout is approximate; optimized for search and diff.

## Table of Contents

- [1. Features](#1-features)
- [2. Other Enhancements](#2-other-enhancements)
- [3. Changes](#3-changes)
- [4. Bug Fixes](#4-bug-fixes)
- [5. Deprecated](#5-deprecated)
- [6. Appendix](#6-appendix)
- [7. Known Limitations](#7-known-limitations)

## Let's Get Started

Release Notes 2.5

Version 2.5 | 2026-07-30 English

Release Notes 2.5 2026-07-30

Release Notes 2.5 2026-07-30

Do you need help getting started in grandMA3? Perfect! Here we describe a few quick steps to get you rolling. The manual will explain functionality in detail while the MA e-Learning in the MA University offers you all kinds of training. All information can be

Let's go! Boot your console or open your onPC and find predefined views on view buttons on the right. To switch between the views, tap the corresponding view buttons.

If this is your first time starting grandMA3 software, patch some fixtures first. Or you can load one of the demo shows delivered with the software. Either way, press Menu. If you use grandMA3 onPC software, there is a symbol in the top left corner there.

Clicking the symbol is the same as pressing Menu on a console.

Tap Backup and then Load, now you are ready to load shows. Would you like to get right on it? Switch Shows to Demo Shows in the title bar first. To do so, tap Shows repeatedly until it says Demo Shows. Once Demo Shows is displayed, it is possible to select any demo show in the list. After you selected a demo show, tap Load.

In case a show was already loaded, a pop-up will appear asking if you want to save the current show first before loading the new one. It's up to you!

Here we go! Now you are ready to work with the grandMA3 software. It is as easy as that! Again – there are view buttons there, which change the screen content. At the bottom, you will find the encoder bar and the command line. Technically that is all you need to get started. For more information, see the grandMA3 help menu. To access the help in the console or the onPC, tap the view buttons named Help or visit the Online Manuals on the MA Lighting website. If you want to learn the grandMA3 software step by step, please see the Quick Start Guide and join the MA e-Learning – it's free of charge and available on the MA Lighting website.

Have fun with using our grandMA3 software! Find all the improvements and changes of this software version further down.

> **Hint:** The grandMA3 software will start using the show file (or status) that was in operation before the software was shut down.

Release Notes 2.5 2026-07-30

## 1. Features

- Color Theme
- Masters Window
- Locate Function
- Recipes
- New Graphics Platform
- Channel Map

The latest release of grandMA3 2.5 rolls out several enhancements that enrich your programming experience. Besides numerous improvements and enhancements, based on your highly appreciated feedback, many bugs were fixed and workflows refined.

Color Theme

#### Improved color theme:

Improved the current user interface to enhance visual clarity and user orientation. The color theme was optimized for use in dark control room environments, enhancing overall usability and visual comfort. Indetail, non-selected UI elements – such as buttons, pool objects, and windows – are displayed with reduced intensity, while selected UI elements are clearly highlighted.

The default color theme (default.xml) was updated, and a theme (default_legacy.xml) was added so that users can revert to the look from the previous software version.

Release Notes 2.5 2026-07-30

Masters Window

#### Added in this release:

The masters window provides easy access to all group masters, world masters, speed masters, playback masters, and timing masters. It provides an overview to quickly determine the status of all masters and shows which masters are not at their default value.

Find the masters window in Add Window - More - Playback - Masters.

To open a temporary masters window:

- Press and hold Group. The masters window opens in the Group Masters tab.

- Tap in the control bar. The masters window opens in the tab that was open last.

The masters window is split into six tabs. The first tab contains the master controls, each of the other five tabs contain all masters of one type.

The green number in the lower right corner of each tab displays the number of masters that are not at their default value and the total amount of masters in that category.

Groups in the Group Masters tab are displayed if their Mode is set to any value other than None. All created worlds are displayed in the World Masters tab. All speed masters, playback masters, and timing masters are displayed in their corresponding tab.

Each master is displayed with its label in the title bar. On the left side below the title bar there is a fader to change the master value. On the left side, there are two or three buttons to quickly influence the value of the master. For speed masters, playback masters, and timing masters, a disabled master is indicated by a red bar above the label.

- Use Full and Zero to set the master to 100 % or 0 % respectively in playback masters and timing masters.
- Group masters and world masters have two sets of buttons. Tap Button Mode in the title bar to select either
Full/Zero or Flash/Black. To set the master to 100 % or 0 % respectively, tap Full or Zero. To temporarily set the master to 100 % or 0 %, tap and hold Flash or Black.

The button mode is set for both the group master and world master tab.

- Speed masters have DS, HS, and Learn or Speed1. Tap Button Mode in the title bar to select either Learn or Speed1.
Tap DS to apply double speed and double the value of the master. Tap HS to apply half speed and half the value of the master. Tap Learn or Speed1 to apply the dedicated function to the speed master.

In the tabs Group Masters and World Masters, if Label Action is set to Locate, tap the title bar of a master to execute the locate function and indicate which page and pool the master is located in. The title button starts to blink red and a temporary pop-up appears. In the temporary pop-up, you can select between Reset or Keep Page:

- If you tap Reset, locate will be deactivated and the pop-up closes.
- If you tap Keep Page, locate ceases and the playback bar stays on the currently selected page. Thus, it does not
return to the page it was selected before executing locate. For more information on Locate see below.

If SelectFixtures is selected, tap the title bar of a world or group master to execute the SelectFixtures keyword for the fixtures of the respective master.

In the bottom of each masters tab, there are buttons to set all masters of one type to the same value. To hide the buttons, disable Button Bar in the window settings.

Release Notes 2.5 2026-07-30

- Group Masters
The buttons in group masters are specific to the mode of the group master.

  - All Positive Full
Set allgroup masters with mode Positive to 100 %.

  - All Positive Zero
Set allgroup masters with mode Positive to 0 %.

  - All Negative Full
Set allgroup masters with mode Negative to 100 %.

  - All Negative Zero
Set allgroup masters with mode Negative to 0 %.

  - All Scaling Full
Set allgroup masters with mode Scaling to 100 %.

  - All Scaling Zero
Set allgroup masters with mode Scaling to 0 %.

  - All Additive Full
Set allgroup masters with mode Additive to 100 %.

  - All Additive Zero
Set allgroup masters with mode Additive to 0 %.

These buttons can also be addressed using commands in combination with the /Type option keyword.

Use this syntax:

FaderMaster Group ["Group_Name" or Group_Number] At [Value] /Type ["Type_Value"]

Example:

To set allgroups that are in mode "Positive" to 100%, type:

User name[Fixture]>FaderMaster Group * At 100 /Type "Positive"

- World Masters
  - All Full
Set allworld masters to full.

  - All Zero
Set allworld masters to zero.

- Speed Masters
  - All Speed1
Sets all speed masters to 60 BPM, 1.00 Hz, or 1.00 s depending on User Settings Speed Readout.

  - All Double Speed
Double the speed of allspeed masters. The new speed value is displayed in the fader of each speed master. An asterisk (*) indicates that a multiplier or divisor was applied to the speed master.

  - All Half Speed
Half the speed of allspeed masters. The new speed value is displayed in the fader of each speed master. An asterisk (*) indicates that a multiplier or divisor was applied to the speed master.

  - All Learn
Apply the Learn function to allspeed masters. To do so, tap the button in the required speed.

- Playback Masters
  - All Full
Set allplayback masters to 100 %.

  - All Zero
Set allplayback masters to 0 %.

Release Notes 2.5 2026-07-30

- Timing Masters
  - All Zero
Set all timing masters to 0 %.

For more information on the status icons see Improved Status Center in Other Enhancements.

In the title bar of the masters window there are four buttons:

- Label Action (Group and World Master tab)
Locate (default): For more information see below.

SelectFixtures: For more information see SelectFixtures Keyword in the User Manual.

- DataPool (Group and World Master tab)
Select from which data pool the masters window shows data. The standard values are <Link Selected> and All Data Pools. If All Data Pools is selected, other data pools in use will be indicated by x.y 'name'.

- Non-Default Only
When enabled, only masters that are not at their default value are displayed. The default value depends on the master type.

- Move Display Icon (when pressing and holding Group)
The window can be moved to other screens. For more information see Change Menu Locations in the User Manual.

To hide the title bar, disable Show Title Bar in the Masters window settings. To hide the button bar, disable Button Bar. The title bar can be organized in the Edit Title Bar settings.

Release Notes 2.5 2026-07-30

Locate Function

#### Added Locate keyword:

For one, it is possible to locate pool objects that are assigned to executors and also locate objects in pools. Repeatedly executing Locate cycles through all pages the pool object is assigned to. If the object is located in numerous pages, a cycle count will be shown as long as you keep the object pressed.

To do so:

1. Press and hold List and tap the pool object you want to locate.
2. A temporary pop-up opens displaying Reset and Keep Page. The pool object displays Here with a pulsating background
in the page it is located.

3. Repeat steps 1 through 2 to locate the pool object on the following page.

Or use this syntax in the command line:

Locate [Object] ["Object_Name" or Object_Number]

Secondly, the page can follow the located object. That is, the object that is assigned to an executor can be located in its pool.

Once the object is located, the object will start pulsating in red and the pool of the object will display a red and dotted frame.

To locate the object in the pool:

- Press and hold List and tap the executor. The frame will be displayed as long as you keep the key pressed.

Or use this syntax:

Locate Page ["Page_Name" or Page_Number]Executor ["Executor_Name" or Executor_Number]

Locate Page ["Page_Name" or Page_Number].["Executor_Name" or Executor_Number]

If Locate is active, the executor label starts to blink.

To cancel locate altogether and return to the spot before executing locate, tap Reset.

To stay on the same page you are currently in, tap Keep Page.

Or use this syntax:

Locate Reset (/KeepPage)

It is possible to latch List in the temporary command controls menu to execute Locate.

Release Notes 2.5 2026-07-30

Recipes

#### Improved recipes:

- Phaser Recipes can be created with the Edit Recipe Mode. For example, to create a phaser recipe: enable Edit
Recipe, tap a group pool object and then tap a position pool object. Then tap Next Step ( ) in the encoder bar and tap another position pool object. A phaser recipe line is created. For more information, see Recipe Editor Window.

- Phaser recipe presets are automatically named after the selected shape, and standard recipe presets after their
selected value. Phaser recipe lines are named after their selection and shape, and standard recipe lines after their selection and value.

- X, Y, Z, and Shuffle are now located at the top left corner of the recipe grid.
- Recipe Templates now link the previously selected group pool object directly to the recipe line. If an MAtricks pool
object is selected after choosing a group and before tapping a recipe template, it is also linked to the recipe line.

- In recipes with more than two steps, the shape editor now has left and right arrows below the 1D layout to skip
through the steps.

- Added Normal and Strict to the pool tab of the selection context area to change the selection mode.
- Added DataPool to the title bar of the MAtricks selection pop-up. Tap to select which data pool the pop-up displays
MAtricks values from.

- Added all buttons of the MAtricks editor to the editor in the context area for MAtricks.
- Added Reset to the MAtricks editor in the context area to delete all MAtricks values.
- Selecting a standard recipe line in the recipe editor (Edit Recipe is enabled) highlights the selected recipe line with a
rotating dotted green frame and marks the last selected preset pool object with a rotating dotted green frame.

- Added to the tool bar at the left side of the recipe editor. Tap to recook the selected recipe line. This is particularly
useful for phaser recipes and standard recipes with timing values.

- Added SpeedMaster column. If a speed master is set for the phaser recipe, the master is indicated in the bottom
right corner of the Speed cells, as itoverrides the speed values. Additionally itis possible to select a speed master for SpeedX values. Tap and hold the SpeedX cell and select a speed master on the left next to the calculator, or select it in the context area tapping SP on the top right.

- If the "Name" cell is selected, the context area displays essential settings to quickly edit a recipe.
These are the columns of the context area:

  - General:
General settings of the phaser recipe.

    - Enabled
Toggle to enable or disable the recipe. Disabled recipes are grayed out and have a red font color.

    - Lock
Toggle to lock or unlock the recipe. If a recipe is locked, UL is displayed in the Lock column.

As long as the recipe is locked, all properties of a recipe cannot be edited anymore.

    - Tags
Tap to open the tags editor and assign or unassign tags. For more information on tags and the tags editor, see Tags.

  - Shape:
Set up a shape for the phaser recipe.

Shape displays the selected shape. Tap to open the shape editor and select a shape.

The first six shapes in the pool are available as buttons.

The 1D view visualizes the selected shape.

  - Time:
Set timing values for the phaser recipe.

    - Speed X

Release Notes 2.5 2026-07-30

    - Measure
  - Playback:
    - Playback NShot
    - Playback Direction
    - Adaptive Measure
    - Adaptive Width
  - Phase:
Set an individual phase by tapping Phase X, or select a default phase value and shuffle value below.

- Only feature groups that are included in the selected world are displayed forabsolute and relative values.
- The context area of the Curve column now displays a 1D layout of the shape. The selected steps are highlighted and
can be changed using the buttons above the 1D layout.

- Added buttons forthe available values to the context area of Speed Master, Direction, Adaptive Measure, and
Adaptive Width. Added the edit rotation clock in the context area of Adaptive XY Rotation.

- Added a calculator to the Editor tab of the context area for Value Absolute and Value Relative.
- Added a context area for the Part, SpeedX, PhaseX, Measure and NShot column. The context area displays the
calculator, as well as special values and slide controls where applicable. The NShot context area additionally displays a 1D layout of the shape. The measure context area additionally has a button to enable or disable Adaptive Measure.

- Added Pause at End to the context area of NShot. Enable Pause at End to set the programmer to the values at the
end of the determined NShot cycles. This allows for a quick and easy adjustment of the value at which NShot should stop. To do so,use the slide control for NShot. Pause at End isdisabled if you clear the programmer.

- The pools in the context area now alldisplay the pool name and icon.
- Added Maximize to the bottom left of the context area. Tap Maximize to only display the pool, sheet, or editor in the
context area and hide the buttons to the leftand right.To return tothe default view of the context area, tap Exit.

- Cleaned up the Sheet tab of the context area. Now, the sheet only displays the No and Name column for objects.
- Added column Link Steps in the Value Source header. This function is only available for phaser recipes with two
steps.

IfLink Steps is set to Yes, complementary values in the shape are adjusted at the same time. Linking affects the properties width, acceleration, and deceleration. By default, Link Steps is set to Yes.

In the shape editor,enable linking by pressing Link Steps in the middle of the control area.

  - Increasing the width of one step decreases the width of the other step and vice versa, so the overall
width of the two steps stays consistent.

  - Acceleration and deceleration change at the same time fora single step. For example, if you increase
acceleration in step 1,deceleration increases accordingly in step 1.

- Added Make Other Symmetrical to the calculator of transition values for phaser recipes with two steps. Tap Make
Other Symmetrical to set the other step of the phaser recipe to a matching transition value so the transitions of both steps look symmetrical. The calculated transition value depends on the transition value in the selected step and the width of both steps.

- Added Turn into Phaser Recipe to the editor of universal phaser presets toeasily convert the universal phaser preset
into a recipe. The new recipe preset is selective.

- If a world is selected, cooking a recipe in the programmer only cooks the channels in the selected world. Once the
recipe isstored all values, including values that are not active in the selected world, are stored as fullycooked.

> **Restriction:** if you use PSR, locked shapes cannot be overwritten during import. Use custom shapes to achieve the desired result.

Release Notes 2.5 2026-07-30

#### New Graphics Platform

#### Added Vulkan graphics platform:

grandMA3 now supports Vulkan as its graphics platform, replacing the previous OpenGL requirement. These changes reflect our ongoing commitment to keeping grandMA3 up to date and ready for the future.

As part of this update, there are changes to the system requirements. For more information, please refer to the updated System Requirements grandMA3 onPC in the User Manual.

Release Notes 2.5 2026-07-30

Channel Map

#### Improved patch:

Added a new channel map to the Insert New Fixture dialog and the Fixture Type Import dialog. This enhancement displays the attribute of each DMX channel and makes fixture types with identical footprints easier to distinguish by providing clear visual differentiation.

The channel map is displayed on the right side of the menu and ispresented in a structured grid view. A Channel Map toggle button has been added to enable or disable the channel map. Itis enabled by default.

The channel map offers two viewing modes: Channels (default) and Structure. Users can switch between these modes viaSort By located in the top-right corner of the channel map. The structure mode is sorted by ID and displays the fixture type hierarchy based on the geometry of the fixture type.

Release Notes 2.5 2026-07-30

## 2. Other Enhancements

#### Updated predefined content:

- Updated demo shows:
  - Demoshow_grandMA3
- Updated the predefined macros.

#### Improved status center:

- The World Master status indicates which world is reduced inintensity. When the master of the selected world is
pulled down, the status displays the icon + "World". When the master of any other world islowered, the icon + "World" x (+ yand so on) is displayed. The maximum amount of allowed characters is 6.The order in which the pool numbers are displayed depends on the order in which the masters were lowered. For example, when lowering an executor assigned toWorld 2,the text‘World 2’ willappear below the World Master status icon. Tapping the world master status icon opens the temporary world masters window. For more information on the masters window see Features.

- Added Group Masters status ( ). Works similiar to world master status, but the pool numbers are displayed in an
ascending order.

- Added Pause At End status ( ).The icon is displayed ifPause at End isactive. For more information,
see Improved recipes.

- Improved the tooltips for the status icons.

#### Improved world master:

- The world master for world 1 is linked to the grand master and the two always have the same value, as world 1
contains all fixtures in the show file.

#### Improved the message center:

- Commands that cannot be executed in the command line are displayed in the command linewarnings and errors
categories. The text isdisplayed in the same colors as the command line feedback.

#### Improved MAtricks:

- Added the possibility to enter a speed master via Speed Master. In the calculator pop-up, speed masters can be
defined to override the predefined MAtricks values, such as Speed From / To values. If thevalue No Master is selected, a set speed master on a higher level in the hierarchy, such as in a cue part or sequence, will not influence the speed of the phaser recipe.

#### Improved special dialog:

- Shapers have mirror buttons. 1/3 mirrors the shapers vertically, 2/4 mirrors horizontally, Rot mirrors the rotation. To
display the buttons on the left side of the window, enable Mirror Bar in the shapers settings.

Release Notes 2.5 2026-07-30

#### Added MAtricks to shapes:

- Add MAtricks values same as in recipes directly to shapes in the edit mode of the shapes pool object.

#### Improved 3D visualization:

- While 3D isinitializing,the status of the shader compilation isdisplayed. If the shader compilation fails,an error
message appears.

- Added culling to optimize how objects or surfaces are rendered, improving performance. Cull Mode is added to
Render Qualities.

Force None willcover both sides of a triangle mesh, which could impact the performance. This is the default.

From Material willtake the predefined cullmode of the mesh.

Added a Cull Mode option to Meshes. Front: Hides the outside faces of the mesh. Back: Hides the inside faces of the mesh. None: Displays both the inside and outside faces of the mesh. Auto: Automatically detects the mesh orientation and switches between Back and None accordingly.

#### Improved presets:

- The title bar of the preset editor can be edited.
- Ifmore than one phaser recipe is added to a preset, the additional phaser recipes reference the firstphaser recipe in
the preset.

#### Improved preview:

- Master Controls and the Custom Master Section now indicate preview mode. All executors that affect the preview
environment are indicated by a red frame.

#### Updated predefined content:

- Auto Focus to Next Cell in the recipe editor window settings is enabled by default innew shows.

#### Improved Lua:

- The Lua Core has been updated to Lua v5.5.0
> **Important:** if you work with Lua bytecode, itis necessary to recompile itwith the updated LUA compiler.

Release Notes 2.5 2026-07-30

#### Improved user rights Presets in user configuration:

- Users with user rights Presets can update presets and change the preset update mode of their user profile. This also
includes Store /Merge.

- The default user right for the Remote user has changed to Presets.
- Storing new presets or other objects is not possible.
- Editing recipes is not possible.
- Setup is not available in layout viewer and 3D viewer.

#### Improved timers:

- The Linked User Profile in the Timers editor was added to define one user profile per timer. The setting can only be
edited, if the Timer Link Type is set to anything but Not Linked. The linked user profile receives pop-ups from the corresponding timer.

#### Improved sequence sheet:

- In track sheet mode and with an active filteror a mask, the sequence sheet always displays the currently running
cue.

- Rearranged the columns in the sequence sheet. Sync, Speed Master, Speed Scale, Morph, and Delay To Phase are
now subcolumns of the new column Phaser.

#### Improved display settings:

- Added Wing ID to the grandMA3 onPC Configure Display settings, allowing users to define the displayed wing in the
command wing bar for each display individually. For more information see command wing Bar in the User Manual

#### Improved temporary filtering in the attribute definitions tab in the patch and the agenda viewer:

- Added in the title bar to enable or disable temporary filtering. A yellow filter row is displayed at the top of the
sheet. For more information see Temporary Filtering.

- Added in the title bar to clear all temporary filters.
- Added temporary filter for Main Attribute in attribute definitions.
- The temporary filter for Hide in attribute definitions is now a selection pop-up.

#### Improved executors:

- Added Render Style to the title bar of the assign menu. The options are Default, Pool, and Executor. Executor
displays details about the assigned object. Pool offers a simplified look reduced to name, appearance, and master value. If the executor isset to Default, the render style that is defined in the page settings is applied. To define a

Release Notes 2.5 2026-07-30

render style per page, added Render Style to the object settings in the Page Pool. Press MA to display the index number of the assigned object in the top right corner on executors that are set to pool render style.

- The Quickeys virtual LED isnow displayed on the executor label If a quickey pool object is assigned.

#### Improved layouts:

- Added Render Style. The style of each layout element can be set up individually. The available styles are Executor,
Pool, and Default.

The render style can be set for the entire layout in the settings of the layout object. This render style is applied to all layout elements that are set to Default. Additionally, individual render styles can be applied in the Render Style column in the Layout and Layout Element Defaults tabs.

#### Improved the running playbacks window:

- Added Touch Mode to the window settings. Additionally, Touch Mode replaces the Off Mode setting.
The options are:

  - None:
Tapping an object does not perform a command.

  - Off:
Tapping an object immediately turns itoff.

  - Select:
Tapping an object in the running playbacks window performs a select command in combination with the object you tap.

#### Improved preset playbacks:

- In the speed settings of an executor, Sync can be set individually if a preset is assigned to an executor or per default
in the Preference and Timings - Preset settings. If enabled, it synchronizes the fixtures of the phaser. For more information about Preset Playback in general see Use Preset in the user manual.

- Speed Master in the executor settings of the assigned preset is grayed out and cannot be edited, if a preset has
MAtricks with Speed Master stored already.

#### Improved network menu:

- If the session switches to TCP only communication, TCP is indicated in orange in the bottom right corner of the
Session cell on the master station.

For more information on TCP, and the IP addresses in sessions see Protocol Details.

> **Hint:** This does not necessarily mean that the network is defective. For example, no data can be sent in an empty show file,resulting in a TCP indicator.

#### Improved plugins and macros:

- Added a play icon ( ) and removed "0.0%" in the progress bar of a running Plugins pool object.

Release Notes 2.5 2026-07-30

- Added a play Icon ( )and the running macro line (number and name) isdisplayed in the progress bar of a Macros
pool object.

#### Improved playback keywords:

- Playback keywords that interact with a sequence or preset while pressing and holding an executor (Swap, Flash,
Black, and Temp) can now also be used directly within pools. To use this feature, enter the desired keyword (for example, Flash) into the command line,then tap and hold a pool object (for example, Sequence 1). The selected action will be applied as long as the object isheld.

#### Improved grandMA3 onPC on Windows®:

- grandMA3 onPC for Windows now allows users to specify a graphics card on systems equipped with multiple GPUs.
To assign the desired graphics adapter, right-click the grandMA3 onPC application and click Properties, select the Shortcut tab. Append adapterindex=X to the end of the Target fieldwhere X is the index of the desired graphics card.

Example:

C:\Program Files\MALightingTechnology\gma3_<version>\bin\app_sstem.exe HOSTTYPE=onPC adapterindex=1.

To determine the adapter index, start grandMA3 onPC, open a System Monitor window, and scroll to the top of the displayed information. Available graphics adapters are listed with their respective indexes, for example:

Use the corresponding adapter index value when configuring the application shortcut.

- Adapter [0] (selected) – currently selected graphics adapter.
- Adapter [1] – additional graphics adapter.

#### Improved grandMA3 onPC on macOS®:

- The application structure was updated. The installer now creates a dedicated grandMA3 onPC application in the
Applications folder, replacing the previous launcher-based setup. This new approach enables a separate app for each grandMA3 onPC software version and a grandMA3 Terminal app. Even if the Terminal app was deleted, itcan stillbe accessed through the grandMA3 onPC software application.

> **Hint:** The new grandMA3 application can stillbe launched through the legacy Launcher. After installing the new version and then starting the legacy launcher, the new version will start once. After this initialstart,the previously selected version willstart up again If the launcher isstarted again.

- To start an additional onPC Instance or a grandMA3 Terminal, right-clickon the grandMA3 application icon in the
Dock or click on File in the title bar of the software or use a shortcut (command + N) to open a new instance and (command + T) to open grandMA3 Terminal. Up to 5 software instances are allowed per device at the same time.

Release Notes 2.5 2026-07-30

> **Important:** To ensure fullfunctionality of grandMA3 onPC, allow access to Local Network, External Media (USB drives),and Microphone permissions when prompted by macOS.

- The installation process of grandMA3 onPC on macOS was significantly optimized. Users will benefit from a
noticeably faster installation experience.

- The grandMA3 onPC application icon was redesigned to better align with native macOS visual style, as itis now
displayed within a square app icon frame. Once the application was launched, the currently running software version number is displayed in the upper section of the icon, allowing users to quickly identify the active version directly from the Dock. In addition, grandMA3 onPC for macOS Tahoe 26 is now categorized in Creativity in Launchpad. Previously, the application was in the Other section. A new startup splash screen was introduced forgrandMA3 onPC on macOS. The splash screen is displayed immediately after launching the application and remains visible while grandMA3 is loading.

Updated Carallon fixture libraryto version 20.1.1.

#### Improved the selected speed master:

- Added LearnMode to the EditSetting tab in the assign menu for the master "Selected Speed".

#### Improved tags:

- Added Pause and Off to Pool Action of tags.

The stability of the grandMA3 software was improved when using the web remote feature.

Release Notes 2.5 2026-07-30English

## 3. Changes

- New keywords:
  - Locate
- New option keywords:
  - /Restart
  - /KeepPage

> **Hint:** For more information about the new keywords, please read the corresponding sections above.

- New color theme colors:
  - ColorDefinitions:
    - Global.ShadowBright
    - Global.SelectedCellBackground
  - Colors:
    - Exec.BlipActive
    - Exec.BlipBackground
    - Exec.BlipPaused
    - Exec.InactiveBackground
    - Global.FocusText
    - ShowCreator.ObjectTypeBackground
    - RenderData.LocatedBackground
    - RenderData.SelectedRowBorder
    - RenderData.Selected
    - RenderData.LocateOverlay
    - TitleButton.ActiveText
    - TitleButton.ActiveTextShadow
    - TitleButton.ActiveWorldText
    - TitleButton.ActiveWorldShadow
    - TitleButton.ActiveSelectionCountText
    - TitleButton.ActiveSelectionCountShadow
    - TitleButton.ActiveFilterText
    - TitleButton.ActiveFilterShadow
    - TitleButton.ActiveInfoText
    - TitleButton.ActiveInfoShadow
    - TitleButton.ActiveDataPoolText
    - TitleButton.ActiveDataPoolShadow
    - TitleButton.ActiveDynamicFilterText
    - TitleButton.ActiveDynamicFilterShadow
- New grandMA3 Lua Functions:
  - GeneratePhasersForChannels(integer:ui_channel_index, {['abs_preset'=light_userdata:handle],
['rel_preset'=light_userdata:handle], ['fade'=number:seconds], ['delay'=number:seconds], ['speed'=number:hz], ['phase'=number:degree], ['measure'=number:percent], ['gridpos'=integer:value], {['channel_function'=integer:value], ['absolute'=number:percent], ['absolute_value'=integer:value], ['relative'=number:percent], ['accel'=number:percent[, 'accel_type'=integer:enum_value(Enums.SplineType)]], ['decel'=number:percent[, 'decel_type'=integer:enum_value(Enums.SplineType)]], ['trans'=number:percent], ['width'=number:percent], ['integrated'=light_userdata:preset_handle]}}): nothing

- Miscellaneous:
  - Renamed timecodes and timecode slots property button Toggle Restart Option → previously Restart
Option.

Release Notes 2.5 2026-07-30

  - The readout for Program Time and Executor Time in the custom master section is now seconds →
previously percent.

  - Select, Goto, and Load were removed from the actions in the tags pool.
  - Changed space to semicolon ";" as a delimiter in OSC commands between sequences names and cue
numbers.

  - The camera pool FOV settings now support a value range of 45–120 degrees → previously 60–120
degrees.

  - The default user rights for the Remote user changed to Presets → previously Admin.
  - The default LED background values in the Desk Lights & Color Theme menu have changed to increase
the backlight.

  - Removed None from the user rights. For show files that were saved in previous versions and had user
rights None assigned, the rights are changed to View.

  - Audio In Device and Audio Out Device in the onPC Local Settings are set to None after a clean start and
in a newly installed onPC software. Previously the sound settings would be derived from the system defaults.

  - Moved Off Mode to the new Touch Mode setting. In show files that were saved in previous software
versions and had Off Mode disabled are loaded with Touch Mode set to None. For more information on Touch Mode, see Other Enhancements.

  - Renamed property Phaser Scale in presets → previously Speed Scale.
  - Renamed property Phaser Speedmaster in presets → previously Speed Master.
  - Renamed the value of LearnMode: Learn Ignores Speed Scale → previously Default.
  - The destination number of shapes has changed from 16 to 4 in the data pools. They are now at
destination 4, which was previously number 16. Therefore, the overall structure has changed, and macros that address data pool numbers instead of names need to be adjusted.

  - Renamed the selection option for grandMA3 in the export dialog of the patch: All Stages → previously
Entire Patch.

Release Notes 2.5 2026-07-30

## 4. Bug Fixes

### 3D

#### Description

Deleting fixtures in the patch could lead to shifts of meshes in the 3D viewer.

With Setup enabled in the 3D viewer, tapping Line up in the encoder toolbar did not work as expected so fixtures were not aligned at the base. Instead the fixtures were rotated on allthree axis.

With Setup enabled in the 3D viewer, tapping Directions in the encoder toolbar opened a calculator instead of a drop-down with grid directions X before Y,and Y before X.

On Windows®, changing the GPU to iGPU in the windows settings was ignored by grandMA3 onPC.

With some complex fixtures, the Follow feature ( ) in the 3D viewer did not work as expected.

### Command Line and Macro

#### Description

Oops did not oops recent changes in the camera and appearance pool edit pop-ups. Instead, it closed the edit pop-up.

Cloning color wheel information was not working properly.

if you stored a recipe to a cue part or a preset, insome cases, the cue part or preset would be stored without creating a recipe line.

IfCreate Handles was enabled in the command editor of an encoder bar object, the handle would only appear in the editor and would not be transferred to the command in the object. Executing the object would return "Illegalname" in the command line history.

if you extracted a selective preset and stored itas global, the values would stillbe stored as selective.

if you created a macro with the command Goto Cue 1 Page X.Y with Create Handles enabled, the command would not be converted correctly.

if you set a custom command inan executor and Create Handles was enabled in the command editor and you then imported the show using PSR, the handle would not be imported correctly.

Using Go- or Goto to play back a cue that contained a phaser sometimes would not have the same result as using Go+.

Calling a magic preset, for example Fixture Thru At Preset 21.1, inserted the values from the preset as deactivated values into the programmer.

In preview mode, IfOutput selects all fixtures outputting live onstage instead of only selecting fixtures outputting in preview.

In the onPC software, if you controlled temporary commands such as Flash or Temp with a mouse, the mouse interaction would not behave as expected.

Presets with universal and selective data additionally called selective data If the preset was called using a fixture where only universal data was stored.

After changing preset mode from universal to global, some presets did not indicate global (G) on the pool object.

Itwas not possible to store the remaining time of a timer in a variable if the time value was less than one minute. This bug is fixed. Additionally, the option keyword /Look could be used to write the remaining time into a variable in the same format as itis displayed in the UI.

if you called a preset containing both selective and universal data on another fixture,attributes from the selective data may be applied even ifonly Universal data should be activated.

if you removed global values from a preset with selective, global, and universal data, a warning pop-up about storing universal values was displayed.

Some masters indicated that they are active in the preview environment although they did not influence preview but the liveenvironment.

if you stored grid position values into an empty preset using /Merge, the recalled values would be wrong on the x-axis.

Itwas not possible to use the command line to assign a preset to the absolute value or relative value properties in a phaser recipe.

The software could crash when editing the settings of a preset that contained recipes.

Itwas not possible to use Transfer Selection and Transfer Programmer into preview without a defined sequence.

The software could crash when executing an empty handle, for example, Store #[].

if you used swap inMAtricks, the values in the command line feedback would not be human readable.

Release Notes 2.5 2026-07-30

#### Description

Commands could stillbe executed ifdesk lock was active and the keyboard shortcuts were used to execute the commands.

if you set more than one custom command for an executor, only the lastone would be displayed on the executor but allcommands would be executed.

Handles in custom commands of an executor displayed the internal handle instead of the readable representation of object number and object name.

Itwas possible to store universal and global data to a color preset for the same fixturewithout triggering a Global/Universal conflict warning pop-up. Additionally globally stored C1/CTO/CTC/Tint values were also applied to fixtures of other fixture types.

Merging recipe lines ina cue with directly stored selection and preset data, did not create an additional recipe line. Instead, the cue only contained one recipe line with the information from the second recipe you created.

Store Cue + triggered a pop-up for merging into the next cue with an integer instead of creating a follow up cue, when the cue number ended with a ".9".For example: Store Cue + on cue 1.9 would trigger a merge pop-up forcue 2 instead of creating cue 1.91.

if you used the on-screen keyboard for command line input, pop-ups would not be triggered.

Executing Lua "SelectedSequence():Dump()" with a running sequence displayed the wrong value for the property "CUENO" in the command line history: "CUENO = ""(Read only)". Additionally, when switching off the sequence and executing Lua "SelectedSequence():Dump()" again, the current cue "1" was displayed, instead of "".

Move Grid Cursor was set to Append X instead of Linked in auto created groups.

The CompareHandle() Lua function was documented with an incorrect number of arguments.

The software could crash when playing back a preset (Go+ Preset X) in specific show files.

Some UserAttributePreferences properties, for example TimeLayerResolution or PhaserLayerResolution, were not saved in show filesor streamed innetwork.

Group At Sequence created multiple empty recipe lines when EditRecipe was enabled.

IfCreate Handle was enabled in the command editor, text input with decimal numbers would not be detected correctly and would apply wrong values.

In some cases, executing a valid command would return an illegalproperty error.But the command itselfwould stillbe executed.

if you spun the rotation encoder of a shaper past the maximum or minimum value, you could not immediately spin itin the other direction.

if you labeled an object while storing it,the firstindex setting would be ignored.

In the phaser editor, if you used Off to disable an attribute,then pressed Off a second time, the temporary off menu would be displayed instead of the off keyword being displayed in the command line.

Itwas not possible to copy a recipe linefrom a cue or preset to a programmer part.

Itwas possible to rename structural objects and delete menus in the show file,resulting in parts of the UI and show filesnot working.

Pressing + followed by .removed the "+" from the command line.

Itwas possible to editmeshes that were locked by a user.

IfOn was assigned as press and Off as release for encoders of special executors 30 and 40, the release function Off would not be executed.

In the sequence sheet, the cue command where Create Handle was enabled did not automatically update the handle when the corresponding cue number was changed.

The Lua command DataPool().sequences:SetChildren('autostart',true) could crash the grandMA3 software.

Loading a show filewith corrupted groups could crash the software.

Copying a preset that contains a phaser recipe may cause the software to crash.

In some cases, presets with data of wheels, such as gobo wheels, that were stored as universal would result ininvalid values in other fixture types.

The Blink mode in statuses was too slow to catch attention.

OSC messages including Swap, Temp, or Black commands did not sent the corresponding sequence information anymore.

Ifmany filterswere used ina show file,the grandmA3 software could crash while storing groups.

Itwas not possible to record masters in timecode shows.

Storing an recipe into an preset pool could have caused the software to crash.

The conversion of cue commands referencing labeled presets of the type All to handles using Create Handlee could fail, but cue commands that were not edited were still working.

Release Notes 2.5 2026-07-30

### Connections

#### Description

A particular USB flash drive was not recognized by grandMA3 onPC when running on macOS.

if you loaded a show fileon a console in session, the volume level of the onPC macOS would change.

if you deleted a DMX-key in the output configuration and always automatically inserted a new output configuration fora fader wing, itwould not be possible to change the device type to DMX key.

IfOSC was configured to have a feedback loop to itself and the mode was set to TCP, the UI would freeze during playback.

When rebooting the master console after changes were made on a second connected console, the Session Data Merge pop-up did not appear, preventing the user from selecting the show file that already existed on the second console.

While insession and rebooting a high-priority console (master), tapping Cancel in the Session Data Merge pop-up made the high-priority console idle and the other console standalone.

The MIDI input did not work after a clean start was performed. Instead, MIDI Data Mode had tobe changed in the output configuration first,and then the MIDI input was received again.

In some cases, the software could crash when altering MAtricks values of phaser recipes in macros.

The MIDI Data Mode in the Output Configuration menu had no Off setting.

In a session, playing back a cue with the Goto command, for example Goto Cue 5, then disconnecting and connecting a console again, reloaded the current cue after reconnecting.

Starting the onPC software on macOS would change the sound output.

In some cases, interacting with a filterpool on a web remote would crash the software.

Itwas not possible to assign masters to timecode tracks.

In session, bitmaps sometimes would not work after changing show files.

if you set a gateway in the extended tab of the My Network Interfaces menu, itwould not be saved once you closed the menu.

Handles would not be recogniced in macros If the name contained square brackets. For example "#[Macro 'Test[1]']".

The software could crash ifweb remote displayed a sheet with a filterthat had one of these filter rules: ID Type, Name, Patch, or Environment.

The selected NDI source was not synced over network and changes were not displayed on connected stations.

Changing the multicast base of another station with the command ChangeMulticastBase IP "172.16.70.21" /Type "Alternative" caused the destination station to enter a continuous network initializationloop.

If the multicast base address was changed in the network, it would not automatically unsubscribe from the previous one.

Connecting a node via grandMA3 onPC Terminal App could crash the software.

In a session with two consoles and one console set to high priority,loading a show filefrom USB on the connected console without saving itand then making changes while the master console was rebooting could result in the show filebeing empty after the master console took over the control of the session.

After a crash on a connected station, a fullshow upload was triggered after rejoining the session instead of a partial upload, which lead to long loading operations with bigger show files.

### Patch

#### Description

if you tapped Revert in the edit appearance pop-up ofa fixturetype in the livepatch, the software could crash.

If alocked sequence was imported with PSR, the sequence would be imported without any cues.

Temporary filteringin the Feature column of attribute definitions in the patch did not filter correctly.

The selection pop-up for temporary filtering in the Target Space and Movement Space columns in the patch did not display any values.

if you replaced a fixture type in GDTF format by the same fixture type in XML format in the patch, additional dimmer values were added to color presets that previously had no dimmer values stored.

Fixture types that included modes without real channels (for example, the Bitmap Control fixture) showed a DMX footprint of -1. This bug is fixed.Such fixtures now correctly display a DMX footprint of 0.

In rare cases, the software could freeze when deleting a fixturetype in the patch.

Release Notes 2.5 2026-07-30

#### Description

if there was already a patched fixture in show file and you inserted a second fixture, Insert New Fixtures would open with the Library tab instead of the Show tab.

Exchanging a large number of fixture types in the patch, unpatching and then patching them again, could crash the software.

if you exported an MVR file,names of groups would not be exported.

In some cases, if you deleted fixtures in the patch and set an FID for a fixture,the software would crash.

Some truss MVR files were not affected by Hide Environmental. Therefore, they remained visible when the setting was enabled in the patch.

Names of already existing variables could be lost in show fileafter PSR.

After modifying the order of layers and classes in an MVR fileand re-importing itvia PSR, the changes were not applied. Instead, the fileswere sorted by their fixture type index.

After importing MVR files,unused classes and layers of fixtures could be deleted from the patch.

Changing subfixtures in the patch could break related filterson groups.

Importing a sequence with cues that have different timestamps could lead to cue loss in the newly imported parent sequence due to a comparison process inPSR.

Ifcalling a color preset with universal and global values for multi instance fixtures, the universal values could be deleted in some instances.

Previously exported fileswere not displayed in the Export dialog of the patch when exporting from grandMA3 and Entire Patch. The grandMA3 filewas exported to "gma3_library\patch\stages" while the dialog listed the files of the directory "gma3_library\patch". This bug is fixed.Now, the exported files are listed and the selection option Entire Patch was renamed All Stages.

If SplitView was enabled in the patch, some modes for fixture types were not displayed when unfolding the fixture type with ▶.

Using PSR, show files with illegal fixture type information could cause the software to freeze and a fullinstall was required.

### Phaser

#### Description

if you set a value for measure in a phaser recipe and enabled Adaptive Measure, the measure cell and shape editor would stilldisplay the value that was set manually and you would stillbe able to edit it.

In some cases, if you stored a phaser recipe preset using the command line,the software would freeze or crash.

Phaser data could get lost after certain patch modifications, such as changing the fixture type of an affected phaser.

The software could crash or the station could drop out of a session if you copied a phaser recipe line in a preset. This bug is fixed. This action now triggers a command line error message in the message center.

Imported shapes did not have the correct values when the readout was set to any decimal or hex readout.

Storing a phaser recipe with a selection ina preset with an active Input Filter,displayed the preset as it had no selection and calling the preset did not run the phaser. The preset was only usable with an auto-cook.

Ifmerging template phaser recipes with the same shape but different attributes to a cue, the already existing attributes in the cue recipe linewere overwritten instead of being added to a new line.

Phaser recipes without a selection that had presets as value sources would not listthese presets as references.

The second number in the phaser step indicator would not display the number of total steps for allsteps but the first and last step of the phaser.

In some cases, itwas not possible to add a new value source to a phaser recipe immediately after deleting a value source.

if you imported a phaser recipe preset that had a filteras the attribute, the filterwould not be referenced in the imported preset.

In the recipe editor, the values calculator would always open to the bottom tab. Now, If a preset is set for a different step, the calculator opens to the corresponding tab.

If a phaser recipe was created in the recipe editor without a selection, and a second phaser recipe used the firstrecipe as a source for itsshape, the references would get lost after the recipes were stored in a preset pool.

In rare cases, if you tapped Insert New Value Source in the recipe editor, the software would crash.

Release Notes 2.5 2026-07-30

#### Description

The software could crash when a 65th step was added, for example, by tapping + in the 1D tab in the shapes editor.

### Playback

#### Description

Custom commands were not executed when they were assigned toSpecialExecutor 5 (Grand Master).

if you triggered Top for a sequence that had an off cue with a follow time, in some cases the timing would be inconsistent.

Labels for speed masters would display * If the speed scale was set to one. This bug is fixed.

Now, they will display *If a speed scale is applied to the speed master. Ifspeed scale is one, no * willbe displayed.

Addressing executors using the FromAddr() Lua function, for example Lua "FromAddr('14.14.1.12.1.101')" could crash the software.

In some cases, nodes would crash ifbitmap was used.

Changing the Speed Master or Speed Scale within a cue required reassertion to take effect.

With a phaser recipe ina sequence, a Release preset assigned in the phaser, and Off when Overridden enabled, the phaser stopped immediately when playing back the sequence.

After executing FastSync on a running phaser with an active NShot value, the NShot value was no longer respected.

After setting the timing master to "0" and setting itas the OffCue fade time, then changing the timing master value to a number greater than "0",the cue stilldidn'tfade out and went off immediately.

In some cases, if you removed a recipe line from a cue, itwould not update immediately and the cue would play back as itwas before.

The phaser recipe playback direction was not inherited on assign, for example, when executing Assign Preset 21.1 At Programmer 0.1.

Moving the last cue of a timecode event to the last frame of the duration did not always trigger this cue during playback.

Store Overwrite Cue xdid not refresh the values automatically in the tracking sheet.

In specific show filesfixtures did not move linear totheir fade time when the next cue was triggered which did not contain additional cue info. For example, fixtures could speed up or slow down instead of moving at a constant speed during the fade time.

Release Notes 2.5 2026-07-30

### Windows, Views, and Menus

#### Description

Repetitive Agenda events could have wrong countdown time.

Disabling the sACN input did not update the indicator text,for example "sACN In",in the corresponding pool object of the Universes pool.

Tapping Max in the calculator for editing a color in the encoder bar did not set the value to 100.

Toggle Preview in the Encoder Bar window and Command Wing Bar window was not displayed in the toggle button style.

Universe pool objects stilldisplayed sACN In even ifsACN input was disabled for the universe.

The TCSlot column in the user profile settings was limited to 8 TCSlots instead of 16.

Deleting a layout that was displayed in the layout viewer, and then selecting <Link Selected> in Layout of the layout viewer, displayed multiple Lua errors in the system monitor.

A number of presets were grayed out, even though they could be selected if you worked in another world, except "World 1".

Assigning a tag to a sequence using the label pop-up of an executor, did not display the tag in the "Assigned" area of the pop-up, even though the tag was assigned to sequence.

Shuffle was missing in the MAtricks editor of the recipe editor.

if you tapped and selected a value source of a phaser recipe in the sequence sheet, a blank recipe editor would open.

Tapping NShot Stay multiple times, did not toggle between Yes and No. Instead it displayed a numeric value.

The displayed parameter count in the tooltip for the status "Not Enough Parameters" did not match the parameter count in the system info window.

If you tried to select text in pop-ups, it would sometimes be only partiallyselected.

Reset Blades in the special dialog did not reset the value. Instead, the value was set to 0.

Enabling Edit title bar in the selection grid window settings, did not display the Title Buttons tab in the settings.

if you had two Shaper dialog windows next to each other, one in Graphical and the other one in Faders view, and then turned the encoder bar shaper encoders for each shaper, the result would be different in the two views.

if you moved a large range of DMX universes, for example by executing Move DMXUniverse 492 Thru 882 At 100, and oopsed this task, this action could freeze the UI.

Temporary filteringin the Action column of the agenda window did not work as expected.

In the calculator for individual fade and delay times, a 0 would be added every time the calculator was opened.

IfGroup by Attribute was enabled in the recipe editor,Insert Step would be grayed out and disabled after adding a step to the recipe.

if you opened the Add Window pop-up, some UI elements, such as pool objects and layouts would not get darker.

The Store View pop-up on screens 6 and 7 did not open in the center of the screen and was slightly too big for the two screens.

Temporary filteringin the agenda viewer was not correctly retrieved.

if you assigned an object to a layout element, the vertical text alignment in the layout element would change to Above, regardless of the previous alignment.

Flash did not work in the pool actions forthe tags pool and ListRef was not available in the pool action for the tags pool.

In the recipe editor,if you pinned the context area in the MAtricks Editor tab and tapped another cell in the recipe grid, the context area would sometimes go blank.

If the context area in the recipe editor was pinned and you cleared the programmer, the pinned context area would stillbe displayed.

if you pinned the MAtricks editor in the context area of the preset editor and turned the preset into a recipe or added a recipe, the MAtricks editor would break.

In the recipe editor,you could open the tabs Pool and Sheet in the context area, even though the displayed values could not be selected.

if you were in Edit Recipe mode and pressed MA, a yellow frame would be displayed around selected pool objects instead of the green frame.

The software could crash if you increased the height of a layout element via encoder rotation.

if you set a range of attribute values in multiple fixtures in the content sheet or track sheet, for example, 21 through 30, itwould result in a long loading operation and the value 21 would be applied to allselected fixtures.

In the Encoder Bar, the wrong physical values would be shown if Highlight was active while the highlight value was in the same range on another channel function.

An unused user profilewould require confirmation ifitwas deleted.

Release Notes 2.5 2026-07-30

#### Description

was not displayed inreferenced pool objects in the executor configuration pool.

Editors that display the lock icon would not update and change correctly between lock icon and pool icon if you locked or unlocked the object.

The virtual keyboard in the Lua input editor would stretch across the whole window regardless of the window size.

Appearances could stillbe edited ifthey were locked.

The input value range of relative calculator values did not match with the value set inReadout.

For example, with Percent selected in Readout, it was not possible to put in negative values.

The World Master status was not displayed if a world that was not selected was assigned to an executor and was not at 100%.

The Timecode Viewer was missing the Tags column, which would appear when at least one single track was added.

In the tags pool, the default pool action List Reference was not available anymore.

The tooltips of shapes pool objects were misleading.

Tapping Adjust Shape in the context area of the recipe editor did not take you directly to the Editor tab of the shape column. Instead, the Pool tab was displayed.

In the bitmap editor,if you tapped an encoder icon, the calculator would open.

Opening the context area for recipes in a preset and tap ,closing the editor again and opening any editor for a preset again, was stillactive and the context area was pinned to the column that was selected before.

If a preset contained a recipe, Recast Preset was not available and grayed out in the preset editor.

Selective presets with Preset Mode set to Global, did not display "G S" on the preset pool object.

In the Fixture Sheet with Preview enabled, show filescould display markers from the Live environment, such as Phaser markers.

The temporary pool menu (opens when pressing List+Preset) did not follow the selected feature group and only displayed the Dimmer pool.

The Trig Type BPM in the Sequence Sheet was not working.

The dynamic function "EditRecipe" ,such as Edit StandardRecipe 1, in the editsettings of a preset pool, was not available.

The Edit tab in the assign menu was empty, after closing the temporary MAtricks editor while creating a recipe.

In the My Interfaces menu in the extended mode, the two-finger tap would only work in the table, not in the empty area below the table.

When Lock Position was enabled in the Layout Viewer window, the Lasso Filter button was grayed out.

In preview, the fixture sheet inDimmer+ or Sheet/Filter mode did not display playback values.

if you created a new MAtricks object in the recipe editor, the firstindex that was set in the MAtricks pool settings would not be adopted.

Filters would not be applied to phaser recipe presets that had no selection and were used in standard recipes.

In some cases, the MAtricks header in the recipe grid of a preset would not be expandable.

Template recipe presets with a selection would not display a feature group indicator bar.

Cues that included a standard recipe with a phaser recipe preset as the value would not display the preset name in the cue.

In some cases, MAgic presets would be grayed out even ifthey could be applied to the current selection.

If the MAtricks header in the recipe editor was collapsed and you moved the column, the software would crash.

if you deleted a mirrored sequence, the mirror icon would not disappear in the other sequence immediately.

In a session, if you set a default cue part for an All preset pool, phasers that were stored in that pool would not run if you called them into the programmer on a connected station.

With a Readout set to Decimal8, editing a WithX value of a shape, the calculator offered a range of "0" to "0".

if you added a phaser recipe after adding a standard recipe, the column order and sorting would be different than if you added a phaser recipe first.

In some cases, previewing an object, and then leaving preview mode, stilldisplayed the preview encoder bar instead of the liveencoder bar.

In some cases, the status for Highlight was active with the "ext"marker, even though no highlight was active.

The feedback when a cue was loaded (Load Cue)was not displayed in the corresponding pool object.

Release Notes 2.5 2026-07-30

#### Description

Double-tapping on an executor configuration in the assign menu would overwrite the executor configuration.

If the selected attribute in the encoder bar was unavailable for the newly selected fixture,the encoder bar would automatically switch to an available attribute. However, the dynamic preset pool would not follow accordingly.

In some cases, Display Mode in the playback window settings displayed a number instead of Text+Icon, Text, or Icon.

In some cases, the scrolling behavior in pools was not working as expected after resizing pools on consoles. Scroll positions changed unexpectedly, and the focus on pool objects sometimes shifted.

Hovering over the network status icon when itwas green, changed the color of the icon to white implying a different status.

When MA was latched in the command section, the text on the Deactivate, Programmer, ListReference, FixtureType, FeatureGroup and AlignTrans buttons was cut off.

In the Scribble editor, the last drawn linecould not be removed by pressing Oops.

Referencing shapes in two phaser recipe lines in cues or presets to each other, would lead to a freeze in the software.

The web remote login pop-up could disappear after resizing the browser window, potentially allowing access without entering the required password.

Parts of the UI remained darkened after closing the update menu on multi-screen devices until additional user interaction occurred, such as tapping anywhere in the UI or pressing ESC twice.

The preset update indicator was displayed in the sequence update color. Presets now correctly use the cyan update indicator, while sequences use the yellow update indicator.

Loading a stored view including the message center did remove the filteringand the title bar was not updated when changing the category filter.

With Split View enabled inpatch, and were hidden in the title bar instead of grayed out.

The attribute toggle buttons above the curves in1D tab of the shapes editor displayed <No Attribute or Filter> instead of <From Preset> with a preset selected as a value source.

Pressing Oops after deleting a mesh, did not restore the link from the model to the mesh.

Therefore they were also not displayed in the 3D viewer anymore.

When selecting multiple cells with Track Sheet enabled in the sequence sheet and entering a value range in the calculator (for example, “21 Thru 30”), the value range was not applied. Instead, allselected cells were assigned the same value.

Changing the POV fader in the Shapers tab of the special dialog with multiple fixtures selected, and then going through the selection with Next, applied the changed POV value only to the last fixture.

The MAtricks columns in the recipe editor were sorted differently depending on whether a standard or a phaser recipe was added.

Previewing a mirrored sequence, put another sequence from the pool inpreview.

With Adaptive Measure enabled, the measure column of phaser recipes was stilldisplaying a value and was not indicated as blocked, even though the value was invalid with adaptive measure active.

The Update menu of presets with Preset Update Mode set to Add New Content did not listin some cases toall presets that can be updated.

If a selected sequence was disabled, the Info window would not refresh and would stilldisplay the current cue.

After executing the command Lua "DumpAllHooks()" multiple times, the System Monitor output became unreadable because several lines of text overlapped.

Tapping and holding on a Selection cell of a recipe line of a sequence, opened the edit pop-up of a group, but displayed data of the sequence.

In some cases, the desk lock would flicker If a pop-up was open while desk lock was activated.

Values in the 3D viewer and layout viewer Setup encoder bar were calculated wrong using + or *, for example setting Pos Z to "4 thru 5" in the calculator, and then enter "+1",did not set the values to "5 thru 6".

The timecode slot indicator in the upper-left corner of the Timecode Pool object did not display the correct number forthe selected timecode slot.

The input pop-up for the Absolute cell in the phaser recipe editor opened with the wrong tab of presets on the right side of the pop-up.

In the pool tab of the context area in the recipe editor, the name of the pool was not displayed.

if you tapped on the fader area in an encoder bar window while the setting Encoder Label was disabled, a calculator would open but itwould not be possible to apply values in it.

if you changed the custom text of a layout element, the text on the element would only change

Release Notes 2.5 2026-07-30

#### Description

after updating the layout.

The temporary views pool wrongly had a data pool setting in the title bar.

With Delete + Menu, itwas possible to delete the main menu, so itcould not be opened anymore.

After selecting a new encoder bar,the programmer indicator would be wrong.

In the running playbacks window and off menu insheet style, the number that indicates the total number of cues in brackets in the No column would include cue zero and the off-cue.

In the timecode viewer, columns that were hidden would reappear after selecting an empty timecode object.

if you cut events in the timecode viewer, they would not be indicated as such.

With some fixture types, the shaper rotation in the special dialog window turned in the oppesite direction as expected.

Some valid presets were incorrectly discarded for a step value in the context area for the Absolute Value cellin the recipe editor.

Deleting a quickey as a layout element, printed "Delete" in the command line every time Clear was pressed.

Itwas not possible to edit a quickey as a layout element in the layout viewer.

In the Info window, the tab counter when ListReference was executed and Tabs in the window settings was disabled, was incorrect.

if you converted a phaser preset into a phaser recipe, warning pop-up would not appear. This bug isfixed and now a pop-up warns users that the values willbecome hard values.

The active datapool would not be transferred to preview if Transfer Selection and Transfer Programmer were enabled.

In an timecode event, itwas not possible to enter Fade Override 0 inan empty cell.

In the layout viewer, the size of the displayed scribbles and appearances changed in previous versions.

In the sequence sheet in the Adjust MAtricks pop-up, it was not possible toopen the Fade From X calculator.

Editing cells for attributes, for example, for dimmer in the tracking sheet, displayed no matching preset pool objects in the calculator.

If closing the off menu, some graphical issues were visible for a second.

Executing a Clear quickey printed an echo with "MSTATE = 1!"in the system monitor.

In preview mode, the encoder bar window and the command wing bar displayed the wrong name for Preview Bar. Also the encoders inside the corresponding window would not update ifPreview Bar was toggled.

Quickeys assigned with MA1 or MA2 codes could not be unlatched.

Itwas not possible to latch Prvw in the command section on grandMA3 onPC.

In a specific show file,the number of phasers displayed in the phaser bar in the command line would not decrease if ClearAll was executed after the phaser bar was drastically increased.

Migrated show filescould omit the pie charts in presets, for example, for appearances without an associated image. Additionally, appearances could be wrongly displayed in front of preset pie charts.

The battery pop-up was missing the state of charge icon ingrandMA3 devices with UPS battery.

if you tapped a MAtricks recipe line,allNone columns in the Editor tab of the contextual area would receive '..'characters after Adjust MAtricks was tapped.

Itwas not possible to lock a recipe line in the preset editor via the Lock column. Also the lock state was expected inLua and you could not set itvia a property.

Screenshots of NDI streams would swap the colors red and blue.

In some cases, the Display pop-up that opens with the menu pop-up would be empty on onPC rack-units.

Ifdeleting multiple objects, for example Delete Sequence Thru, and some of the objects were locked, the command line response did not show the correct information.

Property controls in a network menu could get stuck in a disabled state. IfReloadUI was executed, the property controls were enabled again.

The encoder bar window would not reset If the preview preparation bar was canceled using Esc.

Release Notes 2.5 2026-07-30

6. Deprecated
> **Hint:** The following is deprecated and will be removed in the software in the near future. Make sure you read the sections stated below, so you can adjust your macros and plugins accordingly, if necessary.

- The Lua function HasActivePlayback() is deprecated. It was replaced by IsRunningPlayback(). For more information
on the new Lua function IsRunningPlayback() see Release Notes 2.4.

- /Selective combined with CleanUp no longer works if used to clean up recipes. This command now works with the
/Type option keyword and "Recipe" as the modifier instead of /Selective. For more information see the /Type option keyword.

Release Notes 2.5 2026-07-30

7. Appendix
- We recommend you use a dedicated and a separate physical network for each grandMA3 session.
- When using DMX protocols we recommend you use a dedicated physical network for each protocol.
- XML fileswith exported executor configurations from grandMA3 version 1.2 and priorcannot be properly imported to
grandMA3 version 1.3 orlater due tostructural changes.

- XML fileswith exported analog remote setups from grandMA3 version 1.3 and priorcannot be properly imported to
grandMA3 version 1.4 orlater due tostructural changes.

- XML fileswith exported timecode shows from grandMA3 version 1.3 and prior cannot be properly imported to
grandMA3 version 1.4 orlater due tostructural changes.

Release Notes 2.5 2026-07-30

8. Known Limitations
Software update via network to onPC stations requires confirmation during the install process at the destination system.

Ifmultiple GlobalMasters exist on the network, each with the same session and location name, the station with the higher priority willtake over automatically.

If all stations have the same priority,the station with the longest Online Time becomes the GlobalMaster of all stations.

Recast willonly recast presets to cues if there is a preset linkin the absolute layer.

Loading show filesthat were saved in previous versions deletes the programmer content.

Ifshow filesof approximately 500 MB or more are loaded into PSR, the progress bar may not be displayed in the user interface.
