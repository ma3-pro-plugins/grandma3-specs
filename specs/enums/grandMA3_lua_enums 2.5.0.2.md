---
source: typings
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/plugins.html"
---

# Lua Enums (MA 2.5.0.2)

**typings** catalog from [`grandma3-ts-types`](https://github.com/ma3-pro-plugins/grandma3-ts-types) `Enums.d.ts` (generated from the console `Enums` table on MA **2.5.0.2**). Target is **2.5.0.3** — this is the closest dump. Not Official. Do not hand-edit members.

How to use in a plugin: [`../enums.md`](../enums.md).

Grep a heading. Each member is `` `Name`=value ``. Lua: `Enums.Name.Member` when both are identifiers; otherwise `Enums["Name"]["Member"]`.

681 enums, 5655 members.

## ALSideSizeSpecial

`Hybrid`=-1 `Auto`=0

`Enums.ALSideSizeSpecial.Hybrid`

## ActiveDisplay

`Wave`=0 `Sound`=1 `Beat`=2

`Enums.ActiveDisplay.Wave`

## AgendaMode

`Absolute`=0 `Dawn`=1 `Sunrise`=2 `Sunset`=3 `Dusk`=4

`Enums.AgendaMode.Absolute`

## AgendaTool

`Select`=0 `Store`=1 `Delete`=2 `Cut`=3 `Copy`=4 `Paste`=5 `Call`=6 `Edit`=7

`Enums.AgendaTool.Select`

## AgendaViewMode

`Sheet`=0 `Year`=1 `Month`=2 `Week`=3 `Day`=4

`Enums.AgendaViewMode.Sheet`

## AlignMode

`Off`=0 `/`=1 `<`=2 `>`=3 `><`=4 `<>`=5

`Enums.AlignMode.Off`

## AlignmentH

`Center`=0 `Left`=1 `Right`=2

`Enums.AlignmentH.Center`

## AlignmentV

`Center`=0 `Top`=1 `Bottom`=2

`Enums.AlignmentV.Center`

## ArrangementMarcType

`Small`=0 `Dynamic`=1

`Enums.ArrangementMarcType.Small`

## ArtNetBroadcastThreshold

`Default(5)`=5

`Enums.ArtNetBroadcastThreshold["Default(5)"]`

## ArtNetDataMode

`Broadcast`=0 `Unicast`=1 `Auto`=2 `Input`=3

`Enums.ArtNetDataMode.Broadcast`

## ArtNetTimecodeMode

`Broadcast`=0 `Unicast`=1 `Input`=2

`Enums.ArtNetTimecodeMode.Broadcast`

## AssignType

`Empty`=0 `View`=1 `Macro`=2 `Plugin`=3 `Menu`=4 `Group`=5 `World`=6 `Sequence`=7 `Master`=8 `Sound`=9 `User`=10 `ScreenConfig`=11 `Fixture`=12 `MAtricks`=13 `Video`=14 `Preset`=15 `Quickey`=16 `Timer`=17 `EncoderBar`=18 `Filter`=19 `Executor`=20 `Station`=21 `Tag`=22 `Shape`=23

`Enums.AssignType.Empty`

## AssignmentButtonFunctions

``=0 `Empty`=0 `Flash`=1 `Black`=2 `Go+`=3 `Go-`=4 `>>>`=5 `<<<`=6 `On`=7 `Off`=8 `Learn`=9 `LearnSpeed`=10 `Rate1`=11 `Speed1`=12 `Temp`=13 `Toggle`=14 `Top`=15 `Goto`=16 `Load`=17 `Pause`=18 `Time`=22 `Select`=24 `Swap`=25 `HalfSpeed`=26 `DoubleSpeed`=27 `Kill`=29 `ReSync`=30 `FastSync`=31 `At`=48 `LogIn`=74 `Call`=112 `SelectFixtures`=124

`Enums.AssignmentButtonFunctions.Empty`

## AssignmentButtonFunctionsBlind

``=0 `Empty`=0 `On`=7 `Off`=8 `Toggle`=14

`Enums.AssignmentButtonFunctionsBlind.Empty`

## AssignmentButtonFunctionsGrandMaster

``=0 `Empty`=0 `On`=7 `Off`=8 `Toggle`=14

`Enums.AssignmentButtonFunctionsGrandMaster.Empty`

## AssignmentButtonFunctionsGroup

``=0 `Empty`=0 `SelectFixtures`=124

`Enums.AssignmentButtonFunctionsGroup.Empty`

## AssignmentButtonFunctionsHighlightSolo

``=0 `Empty`=0 `On`=7 `Off`=8 `Toggle`=14

`Enums.AssignmentButtonFunctionsHighlightSolo.Empty`

## AssignmentButtonFunctionsMacro

``=0 `Empty`=0 `Go+`=3 `Go-`=4 `>>>`=5 `<<<`=6 `Off`=8 `Pause`=18 `Call`=112

`Enums.AssignmentButtonFunctionsMacro.Empty`

## AssignmentButtonFunctionsPlaybackMaster

``=0 `Empty`=0

`Enums.AssignmentButtonFunctionsPlaybackMaster.Empty`

## AssignmentButtonFunctionsPlugin

``=0 `Empty`=0 `Go+`=3 `Go-`=4 `>>>`=5 `<<<`=6 `On`=7 `Off`=8 `Learn`=9 `LearnSpeed`=10 `Rate1`=11 `Speed1`=12 `Toggle`=14 `Top`=15 `Goto`=16 `Load`=17 `Pause`=18 `HalfSpeed`=26 `DoubleSpeed`=27 `ReSync`=30 `FastSync`=31 `Call`=112

`Enums.AssignmentButtonFunctionsPlugin.Empty`

## AssignmentButtonFunctionsPreset

``=0 `Empty`=0 `Go+`=3 `>>>`=5 `On`=7 `Off`=8 `Learn`=9 `LearnSpeed`=10 `Rate1`=11 `Speed1`=12 `Toggle`=14 `Pause`=18 `HalfSpeed`=26 `DoubleSpeed`=27 `Kill`=29 `ReSync`=30 `FastSync`=31 `At`=48 `SelectFixtures`=124

`Enums.AssignmentButtonFunctionsPreset.Empty`

## AssignmentButtonFunctionsQuickey

``=0 `Empty`=0 `Go+`=3

`Enums.AssignmentButtonFunctionsQuickey.Empty`

## AssignmentButtonFunctionsRate

``=0 `Empty`=0 `On`=7 `Off`=8 `Rate1`=11 `Toggle`=14 `Pause`=18

`Enums.AssignmentButtonFunctionsRate.Empty`

## AssignmentButtonFunctionsScreenConfig

``=0 `Empty`=0 `Call`=112

`Enums.AssignmentButtonFunctionsScreenConfig.Empty`

## AssignmentButtonFunctionsSequence

``=0 `Empty`=0 `Go+`=3 `Go-`=4 `>>>`=5 `<<<`=6 `On`=7 `Off`=8 `Learn`=9 `LearnSpeed`=10 `Rate1`=11 `Speed1`=12 `Toggle`=14 `Top`=15 `Goto`=16 `Load`=17 `Pause`=18 `Select`=24 `HalfSpeed`=26 `DoubleSpeed`=27 `Kill`=29 `ReSync`=30 `FastSync`=31 `SelectFixtures`=124

`Enums.AssignmentButtonFunctionsSequence.Empty`

## AssignmentButtonFunctionsSoundFile

``=0 `Empty`=0 `Go+`=3 `On`=7 `Off`=8 `Toggle`=14 `Pause`=18

`Enums.AssignmentButtonFunctionsSoundFile.Empty`

## AssignmentButtonFunctionsSoundMaster

``=0 `Empty`=0 `On`=7 `Off`=8 `Toggle`=14

`Enums.AssignmentButtonFunctionsSoundMaster.Empty`

## AssignmentButtonFunctionsSpeed

`Empty`=0 ``=0 `On`=7 `Off`=8 `Learn`=9 `LearnSpeed`=10 `Speed1`=12 `Toggle`=14 `Pause`=18 `HalfSpeed`=26 `DoubleSpeed`=27 `ReSync`=30 `FastSync`=31

`Enums.AssignmentButtonFunctionsSpeed.Empty`

## AssignmentButtonFunctionsTag

``=0 `Empty`=0 `Go+`=3 `Go-`=4 `>>>`=5 `<<<`=6 `On`=7 `Off`=8 `Learn`=9 `LearnSpeed`=10 `Rate1`=11 `Speed1`=12 `Toggle`=14 `Top`=15 `Goto`=16 `Load`=17 `Pause`=18 `Select`=24 `HalfSpeed`=26 `DoubleSpeed`=27 `Kill`=29 `ReSync`=30 `FastSync`=31 `SelectFixtures`=124

`Enums.AssignmentButtonFunctionsTag.Empty`

## AssignmentButtonFunctionsTimecode

``=0 `Empty`=0 `Go+`=3 `Go-`=4 `>>>`=5 `<<<`=6 `On`=7 `Off`=8 `Learn`=9 `LearnSpeed`=10 `Rate1`=11 `Speed1`=12 `Toggle`=14 `Top`=15 `Goto`=16 `Load`=17 `Pause`=18 `Select`=24 `HalfSpeed`=26 `DoubleSpeed`=27 `Kill`=29 `ReSync`=30 `FastSync`=31 `At`=48 `LogIn`=74 `Call`=112 `SelectFixtures`=124

`Enums.AssignmentButtonFunctionsTimecode.Empty`

## AssignmentButtonFunctionsTimer

``=0 `Empty`=0 `Go+`=3 `Off`=8 `Toggle`=14 `Top`=15 `Pause`=18

`Enums.AssignmentButtonFunctionsTimer.Empty`

## AssignmentButtonFunctionsUser

``=0 `Empty`=0 `LogIn`=74

`Enums.AssignmentButtonFunctionsUser.Empty`

## AssignmentButtonFunctionsView

``=0 `Empty`=0 `Call`=112

`Enums.AssignmentButtonFunctionsView.Empty`

## AssignmentButtonFunctionsWorld

``=0 `Empty`=0 `On`=7 `Off`=8 `Toggle`=14 `SelectFixtures`=124

`Enums.AssignmentButtonFunctionsWorld.Empty`

## AssignmentButtonUnpressFunctions

``=0 `Empty`=0 `Go+`=3 `Go-`=4 `>>>`=5 `<<<`=6 `On`=7 `Off`=8 `Learn`=9 `LearnSpeed`=10 `Rate1`=11 `Speed1`=12 `Toggle`=14 `Top`=15 `Goto`=16 `Load`=17 `Pause`=18 `Select`=24 `HalfSpeed`=26 `DoubleSpeed`=27 `Kill`=29 `ReSync`=30 `FastSync`=31 `At`=48 `LogIn`=74 `Call`=112 `SelectFixtures`=124

`Enums.AssignmentButtonUnpressFunctions.Empty`

## AssignmentFaderFunctions

`Empty`=0 ``=0 `Master`=35 `X`=36 `XA`=37 `XB`=38 `Temp`=39 `Rate`=40 `Speed`=41 `Time`=45

`Enums.AssignmentFaderFunctions.Empty`

## AssignmentFaderFunctionsMasterOnly

``=0 `Empty`=0 `Master`=35

`Enums.AssignmentFaderFunctionsMasterOnly.Empty`

## AssignmentFaderFunctionsNone

``=0 `Empty`=0

`Enums.AssignmentFaderFunctionsNone.Empty`

## AssignmentFaderFunctionsPreset____

``=0 `Empty`=0 `Master`=35 `Temp`=39 `Rate`=40 `Speed`=41 `Time`=45

`Enums.AssignmentFaderFunctionsPreset____.Empty`

## AssignmentFaderFunctionsSubTrack

`Master`=1 `X`=2 `XA`=3 `XB`=4 `Temp`=5 `Rate`=6 `Speed`=7 `Time`=11

`Enums.AssignmentFaderFunctionsSubTrack.Master`

## AssignmentProgExecButtonTimeFunctions

``=0 `Empty`=0 `On`=7 `Off`=8 `Toggle`=14

`Enums.AssignmentProgExecButtonTimeFunctions.Empty`

## AssignmentProgExecButtonXFunctions

``=0 `Empty`=0 `On`=7 `Off`=8 `Toggle`=14

`Enums.AssignmentProgExecButtonXFunctions.Empty`

## AssignmentTimingFunctions

``=0 `Empty`=0

`Enums.AssignmentTimingFunctions.Empty`

## AttributeMode

`PanTilt`=0 `XY`=1 `XZ`=2 `YZ`=3

`Enums.AttributeMode.PanTilt`

## AttriebuteEncoderResolution

`Native`=-16777216 `Increment`=167772 `Fine`=1677721 `Coarse`=16777216

`Enums.AttriebuteEncoderResolution.Native`

## AttriebuteEncoderResolutionDefault

`Native`=-16777216 `Default`=0 `Increment`=167772 `Fine`=1677721 `Coarse`=16777216

`Enums.AttriebuteEncoderResolutionDefault.Native`

## AttriebuteEncoderResolutionSmall

`Increment`=167772 `Fine`=1677721 `Coarse`=16777216

`Enums.AttriebuteEncoderResolutionSmall.Increment`

## AutoCreateSource

`FixtureType Presets`=0 `ChannelSets`=1

`Enums.AutoCreateSource.ChannelSets`

## AutoInterface

`Auto`=0

`Enums.AutoInterface.Auto`

## AutoLayoutScrollType

`Vertical`=0 `Horizontal`=1 `Auto`=2

`Enums.AutoLayoutScrollType.Vertical`

## AutoSaveMode

`Off`=0 `5 Minutes`=1 `15 Minutes`=2 `30 Minutes`=3 `60 Minutes`=4 `120 Minutes`=5 `360 Minutes`=6

`Enums.AutoSaveMode.Off`

## AutoStomp

`Off`=0 `Prio`=1 `On`=2

`Enums.AutoStomp.Off`

## AxisGroupType

`XY`=0 `XZ`=1 `YZ`=2

`Enums.AxisGroupType.XY`

## AxisSystem

`Stage`=0 `Object`=1

`Enums.AxisSystem.Stage`

## BackdropPatchType

`Nine`=0 `Frame`=1 `ThreeVertical`=2 `ThreeHorizontal`=3

`Enums.BackdropPatchType.Nine`

## BackupBrowserFilter

`Shows`=0 `Backups`=1 `Demoshows`=2 `Templates`=3

`Enums.BackupBrowserFilter.Shows`

## BeamMode

`No Beam`=0 `Line`=1 `Standard`=2 `High`=3 `High Fancy`=4

`Enums.BeamMode.Line`

## BeamModePatch

`Line`=1 `Simple`=2

`Enums.BeamModePatch.Line`

## BeamType

`Wash`=0 `Spot`=1 `None`=2 `Rectangle`=3 `PC`=4 `Fresnel`=5 `Glow`=6

`Enums.BeamType.Wash`

## BlinkingButtonMode

`Prog`=0 `Exec`=1

`Enums.BlinkingButtonMode.Prog`

## BloomIntensity3d

`Off`=0 `On`=1

`Enums.BloomIntensity3d.Off`

## BodyQuality3d

`None`=0 `Box`=1 `Low`=2 `Simple`=3 `Standard`=4 `High`=5 `Ultra`=6

`Enums.BodyQuality3d.None`

## BodyQuality3dPatch

`Box`=1 `Standard`=4 `Ultra`=6

`Enums.BodyQuality3dPatch.Box`

## BounceType

`No`=0 `Yes`=1 `Compensated`=2

`Enums.BounceType.No`

## BuildType

`Release`=0 `Debug`=1 `Asan`=2

`Enums.BuildType.Release`

## ButtonHeight

`20`=20 `25`=25 `30`=30 `35`=35 `40`=40 `45`=45 `Default`=50 `50`=50 `55`=55 `60`=60

`Enums.ButtonHeight.Default`

## ButtonModeFunction

`Full / Zero`=0 `Flash / Black`=1

`Enums.ButtonModeFunction["Full / Zero"]`

## ButtonModeFunctionSpeedMaster

`Learn`=0 `Speed1`=1

`Enums.ButtonModeFunctionSpeedMaster.Learn`

## CachedObjectSource

`Resource`=0 `Library`=1 `Showfile`=2

`Enums.CachedObjectSource.Resource`

## CalculatorMode

`Double`=0 `Decimal`=1 `Hex`=2 `TimeHz`=3 `TimeBPM`=4 `Seconds`=5 `SpeedHz`=6 `SpeedBPM`=7 `SpeedSec`=8 `Dec8`=9 `Dec16`=10 `Dec24`=11 `Hex8`=12 `Hex16`=13 `Hex24`=14 `Percent`=15 `JointTime`=16 `fps24`=17 `fps25`=18 `fps30`=19 `fps60`=20

`Enums.CalculatorMode.Double`

## CameraMode

`3D`=0 `2D_Front`=1 `2D_Left`=2 `2D_Top`=3 `2D_Right`=4 `2D_Back`=5

`Enums.CameraMode["3D"]`

## CameraType

`Auto`=0 `Front`=1 `Front/Left`=2 `Left`=3 `Back/Left`=4 `Back`=5 `Back/Right`=6 `Right`=7 `Front/Right`=8 `Top`=9

`Enums.CameraType.Auto`

## CategoryName

`Undefined`=0 `System`=1 `Command Line`=2 `Power`=3 `MA-Net`=4 `USB`=5 `Chat`=6

`Enums.CategoryName.Undefined`

## CellGrouping

`SizeDriven`=4294967295

`Enums.CellGrouping.SizeDriven`

## ChangeLevel

`File`=0 `Remove`=1 `Insert`=2 `Exchange`=3 `Move`=4 `Layout`=5 `Delete`=6 `Create`=7 `Full`=8 `FullWithoutContent`=9 `Structural`=10 `Property`=11 `MyProperty`=12 `Little`=13 `None`=14

`Enums.ChangeLevel.File`

## ChannelFilterMode

`Active For Selected`=2 `All For Selected`=3 `Active`=4 `All`=5

`Enums.ChannelFilterMode.Active`

## ChannelFrequency

`60`=0 `30`=1 `15`=2 `Slow1`=3 `Slow2`=4 `Slow3`=5

`Enums.ChannelFrequency.Slow1`

## ChannelSetReadoutMode

`Value`=0 `Value+Name`=1 `Name`=2

`Enums.ChannelSetReadoutMode.Value`

## ChildrenFillPolicy

`Default`=0 `RowFirst`=1 `ColumnFirst`=2

`Enums.ChildrenFillPolicy.Default`

## CleanupOperation

`None`=0 `NoReference`=1 `Recipe`=4 `Duplicates`=8 `StackAll`=16 `GridPosition`=32

`Enums.CleanupOperation.None`

## ClipMode

`None`=0 `Clip`=1 `Wrap`=2

`Enums.ClipMode.None`

## ClockSources

`Session Time`=0 `Timecode`=1 `Time Zone`=2 `Timer`=3

`Enums.ClockSources.Timecode`

## CloningWindowMode

`Sheet`=0 `Grid`=1 `Layout`=2

`Enums.CloningWindowMode.Sheet`

## CmdEventStatus

`Off`=0 `On`=1

`Enums.CmdEventStatus.Off`

## ColorDisplayMode

`RGB`=1 `CMY`=2

`Enums.ColorDisplayMode.RGB`

## ColorDisplayModeAuto

`Auto`=0 `RGB`=1 `CMY`=2

`Enums.ColorDisplayModeAuto.Auto`

## ColorEncoderFunction

`Auto`=0 `HSB`=1 `RGB`=2 `CMY`=3 `CIE`=4

`Enums.ColorEncoderFunction.Auto`

## ColorMixMode

`Fixture Type`=0 `Rec.709`=1 `Rec.2020`=2 `Standard`=3

`Enums.ColorMixMode.Standard`

## ColorPickerWindowMode

`CIE`=0 `HSB`=1 `Fader`=2 `Book`=3

`Enums.ColorPickerWindowMode.CIE`

## ColorSample

`CES01`=0 `CES02`=1 `CES03`=2 `CES04`=3 `CES05`=4 `CES06`=5 `CES07`=6 `CES08`=7 `CES09`=8 `CES10`=9 `CES11`=10 `CES12`=11 `CES13`=12 `CES14`=13 `CES15`=14 `CES16`=15 `CES17`=16 `CES18`=17 `CES19`=18 `CES20`=19 `CES21`=20 `CES22`=21 `CES23`=22 `CES24`=23 `CES25`=24 `CES26`=25 `CES27`=26 `CES28`=27 `CES29`=28 `CES30`=29 `CES31`=30 `CES32`=31 `CES33`=32 `CES34`=33 `CES35`=34 `CES36`=35 `CES37`=36 `CES38`=37 `CES39`=38 `CES40`=39 `CES41`=40 `CES42`=41 `CES43`=42 `CES44`=43 `CES45`=44 `CES46`=45 `CES47`=46 `CES48`=47 `CES49`=48 `CES50`=49 `CES51`=50 `CES52`=51 `CES53`=52 `CES54`=53 `CES55`=54 `CES56`=55 `CES57`=56 `CES58`=57 `CES59`=58 `CES60`=59 `CES61`=60 `CES62`=61 `CES63`=62 `CES64`=63 `CES65`=64 `CES66`=65 `CES67`=66 `CES68`=67 `CES69`=68 `CES70`=69 `CES71`=70 `CES72`=71 `CES73`=72 `CES74`=73 `CES75`=74 `CES76`=75 `CES77`=76 `CES78`=77 `CES79`=78 `CES80`=79 `CES81`=80 `CES82`=81 `CES83`=82 `CES84`=83 `CES85`=84 `CES86`=85 `CES87`=86 `CES88`=87 `CES89`=88 `CES90`=89 `CES91`=90 `CES92`=91 `CES93`=92 `CES94`=93 `CES95`=94 `CES96`=95 `CES97`=96 `CES98`=97 `CES99`=98

`Enums.ColorSample.CES01`

## ColorSource

`Red`=0 `Green`=1 `Blue`=2 `Alpha`=3 `Intensity`=4 `Const`=5

`Enums.ColorSource.Red`

## ColorSpaceMode

`sRGB`=0 `ProPhoto`=1 `ANSI`=2 `Custom`=3

`Enums.ColorSpaceMode.sRGB`

## ColorWheelMode

`Prefer Mix Color`=0 `Mix Color Only`=1 `Color Wheel Only`=2

`Enums.ColorWheelMode["Prefer Mix Color"]`

## ColumnOrder

`Left Right`=0 `Right Left`=1

`Enums.ColumnOrder["Left Right"]`

## CommandWingBarDisplayMode

`Labels`=0 `Hardware Buttons`=1

`Enums.CommandWingBarDisplayMode.Labels`

## ComponentType

`Input`=0 `Output`=1 `PowerSource`=2 `Consumer`=3 `Fuse`=4 `NetworkProvider`=5 `NetworkInput`=6 `NetworkOutput`=7 `NetworkInOut`=8

`Enums.ComponentType.Input`

## Config

`MaxMultiPatchPerFixture`=1024 `MaxElementsPerLayout`=16384

`Enums.Config.MaxMultiPatchPerFixture`

## ConnectionLimitConsole

`1`=1 `2`=2

`Enums.ConnectionLimitConsole["1"]`

## ConnectionLimitOnPC

`1`=1 `2`=2 `3`=3 `4`=4 `5`=5

`Enums.ConnectionLimitOnPC["1"]`

## ConnectorType

`BNC`=0 `TBLK`=1 `TAG`=2 `KRN`=3 `STJ`=4 `MSTJ`=5 `RCA`=6 `SCART`=7 `SVIDEO`=8 `MDIN4`=9 `MDIN5`=10 `MDIN6`=11 `XLR3`=12 `XLR4`=13 `XLR5`=14 `RJ45`=15 `RJ11`=16 `DB9`=17 `DB15`=18 `DB25`=19 `DB37`=20 `DB50`=21 `HD15`=22 `HD25`=23 `DIN3`=24 `DIN5`=25 `EDAC20`=26 `EDAC56`=27 `EDAC90`=28 `EDAC120`=29 `DL96`=30 `SCSI68`=31 `IEE488`=32 `CENT50`=33 `CENT36`=34 `CENT24`=35 `DisplayPort`=36 `DVI`=37 `HDMI`=38 `PS2`=39 `TL_ST`=40 `LCDUP`=41 `SCDUP`=42 `SC`=43 `ST`=44 `NL4`=45 `CACOM`=46 `USB`=47 `N_CON`=48 `F_CON`=49 `IEC_60320_C7_C8`=50 `CEE_7_7`=51 `IEC_60320_C13_14`=52 `Edison`=53 `Eieland`=54 `CEE_16A_2P`=55 `CEE_16A_2P_110`=56 `CEE_32A`=57 `CEE_32A_2P`=58 `CEE_32A_2P_110`=59 `CEE_63A`=60 `CEE_125A`=61 `Powerlock`=62 `Powerlock_120A`=63 `Powerlock_400A`=64 `Powerlock_660A`=65 `Powerlock_800A`=66 `Camlock`=67 `NAC3FCA`=68 `NAC3FCB`=69 `PowerconTRUE1`=70 `PowerCONTRUE1TOP`=71 `Socapex_16`=72 `Socapex_7`=73 `Socapex_9`=74 `HAN_16`=75 `HAN_4`=76 `L6_20`=77 `L15_30`=78 `Stagepin`=79 `HUBBEL_6_4`=80 `DIN56905`=81

`Enums.ConnectorType.BNC`

## ContentSheetCueMode

`Current Cue`=0 `Previous Cue`=1 `Next Cue`=2 `Manual`=3

`Enums.ContentSheetCueMode.Manual`

## ContextValueType

`Preset`=0 `Generator`=1 `Bitmap`=2

`Enums.ContextValueType.Preset`

## CookMode

`Ask`=-1 `Abort`=0 `Overwrite`=1 `MergeLowPriority`=2 `Merge`=3 `Remove`=4

`Enums.CookMode.Ask`

## CopyCueOnly

`Off`=0 `On`=1 `On (Default New)`=2 `DimmerOnly`=3 `DimmerOnly (Default New)`=4

`Enums.CopyCueOnly.Off`

## CopyCueOnlyPopup

`Tracking`=0 `Cue Only`=2 `Dimmer Cue Only`=4

`Enums.CopyCueOnlyPopup.Tracking`

## CountdownAlertRange

`Local`=0 `All Stations`=1

`Enums.CountdownAlertRange.Local`

## CountdownAlertType

`None`=0 `Pop-Up`=1 `Command`=2 `Command & Pop-Up`=3

`Enums.CountdownAlertType.None`

## CreateBy

`Unknown`=0 `User Conversion`=1 `System Conversion`=2

`Enums.CreateBy.Unknown`

## CrossSectionType

`TrussFramework`=0 `Tube`=1

`Enums.CrossSectionType.TrussFramework`

## CueAssert

``=0 `None`=0 `Assert`=1 `X-Assert`=2

`Enums.CueAssert.None`

## CueCommandMode

`Enabled`=0 `Force No`=1 `Force Yes`=2

`Enums.CueCommandMode.Enabled`

## CueCopyDst

`Retain`=0 `Replace with Release`=1 `Replace with Default`=2

`Enums.CueCopyDst.Retain`

## CueCopyDstCmd

`Keep`=0 `ForceRelease`=1 `ForceDefault`=2

`Enums.CueCopyDstCmd.Keep`

## CueCopyDstMode

`Overwrite`=0 `Merge`=1

`Enums.CueCopyDstMode.Overwrite`

## CueCopySrc

`Content`=0 `Status`=1 `Look`=2

`Enums.CueCopySrc.Content`

## CueOnly

`Off`=0 `On`=1 `OnDefaultNew`=2 `DimmerOnly`=3 `DimmerOnlyDefaultNew`=4

`Enums.CueOnly.Off`

## CueOnlyPopup

`Tracking`=0 `Cue Only`=1 `Dimmer Cue Only`=3

`Enums.CueOnlyPopup.Tracking`

## CueOperationMode

`Cue Only`=0 `Tracking`=1

`Enums.CueOperationMode.Tracking`

## CuePartAppearance

`Off`=0 `Number`=1 `Num+Name`=2 `All`=3

`Enums.CuePartAppearance.Off`

## CuePartAppearanceContent

`Off`=0 `Number`=1 `Num+Name`=2

`Enums.CuePartAppearanceContent.Off`

## CuePartMode

`Default`=4294967295

`Enums.CuePartMode.Default`

## CuePartTextures

`IconCooking`=0 `IconCookingPhaser`=1

`Enums.CuePartTextures.IconCooking`

## CueTimeNone

`None`=-1

`Enums.CueTimeNone.None`

## CueTrigger

`Go`=0 `Time`=1 `Follow`=2 `Sound`=3 `BPM`=4

`Enums.CueTrigger.Go`

## CueZeroMode

`Off`=0 `All Used Attributes`=1 `Only Used Dimmers`=2

`Enums.CueZeroMode.Off`

## CullMode

`Force None`=0 `From Material`=1

`Enums.CullMode["Force None"]`

## CustomIdEnum

`None`=0 `Same as FID`=4294967295

`Enums.CustomIdEnum.None`

## DGShaderTypes

`Vertex`=0 `Fragment`=1 `Geometry`=2 `Compute`=3

`Enums.DGShaderTypes.Vertex`

## DMXBreak

`Overwrite`=-1

`Enums.DMXBreak.Overwrite`

## DMXMergeMode

`Off`=0 `Prio`=1 `HTP`=2 `LowTP`=3

`Enums.DMXMergeMode.Off`

## DMXReadoutMode

`Hex8`=0 `Hex16`=1 `Hex24`=2 `Dec8`=3 `Dec16`=4 `Dec24`=5 `Percent`=6

`Enums.DMXReadoutMode.Hex8`

## DMXValueReadoutMode

`Percent`=0 `Decimal`=1 `Hex`=2

`Enums.DMXValueReadoutMode.Percent`

## DMXVirtualResolution

`8 bits`=1 `16 bits`=2 `24 bits`=3

`Enums.DMXVirtualResolution["8 bits"]`

## DSCPCodes

`CS0 (Default)`=0 `CS1`=8 `AF11`=10 `AF12`=12 `AF13`=14 `CS2`=16 `AF21`=18 `AF22`=20 `AF23`=22 `CS3`=24 `AF31`=26 `AF32`=28 `AF33`=30 `CS4`=32 `AF41`=34 `AF42`=36 `AF43`=38 `CS5`=40 `Voice-Admit`=44 `EF`=46 `CS6`=48 `CS7`=56

`Enums.DSCPCodes.CS1`

## DSCPCodesDMX

`CS0`=0 `CS1`=8 `AF11`=10 `AF12`=12 `AF13`=14 `CS2`=16 `AF21`=18 `AF22`=20 `AF23`=22 `CS3`=24 `AF31`=26 `AF32`=28 `AF33`=30 `CS4 (Default)`=32 `AF41`=34 `AF42`=36 `AF43`=38 `CS5`=40 `Voice-Admit`=44 `EF`=46 `CS6`=48 `CS7`=56

`Enums.DSCPCodesDMX.CS0`

## DataMergeTimeout

`Unlimited`=9223372036854775807

`Enums.DataMergeTimeout.Unlimited`

## DataNegotiationMode

`Cancel`=0 `Use Master`=1 `Merge`=2 `Use Mine`=3

`Enums.DataNegotiationMode.Cancel`

## DataNegotiationModeDefault

`Cancel`=0 `Keep Only Master Data`=1 `Merge All Data`=2

`Enums.DataNegotiationModeDefault.Cancel`

## DatumMode

`Full`=0 `Date`=1 `Time`=2

`Enums.DatumMode.Full`

## DebugUsbDataSection

`All`=0 `DmxIn`=1 `DmxInCheck`=2 `DmxOut`=3 `Midi`=4 `Smpte`=5 `Ups`=6 `Analog`=7 `Digital`=8 `Button`=9 `Encoder`=10 `Fader`=11 `Led`=12 `Sync`=13 `Protocol`=14 `HeartBeat`=15 `Software`=16 `NotifierLayer`=17 `Text`=18 `RTC`=19 `Capabilities`=20

`Enums.DebugUsbDataSection.All`

## Default

`Default`=4294967295

`Enums.Default.Default`

## DefinedPoolColumns

`Take Current Width`=4294967294 `Not Defined`=4294967295

`Enums.DefinedPoolColumns["Take Current Width"]`

## DeprecatedExecConfigType

`Master`=11

`Enums.DeprecatedExecConfigType.Master`

## DeprecatedLearnMode

`Default`=0

`Enums.DeprecatedLearnMode.Default`

## DeskLightChannel

`DeskLights`=1 `LedEncoder`=2 `LedFader`=3 `LedExec`=4 `LedKeyboard`=5 `LedOther`=6 `ScreenBig`=7 `ScreenLetter`=8 `ScreenSmall`=9 `ScreenExternal`=10

`Enums.DeskLightChannel.DeskLights`

## DimmerWheelResolution

`Normal`=0 `Coarse`=1 `Fine`=2

`Enums.DimmerWheelResolution.Normal`

## Disabled

`Disabled`=0 ``=1

`Enums.Disabled.Disabled`

## DispView

`Realtime`=0 `Timing`=1 `CPU`=2 `Memory`=3 `CPU Temp`=4 `GPU Temp`=5 `Sys Temp`=6 `Fan`=7 `Details`=8 `HDD`=9 `Network`=10

`Enums.DispView.Realtime`

## DisplayIndex

`None`=4294967295

`Enums.DisplayIndex.None`

## DisplayNone

`None`=4294967295

`Enums.DisplayNone.None`

## DisplayNumber

`Intern1`=0 `Intern2`=1 `Intern3`=2 `Extern4`=3 `Extern5`=4 `Small6`=5 `Small7`=6 `Encoders`=7 `Executors1`=8 `Executors2`=9 `Executors3`=10 `Executors4`=11 `Executors5`=12 `Executors6`=13 `TouchMapper`=14 `None`=4294967295

`Enums.DisplayNumber.Intern1`

## DisplayScales

`0.5x`=8388608 `0.75x`=12582912 `1x`=16777216 `1.25x`=20971520 `1.5x`=25165824 `1.75x`=29360128 `2x`=33554432 `2.5x`=41943040

`Enums.DisplayScales["0.5x"]`

## DisplayType

`Big`=0 `Long`=1 `Small`=2

`Enums.DisplayType.Big`

## DisplayTypePreference

`Any`=0 `Big`=1 `Long`=2 `Small`=3 `BigOrLong`=4 `BigOrSmall`=5 `LongOrSmall`=6 `BigLongSmall`=7

`Enums.DisplayTypePreference.Any`

## DmxCurveEditTool

`MoveArea`=0 `Select`=1 `AddAbsolute`=2 `Delete`=3 `MovePoint`=4 `MoveSpline`=5

`Enums.DmxCurveEditTool.MoveArea`

## DmxCurveModes

`MinMax`=0 `Switch`=1 `Custom`=2

`Enums.DmxCurveModes.MinMax`

## DmxPrio

`Lowest`=0 `Low`=16 `LTP`=32 `High`=48 `Highest`=64 `HTP`=80 `Swap`=96 `Prog`=112 `Super`=128

`Enums.DmxPrio.Lowest`

## DmxSheetCellType

`NotPatched`=0 `Patched1`=1 `Patched2`=2 `Selected`=3 `SelectedInverted`=4 `PartlySelected`=5 `NotRequested`=6 `Parked`=7 `DmxTest`=8

`Enums.DmxSheetCellType.NotPatched`

## DmxSheetFixedColumnType

`Address`=0 `Address2`=1

`Enums.DmxSheetFixedColumnType.Address`

## DmxSheetHeaderType

``=0

`Enums.DmxSheetHeaderType[""]`

## DmxSheetSettingsAddressMode

`Univ.addr`=0 `Absolute`=1

`Enums.DmxSheetSettingsAddressMode.Absolute`

## DmxSheetSettingsLevelbar

`Off`=0 `Background`=1 `Bar`=2 `Programmer`=3

`Enums.DmxSheetSettingsLevelbar.Off`

## DmxSheetSettingsSelected

`Selected`=4294967295

`Enums.DmxSheetSettingsSelected.Selected`

## DmxSheetSettingsShowField

`Attribute`=0 `Id`=1 `Value`=2

`Enums.DmxSheetSettingsShowField.Attribute`

## DmxSheetSettingsViewMode

`Sheet`=0

`Enums.DmxSheetSettingsViewMode.Sheet`

## DmxState

`Off`=0 `Out`=1 `In`=2 `RDM`=5

`Enums.DmxState.Off`

## DmxTesterAddressMode

`Uni`=0 `Abs`=1

`Enums.DmxTesterAddressMode.Uni`

## DmxTesterMode

`All`=0 `Patched`=1 `Unpatched`=2

`Enums.DmxTesterMode.All`

## DriveType

`Invalid`=0 `Internal`=1 `Removeable`=2 `OldVersion`=3 `RemoteDrive`=4

`Enums.DriveType.Invalid`

## DynamicPresetModeDefault

`Default`=0 `Selective`=1 `Global`=2 `Universal`=3 `ForceGlobal`=4 `ForceUniversal`=5

`Enums.DynamicPresetModeDefault.Default`

## DynamicPresetPool

`Dynamic`=4294967295

`Enums.DynamicPresetPool.Dynamic`

## ECPin

`0`=0 `off`=0 ``=0 `false`=0 `on`=1 `1`=1 `true`=1 `Yes`=1

`Enums.ECPin.off`

## ECPlay

`No`=0 `0`=0 `false`=0 `off`=0 `1`=1 `true`=1 `on`=1 ``=1 `Yes`=1

`Enums.ECPlay.No`

## ECRec

`No`=0 `0`=0 `false`=0 `off`=0 `1`=1 `true`=1 `on`=1 ``=1 `Yes`=1

`Enums.ECRec.No`

## EC_AutoGrid

`Manual`=0 `Auto`=1

`Enums.EC_AutoGrid.Manual`

## EC_NoGrid

``=2147483647 `None`=2147483647

`Enums.EC_NoGrid.None`

## EmptyAsZero

``=0

`Enums.EmptyAsZero[""]`

## EmptyAsZeroFID

``=0 `None`=0

`Enums.EmptyAsZeroFID.None`

## EncoderBarContext

`Default`=0 `Window`=1 `Overlay`=2

`Enums.EncoderBarContext.Default`

## EncoderFactor

`Disabled`=0 `Div50`=335544 `Div25`=671088 `Div10`=1677721 `Div5`=3355443 `Div2.55`=6579300 `Div2`=8388608 `One`=16777216 `Mul2`=33554432 `Mul2.55`=42781900 `Mul5`=83886080 `Mul10`=167772160 `Mul25`=419430400 `Mul50`=838860800

`Enums.EncoderFactor.Disabled`

## EncoderFunction

`CueSettings`=0 `CueTiming`=1 `PresetTiming1`=2 `PresetTiming2`=3 `PresetTiming3`=4 `MIB`=6 `Cmd`=8 `Data Edit`=9

`Enums.EncoderFunction.CueSettings`

## EncoderFunctionLayoutView

`Position`=0 `Arrangement`=1

`Enums.EncoderFunctionLayoutView.Position`

## EncoderGroupType

`Timing`=0 `Value`=0 `Speed`=0

`Enums.EncoderGroupType.Timing`

## EncoderLink

`Single`=0 `Feature`=1 `AtFilter`=2

`Enums.EncoderLink.Single`

## EncoderLinkPhaser

`Single`=0 `Feature`=1 `AtFilter`=2

`Enums.EncoderLinkPhaser.Single`

## EncoderLinkResolution

`Single`=0 `FeatureGroup`=1

`Enums.EncoderLinkResolution.Single`

## EncoderLinkValues

`Single`=0 `Feature`=1

`Enums.EncoderLinkValues.Single`

## EncoderResolution3d

`Coarse`=0 `Fine`=1 `Increment`=2

`Enums.EncoderResolution3d.Coarse`

## EncoderResolutionType

`Slow`=0 `Fast`=1

`Enums.EncoderResolutionType.Slow`

## EncoderRing

`Inner`=0 `Outer`=1 `Both`=2

`Enums.EncoderRing.Inner`

## EncoderType

`WheelMaster`=0 `ColorPicker`=1 `PanTiltFollow`=2 `PanTrackpad`=3 `TiltTrackpad`=4 `Inside1`=5 `Outside1`=6 `Inside2`=7 `Outside2`=8 `Inside3`=9 `Outside3`=10 `Inside4`=11 `Outside4`=12 `Inside5`=13 `Outside5`=14 `Executor`=16 `ValueFadeControl`=17

`Enums.EncoderType.WheelMaster`

## EncoderUIStyle

`None`=0 `Rotate`=1 `Drag`=2

`Enums.EncoderUIStyle.None`

## Enums

`X before Y`=0 `Y before X`=1

`Enums.Enums["X before Y"]`

## EventsPlaybackRecord

`Manual Events`=0 `All Events`=1

`Enums.EventsPlaybackRecord["Manual Events"]`

## ExecConfigHeight

`1`=1 `2`=2 `3`=3 `4`=4

`Enums.ExecConfigHeight["1"]`

## ExecConfigType

`Sequence`=0 `Macro`=1 `View`=2 `World`=3 `Group`=4 `Preset`=5 `Plugin`=6 `User`=7 `Sound`=8 `ScreenConfig`=9 `Timer`=10 `GrandMaster`=11 `SpeedMaster`=12 `PlaybackMaster`=13 `SelectedMaster`=14 `TimingMaster`=15

`Enums.ExecConfigType.Sequence`

## ExecConfigWidth

`1`=1 `2`=2 `3`=3 `4`=4 `5`=5

`Enums.ExecConfigWidth["1"]`

## ExecDisplayMode

`Data`=0 `Appearance`=1 `Data and Appearance`=2

`Enums.ExecDisplayMode.Data`

## ExecEditorTab

`Object`=0 `Handle`=1 `Edit Setting`=2 `Edit`=3 `LastTab`=4

`Enums.ExecEditorTab.Object`

## ExecEvent

`None`=0 `Key`=1 `KeyUnpress`=2 `MAKey`=3 `MAKeyUnpress`=4 `Fader`=5 `MAFader`=6 `EncoderLeft`=7 `MAEncoderLeft`=8 `EncoderRight`=9 `MAEncoderRight`=10 `Encoder`=11 `MAEncoder`=12

`Enums.ExecEvent.None`

## ExitCode

`Normal`=0 `Restart`=1 `Reboot`=2 `AutoPluginFailed`=3 `PowerDown`=4 `GeneralError`=5

`Enums.ExitCode.Normal`

## ExternTimeSyncMode

`None`=0 `NTP`=1

`Enums.ExternTimeSyncMode.None`

## ExtraStatusInfo

``=0 `Join`=1 `Create`=2

`Enums.ExtraStatusInfo.Join`

## FaderEnable

`Toggle`=0 `AlwaysOn`=1 `Disabled`=2

`Enums.FaderEnable.Toggle`

## FaderFunctions

`Master`=35 `XFade`=36 `XFadeA`=37 `XFadeB`=38 `Temp`=39 `Rate`=40 `Speed`=41 `Highlight`=42 `Lowlight`=43 `Solo`=44 `Time`=45

`Enums.FaderFunctions.Master`

## FailedCookedPart

`None`=0 `Group`=1 `Matricks`=2 `Preset`=3 `Filter`=4 `GroupPartlyCooked`=5 `IntegratedPresetMiss`=6

`Enums.FailedCookedPart.None`

## FailureMode

`Timeout 10s`=10 `Timeout 20s`=20 `Timeout 30s`=30 `Timeout 1m`=60 `Timeout 10m`=600 `Timeout 30m`=1800 `Timeout 1h`=3600 `Hold`=65535

`Enums.FailureMode.Hold`

## FalloffType

`None`=0 `Linear`=1 `Correct`=2

`Enums.FalloffType.None`

## FilterAction

`Select`=1 `Call`=9 `None`=255

`Enums.FilterAction.Select`

## FilterRuleStatic

`Yes`=0 `No`=1

`Enums.FilterRuleStatic.Yes`

## FilterRuleTypes

`Show`=0 `Hide`=1

`Enums.FilterRuleTypes.Show`

## FixedColumns

`Auto`=-1

`Enums.FixedColumns.Auto`

## FixturGraphicSource

`Auto`=0 `Value`=1 `Output`=2 `DMX`=3

`Enums.FixturGraphicSource.Auto`

## FixtureAppearanceMode

`None`=0 `Enabled`=1 `Graphic`=2

`Enums.FixtureAppearanceMode.None`

## FixtureGraphicMode

`None`=0 `Flip`=1 `Simple`=2 `Gobo`=3

`Enums.FixtureGraphicMode.None`

## FixtureIdEnum

`None`=0 `Same as CID`=4294967295

`Enums.FixtureIdEnum.None`

## FixtureInvert

`No`=0 `false`=0 ``=0 `<Blank>`=0 `off`=0 `0`=0 `true`=1 `on`=1 `1`=1 `Inverted`=1 `Yes`=1

`Enums.FixtureInvert.No`

## FixtureLibraryChannelSort

`Channels`=0 `Structure`=1

`Enums.FixtureLibraryChannelSort.Channels`

## FixtureMoveOperation

`Absolute`=1 `Relative`=2

`Enums.FixtureMoveOperation.Absolute`

## FixtureOffsets

`None`=0 `30°`=30 `45°`=45 `60°`=60 `90°`=90 `180°`=180 `270°`=270 `360°`=360

`Enums.FixtureOffsets.None`

## FixtureSheetFixedColumnType

``=0 `Selected`=1 `SelectedInverted`=2 `PartlySelected`=3 `InvalidGridPosition`=4 `MainMultiPatchSelected`=5 `SelectedEdge`=6

`Enums.FixtureSheetFixedColumnType.Selected`

## FixtureSheetHeaderType

``=0 `Selected`=1 `SelectedInverted`=2 `PartlySelected`=3

`Enums.FixtureSheetHeaderType.Selected`

## FixtureSheetSortMode

`FID`=0 `CID`=1

`Enums.FixtureSheetSortMode.FID`

## FixtureSourceType

`Fixture Types`=0 `Classes`=1 `Layers`=2

`Enums.FixtureSourceType.Classes`

## FixtureTypeSource

`grandMA3`=0 `grandMA2`=1 `GDTF`=2 `User`=3 `Shares`=4 `In current show`=5

`Enums.FixtureTypeSource.grandMA3`

## FixtureTypeSourceImport

`grandMA3`=0 `grandMA2`=1 `User`=3 `Shares`=4

`Enums.FixtureTypeSourceImport.grandMA3`

## FixtureTypeXYZStatus

`No`=0 `Partial`=1 `Yes`=2

`Enums.FixtureTypeXYZStatus.No`

## FlipOption

`X`=0 `Y`=1

`Enums.FlipOption.X`

## FocusPriority

`Never`=0 `TabOnly`=1 `CanHaveFocus`=2 `WantsFocus`=3 `InitialFocus`=4

`Enums.FocusPriority.Never`

## FocusReason

`None`=0 `ViewChangedLimited`=1 `ViewChanged`=2 `UserClick`=3 `UserClickTitle`=4 `UserKeyTab`=5 `Lua`=6 `RestoreAfterModal`=7 `CmdlineInput`=8

`Enums.FocusReason.None`

## FocusSearchPolicy

`Default`=0 `Force`=1 `Suppress`=2

`Enums.FocusSearchPolicy.Default`

## FollowPreview

`0`=0 `No`=0 `false`=0 `off`=0 `1`=1 `on`=1 `true`=1 `Yes`=1 `Configurable`=2 `Inherited`=3

`Enums.FollowPreview.No`

## FontSizeType

`Point`=0 `Pixel`=1

`Enums.FontSizeType.Point`

## FontSizes

`9`=9 `11`=11 `14`=14 `16`=16 `18`=18 `20`=20 `24`=24 `28`=28 `32`=32

`Enums.FontSizes["9"]`

## FrameFormat

`Seconds`=0 `24 fps`=24 `25 fps`=25 `30 fps`=30 `60 fps`=60

`Enums.FrameFormat.Seconds`

## FrameFormatClockSource

`<Clock Source>`=0 `24 fps`=24 `25 fps`=25 `30 fps`=30 `60 fps`=60 `Seconds`=100

`Enums.FrameFormatClockSource.Seconds`

## FrameFormatDefault

`Default`=0 `24 fps`=24 `25 fps`=25 `30 fps`=30 `60 fps`=60 `Seconds`=100

`Enums.FrameFormatDefault.Default`

## FunctionMode

`WM_Unknown`=0 `WM_2D`=1 `WM_1D`=2 `WM_Phase`=3 `WM_Width`=4

`Enums.FunctionMode.WM_Unknown`

## FuseRating

`B`=0 `C`=1 `D`=2 `K`=3 `Z`=4

`Enums.FuseRating.B`

## GE_MGSWindowMode

`Grid`=0 `List`=1

`Enums.GE_MGSWindowMode.Grid`

## GE_MessageNotificationType

`None`=0 `Notification`=1 `Pop-up`=2

`Enums.GE_MessageNotificationType.None`

## GE_StatusBlink

`None`=0 `Once`=1 `Always`=2

`Enums.GE_StatusBlink.None`

## GE_StatusCategory

`None`=0 `Highlight`=1 `Solo`=2 `Blind`=3 `Parked`=4 `Tester`=5 `NotEnoughParameters`=6 `ParameterOverload`=7 `Filter`=8 `World`=9 `TimecodeRec`=10 `Worldserver`=11 `Battery`=12 `RecipeEditing`=13 `Lowlight`=14 `Preview`=15 `ShowDataMemory`=16 `Phasers`=17 `Reserved`=18 `FlowControl`=19 `KeyboardShortcuts`=20 `NoFixturesPatched`=21 `EncoderBar`=22 `GrandMaster`=23 `WorldMaster`=24 `RateMaster`=25 `USBNetwork`=26 `CPU`=27 `Memory`=28 `CPUTemp`=29 `GPUTemp`=30 `FanRPM`=31 `DiskSpace`=32 `PatchOpen`=33 `FreezeNShot`=34 `GroupMasters`=35

`Enums.GE_StatusCategory.None`

## GE_StatusSource

`My`=0 `All`=1

`Enums.GE_StatusSource.My`

## GE_StatusVisibility

`Never`=0 `On Activity`=1 `Always`=2

`Enums.GE_StatusVisibility.Never`

## GelGridType

`List`=0 `Small Icons`=1 `Big Icons`=2

`Enums.GelGridType.List`

## GelSortType

`None`=0 `Name`=1 `Key`=2

`Enums.GelSortType.None`

## GenVirtualDimmer

`No`=0 `Yes`=1

`Enums.GenVirtualDimmer.No`

## GenerateParmeters

`DimmerIncrement`=0 `AmountHue`=1 `AmountSaturation`=2 `SortColor`=3 `GelList`=4

`Enums.GenerateParmeters.DimmerIncrement`

## GeneratorLimits

`14d`=0

`Enums.GeneratorLimits["14d"]`

## GeometryType

`None`=0 `Axis`=1 `Beam`=2 `FilterColor`=3 `FilterGobo`=4 `FilterBeam`=5 `FilterShaper`=6 `MediaServerLayer`=7 `MediaServerCamera`=8 `MediaServerMaster`=9 `Display`=10 `Laser`=11 `WiringObject`=12 `Inventory`=13 `Structure`=14 `Support`=15 `Magnet`=16 `Reference`=17

`Enums.GeometryType.None`

## GestureId

`Pan`=0 `Swipe`=1 `Click`=2 `PanScrollArea`=3 `!Invalid!`=32769

`Enums.GestureId.Pan`

## GestureResult

`Ignore`=0 `EventProcessed`=1 `MayBeGesture`=2 `TriggerGesture`=3 `TriggerGesturePassEvent`=4 `FinishGesture`=5 `FinishGesturePassEvent`=6 `CancelGesture`=7

`Enums.GestureResult.Ignore`

## GestureStatus

`None`=0 `Updated`=1 `Finishing`=2 `Finished`=3 `Canceled`=4

`Enums.GestureStatus.None`

## GoboMode

`Disabled`=0 `Enabled`=1 `Animated`=2

`Enums.GoboMode.Disabled`

## GrandKnob

`GrandKnob`=100 `None`=4294967295

`Enums.GrandKnob.GrandKnob`

## GridColumnFilterCollect

`Condensed`=0 `Full`=1 `Extended`=2

`Enums.GridColumnFilterCollect.Condensed`

## GridContentFilterMode

`And`=0 `Or`=1

`Enums.GridContentFilterMode.And`

## GridCursorMovement

`None`=0 `Append X`=1 `New Line`=2

`Enums.GridCursorMovement.None`

## GridCursorMovementGroup

`None`=0 `Append X`=1 `New Line`=2 `<Linked>`=3

`Enums.GridCursorMovementGroup.None`

## GridDirection

`X before Z`=0 `X before Y`=0 `Y before Z`=0 `Z before Y`=1 `Z before X`=1 `Y before X`=1

`Enums.GridDirection["X before Z"]`

## GridMatrixRotation

`0°`=0 `90°`=1 `180°`=2 `270°`=3

`Enums.GridMatrixRotation["0°"]`

## GridMergeMode

`Off`=0 `Append X`=1

`Enums.GridMergeMode.Off`

## GridModeAgenda

`Month`=0 `Week`=1 `Day`=2

`Enums.GridModeAgenda.Month`

## GridSortOrder

`None`=0 `Asc`=1 `Desc`=2

`Enums.GridSortOrder.None`

## GridTool

`Linearize`=0 `Transpose`=1 `Rotate`=2 `Flip`=3 `Align`=4 `RemoveGaps`=5 `RemoveOffset`=6 `Newline`=7 `Multiply`=8 `Divide`=9 `MakeSymmetrical`=10 `UseMatricksPositions`=11 `Perspective`=12 `Planar`=13

`Enums.GridTool.Linearize`

## GridType

`Fixture`=0 `FixtureType`=1 `FixtureSource`=2 `ChannelSet`=3 `FTPreset`=4

`Enums.GridType.Fixture`

## GroupMasterMode

`None`=0 `Positive`=1 `Negative`=2 `Scaling`=3 `Additive`=4

`Enums.GroupMasterMode.None`

## GroupMemoryType

`Compressed`=0 `Uncompressed`=1

`Enums.GroupMemoryType.Compressed`

## GroupSelectionType

`Relative`=0 `Absolute`=1

`Enums.GroupSelectionType.Relative`

## GuidOptions

`Original`=0 `New`=1

`Enums.GuidOptions.Original`

## HardwareButtonDisplayMode

`Text+Icon`=0 `Text`=1 `Icon`=2

`Enums.HardwareButtonDisplayMode.Text`

## HostOs

`Undefined`=0 `Linux`=1 `Windows`=2 `Mac`=3 `Rtos`=4

`Enums.HostOs.Undefined`

## HostRevision

`Rev1`=0 `Rev2`=1 `Rev3`=2

`Enums.HostRevision.Rev1`

## HostStatus

`Undefined`=0 `Startup`=1 `Standalone`=2 `Connected`=3 `LocalMaster`=4 `IdleMaster`=5 `GlobalMaster`=6 `NormalShutdown`=7 `ErrorShutdown`=8 `UpdateMode`=9 `LicenceInvalid`=10

`Enums.HostStatus.Undefined`

## HostSubType

`Undefined`=0 `Recovery`=1 `FullSize`=20 `FullSizeCRV`=21 `Light`=22 `LightCRV`=23 `Compact`=24 `CompactXT`=25 `RPU`=26 `Medium`=40 `Large`=41 `XLarge`=42 `onPC2Port`=60 `onPC4Port`=61 `onPC8Port`=62 `Node2Port`=63 `Node4Port`=64 `Node8Port`=65 `Node2PortWM`=66 `Node2PortDIN`=67 `Node4PortDIN`=68 `Node8PortDIN`=69 `onPC2PortDIN`=70 `onPC4PortDIN`=71 `onPC8PortDIN`=72 `Vis+Dongle`=73 `Visualizer`=74 `IONode`=75 `IONodeDIN`=76 `MA-Net3-duct`=77 `TrackingServer`=78 `MediaServer`=79 `Wing-MM`=90 `Wing-MFX`=91 `Wing-MFE`=92 `Wing-onPC`=93 `Wing-Extension`=94 `Wing-onPCXT`=95 `Wing-onPCFader`=96 `onPCRackUnit`=97 `MAkerStation`=98 `DMX-key`=99 `DMX-key starter`=100 `Wing-Reserved`=101

`Enums.HostSubType.Undefined`

## HostType

`Undefined`=0 `Console`=1 `onPC`=2 `PU`=3 `NetworkNode`=4 `InternalWing`=5 `Switch`=6 `Plugin`=7 `PluginSmall`=8 `Extension`=9 `UpdateMode`=10

`Enums.HostType.Undefined`

## Ignore

``=0 `Ignore`=1

`Enums.Ignore.Ignore`

## IgnoreFT

`Ignore FT`=4294967294 `Follow FT`=4294967295 ``=4294967295

`Enums.IgnoreFT["Ignore FT"]`

## ImageBackGroundMode

`Stretch`=0 `Bar`=1 `Crop`=2 `Tile`=3 `Center`=4

`Enums.ImageBackGroundMode.Stretch`

## ImageMirror

`None`=0 `Horizontal`=1 `Vertical`=2 `Both`=3

`Enums.ImageMirror.None`

## ImageResolution

`Full`=0 `64`=64 `128`=128 `256`=256 `512`=512

`Enums.ImageResolution.Full`

## ImageRotation

`None`=0 `90°`=1 `180°`=2 `270°`=3

`Enums.ImageRotation.None`

## ImageSource

`Gobos`=0 `Symbols`=1 `Images`=2 `Videos`=3

`Enums.ImageSource.Gobos`

## ImageStoreSource

`ScreenShot`=0 `NDI`=1

`Enums.ImageStoreSource.ScreenShot`

## Index

`Illegal`=-1

`Enums.Index.Illegal`

## IndividualTiming

`Default`=0 `Normalized`=1

`Enums.IndividualTiming.Default`

## InfoAppearanceMode

`Off`=0 `Note`=1 `Label + Note`=2

`Enums.InfoAppearanceMode.Off`

## InfoLinkMode

`None`=0 `SelectedSequence`=1 `SelectedMacro`=2 `LastSelectedObject`=3

`Enums.InfoLinkMode.None`

## InfoWindowMode

`Object`=0 `CurrentChild`=1 `NextChild`=2 `AllChildren`=3 `ObjectAndChildren`=4

`Enums.InfoWindowMode.Object`

## InputControl3d

`Select`=0 `Follow`=1 `Camera Orbit`=2 `Camera Zoom`=3 `Camera Pivot`=4 `Camera Move`=5 `Camera Set Pivot`=6

`Enums.InputControl3d.Select`

## InputType

`Mouse`=0 `Touch`=1 `Keyboard`=2 `Scroller`=3

`Enums.InputType.Mouse`

## InternalQueues

`Cmd`=0 `Root`=1 `App`=2 `Pult`=3 `RT`=4 `Manet`=5

`Enums.InternalQueues.Cmd`

## InvalidFootprint

`?`=-1

`Enums.InvalidFootprint["?"]`

## ItemGroupPosition

`None`=0 `Begin`=1 `Center`=2 `End`=3 `Single`=4

`Enums.ItemGroupPosition.None`

## KeyAction

`Release`=0 `Press`=1 `Hold`=2 `DoublePress`=3 `ReleaseAfterHold`=4 `Click`=5 `AfterDoublePress`=6

`Enums.KeyAction.Release`

## KeyFunctions

`Flash`=1 `Black`=2 `Go`=3 `GoBack`=4 `GoFast`=5 `GoBackFast`=6 `On`=7 `Off`=8 `Learn`=9 `LearnSpeed`=10 `Rate1`=11 `Speed1`=12 `Temp`=13 `Toggle`=14 `Top`=15 `Goto`=16 `Load`=17 `Pause`=18 `Highlight`=19 `Lowlight`=20 `Solo`=21 `Time`=22 `Step`=23 `Select`=24 `Swap`=25 `HS`=26 `DS`=27 `Record`=28 `Kill`=29 `ReSync`=30 `FastSync`=31

`Enums.KeyFunctions.Flash`

## KeyboardCodes

`None`=-1 `Space`=32 `Apostrophe`=39 `Comma`=44 `Minus`=45 `Period`=46 `Slash`=47 `0`=48 `1`=49 `2`=50 `3`=51 `4`=52 `5`=53 `6`=54 `7`=55 `8`=56 `9`=57 `Semicolon`=59 `Equal`=61 `A`=65 `B`=66 `C`=67 `D`=68 `E`=69 `F`=70 `G`=71 `H`=72 `I`=73 `J`=74 `K`=75 `L`=76 `M`=77 `N`=78 `O`=79 `P`=80 `Q`=81 `R`=82 `S`=83 `T`=84 `U`=85 `V`=86 `W`=87 `X`=88 `Y`=89 `Z`=90 `LeftBracket`=91 `Backslash`=92 `RightBracket`=93 `GraveAccent`=96 `World1`=161 `World2`=162 `Escape`=256 `Enter`=257 `Tab`=258 `Backspace`=259 `Insert`=260 `Delete`=261 `Right`=262 `Left`=263 `Down`=264 `Up`=265 `PageUp`=266 `PageDown`=267 `Home`=268 `End`=269 `CapsLock`=280 `ScrollLock`=281 `NumLock`=282 `PrintScreen`=283 `Pause`=284 `F1`=290 `F2`=291 `F3`=292 `F4`=293 `F5`=294 `F6`=295 `F7`=296 `F8`=297 `F9`=298 `F10`=299 `F11`=300 `F12`=301 `kpDecimal`=330 `kpDivide`=331 `kpMultiply`=332 `kpSubtract`=333 `kpAdd`=334 `LeftShift`=340 `LeftCtrl`=341 `LeftAlt`=342 `RightShift`=344 `RightCtrl`=345 `RightAlt`=346 `Delta`=349

`Enums.KeyboardCodes.None`

## KeyboardModifier

`None`=-1 `Shift`=340 `Ctrl`=341 `Alt`=342

`Enums.KeyboardModifier.None`

## KnockInMIB

`Off`=0 `Post`=1

`Enums.KnockInMIB.Off`

## LampType

`Discharge`=0 `Tungsten`=1 `Halogen`=2 `LED`=3

`Enums.LampType.Discharge`

## LaserColorType

`RGB`=0 `SingleWaveLength`=1

`Enums.LaserColorType.RGB`

## LastSelectedTab

`Import`=0 `Export`=1 `CreateGroups`=2 `CreatePresets`=3 `AutoCreatePresets`=4 `AutoStorePresets`=5

`Enums.LastSelectedTab.Import`

## LayoutElementAlignmentH

`Center`=0 `Left`=1 `Right`=2 `OutsideLeft`=3 `OutsideRight`=4

`Enums.LayoutElementAlignmentH.Center`

## LayoutElementAlignmentV

`Center`=0 `Top`=1 `Bottom`=2 `Above`=3 `Below`=4

`Enums.LayoutElementAlignmentV.Center`

## LayoutElementSelectionRelevance

`Off`=0 `Background`=1

`Enums.LayoutElementSelectionRelevance.Off`

## LayoutFitType

`Elements`=0 `Canvas`=1 `Both`=2

`Enums.LayoutFitType.Elements`

## LayoutGridStyle

`Off`=0 `Lines`=1 `Dots`=2

`Enums.LayoutGridStyle.Off`

## LayoutLassoSelectionFilter

`All`=0 `Fixtures`=1 `Others`=2

`Enums.LayoutLassoSelectionFilter.All`

## LayoutOutputSelection

`Value`=0 `DMX`=1 `Output`=2

`Enums.LayoutOutputSelection.Value`

## LayoutSizePolicy

`Fixed`=0 `Stretch`=1 `Content`=2

`Enums.LayoutSizePolicy.Fixed`

## LayoutStretch

`Stretch`=0 `Bar`=1 `Crop`=2

`Enums.LayoutStretch.Stretch`

## LayoutTool

`Operate`=0 `Select`=1 `Add`=2 `Delete`=3 `Move`=4 `Resize`=5 `ResizeFixedRatio`=6 `Auto`=7

`Enums.LayoutTool.Operate`

## LayoutType

`Line`=0 `Grid`=1 `Circle`=2

`Enums.LayoutType.Line`

## LayoutVisibility

`Hidden`=0 `Visible`=1

`Enums.LayoutVisibility.Hidden`

## LearnMode

`Learn Ignores Speed Scale`=0 `Learn Respects Speed Scale`=1 `Auto Increase Speed Scale`=2

`Enums.LearnMode["Learn Ignores Speed Scale"]`

## LearnModeSuffix

``=0 `(*)`=1 `(+)`=2

`Enums.LearnModeSuffix[""]`

## LicenseRequest

`Auto`=0 `On`=1 `Off`=2

`Enums.LicenseRequest.Auto`

## LineHeights

`Auto`=0 `1`=1 `2`=2 `3`=3 `4`=4 `6`=6 `8`=8 `10`=10 `12`=12

`Enums.LineHeights.Auto`

## LinearizeOption

`SelectionOrder`=0 `Numerical`=1 `LeftToRight`=2 `TopToBottom`=3

`Enums.LinearizeOption.SelectionOrder`

## LinesOverlayType

`None`=0 `All`=1 `All Dimmer 0`=2 `Selected`=3 `Selected Dimmer 0`=4

`Enums.LinesOverlayType.None`

## LinkRemoteDatapool

`Link Remote`=128

`Enums.LinkRemoteDatapool["Link Remote"]`

## LockTypes

``=0 `UL`=1 `PL`=2 `SL`=3

`Enums.LockTypes.UL`

## LockedYesNo

`0`=0 `No`=0 `false`=0 `off`=0 `1`=1 `true`=1 `on`=1 `Yes`=1 `UL`=1

`Enums.LockedYesNo.No`

## LoopMode

`Loop`=0 `Pause`=1 `Off`=2

`Enums.LoopMode.Loop`

## MIDIMode

`In`=0 `Out`=1 `In & Out & Thru`=2 `In & Out`=3 `Off`=4

`Enums.MIDIMode.In`

## MIDITCMode

`In`=0 `Out`=1 `In & Out & Thru`=2

`Enums.MIDITCMode.In`

## MacroLineWait

`Go`=-1 `Follow`=0

`Enums.MacroLineWait.Go`

## MacroPoolAction

`Toggle`=2 `Call`=9 `None`=255

`Enums.MacroPoolAction.Toggle`

## Master

`DefaultMaster`=0 `DefaultXFade`=1 `DefaultXFadeA`=2 `DefaultXFadeB`=3 `DefaultTemp`=4 `DefaultRate`=5 `DefaultSpeed`=6 `DefaultHighlight`=7 `DefaultLowlight`=8 `DefaultSolo`=9 `DefaultTime`=10 `GrandMaster`=11 `GrandWorld`=12 `GrandHighlight`=13 `GrandLowlight`=14 `GrandSolo`=15 `GrandRate`=16 `GrandReserved`=17 `GrandProgramTime`=18 `GrandProgramXFade`=19 `GrandExecTime`=20 `GrandExecXFade`=21 `GrandSoundOut`=23 `GrandSoundIn`=24 `GrandSoundFade`=25 `Speed1`=26 `Speed2`=27 `Speed3`=28 `Speed4`=29 `Speed5`=30 `Speed6`=31 `Speed7`=32 `Speed8`=33 `Speed9`=34 `Speed10`=35 `Speed11`=36 `Speed12`=37 `Speed13`=38 `Speed14`=39 `Speed15`=40 `BPM`=41 `Playback1`=42 `Playback2`=43 `Playback3`=44 `Playback4`=45 `Playback5`=46 `Playback6`=47 `Playback7`=48 `Playback8`=49 `Playback9`=50 `Playback10`=51 `Playback11`=52 `Playback12`=53 `Playback13`=54 `Playback14`=55 `Playback15`=56 `Playback16`=57 `Playback17`=58 `Playback18`=59 `Playback19`=60 `Playback20`=61 `Playback21`=62 `Playback22`=63 `Playback23`=64 `Playback24`=65 `Playback25`=66 `Playback26`=67 `Playback27`=68 `Playback28`=69 `Playback29`=70 `Playback30`=71 `Playback31`=72 `Playback32`=73 `Playback33`=74 `Playback34`=75 `Playback35`=76 `Playback36`=77 `Playback37`=78 `Playback38`=79 `Playback39`=80 `Playback40`=81 `Playback41`=82 `Playback42`=83 `Playback43`=84 `Playback44`=85 `Playback45`=86 `Playback46`=87 `Playback47`=88 `Playback48`=89 `Playback49`=90 `Playback50`=91 `Timing1`=93 `Timing2`=94 `Timing3`=95 `Timing4`=96 `Timing5`=97 `Timing6`=98 `Timing7`=99 `Timing8`=100 `Timing9`=101 `Timing10`=102 `Timing11`=103 `Timing12`=104 `Timing13`=105 `Timing14`=106 `Timing15`=107 `Timing16`=108 `Timing17`=109 `Timing18`=110 `Timing19`=111 `Timing20`=112 `Timing21`=113 `Timing22`=114 `Timing23`=115 `Timing24`=116 `Timing25`=117 `Timing26`=118 `Timing27`=119 `Timing28`=120 `Timing29`=121 `Timing30`=122 `Timing31`=123 `Timing32`=124 `Timing33`=125 `Timing34`=126 `Timing35`=127 `Timing36`=128 `Timing37`=129 `Timing38`=130 `Timing39`=131 `Timing40`=132 `Timing41`=133 `Timing42`=134 `Timing43`=135 `Timing44`=136 `Timing45`=137 `Timing46`=138 `Timing47`=139 `Timing48`=140 `Timing49`=141 `Timing50`=142 `None`=255

`Enums.Master.DefaultMaster`

## MasterPriority

`Never`=0 `VeryLow`=1 `Low`=2 `Normal`=3 `High`=4

`Enums.MasterPriority.Never`

## MasterReaction

`None`=0 `Group`=1 `Grand`=2

`Enums.MasterReaction.None`

## MasterTitleFunction

`Locate`=0 `SelectFixtures`=1

`Enums.MasterTitleFunction.Locate`

## MatricksBlockNone

`No Block`=-1 `None`=0

`Enums.MatricksBlockNone.None`

## MatricksGroupNone

`No Group`=-1 `None`=0

`Enums.MatricksGroupNone.None`

## MatricksIndexNone

`No XYZ`=-2 `None`=-1

`Enums.MatricksIndexNone.None`

## MatricksInvert

``=0 `On`=1

`Enums.MatricksInvert.On`

## MatricksInvertStyle

`Pan`=0 `Tilt`=1 `P+T`=2 `All`=3

`Enums.MatricksInvertStyle.Pan`

## MatricksShiftNone

`None`=0 `No Shift`=32768

`Enums.MatricksShiftNone.None`

## MatricksShuffleNone

`None`=0 `No Shuffle`=32768

`Enums.MatricksShuffleNone.None`

## MatricksTabs

`X`=0 `Y`=1 `Z`=2 `Shuffle`=3

`Enums.MatricksTabs.X`

## MatricksWingsNone

`No Wings`=-1 `None`=0

`Enums.MatricksWingsNone.None`

## MatrixWidthAuto

`No Width`=-1 `None`=0

`Enums.MatrixWidthAuto.None`

## MeasurementInterpolation

`Linear`=0 `Step`=1 `Log`=2

`Enums.MeasurementInterpolation.Linear`

## MeasurementStatus

`Measuring Fixture`=0 `No Device Found`=1 `Device Found`=2 `Dark Calibration Successful`=3 `Dark Calibration Failed`=4 `Idle`=5

`Enums.MeasurementStatus.Idle`

## MessageCategory

`Undefined`=0 `System`=1 `Cmdline`=2 `Power`=3 `Manet`=4 `USB`=5 `Chat`=6

`Enums.MessageCategory.Undefined`

## MessageCategoryName

`Undefined`=0 `System`=1 `Command Line`=2 `Power`=3 `MA-Net`=4 `USB`=5 `Chat`=6

`Enums.MessageCategoryName.Undefined`

## MessageCenterRememberedTab

`Messages`=0 `Statuses`=1

`Enums.MessageCenterRememberedTab.Messages`

## MessagePriority

`Undefined`=0 `Information`=1 `Warnings`=2 `Errors`=3 `Alerts`=4

`Enums.MessagePriority.Undefined`

## MibEnableMode

`Enabled`=0 `Never`=1 `Force Early`=2 `Force UponGo`=3 `Force Late`=4

`Enums.MibEnableMode.Enabled`

## MibMode

`Default`=0 `None`=1 `Defined`=2 `Early`=3 `UponGo`=4 `Late`=5

`Enums.MibMode.Default`

## MibModeSequence

`None`=1 `Early`=3 `UponGo`=4 `Late`=5

`Enums.MibModeSequence.None`

## MibMultiStep

`Running`=0 `Paused`=1

`Enums.MibMultiStep.Running`

## MibPreferenceLevel

`Never(0)`=0 `Never`=0 `Worst`=1 `Worst(1)`=1 `Bad(25)`=25 `Bad`=25 `Normal`=50 `Normal(50)`=50 `Good`=75 `Good(75)`=75 `Best`=100 `Best(100)`=100

`Enums.MibPreferenceLevel.Never`

## MibTiming

`Default`=9223372036854775807

`Enums.MibTiming.Default`

## MidiShowControlCommandMode

`Extensions`=0 `General Light`=1 `Moving Light`=2 `All`=127

`Enums.MidiShowControlCommandMode.Extensions`

## MidiShowControlExecMode

`Default`=0 `Executor.Page`=1 `Executor Page`=2

`Enums.MidiShowControlExecMode.Default`

## MidiShowControlRowDisabled

`Disabled`=65535

`Enums.MidiShowControlRowDisabled.Disabled`

## MidiShowControlSendTo

`Group`=0 `Device`=1 `All`=2

`Enums.MidiShowControlSendTo.Group`

## MiniFadersMode

`None`=0 `Full`=1 `Blades`=2 `Rotation`=3

`Enums.MiniFadersMode.None`

## ModalResult

`None`=0 `Ok`=1 `Cancel`=2 `Confirm`=3

`Enums.ModalResult.None`

## Month

`January`=0 `February`=1 `March`=2 `April`=3 `May`=4 `June`=5 `July`=6 `August`=7 `September`=8 `October`=9 `November`=10 `December`=11

`Enums.Month.January`

## MonthShort

`Jan`=0 `Feb`=1 `Mar`=2 `Apr`=3 `May`=4 `Jun`=5 `Jul`=6 `Aug`=7 `Sep`=8 `Oct`=9 `Nov`=10 `Dec`=11

`Enums.MonthShort.Jan`

## MouseButtonTypes

`Left`=0 `Right`=1 `Middle`=2

`Enums.MouseButtonTypes.Left`

## MouseCursorSize

`Small`=0 `Medium`=1 `Large`=2

`Enums.MouseCursorSize.Small`

## MouseSpeed

`Slow`=1 `Normal`=2 `Fast`=3

`Enums.MouseSpeed.Slow`

## MoveValueToPart

`Default`=4294967295

`Enums.MoveValueToPart.Default`

## MultiCastBase

`Default`=66796 `Alternative`=66799

`Enums.MultiCastBase.Default`

## MultiLedBeamMode

`Separated Beams`=0 `Single Beam Mean Color`=1 `Single Beam Dynamic Gobo`=2

`Enums.MultiLedBeamMode["Separated Beams"]`

## MvrObjectType

`Fixture`=0 `GroupObject`=1 `SceneObject`=2 `FocusPoint`=3 `Truss`=4 `VideoScreen`=5 `Projector`=6 `Support`=7 `MISSING`=8

`Enums.MvrObjectType.Fixture`

## MvrTab

`MVR`=0 `Patch`=1

`Enums.MvrTab.MVR`

## NDIBandwidth

`Lowest`=0 `Highest`=100

`Enums.NDIBandwidth.Lowest`

## NackStat

`Reset`=0

`Enums.NackStat.Reset`

## NetworkFilter

`All`=0 `My Session`=1 `Not My Session`=2 `Wrong Version`=3 `My Location`=4

`Enums.NetworkFilter.All`

## NoName



## None

``=4294967295 `None`=4294967295

`Enums.None.None`

## NoneAndDefault

`None`=0 `Default`=1000001

`Enums.NoneAndDefault.None`

## None_only

`None`=4294967295

`Enums.None_only.None`

## NotificationType

`Timed`=0 `Permanent`=1

`Enums.NotificationType.Timed`

## OSCMode

`UDP`=0 `TCP`=1

`Enums.OSCMode.UDP`

## OffCueTrigger

`Go`=0 `Time`=1 `Follow`=2 `Sound`=3 `BPM`=4 `No Trigger`=5 ``=5

`Enums.OffCueTrigger.Go`

## OnOff

`Off`=0 `On`=1

`Enums.OnOff.Off`

## OnOffStatus

`Off`=0 `On`=1 `Toggle`=2 `Undefined`=3

`Enums.OnOffStatus.Off`

## OopsConfirmation

`Never`=0 `Main`=1 `Always`=2

`Enums.OopsConfirmation.Never`

## Orientation

`Vertical`=0 `Horizontal`=1

`Enums.Orientation.Vertical`

## OutputDelay

`None`=0 `Max`=30

`Enums.OutputDelay.None`

## PSRPatchFilterType

`None`=0 `Matched`=1 `Unmatched`=2 `Conflicted`=3

`Enums.PSRPatchFilterType.None`

## PUPriority

`Never`=0 `VeryLow`=1 `Low`=2 `Normal`=3 `High`=4

`Enums.PUPriority.Never`

## PatchOffset

`None`=-1

`Enums.PatchOffset.None`

## PatchType

``=0 `Coarse`=1 `Fine`=2 `Ultra`=3

`Enums.PatchType.Coarse`

## Patched

``=-1

`Enums.Patched[""]`

## PathContentType

`System`=0 `User`=1 `Mixed`=2

`Enums.PathContentType.System`

## PathType

`BinaryDir`=0 `ExternalRoot`=1 `ExternalPackages`=2 `MADir`=3 `VersionDir`=4 `InstallationPackages`=5 `UpdateDir`=6 `WebDaemon`=7 `Data`=8 `Shared`=9 `Config`=10 `Usb`=11 `Temp`=12 `Undo`=13 `CrashLog`=14 `UploadedCrashLogs`=15 `InvalidCrashLogs`=16 `Statistics`=17 `CombinedShaders`=18 `Showfiles`=19 `Backupfiles`=20 `DemoShowfiles`=21 `PSRFiles`=22 `Resource`=23 `WebResource`=24 `Language`=25 `ColorTheme`=26 `Dummy`=27 `ShadersSmall`=28 `Shaders`=29 `Textures`=30 `Fonts`=31 `GoboImageLibrary`=32 `GoboImageCache`=33 `Mesh`=34 `MaterialLibrary`=35 `RenderQuality`=36 `SymbolImageLibrary`=37 `ImageLibrary`=38 `VideoLibrary`=39 `GelLibrary`=40 `AgendaLibrary`=41 `AddonLibrary`=42 `MenuLibrary`=43 `PluginLibrary`=44 `MacroLibrary`=45 `QuickeyLibrary`=46 `MatricksLibrary`=47 `PresetLibrary`=48 `GeneratorsLibrary`=49 `BitmapsLibrary`=50 `FilterLibrary`=51 `ShapeLibrary`=52 `FixtureLibrary`=53 `GrandMA2Library`=54 `GrandMA3Library`=55 `WorldServerLibrary`=56 `Keyboards`=57 `KeyboardShortcuts`=58 `Software`=59 `VizLibrary`=60 `MvrLibrary`=61 `DmxCurvesLibrary`=62 `PythonLibrary   `=63 `Library`=64 `TemplateShowfiles`=65 `UserMedia`=66 `UserSoundLibrary`=67 `UserVideoLibrary`=68 `UserImageLibrary`=69 `UserSymbols`=70 `ScribbleLibrary`=71 `AppearanceLibrary`=72 `NetworkKeys`=73 `UserInOut`=74 `OSC`=75 `SACN`=76 `ArtNet`=77 `UserRemotesDC`=78 `UserRemotesDMX`=79 `UserRemotesMIDI`=80 `UserOutputConfig`=81 `UserDeviceConfig`=82 `UserFixtures`=83 `UserFixtureTypeResources`=84 `UserGobos`=85 `UserMeshes`=86 `UserMeshImages`=87 `UserMaterials`=88 `UserGdtfResources`=89 `UserMvr`=90 `UserUsers`=91 `UserProfiles`=92 `UserViews`=93 `ViewButtonLibrary`=94 `UserCameras`=95 `UserScreenConfigurations`=96 `UserRenderQuality`=97 `UserKeyboardShortcuts`=98 `UserGels`=99 `UserEncoderBars`=100 `UserAgendas`=101 `UserCertificates`=102 `UserColorThemes`=103 `UserDataPools`=104 `CustomPluginLibrary`=105 `UserLayouts`=106 `UserExecConfigs`=107 `UserMacros`=108 `UserMatricks`=109 `UserPresets`=110 `UserGroups`=111 `UserSequences`=112 `UserWorlds`=113 `UserFilters`=114 `UserExecutors`=115 `UserTimecodes`=116 `UserTimers`=117 `UserBitmaps`=118 `UserGenerators`=119 `UserQuickeys`=120 `UserShapes`=121 `UserPatch`=122 `UserStages`=123 `UserDmxCurves`=124

`Enums.PathType.BinaryDir`

## PhaseRangesValue

`0 Thru 90°`=-9205357638345293824 `0 Thru 180°`=-9187343239835811840 `0 Thru 360°`=-9151314442816847872 `0 Thru -360°`=-8142508126285856768 `0 Thru -180°`=-8106479329266892800 `0 Thru -90°`=-8088464930757410816 `90°`=4194304 `180°`=8388608 `270°`=12582912 `360°`=16777216 `No Phase`=2147483645 `Swap Phase`=2147483646

`Enums.PhaseRangesValue["0 Thru 90°"]`

## PhaseRangesValueNone

`0 Thru 90°`=-9205357638345293824 `0 Thru 180°`=-9187343239835811840 `0 Thru 360°`=-9151314442816847872 `0 Thru -360°`=-8142508126285856768 `0 Thru -180°`=-8106479329266892800 `0 Thru -90°`=-8088464930757410816 `90°`=4194304 `180°`=8388608 `270°`=12582912 `360°`=16777216 `No Phase`=2147483645 `Swap Phase`=2147483646 `None`=2147483647

`Enums.PhaseRangesValueNone.None`

## PhaseValueNone

`0°`=0 `90°`=4194304 `180°`=8388608 `270°`=12582912 `360°`=16777216 `No Phase`=2147483645 `Swap Phase`=2147483646 `None`=2147483647

`Enums.PhaseValueNone.None`

## PhaserAbsRelMode

`Absolute`=1 `Relative`=2 `Abs+Rel`=3

`Enums.PhaserAbsRelMode.Absolute`

## PhaserBars

`2DBar`=0 `PhaserBar`=1 `PresetBar`=2

`Enums.PhaserBars.PhaserBar`

## PhaserEditTool

`MoveArea`=0 `Select`=1 `AddAbsolute`=2 `AddRelative`=3 `MovePoint`=4 `MoveSpline`=5 `ChangeSize`=6 `ChangeRotation`=7 `ChangePhase`=8 `ChangeWidth`=9 `SelectForm`=10 `ChangeSpeed`=11

`Enums.PhaserEditTool.MoveArea`

## PhaserEncoderFunction

`Move & Size`=0

`Enums.PhaserEncoderFunction["Move & Size"]`

## PhaserFields

`AbsPreset`=0 `RelPreset`=1 `Fade`=2 `Delay`=3 `Speed`=4 `Phase`=5 `GridPos`=6 `Measure`=7 `NShot`=8

`Enums.PhaserFields.AbsPreset`

## PhaserLineHeight

`Auto`=50

`Enums.PhaserLineHeight.Auto`

## PhaserMode1D

`Value`=0 `Transition`=1

`Enums.PhaserMode1D.Value`

## PhaserRecipeContextTab

`Pool`=0 `List`=1 `Editor`=2

`Enums.PhaserRecipeContextTab.Pool`

## PhaserRecipeDirection

`Forward`=0 `Backward`=1 `Alternate`=2

`Enums.PhaserRecipeDirection.Forward`

## PhaserRecipeStepLinking

``=0 `None`=0 `Linked`=1

`Enums.PhaserRecipeStepLinking.None`

## PhaserRecipeValueSpecials

`Release`=1124073472 `ChannelFunctionDefault`=1124073473 `Default`=1124073474 `Highlight`=1124073475 `Lowlight`=1124073476 `Zero`=1124073477 `Full`=1124073478 `None`=1124073479

`Enums.PhaserRecipeValueSpecials.Release`

## PhaserRecipeValueSpecialsRaw

`Remove`=264 `Release`=1124073472 `ChannelFunctionDefault`=1124073473 `Default`=1124073474 `Highlight`=1124073475 `Lowlight`=1124073476 `Zero`=1124073477 `Full`=1124073478 `None`=1124073479

`Enums.PhaserRecipeValueSpecialsRaw.Remove`

## PhaserSheetMode

`Step`=0 `Layer Condensed`=1 `Layer Expanded`=2

`Enums.PhaserSheetMode.Step`

## PhaserTransformations

`None`=0 `MirrorValues`=1 `MirrorTimeMiddle`=2 `MirrorTimeStart`=3 `SquashToOne`=4

`Enums.PhaserTransformations.None`

## PhaserTransformationsShort

`None`=0 `Mirror`=1

`Enums.PhaserTransformationsShort.None`

## PhaserValueFields

`Integrated`=0 `Absolute`=1 `Relative`=2 `Accel`=3 `Decel`=4 `Trans`=5 `Width`=6

`Enums.PhaserValueFields.Integrated`

## PhaserViewMode

`Auto`=0 `2D`=1 `1D`=2 `Sheet`=3

`Enums.PhaserViewMode.Auto`

## PhysicalUnit

`None`=0 `Percent`=1 `Length`=2 `Mass`=3 `Time`=4 `Temperature`=5 `LuminousIntensity`=6 `Angle`=7 `Force`=8 `Frequency`=9 `Current`=10 `Voltage`=11 `Power`=12 `Energy`=13 `Area`=14 `Volume`=15 `Speed`=16 `Acceleration`=17 `AngularSpeed`=18 `AngularAccc`=19 `WaveLength`=20 `ColorComponent`=21

`Enums.PhysicalUnit.None`

## PlaybackMaster

`Playback1`=0 `Playback2`=1 `Playback3`=2 `Playback4`=3 `Playback5`=4 `Playback6`=5 `Playback7`=6 `Playback8`=7 `Playback9`=8 `Playback10`=9 `Playback11`=10 `Playback12`=11 `Playback13`=12 `Playback14`=13 `Playback15`=14 `Playback16`=15 `Playback17`=16 `Playback18`=17 `Playback19`=18 `Playback20`=19 `Playback21`=20 `Playback22`=21 `Playback23`=22 `Playback24`=23 `Playback25`=24 `Playback26`=25 `Playback27`=26 `Playback28`=27 `Playback29`=28 `Playback30`=29 `Playback31`=30 `Playback32`=31 `Playback33`=32 `Playback34`=33 `Playback35`=34 `Playback36`=35 `Playback37`=36 `Playback38`=37 `Playback39`=38 `Playback40`=39 `Playback41`=40 `Playback42`=41 `Playback43`=42 `Playback44`=43 `Playback45`=44 `Playback46`=45 `Playback47`=46 `Playback48`=47 `Playback49`=48 `Playback50`=49 `None`=255

`Enums.PlaybackMaster.Playback1`

## PlaybackPriority

`Super`=0 `Swap`=2 `HTP`=3 `Highest`=4 `High`=5 `LTP`=6 `Low`=7 `Lowest`=8

`Enums.PlaybackPriority.Super`

## PlaybackSourceSubTypes

``=0 `Tracked`=1 `Blocked`=2 `UpGoing`=3 `DownGoing`=4 `MIB`=5 `MIBFade`=6

`Enums.PlaybackSourceSubTypes.Tracked`

## PlaybackType

`Programmer`=0 `Preset`=1 `Sequence`=2 `Timecode`=3 `Macro`=4 `Timer`=5 `Sound`=6 `Generator`=7 `All`=8

`Enums.PlaybackType.Programmer`

## PlaybackWindowExecFrom

`None`=0 `01-05`=1 `06-10`=2 `11-15`=3 `16-20`=4 `21-25`=5 `26-30`=6 `31-35`=7 `36-40`=8 `41-45`=9 `46-50`=10 `51-55`=11 `56-60`=12 `61-65`=13 `66-70`=14 `71-75`=15 `81-85`=15 `76-80`=16 `86-90`=16

`Enums.PlaybackWindowExecFrom.None`

## PlaybacksOff

`Keep Playbacks`=0 `Playbacks Off`=1

`Enums.PlaybacksOff["Keep Playbacks"]`

## PlaybacksToShow

`Sequences`=0 `Macros`=1 `Timecodes`=2 `Presets`=3 `Timers`=4 `SoundFiles`=5 `All`=6

`Enums.PlaybacksToShow.Sequences`

## PluginPlacement

`Single`=0 `Multi`=1 `ForceMulti`=2

`Enums.PluginPlacement.Single`

## PluginPoolAction

`Toggle`=2 `Call`=9 `None`=255

`Enums.PluginPoolAction.Toggle`

## PolicyOnEnter

`Nothing`=0 `Clear`=1 `SelectAll`=2

`Enums.PolicyOnEnter.Nothing`

## PoolSizeFactor

`Half`=0 `Normal`=1 `Double`=2

`Enums.PoolSizeFactor.Half`

## Pooltype

`None`=0 `Appearance`=1 `ImageGobo`=2 `Mesh`=3 `SymbolImage`=4 `UserImage`=5 `VideoFile`=6 `Plugin`=7 `SoundFile`=8 `Camera`=9 `DataPool`=10 `EncoderBar`=11 `ExecConfig`=12 `ExecPage`=13 `Filter`=14 `Gel`=15 `Group`=16 `Layout`=17 `Macro`=18 `Material`=19 `Menu`=20 `Matricks`=21 `ObjectTag`=22 `Preset`=23 `Quickey`=24 `GeneratorRandom`=25 `GeneratorBitmap`=26 `RenderQuality`=27 `Scribble`=28 `Sequence`=29 `Tag`=30 `Timecode`=31 `Timer`=32 `View`=33 `World`=34 `User`=35 `UserProfile`=36 `Shape`=37 `TimecodeSlot`=38 `Universe`=39 `sMArt`=40

`Enums.Pooltype.None`

## PresetAction

`Toggle`=2 `Go+`=3 `Flash`=4 `Temp`=5 `At`=6 `SelFix/At`=7 `SelFix/Extract`=8 `None`=255

`Enums.PresetAction.Toggle`

## PresetActionToken

`None`=0 `Flash`=1 `Go+`=3 `Temp`=13 `Toggle`=14 `At`=48 `SelFix/Extract`=55 `SelFix/At`=124 `Pool Default`=417

`Enums.PresetActionToken.None`

## PresetDisplayMode

`Text and Icon`=0 `Text`=1 `Icon`=2 `Auto`=3

`Enums.PresetDisplayMode.Text`

## PresetFilterMode

`None`=-1 `Input`=0 `Output`=1 `Both`=2

`Enums.PresetFilterMode.None`

## PresetIsPlayback

`Auto`=0 `On`=1

`Enums.PresetIsPlayback.Auto`

## PresetLinkMode

`None`=-1 `Referenced`=0 `Integrated`=1 `Both`=2

`Enums.PresetLinkMode.None`

## PresetMode

`Default`=0 `Selective`=1 `Global`=2 `Universal`=3

`Enums.PresetMode.Default`

## PresetModeDefault

`Default`=0 `Selective`=1 `Global`=2 `Universal`=3 `ForceGlobal`=4 `ForceUniversal`=5

`Enums.PresetModeDefault.Default`

## PresetModeWithoutDefault

`Selective`=1 `Global`=2 `Universal`=3

`Enums.PresetModeWithoutDefault.Selective`

## PresetReadoutMode

`Name`=0 `Value`=1 `Name+Value`=2 `ID`=3 `ID+Name`=4 `ID+Name+Value`=5

`Enums.PresetReadoutMode.Name`

## PresetReadoutModeAuto

`Auto`=-1 `Name`=0 `Value`=1 `Name+Value`=2 `ID`=3 `ID+Name`=4 `ID+Name+Value`=5

`Enums.PresetReadoutModeAuto.Auto`

## PresetValuesMode

`Normal`=0 `Default`=1 `Highlight`=2 `Lowlight`=3

`Enums.PresetValuesMode.Normal`

## Pretty_RDMSensorUnit

``=0 `°C`=1 `V (DC)`=2 `V (AC P-P)`=3 `V (AC RMS)`=4 `A (DC)`=5 `A (AC P-P)`=6 `A (AC RMS)`=7 `Hz`=8 `Ω`=9 `W`=10 `kg`=11 `m`=12 `m²`=13 `m³`=14 `kg/(m²)`=15 `m/s`=16 `m/(s²)`=17 `N`=18 `J`=19 `P`=20 `s`=21 `°`=22 `sr`=23 `cd`=24 `lm`=25 `lx`=26 `IRE`=27 `B`=28 `UNITS_MS`=128

`Enums.Pretty_RDMSensorUnit.Hz`

## PrettyRDMSensorUnitPrefix

``=0 `d`=1 `c`=2 `m`=3 `micro`=4 `n`=5 `p`=6 `f`=7 `a`=8 `z`=9 `y`=10 `da`=17 `h`=18 `k`=19 `M`=20 `G`=21 `T`=22 `P`=23 `E`=24 `Z`=25 `Y`=26

`Enums.PrettyRDMSensorUnitPrefix.d`

## PreviewAutoStart

`Off`=0 `Single`=1 `Multi`=2

`Enums.PreviewAutoStart.Off`

## PreviewTransfer

`Clear`=0 `Copy`=1

`Enums.PreviewTransfer.Clear`

## PriorityName

`Undefined`=0 `Information`=1 `Warnings`=2 `Errors`=3 `Alerts`=4

`Enums.PriorityName.Undefined`

## ProgLayer

`Fade`=2 `Delay`=3 `Speed`=4 `SpeedMaster`=5 `Phase`=6 `GridPos`=7 `Measure`=8 `NShot`=9 `Absolute`=11 `Relative`=12 `Accel`=13 `Decel`=14 `Transition`=15 `Width`=16 `CueAbs`=18 `CueRel`=19 `DMX`=20 `Output`=21

`Enums.ProgLayer.Fade`

## ProgLayerAuto

`Auto`=-1 `Fade`=2 `Delay`=3 `Speed`=4 `SpeedMaster`=5 `Phase`=6 `GridPos`=7 `Measure`=8 `NShot`=9 `Absolute`=11 `Relative`=12 `Accel`=13 `Decel`=14 `Transition`=15 `Width`=16 `CueAbs`=18 `CueRel`=19 `DMX`=20 `Output`=21

`Enums.ProgLayerAuto.Auto`

## ProgUpdateCueMode

`All`=0 `Selected`=1 `LastGo`=2

`Enums.ProgUpdateCueMode.All`

## ProgValueSource

`None`=0 `ProgValue`=1 `ProgPreset`=2 `ProgIntegrated`=3 `ActiveValue`=4 `ActivePreset`=5 `ActiveIntegrated`=6 `ProgOther`=7 `Playback`=8 `PlaybackTracked`=9 `PlaybackBlocked`=10 `PlaybackUpGoing`=11 `PlaybackDownGoing`=12 `PlaybackMIB`=13 `PlaybackMIBFade`=14 `PlaybackOther`=15 `PlaybackOtherTracked`=16 `PlaybackOtherBlocked`=17 `PlaybackOtherUpGoing`=18 `PlaybackOtherDownGoing`=19 `PlaybackOtherMIB`=20 `PlaybackOtherMIBFade`=21 `SelectedPlayback`=22 `SelectedPlaybackTracked`=23 `SelectedPlaybackBlocked`=24 `SelectedPlaybackUpGoing`=25 `SelectedPlaybackDownGoing`=26 `SelectedPlaybackMIB`=27 `SelectedPlaybackMIBFade`=28

`Enums.ProgValueSource.None`

## ProgrammingLayer

`Fade`=2 `Delay`=3 `Speed`=4 `SpeedMaster`=5 `Phase`=6 `GridPos`=7 `Measure`=8 `NShot`=9 `Absolute`=11 `Relative`=12 `Accel`=13 `Decel`=14 `Transition`=15 `Width`=16

`Enums.ProgrammingLayer.Fade`

## ProgrammingLayerGroup

`Values`=0 `Phaser`=1 `Steps`=2

`Enums.ProgrammingLayerGroup.Values`

## PropertyRadioButtonListEnabledItems

`AllEnabled`=4294967295

`Enums.PropertyRadioButtonListEnabledItems.AllEnabled`

## PropertyRadioButtonListSetType

`Set`=0 `Direct`=1 `Property`=2

`Enums.PropertyRadioButtonListSetType.Set`

## PsrDataPool

`Original`=4294967295

`Enums.PsrDataPool.Original`

## PsrFileMode

`Show`=0 `MVR`=1

`Enums.PsrFileMode.Show`

## PsrOperation

`Closed`=0 `Preparation`=1 `OpenPatch`=2 `Conversion`=3 `OpenImport`=4 `Importing`=5 `Dependencies`=6 `HandleMatch`=7 `MvrPreparation`=8 `MvrOpenPatch`=9

`Enums.PsrOperation.Closed`

## PsrTab

`Show`=0 `Patch`=1 `Import`=2

`Enums.PsrTab.Show`

## PultType

`Any`=0 `Conventional`=1 `Web`=2

`Enums.PultType.Any`

## RDMCommandClass

`DISCOVER`=16 `DISCOVER_RESP`=17 `GET`=32 `GET_RESP`=33 `SET`=48 `SET_RESP`=49

`Enums.RDMCommandClass.DISCOVER`

## RDMDataType

`DS_NOT_DEFINED`=0 `DS_BIT_FIELD`=1 `DS_ASCII`=2 `DS_UNSIGNED_BYTE`=3 `DS_SIGNED_BYTE`=4 `DS_UNSIGNED_WORD`=5 `DS_SIGNED_WORD`=6 `DS_UNSIGNED_DWORD`=7 `DS_SIGNED_DWORD`=8 `DS_MS`=128

`Enums.RDMDataType.DS_NOT_DEFINED`

## RDMLampOnMode

`LAMP_ON_MODE_OFF`=0 `LAMP_ON_MODE_DMX`=1 `LAMP_ON_MODE_ON`=2 `LAMP_ON_MODE_AFTER_CAL`=3 `Manufacturer-Specific Modes`=128

`Enums.RDMLampOnMode.LAMP_ON_MODE_OFF`

## RDMLampState

`LAMP_OFF`=0 `LAMP_ON`=1 `LAMP_STRIKE`=2 `LAMP_STANDBY`=3 `LAMP_NOT_PRESENT`=4 `LAMP_ERROR`=127 `Manufacturer-Specific States`=128

`Enums.RDMLampState.LAMP_OFF`

## RDMManufacturerId

`ESTA`=0 `GEE`=1 `Creative Lighting And Sound Systems Pty Ltd`=161 `St. Anne Engineering GmbH`=257 `Bortis Elektronik`=258 `LGR`=364 `ABLELITE INTERNATIONAL`=578 `Imlight-Showtechnic`=603 `Acuity Brands Lighting Inc.`=623 `LLC Likhoslavl Plant of Lighting Engineering (Svetotehnika)`=672 `LLC Moscow Experimental Lighting Plant (TeleMechanic)`=673 `OJSC Kadoshkinsky electrotechnical`=674 `Jinnax Opto Technology Co., Ltd.`=682 `RE-Engineering`=701 `Growflux LLC`=712 `Acclaim Lighting`=714 `GVA Lighting, Inc.`=715 `Winona Lighting`=720 `Tait Towers Manufacturing Inc.`=737 `Lutron Electronics`=748 `Shanghai Moons Automation Control Co., Ltd`=771 `feno GmbH`=774 `ImageCue LLC`=776 `Carallon Ltd.`=812 `Lux Lumen`=826 `Rosstech Signals Inc.`=843 `Strich Labs`=911 `Alcorn McBride Inc.`=913 `i2Systems`=915 `Prism Projection`=916 `Lightforce Lasertechnik`=923 `eX Systems`=981 `FLUX ECLAIRAGE`=1060 `Guangzhou VAS Lighting Co., Ltd.`=1088 `Birdbrain Labs LLC`=1102 `Lamp & Pencil`=1109 `Krisledz Pte. Ltd.`=1166 `Grand Canyon LED Lighting System (Suzhou) Co., Ltd.`=1167 `MEB Veranstaltungstechnik GmbH`=1190 `Edward J. Keefe Jr.`=1193 `Targetti Sankey Spa`=1239 `ChamSys Ltd.`=1290 `Ambitsel, Inc.`=1308 `OSRAM`=1321 `TERMINAL-COM`=1335 `EverBrighten Co., Ltd.`=1344 `PRO-SOLUTIONS`=1375 `COSMOLIGHT SRL`=1387 `Lumascape Lighting Industries`=1388 `JIAXING XINHUALI LIGHTING & SOUNDING CO., LTD.`=1395 `Innovation LED Limited`=1408 `Shenzhen Lesan Lighting Co., Ltd.`=1451 `Turkowski GmbH`=1461 `Brighten Technology Development Co., Ltd.`=1487 `D-LED Illumination Technologies Ltd.`=1491 `Guangzhou Chai Yi Light Co., Ltd.`=1519 `Diginet Control Systems Pty Ltd`=1545 `Lighting Science Group (formerly LED Effects, Inc.)`=1547 `CKC Lighting Co., Ltd.`=1579 `RDC, Inc. d.b.a. LynTec`=1616 `OFilms`=1630 `LEDART LLC`=1668 `IBL/ESD-Datentechnik GmbH`=1669 `Light.Audio.Design`=1696 `RHENAC Systems GmbH`=1732 `L&L Luce&Light`=1735 `American-Pro International`=1742 `Equipson S.A.`=1766 `SISTEMA Jsc`=1772 `CTG sp. z o.o.`=1776 `Drinelec`=1794 `Conceptinetics Technologies and Consultancy Ltd.`=1799 `Theatrelight New Zealand`=1807 `D.T.S. Illuminazione srl`=1808 `Laser Imagineering GmbH`=1810 `SGM A/S`=1836 `RayComposer - R. Adams`=1839 `Galaxia Electronics`=1842 `CPOINT`=1844 `Corsair Technology Ltd.`=1851 `Panasonic Corporation`=1871 `LEDEngin Inc.`=1887 `lumenetix`=1910 `FATEC sarl`=1930 `MY-Semi Inc.`=1938 `ADDiCTiON BoX GbR`=1968 `Griven S.r.l.`=1996 `THELIGHT Luminary for Cine and TV S.L.`=2045 `Event Lighting Pty, Ltd.`=2055 `Zero 88`=2056 `Junction Inc. Ltd`=2129 `Juno Lighting Group`=2136 `ARC Solid-State Lighting Corp.`=2165 `OTTEC Technology GmbH`=2168 `SIRS-E`=2181 `Highendled Electronics Company Limited`=2186 `ADL Electronics Ltd.`=2202 `Adam Hall GmbH`=2212 `PiXL Factory`=2218 `Bushveld Labs`=2220 `AAdyn Technology`=2223 `KIM Lighting`=2224 `MCI Group`=2226 `Stealth Light srl`=2227 `Lug Light Factory Sp. z o. o.`=2237 `Ehrgeiz`=2245 `SVI Public Company Limited`=2259 `Sensa-Lite Ltd.`=2260 `PatternAgents, LLC`=2263 `W.A. Benjamin Electric Co.`=2264 `STILED`=2265 `Red Arrow Controls`=2272 `ShowLED`=2285 `SanDevices, LLC`=2289 `Eulum Design, LLC`=2294 `ACS - Ackerman Computer Sciences`=2297 `Phaton Lighting Co., Ltd.`=2298 `GermTec GmbH & Co. KG`=2305 `Bigbear Co., Ltd.`=2308 `GRE Alpha`=2316 `ACTOR-MATE CO., LTD.`=2326 `David O Smith Design`=2328 `Krislite Pte. Ltd.`=2331 `AquaTronic`=2358 `HDT impex s.r.o.`=2362 `Shenzhen CreateLED Electronics Co., Ltd`=2368 `TBE Srl`=2374 `Guangzhou GTD Lighting Technology Co., Ltd`=2385 `Illum Technology LLC (previously Verde Designs, Inc.)`=2392 `kLabs Research UK`=2394 `Elaborated Networks GmbH`=2399 `Fineline Solutions Ltd.`=2400 `Fontana Fountains`=2405 `Marumo Electric Co., Ltd.`=2420 `KB Design`=2421 `Teamboyce Limited`=2426 `Brink Electronics`=2429 `RaumZeitLabor e.V.`=2431 `Moog Animatics`=2432 `Luxam, Ltd.`=2433 `AC Entertainment Products Ltd.`=2434 `ROE Visual Co. Ltd.`=2438 `mathertel.de`=2439 `Glow Motion Technologies, LLC.`=2443 `Shenzhen Longrich Energy Sources Technology Co., Ltd.`=2444 `Ecosense Lighting Company Limited`=2446 `Digital Sputnik Lighting`=2447 `CCI Power Supplies, LLC`=2454 `Aixz International (S)`=2458 `LLC Lighting Technologies production`=2462 `Rnet Lighting Technology Limited`=2464 `Fountain People`=2466 `Prolight Concepts Ltd.`=2469 `Robert Juliat`=2478 `Autotech Co.`=2479 `Aquatique Show Int.`=2483 `Brompton Technology Ltd.`=2484 `Prolites S.A.L.`=2488 `Argetron Elektrik Elektronik Organizasyon Gida San. ve Dis Tic. Ltd. Sti.`=2497 `Velleman nv`=2499 `Crystal Fountains Inc.`=2504 `Motomuto Aps`=2508 `WLPS Wodielite Production Services`=2515 `Mittomakers`=2518 `Unilumin Group`=2519 `Starway`=2537 `deskontrol electronics`=2556 `Newlab S.r.l.`=4826 `Luxlight Skandinavien AB`=4832 `Kolberg Percussion GmbH`=4842 `Stage Services Ltd.`=4852 `Hollywood Rentals LLC`=4858 `City Design S.p.A.`=4862 `Blossom Communications Corp.`=4894 `Raven Systems Design, Inc.`=4919 `VT-Control`=4941 `Ingenieurbuero Stahlkopf`=4976 `Smartpark Creative Solutions`=5038 `SEIKO Epson Corporation`=5216 `HUMAL Elektroonika OU`=5220 `Grid Show Systems Inc.`=5264 `Intense Lighting, LLC`=5280 `Zaklad Elektroniczny AGAT s.c.`=5292 `v2 Lighting Group, Inc.`=5382 `Fire & Magic`=5454 `GuangZhou MCSWE Technologies, INC`=5536 `Music & Lights S.r.l.`=5584 `techKnow Design Ltd.`=5658 `LEDsistem Teknolojileri Tic. Ltd. Sti.`=5670 `Nerd-s Meter`=5674 `awaptec GmbH`=5776 `Electrone Americas Ltd. Co.`=5806 `Traxon Technologies Ltd.`=5852 `Aboutshow Color Light Co., LTD`=5860 `Lite Puter Enterprise Co., Ltd.`=5882 `Serva Transport Systems GmbH`=5902 `Yuesheng International Limited`=5968 `GUANZHOU KAVON STAGE EQUIPMENT CO., LTD.`=6280 `Solid State Luminaires`=6456 `PLS Electronics Ltd.`=6552 `Duralamp S.p.A.`=6585 `Cineo Lighting`=6669 `WADAK GmbH`=6678 `Red Lighting s.r.l.`=6717 `TMB`=6906 `PH Lightning AB`=7089 `ALS Stanislaw Binkiewicz`=7104 `Studio S Music City`=7110 `Vehtec Tecnologia Ltda`=7296 `Moda Light`=7821 `Masiero s.r.l.`=7887 `Antari Lighting And Effects Ltd.`=7896 `Gantom Lighting & Controls`=8209 `Padura Elektronik GmbH`=8319 `ALADIN Architekturlicht GmbH`=8358 `AZ e-lite Pte Ltd`=8365 `Alkalite LED Technology Corp`=8374 `ARRI -- Arnold & Richter Cine Technik GmbH & Co. Betriebs KG`=8377 `AusChristmasLighting`=8378 `Brother,Brother & Sons Aps`=8481 `BEGLEC NV`=8482 `Bart van Stiphout Electronics & Software`=8496 `Culture Crew bvba`=8609 `CHAUVET Lighting`=8612 `CaptSystemes`=8617 `Coolon Pty Ltd`=8627 `CHROMLECH`=8628 `ChromaCove LLC`=8629 `D-Light Designs, LLC`=8726 `D.E.F. Srl`=8738 `DAS Integrator Pte Ltd`=8740 `Dream Solutions Ltd.`=8761 `EAS SYSTEMS`=8864 `Elation Lighting`=8870 `Engineering Solutions Inc.`=8873 `EUTRAC - Intelligent Lighting GmbH`=8874 `EVC`=8875 `Etherlight`=8889 `Focon Showtechnic`=9015 `Gekko Technology Ltd.`=9138 `HB-Laserkomponenten GmbH`=9249 `Hungaroflash`=9258 `Helvar Ltd`=9266 `Hale Microsystems LLC`=9328 `Lighting Innovation Group AG`=9379 `IT Ihme`=9386 `LEADER LIGHT s.r.o.`=9761 `LDDE Vertriebs Gmbh`=9762 `Leonh Hardware Enterprise Inc.`=9763 `Lisys Fenyrendszer Zrt.`=9764 `LLT Lichttechnik GmbH&CO.KG`=9766 `Laservision Pty Ltd`=9776 `Lehigh Electric Products`=9778 `LjusDesign AB`=9781 `Lumonic Limited`=9782 `Loxone Electronics GmbH`=9783 `Lumenec Pty. Ltd.`=9786 `I-Pix Digital Light Ltd.`=9788 `MEGATECHNICS Ltd.`=9890 `Milford Instruments Ltd.`=9908 `Nila Inc.`=10020 `Nixer Ltd.`=10036 `Callegenix LLC`=10152 `Pioneer Corporation`=10273 `Peter Maes Technology`=10278 `Peternet Electronics BVBA`=10279 `PR-Electronic`=10281 `Planungsbuero`=10294 `ROAL Electronics SpA`=10535 `Getlux Ltd.`=10628 `ALL-DO INTERNATIONALCO., LTD.`=10649 `Sturdy Corporation`=10657 `SRS Light Design`=10665 `Steinigke Showtechnic GmbH`=10666 `Selectron Bvba`=10674 `Showtec (Highlite International B.V.)`=10676 `Sundrax, LLC`=10679 `Spotlight s.r.l.`=10680 `State Automation Pty Ltd.`=10682 `Stroytsirk LLC`=10728 `Thorn Lighting Limited`=10789 `Toni Maroni Gmb`=10790 `Urban Visuals & Effects Ltd.`=10923 `Visual Productions`=11048 `WERPAX bvba`=11170 `The White Rabbit Company, Inc.`=11177 `Williams Electronic Design Ltd.`=11188 `DMX4ALL GmbH`=11290 `XTBA`=11306 `Lighting Services Inc.`=11488 `Stellascapes`=11720 `de koster Special Effects`=12853 `Macostar International Ltd.`=13192 `Global Design Solutions, Ltd.`=13364 `Lumishore Ltd. UK`=13853 `Lumenpulse Lighting Inc.`=13880 `Lichttechnik & Sonderbau`=14295 `Yifeng Lighting Co., Ltd.`=14341 `ACME EFFECTS LTD.`=14342 `LanBolight Technology Co., LTD.`=14440 `Fly Dragon Lighting Equipment Co.,ltd`=14472 `Guangzhou Yajiang (Yagang - Silver Star) Photoelectric Equipment Ltd.`=14474 `TheOlymp - Networking & InterNet Services`=14903 `NXP Semiconductors B.V.`=15120 `zactrack Lighting Technologies Gmbh`=15664 `SAN JACK ANALOG HOUSE CO., LTD.`=16465 `Altman Stage Lighting`=16689 `AVAB America, Inc.`=16705 `AC Lasers`=16707 `ADB - TTV Technologies nv`=16708 `ADE ELETTRONICA srl`=16709 `Anidea Engineering, Inc.`=16713 `Artistic Licence Engineering Ltd.`=16716 `Amptown Lichttechnik GmbH`=16717 `Anytronics Ltd.`=16718 `Apogee Lighting`=16720 `Aquarii, Inc.`=16721 `Audio Scene`=16723 `Arnold Tang Productions`=16724 `Audio Visual Devices P/L`=16726 `Adelto Limited`=16740 `Alenco BV`=16748 `ARNOLD LICHTTECHNIK`=16754 `Astera LED Technology GmbH`=16755 `AYRTON`=16761 `BECKHOFF Automation GmbH`=16961 `Bill Coghill Company : Bill Coghill Design`=16963 `Bytecraft Entertainment Pty Ltd`=16965 `BOTEX`=16975 `Barco`=16979 `Birket Engineering, Inc.`=17058 `CDCA Ltd.`=17220 `CAST Software`=17223 `C.I.Tronics Lighting Designers Ltda`=17225 `Color Kinetics Inc.`=17227 `Coemar Spa`=17229 `CLAY PAKY S.p.A`=17232 `Capricorn Software`=17235 `City Theatrical, Inc.`=17236 `Connex GmbH`=17240 `Cinetix Medien u. Interface GmbH`=17257 `CODEM MUSIC S.r.l.`=17263 `DIGITAL ART SYSTEM`=17473 `ELETTROLAB S.r.l.`=17474 `Claudio Dal Cero Engineering`=17475 `D.O.M. Datenverarbeitung GmbH`=17476 `Dezelectric Kft.`=17477 `Doug Fleenor Design, Inc.`=17478 `Durand Interstellar, Inc.`=17481 `Dove Lighting Systems, Inc.`=17484 `Digimedia Multimedia Lighting Solutions`=17485 `DALCNET SRL`=17486 `DMXPROFI.EU GmbH i.G.`=17488 `Devantech Ltd.`=17494 `DF elettronica s.r.l.`=17510 `Diamante Lighting Srl`=17513 `E:cue Control GmbH`=17722 `Engineering Arts`=17729 `EC Elettronica Srl`=17731 `Electronics Diversified LLC`=17732 `Ingenieurbuero fuer Nachrichtentechnik in der Studio und Veranstaltungstechnik`=17740 `ELM Video Technology, Inc.`=17741 `ENTTEC Pty Ltd`=17742 `EREA`=17746 `ERAL srl`=17747 `Entertainment Technology`=17748 `Les Eclairages Lou Inc.`=17763 `Element Labs Inc.`=17772 `OKEROAB AB`=17969 `Flashlight/Ampco Holding`=17996 `Flexvisual`=18006 `MagicFX B.V.`=18008 `Global Special Effects`=18040 `Goddard Design Co.`=18244 `GPE srl`=18245 `G-LEC Europe GmbH`=18252 `DES`=18256 `Golden Sea Disco Light Manufacturer`=18259 `General Luminaire (Shanghai) Ltd.`=18284 `Horizon Control Inc.`=18499 `HxDx`=18500 `Howard Eaton Lighting Ltd.`=18501 `HBE Lighting Systems`=18508 `Hollywood Controls Inc.`=18511 `Enfis Ltd`=18518 `Rena Electronica B.V.`=18561 `inoage GmbH`=18753 `IBEX UK Limited`=18754 `Ingham Designs`=18756 `Insta Elektro GmbH`=18757 `IGuzzini illuminazione spa`=18759 `Ice House Productions`=18760 `I-Lum`=18764 `Interactive Technologies, Inc.`=18766 `Interesting Products, Inc.`=18768 `Invisible Rival Incorporated`=18770 `Integrated System Technologies Ltd.`=18771 `Integrated Theatre, Inc.`=18772 `Innovation Solutions Ltd.`=18803 `Joshua 1 Systems Inc.`=18993 `JANUS srl`=19009 `JB-lighting GmbH`=19010 `Johnsson Lighting Technologies AB`=19020 `JSC MFG`=19027 `James Thomas Engineering`=19028 `Jands Pty Ltd.`=19041 `RVL techniek`=19148 `KissBox`=19266 `Kino Flo, Inc.`=19270 `KLH Electronics PLC`=19276 `KMX Inc.`=19277 `kuwatec, Inc.`=19285 `LAM32 srl`=19488 `LaserAnimation Sollinger GmbH`=19521 `Leviton Manufacturing Co., Inc.`=19525 `LightGeist Ltd.`=19527 `LUMINEX Lighting Control Equipment bvba`=19532 `Ultratec Special Effects`=19533 `LightProcessor Ltd`=19536 `High End Systems Inc.`=19538 `Licht-, Steuer- und Schaltanlagenbau GmbH (LSS GmbH)`=19539 `Licht-Technik`=19540 `LumenRadio AB`=19541 `LEDValley Technologies Sdn Bhd`=19542 `LightWild LC`=19543 `Lex Products Corp.`=19544 `Laser Technology Ltd.`=19545 `LightMinded Industries, Inc.`=19546 `LightLife, Gesellschaft fuer audiovisuelle Erlebnisse mbH`=19547 `LED Team`=19556 `Legargeant and Associates`=19557 `LIGHTOLIER`=19561 `Lampo Lighting Designers`=19564 `LSC Lighting Systems (Aust) Pty. Ltd.`=19571 `acdc LED Ltd.`=19676 `LED Company s.r.o.`=19685 `MA Lighting Technology GmbH`=19777 `LAN Systems--Midibox project`=19778 `Les Generateurs de brouillard MDG Fog Generators Ltd.`=19780 `Mode Lighting (UK) Ltd.`=19788 `Martin Professional A/S`=19792 `medien technik cords`=19796 `Avolites Ltd.`=19798 `MX design`=19800 `MARTINI S.p.A.`=19809 `Mueller Elektronik`=19831 `Company NA`=20033 `NJD Electronics`=20042 `NOVALIGHT S.r.l.`=20044 `AIM Northwest`=20055 `Niko`=20073 `Oase GmbH`=20289 `DDS Elettronica`=20300 `Outsight Pty Ltd.`=20341 `Philips Entertainment Lighting Asia`=20545 `Pathway Connectivity Inc.`=20547 `Peperoni Lighting-Solutions`=20556 `Peter Meyer Project Management Adviser GmbH`=20557 `Production Resource Group`=20562 `Philips Selecon`=20563 `PXM s.c.`=20568 `LED, Inc.`=20578 `Peradise`=20581 `Pfannenberg GmbH`=20582 `Philips Lighting BV`=20584 `Pulsar Light of Cambridge Ltd.`=20597 `DJPOWER ELECTRONIC STAGE LIGHTING FIXTURE FACTORY (GUANGZHOU)`=20781 `JAP Optoelectronic Ltd.`=20809 `QMAXZ lighting`=20813 `QuickSilver Controls, Inc.`=20819 `Quicklights`=20844 `Revolution Display`=21060 `Radical Lighting Ltd.`=21068 `RUIZ TECH`=21069 `RNC Systems Inc.`=21070 `RootPath Ltd.`=21072 `RoscoLab Ltd`=21074 `Robe Show Lighting s.r.o.`=21075 `Stage Technologies Limited`=21313 `Industrias Sola Basic S.A. de C.V.`=21314 `Ocean Thin Films Inc.`=21315 `Stardraw.com Ltd.`=21316 `Selador`=21317 `Synthe FX, LLC`=21318 `SGM Technology For Lighting SPA`=21319 `Schreder`=21320 `Soundsculpture Incorporated`=21321 `SAS Productions`=21322 `SK-Software`=21323 `SOUNDLIGHT`=21324 `Sand Network Systems`=21326 `Sean Sill`=21331 `Stagetronics Ltda`=21332 `OOO SAMLIGHT`=21334 `SpaceCannon vH`=21347 `ShowCAD Control Systems Ltd.`=21352 `StageLine Electronic`=21356 `Spectrum Manufacturing Inc.`=21360 `STG-Beikirch Industrieelektronik + Sicherheitstechnik GmbH & Co. KG`=21364 `SV-wtu eU`=21366 `SWISSON AG`=21367 `Simon Tech`=21416 `AUTOLUX Handels- und ProduktionsgmbH`=21553 `TecArt Lighting`=21569 `Technographic Displays Ltd.`=21572 `TESI Elettronica srl`=21573 `Tempest Lighting Inc.`=21580 `TalentStorm Enterprises, Inc.`=21587 `TamaTech Labo Company Ltd,`=21588 `UP-LUX Eletronica Ltda.`=21840 `Martin Sukale Medientechnik GbR`=21845 `Vari-Lite, Inc.`=22092 `Vision Quest Lighting Inc.`=22097 `Viso Systems Aps`=22099 `W-DEV`=22340 `Wildfire, Inc.`=22342 `Wireless Solution Sweden AB`=22355 `Wybron, Inc.`=22361 `Xtraordinary Musical Accolade Systems`=22605 `XENON ARCHITECTURAL LIGHTING`=22629 `www.doityourselfchristmas.com hobbyists`=22637 `Plsao Optoelectronics Technology Co., Ltd.`=22664 `Zingerli Show Engineering`=23123 `OXO`=23616 `Mediatec Group`=23980 `Alektra AB`=24908 `Advatek Lighting`=24916 `Apollo Design Technology, Inc`=24932 `Advanced Lighting Systems`=24940 `CDS advanced technology bv`=25444 `Heliospectra AB`=25626 `Digilin Australia`=25697 `Dangeross Design`=25700 `dilitronics GmbH`=25708 `eldoLED BV`=25711 `eBrain GmbH`=25922 `euroGenie`=25927 `ELC lighting`=25964 `Environmental Lighting Solutions`=25971 `Electronic Theatre Controls, Inc.`=25972 `eventa Aktiengesellschaft`=25974 `Freescale Semiconductor U.K. Ltd.`=26227 `Lumisia Co., Ltd.`=26454 `GLP German Light Products GmbH`=26476 `Toshiba Lighting & Technology Corporation`=26608 `ChamberPlus Co., Ltd`=26646 `James Embedded Systems Engineering (JESE Ltd)`=26724 `Hubbell Entertainment, Inc.`=26725 `HERA LED`=26732 `iLight Technologies Inc`=26956 `Ittermann electronic GmbH`=26996 `JPK Systems Limited`=27243 `Key Delfin`=27492 `Ephesus Lighting`=27630 `Zumtobel Lighting GmbH`=27757 `Claude Heintz Design`=27768 `Ambra Elettronica s.r.l.`=27794 `MAL Effekt-Technik GmbH`=28001 `MBN GmbH`=28002 `Sein & Schein GmbH`=28003 `Lumina Visual Productions`=28650 `Pharos Architectural Controls`=28776 `Pr-Lighting Ltd.`=28786 `PixelRange Inc.`=28792 `Pangolin Laser Systems, Inc.`=28912 `The Light Source, Inc.`=29009 `Sean Christopher FX`=29539 `Ballantyne Strong Inc.`=29541 `Strand Lighting Ltd.`=29548 `WET`=30564 `DigitaLicht AG`=30600 `Mole-Richardson Co.`=30734 `XLN-t bvba`=30828 `LED Flex Limited`=30900 `DC Reactive`=31164 `Open Lighting`=31344 `Anaren Inc.`=31392 `Arthur Digital Solutions Kft`=32487 `RESERVED FOR PROTOTYPING/EXPERIMENTAL USE ONLY 0`=32752 `RESERVED FOR PROTOTYPING/EXPERIMENTAL USE ONLY 1`=32753 `RESERVED FOR PROTOTYPING/EXPERIMENTAL USE ONLY 2`=32754 `RESERVED FOR PROTOTYPING/EXPERIMENTAL USE ONLY 3`=32755 `RESERVED FOR PROTOTYPING/EXPERIMENTAL USE ONLY 4`=32756 `RESERVED FOR PROTOTYPING/EXPERIMENTAL USE ONLY 5`=32757 `RESERVED FOR PROTOTYPING/EXPERIMENTAL USE ONLY 6`=32758 `RESERVED FOR PROTOTYPING/EXPERIMENTAL USE ONLY 7`=32759 `RESERVED FOR PROTOTYPING/EXPERIMENTAL USE ONLY 8`=32760 `RESERVED FOR PROTOTYPING/EXPERIMENTAL USE ONLY 9`=32761 `RESERVED FOR PROTOTYPING/EXPERIMENTAL USE ONLY a`=32762 `RESERVED FOR PROTOTYPING/EXPERIMENTAL USE ONLY b`=32763 `RESERVED FOR PROTOTYPING/EXPERIMENTAL USE ONLY c`=32764 `RESERVED FOR PROTOTYPING/EXPERIMENTAL USE ONLY d`=32765 `RESERVED FOR PROTOTYPING/EXPERIMENTAL USE ONLY e`=32766 `RESERVED FOR PROTOTYPING/EXPERIMENTAL USE ONLY f`=32767 `ESTA1`=65535

`Enums.RDMManufacturerId.ESTA`

## RDMNotificationThresholdOperator

``=0 `Is`=1 `IsNot`=2 `Greate`=3 `Less`=4

`Enums.RDMNotificationThresholdOperator.Is`

## RDMPID

`None`=0 `DISC_UNIQUE_BRANCH`=1 `DISC_MUTE`=2 `DISC_UN_MUTE`=3 `PROXIED_DEVICES`=16 `PROXIED_DEVICE_COUNT`=17 `COMMS_STATUS`=21 `QUEUED_MESSAGE`=32 `STATUS_MESSAGES`=48 `STATUS_ID_DESCRIPTION`=49 `CLEAR_STATUS_ID`=50 `SUB_DEVICE_STATUS_REPORT_THRESHOLD`=51 `SUPPORTED_PARAMETERS`=80 `PARAMETER_DESCRIPTION`=81 `DEVICE_INFO`=96 `PRODUCT_DETAIL_ID_LIST`=112 `DEVICE_MODEL_DESCRIPTION`=128 `MANUFACTURER_LABEL`=129 `DEVICE_LABEL`=130 `FACTORY_DEFAULTS`=144 `LANGUAGE_CAPABILITIES`=160 `LANGUAGE`=176 `SOFTWARE_VERSION_LABEL`=192 `BOOT_SOFTWARE_VERSION_ID`=193 `BOOT_SOFTWARE_VERSION_LABEL`=194 `DMX_PERSONALITY`=224 `DMX_PERSONALITY_DESCRIPTION`=225 `DMX_START_ADDRESS`=240 `SLOT_INFO`=288 `SLOT_DESCRIPTION`=289 `DEFAULT_SLOT_VALUE`=290 `SENSOR_DEFINITION`=512 `SENSOR_VALUE`=513 `RECORD_SENSORS`=514 `DEVICE_HOURS`=1024 `LAMP_HOURS`=1025 `LAMP_STRIKES`=1026 `LAMP_STATE`=1027 `LAMP_ON_MODE`=1028 `DEVICE_POWER_CYCLES`=1029 `DISPLAY_INVERT`=1280 `DISPLAY_LEVEL`=1281 `PAN_INVERT`=1536 `TILT_INVERT`=1537 `PAN_TILT_SWAP`=1538 `REAL_TIME_CLOCK`=1539 `IDENTIFY_DEVICE`=4096 `RESET_DEVICE`=4097 `POWER_STATE`=4112 `PERFORM_SELFTEST`=4128 `SELF_TEST_DESCRIPTION`=4129 `CAPTURE_PRESET`=4144 `PRESET_PLAYBACK`=4145

`Enums.RDMPID.None`

## RDMParameterCommand

`None`=0 `CC_GET`=1 `CC_SET`=2 `CC_GET_SET`=3

`Enums.RDMParameterCommand.None`

## RDMParameterType

`Rdm`=0 `FixtureType`=1 `Fixture`=2

`Enums.RDMParameterType.Rdm`

## RDMPidValueDisplayInvert

`Off`=0 `On`=1 `Auto`=2

`Enums.RDMPidValueDisplayInvert.Off`

## RDMPidValueFactoryDefaults

`False`=0 `True`=1

`Enums.RDMPidValueFactoryDefaults.False`

## RDMPidValueOnOff

`Off`=0 `On`=1

`Enums.RDMPidValueOnOff.Off`

## RDMPidValueResetDevice

``=0 `Warm`=1 `Cold`=255

`Enums.RDMPidValueResetDevice.Warm`

## RDMPowerStateDefines

`POWER_STATE_FULL_OFF`=0 `POWER_STATE_SHUTDOWN`=1 `POWER_STATE_STANDBY`=2 `POWER_STATE_NORMAL`=255

`Enums.RDMPowerStateDefines.POWER_STATE_FULL_OFF`

## RDMProductCategory

`PRODUCT_CATEGORY_NOT_DECLARED`=0 `PRODUCT_CATEGORY_FIXTURE`=256 `PRODUCT_CATEGORY_FIXTURE_FIXED`=257 `PRODUCT_CATEGORY_FIXTURE_MOVING_YOKE`=258 `PRODUCT_CATEGORY_FIXTURE_MOVING_MIRROR`=259 `PRODUCT_CATEGORY_FIXTURE_OTHER`=511 `PRODUCT_CATEGORY_FIXTURE_ACCESSORY`=512 `PRODUCT_CATEGORY_FIXTURE_ACCESSORY_COLOR`=513 `PRODUCT_CATEGORY_FIXTURE_ACCESSORY_YOKE`=514 `PRODUCT_CATEGORY_FIXTURE_ACCESSORY_MIRROR`=515 `PRODUCT_CATEGORY_FIXTURE_ACCESSORY_EFFECT`=516 `PRODUCT_CATEGORY_FIXTURE_ACCESSORY_BEAM`=517 `PRODUCT_CATEGORY_FIXTURE_ACCESSORY_OTHER`=767 `PRODUCT_CATEGORY_PROJECTOR`=768 `PRODUCT_CATEGORY_PROJECTOR_FIXED`=769 `PRODUCT_CATEGORY_PROJECTOR_MOVING_YOKE`=770 `PRODUCT_CATEGORY_PROJECTOR_MOVING_MIRROR`=771 `PRODUCT_CATEGORY_PROJECTOR_OTHER`=1023 `PRODUCT_CATEGORY_ATMOSPHERIC`=1024 `PRODUCT_CATEGORY_ATMOSPHERIC_EFFECT`=1025 `PRODUCT_CATEGORY_ATMOSPHERIC_PYRO`=1026 `PRODUCT_CATEGORY_ATMOSPHERIC_OTHER`=1279 `PRODUCT_CATEGORY_DIMMER`=1280 `PRODUCT_CATEGORY_DIMMER_AC_INCANDESCENT`=1281 `PRODUCT_CATEGORY_DIMMER_AC_FLUORESCENT`=1282 `PRODUCT_CATEGORY_DIMMER_AC_COLDCATHODE`=1283 `PRODUCT_CATEGORY_DIMMER_AC_NONDIM`=1284 `PRODUCT_CATEGORY_DIMMER_AC_ELV`=1285 `PRODUCT_CATEGORY_DIMMER_AC_OTHER`=1286 `PRODUCT_CATEGORY_DIMMER_DC_LEVEL`=1287 `PRODUCT_CATEGORY_DIMMER_DC_PWM`=1288 `PRODUCT_CATEGORY_DIMMER_CS_LED`=1289 `PRODUCT_CATEGORY_DIMMER_OTHER`=1535 `PRODUCT_CATEGORY_POWER`=1536 `PRODUCT_CATEGORY_POWER_CONTROL`=1537 `PRODUCT_CATEGORY_POWER_SOURCE`=1538 `PRODUCT_CATEGORY_POWER_OTHER`=1791 `PRODUCT_CATEGORY_SCENIC`=1792 `PRODUCT_CATEGORY_SCENIC_DRIVE`=1793 `PRODUCT_CATEGORY_SCENIC_OTHER`=2047 `PRODUCT_CATEGORY_DATA`=2048 `PRODUCT_CATEGORY_DATA_DISTRIBUTION`=2049 `PRODUCT_CATEGORY_DATA_CONVERSION`=2050 `PRODUCT_CATEGORY_DATA_OTHER`=2303 `PRODUCT_CATEGORY_AV`=2304 `PRODUCT_CATEGORY_AV_AUDIO`=2305 `PRODUCT_CATEGORY_AV_VIDEO`=2306 `PRODUCT_CATEGORY_AV_OTHER`=2559 `PRODUCT_CATEGORY_MONITOR`=2560 `PRODUCT_CATEGORY_MONITOR_ACLINEPOWER`=2561 `PRODUCT_CATEGORY_MONITOR_DCPOWER`=2562 `PRODUCT_CATEGORY_MONITOR_ENVIRONMENTAL`=2563 `PRODUCT_CATEGORY_MONITOR_OTHER`=2815 `PRODUCT_CATEGORY_CONTROL`=28672 `PRODUCT_CATEGORY_CONTROL_CONTROLLER`=28673 `PRODUCT_CATEGORY_CONTROL_BACKUPDEVICE`=28674 `PRODUCT_CATEGORY_CONTROL_OTHER`=28927 `PRODUCT_CATEGORY_TEST`=28928 `PRODUCT_CATEGORY_TEST_EQUIPMENT`=28929 `PRODUCT_CATEGORY_TEST_EQUIPMENT_OTHER`=29183 `PRODUCT_CATEGORY_OTHER`=32767 `PRODUCT_CATEGORY__MANUFACTORER_SPECIFIC`=32768

`Enums.RDMProductCategory.PRODUCT_CATEGORY_NOT_DECLARED`

## RDMProductDetail

`PRODUCT_DETAIL_NOT DECLARED`=0 `PRODUCT_DETAIL_ARC`=1 `PRODUCT_DETAIL_METAL_HALIDE`=2 `PRODUCT_DETAIL_INCANDESCENT`=3 `PRODUCT_DETAIL_LED`=4 `PRODUCT_DETAIL_FLUROESCENT`=5 `PRODUCT_DETAIL_COLDCATHODE`=6 `PRODUCT_DETAIL_ELECTROLUMINESCENT`=7 `PRODUCT_DETAIL_LASER`=8 `PRODUCT_DETAIL_FLASHTUBE`=9 `PRODUCT_DETAIL_COLORSCROLLER`=256 `PRODUCT_DETAIL_COLORWHEEL`=257 `PRODUCT_DETAIL_COLORCHANGE`=258 `PRODUCT_DETAIL_IRIS_DOUSER`=259 `PRODUCT_DETAIL_DIMMING_SHUTTER`=260 `PRODUCT_DETAIL_PROFILE_SHUTTER`=261 `PRODUCT_DETAIL_BARNDOOR_SHUTTER`=262 `PRODUCT_DETAIL_EFFECTS_DISC`=263 `PRODUCT_DETAIL_GOBO_ROTATOR`=264 `PRODUCT_DETAIL_VIDEO`=512 `PRODUCT_DETAIL_SLIDE`=513 `PRODUCT_DETAIL_FILM`=514 `PRODUCT_DETAIL_OILWHEEL`=515 `PRODUCT_DETAIL_LCDGATE`=516 `PRODUCT_DETAIL_FOGGER_GLYCOL`=768 `PRODUCT_DETAIL_FOGGER_MINERALOIL`=769 `PRODUCT_DETAIL_FOGGER_WATER`=770 `PRODUCT_DETAIL_C02`=771 `PRODUCT_DETAIL_LN2`=772 `PRODUCT_DETAIL_BUBBLE`=773 `PRODUCT_DETAIL_FLAME_PROPANE`=774 `PRODUCT_DETAIL_FLAME_OTHER`=775 `PRODUCT_DETAIL_OLEFACTORY_STIMULATOR`=776 `PRODUCT_DETAIL_SNOW`=777 `PRODUCT_DETAIL_WATER_JET`=778 `PRODUCT_DETAIL_WIND`=779 `PRODUCT_DETAIL_CONFETTI`=780 `PRODUCT_DETAIL_HAZARD`=781 `PRODUCT_DETAIL_PHASE_CONTROL`=1024 `PRODUCT_DETAIL_REVERSE_PHASE_CONTROL`=1025 `PRODUCT_DETAIL_SINE`=1026 `PRODUCT_DETAIL_PWM`=1027 `PRODUCT_DETAIL_DC`=1028 `PRODUCT_DETAIL_HFBALLAST`=1029 `PRODUCT_DETAIL_HFHV_NEONBALLAST`=1030 `PRODUCT_DETAIL_HFHV_EL`=1031 `PRODUCT_DETAIL_MHR_BALLAST`=1032 `PRODUCT_DETAIL_BITANGLE_MODULATION`=1033 `PRODUCT_DETAIL_FREQUENCY_MODULATION`=1034 `PRODUCT_DETAIL_HIGHFREQUENCY_12V`=1035 `PRODUCT_DETAIL_RELAY_MECHANICAL`=1036 `PRODUCT_DETAIL_RELAY_ELECTRONIC`=1037 `PRODUCT_DETAIL_SWITCH_ELECTRONIC`=1038 `PRODUCT_DETAIL_CONTACTOR`=1039 `PRODUCT_DETAIL_MIRRORBALL_ROTATOR`=1280 `PRODUCT_DETAIL_OTHER_ROTATOR`=1281 `PRODUCT_DETAIL_KABUKI_DROP`=1282 `PRODUCT_DETAIL_CURTAIN`=1283 `PRODUCT_DETAIL_LINESET`=1284 `PRODUCT_DETAIL_MOTOR_CONTROL`=1285 `PRODUCT_DETAIL_DAMPER_CONTROL`=1286 `PRODUCT_DETAIL_SPLITTER`=1536 `PRODUCT_DETAIL_ETHERNET_NODE`=1537 `PRODUCT_DETAIL_MERGE`=1538 `PRODUCT_DETAIL_DATAPATCH`=1539 `PRODUCT_DETAIL_WIRELESS_LINK`=1540 `PRODUCT_DETAIL_PROTOCOL_CONVERTOR`=1793 `PRODUCT_DETAIL_ANALOG_DEMULTIPLEX`=1794 `PRODUCT_DETAIL_ANALOG_MULTIPLEX`=1795 `PRODUCT_DETAIL_SWITCH_PANEL`=1796 `PRODUCT_DETAIL_ROUTER`=2048 `PRODUCT_DETAIL_FADER`=2049 `PRODUCT_DETAIL_MIXER`=2050 `PRODUCT_DETAIL_CHANGEOVER_MANUAL`=2304 `PRODUCT_DETAIL_CHANGEOVER_AUTO`=2305 `PRODUCT_DETAIL_TEST`=2306 `PRODUCT_DETAIL_GFI_RCD`=2560 `PRODUCT_DETAIL_BATTERY`=2561 `PRODUCT_DETAIL_CONTROLLABLE_BREAKER`=2562 `PRODUCT_DETAIL_OTHER`=32767 `Manufacturer Specific`=32768

`Enums.RDMProductDetail.PRODUCT_DETAIL_ARC`

## RDMResponseNackReason

`The responder cannot comply with request because the message is not implemented in responder.`=0 `The responder cannot interpret request as controller data was not formatted correctly.`=1 `The responder cannot comply due to an internal hardware fault.`=2 `Proxy is not the RDM line master and cannot comply with message.`=3 `SET Command normally allowed but being blocked currently.`=4 `Not valid for Command Class attempted. May be used where GET allowed but SET is not supported.`=5 `Value for given Parameter out of allowable range or not supported.`=6 `Buffer or Queue space currently has no free space to store data.`=7 `Incoming message exceeds buffer capacity.`=8 `Sub-Device is out of range or unknown.`=9 `The proxy buffer is full and can not store any more Queued Message or Status Message responses.`=10

`Enums.RDMResponseNackReason["The responder cannot comply with request because the message is not implemented in responder."]`

## RDMSensorType

`SENS_TEMPERATURE`=0 `SENS_VOLTAGE`=1 `SENS_CURRENT`=2 `SENS_FREQUENCY`=3 `SENS_RESISTANCE`=4 `SENS_POWER`=5 `SENS_MASS`=6 `SENS_LENGTH`=7 `SENS_AREA`=8 `SENS_VOLUME`=9 `SENS_DENSITY`=10 `SENS_VELOCITY`=11 `SENS_ACCELERATION`=12 `SENS_FORCE`=13 `SENS_ENERGY`=14 `SENS_PRESSURE`=15 `SENS_TIME`=16 `SENS_ANGLE`=17 `SENS_POSITION_X`=18 `SENS_POSITION_Y`=19 `SENS_POSITION_Z`=20 `SENS_ANGULAR_VELOCITY`=21 `SENS_LUMINOUS_INTENSITY`=22 `SENS_LUMINOUS_FLUX`=23 `SENS_ILLUMINANCE`=24 `SENS_CHROMINANCE_RED`=25 `SENS_CHROMINANCE_GREEN`=26 `SENS_CHROMINANCE_BLUE`=27 `SENS_CONTACTS`=28 `SENS_MEMORY`=29 `SENS_ITEMS`=30 `SENS_HUMIDITY`=31 `SENS_COUNTER_16BIT`=32 `SENS_OTHER`=127 `SENS_MS`=128

`Enums.RDMSensorType.SENS_TEMPERATURE`

## RDMSensorUnit

`UNITS_NONE`=0 `UNITS_CENTIGRADE`=1 `UNITS_VOLTS_DC`=2 `UNITS_VOLTS_AC_PEAK`=3 `UNITS_VOLTS_AC_RMS`=4 `UNITS_AMPERE_DC`=5 `UNITS_AMPERE_AC_PEAK`=6 `UNITS_AMPERE_AC_RMS`=7 `UNITS_HERTZ`=8 `UNITS_OHM`=9 `UNITS_WATT`=10 `UNITS_KILOGRAM`=11 `UNITS_METERS`=12 `UNITS_METERS_SQUARED`=13 `UNITS_METERS_CUBED`=14 `UNITS_KILOGRAMMES_PER_METER_CUBED`=15 `UNITS_METERS_PER_SECOND`=16 `UNITS_METERS_PER_SECOND_SQUARED`=17 `UNITS_NEWTON`=18 `UNITS_JOULE`=19 `UNITS_PASCAL`=20 `UNITS_SECOND`=21 `UNITS_DEGREE`=22 `UNITS_STERADIAN`=23 `UNITS_CANDELA`=24 `UNITS_LUMEN`=25 `UNITS_LUX`=26 `UNITS_IRE`=27 `UNITS_BYTE`=28 `UNITS_MS`=128

`Enums.RDMSensorUnit.UNITS_NONE`

## RDMSensorUnitPrefix

`PREFIX_NONE`=0 `PREFIX_DECI`=1 `PREFIX_CENTI`=2 `PREFIX_MILLI`=3 `PREFIX_MICRO`=4 `PREFIX_NANO`=5 `PREFIX_PICO`=6 `PREFIX_FEMPTO`=7 `PREFIX_ATTO`=8 `PREFIX_ZEPTO`=9 `PREFIX_YOCTO`=10 `PREFIX_DECA`=17 `PREFIX_HECTO`=18 `PREFIX_KILO`=19 `PREFIX_MEGA`=20 `PREFIX_GIGA`=21 `PREFIX_TERRA`=22 `PREFIX_PETA`=23 `PREFIX_EXA`=24 `PREFIX_ZETTA`=25 `PREFIX_YOTTA`=26

`Enums.RDMSensorUnitPrefix.PREFIX_NONE`

## RDMSlotId

`SD_INTENSITY`=1 `SD_INTENSITY_MASTER`=2 `SD_PAN`=257 `SD_TILT`=258 `SD_COLOR_WHEEL`=513 `SD_COLOR_SUB_CYAN`=514 `SD_COLOR_SUB_YELLOW`=515 `SD_COLOR_SUB_MAGENTA`=516 `SD_COLOR_ADD_RED`=517 `SD_COLOR_ADD_GREEN`=518 `SD_COLOR_ADD_BLUE`=519 `SD_COLOR_CORRECTION`=520 `SD_COLOR_SCROLL`=521 `SD_COLOR_SEMAPHORE`=528 `SD_COLOR_ADD_AMBER`=529 `SD_COLOR_ADD_WHITE`=530 `SD_COLOR_ADD_WARM_WHITE`=531 `SD_COLOR_ADD_COOL_WHITE`=532 `SD_COLOR_SUB_UV`=533 `SD_COLOR_HUE`=534 `SD_COLOR_SATURATION`=535 `SD_STATIC_GOBO_WHEEL`=769 `SD_ROTO_GOBO_WHEEL`=770 `SD_PRISM_WHEEL`=771 `SD_EFFECTS_WHEEL`=772 `SD_BEAM_SIZE_IRIS`=1025 `SD_EDGE`=1026 `SD_FROST`=1027 `SD_STROBE`=1028 `SD_ZOOM`=1029 `SD_FRAMING_SHUTTER`=1030 `SD_SHUTTER_ROTATE`=1031 `SD_DOUSER`=1032 `SD_BARN_DOOR`=1033 `SD_LAMP_CONTROL`=1281 `SD_FIXTURE_CONTROL`=1282 `SD_FIXTURE_SPEED`=1283 `SD_MACRO`=1284 `SD_POWER_CONTROL`=1285 `SD_FAN_CONTROL`=1286 `SD_HEATER_CONTROL`=1287 `SD_FOUNTAIN_CONTROL`=1288 `SD_UNDEFINED`=65535

`Enums.RDMSlotId.SD_INTENSITY`

## RDMSlotType

`ST_PRIMARY`=0 `ST_SEC_FINE`=1 `ST_SEC_TIMING`=2 `ST_SEC_SPEED`=3 `ST_SEC_CONTROL`=4 `ST_SEC_INDEX`=5 `ST_SEC_ROTATION`=6 `ST_SEC_INDEX_ROTATE`=7 `ST_SEC_UNDEFINED`=255

`Enums.RDMSlotType.ST_PRIMARY`

## RDMStatusMessageType

`STATUS_NONE`=0 `STATUS_GET_LAST_MESSAGE`=1 `STATUS_ADVISORY`=2 `STATUS_WARNING`=3 `STATUS_ERROR`=4 `STATUS_ADVISORY_CLEARED`=18 `STATUS_WARNING_CLEARED`=19 `STATUS_ERROR_CLEARED`=20

`Enums.RDMStatusMessageType.STATUS_NONE`

## RealtimeCmdSource

`Original`=0 `Local`=1 `Network`=2

`Enums.RealtimeCmdSource.Original`

## RealtimeCmdType

`Key`=0 `Fader`=1 `Encoder`=2 `OwO`=3 `TimeCode`=4 `SoundToLight`=5 `GeneratorControl`=6 `DCRemote`=7 `Midi`=8 `PSN`=9

`Enums.RealtimeCmdType.Key`

## RealtimeSection

`Start`=0 `DMXDecompress`=1 `DMXMix`=2 `Jobque`=3 `SendRTStream`=4 `Lua`=5 `GroupMaster`=6 `Timecode`=7 `Playback`=8 `Highlight`=9 `CalcChannel`=10 `Wait1`=11 `DMXCompress`=12 `DMXTransfer`=13 `PostRealtime`=14 `Wait2`=15 `ChannelCompress`=16 `LED`=17

`Enums.RealtimeSection.Start`

## RecipeCleanupOperation

`NoOutput`=0 `NotCooked`=1 `CookedButOverwritten`=2

`Enums.RecipeCleanupOperation.NoOutput`

## RecipeContext

`None`=0 `Groups`=4 `Shapes`=5 `Presets`=6 `Worlds`=7 `Filters`=8 `Attributes`=10

`Enums.RecipeContext.None`

## RecipeContextMenu

`GridContextNone`=0 `GridContextBoolean`=2 `ShapeEditContent`=5 `GridContextNumericKeypadValues`=6 `GridContextMatricks`=9 `GridContextPhaserRecipe`=11 `GridContextStandardRecipe`=12 `GridContextNumericKeypadPart`=13 `GridContextNumericKeypadMeasure`=14 `GridContextNumericKeypadNshot`=15 `GridContextNumericKeypadSpeed`=16 `GridContextNumericKeypadPhase`=17 `GridContextCurve`=18 `GridContextNShotDirection`=19 `GridContextRotation`=20 `GridContextSpeedMaster`=21

`Enums.RecipeContextMenu.GridContextNone`

## RecipeContextPool

`GridContextPoolSelection`=4 `GridContextPoolShapes`=5 `GridContextPoolValues`=6 `GridContextPoolFilter`=8 `GridContextPoolMatricks`=9

`Enums.RecipeContextPool.GridContextPoolSelection`

## RecipeContextSheet

`GridContextSheetSelection`=4 `GridContextSheetValues`=6 `GridContextSheetFilter`=8 `GridContextSheetAttributes`=10

`Enums.RecipeContextSheet.GridContextSheetSelection`

## RecipePresetReadoutMode

`Name`=0 `ID`=3 `ID+Name`=4 `ID+Long Name`=6

`Enums.RecipePresetReadoutMode.Name`

## RecipeStoreMode

`Normal`=0 `NoSelection`=1

`Enums.RecipeStoreMode.Normal`

## RecordGo

`as Go`=0 `as Goto (Status)`=1

`Enums.RecordGo["as Go"]`

## ReductionPolicy

`None`=0 `PreferFirst`=1 `PreferLast`=2 `Equal`=3 `EqualFirst`=4 `EqualLast`=5

`Enums.ReductionPolicy.None`

## RelationType

`Multiply`=0 `Override`=1

`Enums.RelationType.Multiply`

## ReleaseType

`Alpha`=0 `Beta`=1 `Release`=2

`Enums.ReleaseType.Alpha`

## RemoteMidiType

`Note`=0 `NoteAttack`=1 `NoteAttackDecay`=2 `Control`=3

`Enums.RemoteMidiType.Note`

## RemoteResolution

`8bit`=1 `16bit`=2 `24bit`=3

`Enums.RemoteResolution["8bit"]`

## Render_Style

`Pool`=1 `Executor`=2

`Enums.Render_Style.Pool`

## RequestedSize

`Default`=0

`Enums.RequestedSize.Default`

## ResolutionLimit1440p

`480p`=0 `720p`=1 `1080p`=2 `1440p`=3

`Enums.ResolutionLimit1440p["480p"]`

## ResolutionLimit4k

`480p`=0 `720p`=1 `1080p`=2 `1440p`=3 `4k`=4

`Enums.ResolutionLimit4k["480p"]`

## ResolutionLimitUnlimited

`480p`=0 `720p`=1 `1080p`=2 `1440p`=3 `4k`=4 `Unlimited`=5

`Enums.ResolutionLimitUnlimited.Unlimited`

## RestartOption

`Continue`=0 `Reset`=1

`Enums.RestartOption.Continue`

## Roles

`Default`=0 `Display`=1 `DisplayShort`=2 `Edit`=4 `ObjectNoOnly`=8

`Enums.Roles.Default`

## RotateOption

`Left`=0 `Right`=1

`Enums.RotateOption.Left`

## RotationMode

`Single`=0 `Group`=1

`Enums.RotationMode.Single`

## RowFilter

`All`=0 `Used`=1 `Unused`=2 `Selection`=3

`Enums.RowFilter.All`

## RowOrder

`Up Down`=0 `Down Up`=1

`Enums.RowOrder["Up Down"]`

## SCVirtualKeyCode

``=0 `UNKNOWN`=0 `MA1`=1 `MA2`=2 `PREV`=3 `NEXT`=4 `SET`=5 `UP`=6 `SELFIX`=7 `DOWN`=8 `MENU`=9 `HIGHLIGHT`=10 `SOLO`=11 `FREEZE`=12 `PREVIEW`=13 `BLIND`=14 `XKEYS`=15 `PAGE_UP`=16 `PAGE_DOWN`=17 `LIST`=18 `X1`=19 `X2`=20 `X3`=21 `X4`=22 `X5`=23 `X6`=24 `X7`=25 `X8`=26 `X9`=27 `X10`=28 `X11`=29 `X12`=30 `X13`=31 `X14`=32 `X15`=33 `X16`=34 `EXEC`=35 `FADER`=36 `DEF_GO`=37 `DEF_PAUSE`=38 `DEF_GOBACK`=39 `PAUSE`=40 `GOBACK`=41 `GO`=42 `LEARN`=43 `GOBACKFAST`=44 `GOFAST`=45 `ON`=46 `OFF`=47 `MOVE`=48 `COPY`=49 `DELETE`=50 `ALIGN`=51 `STOMP`=52 `HELP`=53 `SELECT`=54 `GOTO`=55 `FIXTURE`=56 `CHANNEL`=57 `GROUP`=58 `SEQUENCE`=59 `CUE`=60 `PRESET`=61 `EDIT`=62 `ASSIGN`=63 `TIME`=64 `UPDATE`=65 `STORE`=66 `NUM0`=67 `NUM1`=68 `NUM2`=69 `NUM3`=70 `NUM4`=71 `NUM5`=72 `NUM6`=73 `NUM7`=74 `NUM8`=75 `NUM9`=76 `PLUS`=77 `THRU`=78 `MINUS`=79 `DOT`=80 `IF`=81 `AT`=82 `SLASH`=83 `PLEASE`=84 `FULL`=85 `UNDO`=86 `OOPS`=86 `CLEAR`=87 `ESC`=88 `ENCODER_INSIDE1`=89 `ENCODER_OUTSIDE1`=90 `ENCODER_INSIDE2`=91 `ENCODER_OUTSIDE2`=92 `ENCODER_INSIDE3`=93 `ENCODER_OUTSIDE3`=94 `ENCODER_INSIDE4`=95 `ENCODER_OUTSIDE4`=96 `ENCODER_INSIDE5`=97 `ENCODER_OUTSIDE5`=98 `USER1`=99 `USER2`=100 `FLASH`=101 `BLACK`=102 `KILL`=103 `RATE1`=104 `TEMP`=105 `TOGGLE`=106 `TOP`=107 `LOAD`=108 `LOWLIGHT`=109 `GOSTEP`=110 `SWAP`=111 `HALF_SPEED`=112 `DOUBLE_SPEED`=113 `RECORD`=114 `PREV_X`=115 `PREV_Y`=116 `PREV_Z`=117 `PREV_STEP`=118 `NEXT_X`=119 `NEXT_Y`=120 `NEXT_Z`=121 `NEXT_STEP`=122 `STEP`=123 `TOGGLE_STEP`=124 `TOGGLE_MATRICKS`=125 `RESET_MATRICKS`=126 `ONPC_SCREEN2`=127 `ONPC_SCREEN3`=128 `ONPC_SCREEN4`=129 `ONPC_SCREEN5`=130 `ONPC_SCREEN6`=131 `ONPC_SCREEN7`=132 `ASTERISK`=133 `FIX`=134 `CLONE`=135 `GRID`=136 `LAYOUT`=137 `TIMECODE`=138 `VIEW`=139 `DMX`=140 `PHASER`=141 `MACRO`=142 `PAGE`=143 `EXECUTOR`=144 `FLIP`=145 `LOCATE`=146

`Enums.SCVirtualKeyCode.UNKNOWN`

## SMPTEMode

`In`=0 `Out`=1

`Enums.SMPTEMode.In`

## SacnDataMode

`Output Multicast`=0 `Output Unicast`=1 `Input Multicast`=2 `Input Unicast`=3

`Enums.SacnDataMode["Output Multicast"]`

## ScrollItemPlacementType

`Auto`=0 `Begin`=1 `End`=2

`Enums.ScrollItemPlacementType.Auto`

## ScrollParamEntity

`Item`=0 `Area`=1

`Enums.ScrollParamEntity.Item`

## ScrollParamValueType

`Relative`=0 `Absolute`=1

`Enums.ScrollParamValueType.Relative`

## ScrollReason

`Automatic`=0 `User`=1

`Enums.ScrollReason.Automatic`

## ScrollType

`Vertical`=0 `Horizontal`=1

`Enums.ScrollType.Vertical`

## SectionCount

`Auto`=0 `1`=1 `2`=2 `3`=3

`Enums.SectionCount.Auto`

## SelectedEnvironment

`Normal`=0 `Preview`=1

`Enums.SelectedEnvironment.Normal`

## SelectedFeatureMode

`Feature`=0 `FeatureGroup`=1

`Enums.SelectedFeatureMode.Feature`

## SelectedSelection

`1`=0 `2`=1

`Enums.SelectedSelection["1"]`

## SelectionAlignment

`None`=0 `Left`=1 `Center`=2 `Right`=3

`Enums.SelectionAlignment.None`

## SelectionMode

`2D Grid`=0 `Linearize`=1

`Enums.SelectionMode.Linearize`

## SelectionModeLayout

`2D Grid`=0 `Linearize`=1

`Enums.SelectionModeLayout.Linearize`

## SelectionViewFontSize

`Automatic`=0 `Default`=1 `10`=2 `12`=3 `14`=4 `16`=5 `18`=6 `24`=7 `28`=8 `32`=9

`Enums.SelectionViewFontSize.Automatic`

## SeqMasterGoMode

`None`=0 `Go`=1 `On`=2 `Top`=3

`Enums.SeqMasterGoMode.None`

## SeqRestartMode

`First Cue`=0 `Current Cue`=1 `Next Cue`=2

`Enums.SeqRestartMode["First Cue"]`

## SequenceAction

`Select`=1 `Toggle`=2 `Go+`=3 `Flash`=4 `Temp`=5 `Top`=12 `Goto`=13 `Load`=14 `None`=255

`Enums.SequenceAction.Select`

## SequenceActionToken

`None`=0 `Flash`=1 `Go+`=3 `Temp`=13 `Toggle`=14 `Top`=15 `Goto`=16 `Load`=17 `Select`=24 `Pool Default`=417

`Enums.SequenceActionToken.None`

## SequenceCountdown

`Off`=0 `Duration`=1 `All`=2

`Enums.SequenceCountdown.Off`

## SequenceLinkType

`Fixed`=0 `Selected`=1 `LastGo`=2

`Enums.SequenceLinkType.Fixed`

## SessionTimeStyle

`Digital`=0 `Date DD-MM-YYYY`=1 `Date MM-DD-YYYY`=2 `Digital AM/PM`=3 `Dawn`=4 `Sunrise`=5 `Sunset`=6 `Dusk`=7

`Enums.SessionTimeStyle.Digital`

## SessionTimeStyleTZ

`Digital`=0 `Digital AM/PM`=3

`Enums.SessionTimeStyleTZ.Digital`

## SetupType

`Undefined`=0 `Live`=1 `Edit`=2

`Enums.SetupType.Undefined`

## ShadowMapQuality

`None`=0 `Low`=1 `Medium`=2 `High`=3 `Very High`=4

`Enums.ShadowMapQuality.None`

## ShadowMode

`Disabled`=0 `Enabled`=1

`Enums.ShadowMode.Disabled`

## ShapePhaserRecipeDirection

`Forward`=0 `Backward`=1 `Alternate`=2 `Take from Shape`=2147483647

`Enums.ShapePhaserRecipeDirection.Forward`

## ShapeYesNo

`No`=0 `Yes`=1 `Take from Shape`=2147483647

`Enums.ShapeYesNo.No`

## ShaperBarMode

`Blades`=0 `Frame`=1

`Enums.ShaperBarMode.Blades`

## ShaperControlMode

`Ins+Rot`=0 `A+B`=1

`Enums.ShaperControlMode["Ins+Rot"]`

## ShaperEncoderLinkMode

`None`=0 `All`=1 `Parallel`=2 `Mirrored`=3

`Enums.ShaperEncoderLinkMode.None`

## ShaperViewMode

`Graphical`=0 `Faders`=1

`Enums.ShaperViewMode.Graphical`

## SheetMode

`Fixture`=0 `Channel`=1 `Dimmer+`=2 `Sheet/Filter`=3

`Enums.SheetMode.Fixture`

## SheetSettingsMergeMode

`None`=0 `Feature`=1 `Feature Group`=2

`Enums.SheetSettingsMergeMode.None`

## ShowCreatorObjectType

`Appearances`=0 `Cameras`=1 `Encoder Bars`=2 `Gels`=3 `Render Qualities`=4 `Scribbles`=5 `Users`=6 `UserProfiles`=7 `Views`=8 `Gobos`=9 `Images`=10 `Meshes`=11 `Sounds`=12 `Symbols`=13 `Videos`=14 `Data Pools`=15 `Bitmaps`=16 `Executor Configurations`=17 `Filters`=18 `Generators`=19 `Groups`=20 `Layouts`=21 `Macros`=22 `MAtricks`=23 `Pages`=24 `Plugins`=25 `Presets`=26 `Quickeys`=27 `Sequences`=28 `Shapes`=29 `Timecodes`=30 `Timers`=31 `Worlds`=32

`Enums.ShowCreatorObjectType.Appearances`

## ShowCreatorType

`AutoStore`=0 `AutoCreate`=1 `Groups`=2 `Generate`=3 `Import`=4 `Export`=5

`Enums.ShowCreatorType.AutoStore`

## ShowFileSegmentsMask

`Nothing`=0 `NoShowData`=1 `LocalSettings`=2 `OutputStations`=4 `DmxProtocols`=8 `All`=15

`Enums.ShowFileSegmentsMask.Nothing`

## ShowFileStatus

`Undefined`=0 `NoShow`=1 `ShowLoaded`=2 `ShowDownloaded`=3 `DataNegotiationActive`=4 `ShowSaving`=5 `DataNegotiationWaitingForNewMaster`=6 `DataNegotiationMaster`=7 `DataNegotiationSlave`=8 `ShowUploading`=9 `ShowMediaUploading`=10 `ShowDownloading`=11 `ShowMediaDownloading`=12 `ShowDownloadIgnore`=13 `ShowPSRConversion`=14

`Enums.ShowFileStatus.Undefined`

## ShowPathType

`Show`=19 `Backup`=20 `Demo`=21 `Template`=65

`Enums.ShowPathType.Show`

## ShowUserEncoder

`Default`=0 `Exec`=1 `Xkeys`=2

`Enums.ShowUserEncoder.Default`

## ShowfileSelectorMode

`Premenu`=0 `Load`=1 `Saveas`=2 `Delete`=3 `Newshow`=4 `Startupshow`=5 `Psr`=6

`Enums.ShowfileSelectorMode.Premenu`

## ShuffleMode

`Auto`=0 `Linked`=1 `Unlinked`=2

`Enums.ShuffleMode.Auto`

## SignalOff

`Off`=4294967295

`Enums.SignalOff.Off`

## SignalSlot

`Slot 1`=0 `Slot 2`=1 `Slot 3`=2 `Slot 4`=3 `Slot 5`=4 `Slot 6`=5 `Slot 7`=6 `Slot 8`=7 `Slot 9`=8 `Slot 10`=9 `Slot 11`=10 `Slot 12`=11 `Slot 13`=12 `Slot 14`=13 `Slot 15`=14 `Slot 16`=15 `Off`=4294967295

`Enums.SignalSlot.Off`

## SortColorBy

`Hue`=0 `Saturation`=1

`Enums.SortColorBy.Hue`

## SoundPoolAction

`Toggle`=2 `Go+`=3 `Pause`=10 `Off`=11 `None`=255

`Enums.SoundPoolAction.Toggle`

## SoundValues

`All`=0 `Bass`=1 `Mid`=2 `High`=3 `Band1`=4 `Band2`=5 `Band3`=6 `Band4`=7 `Band5`=8 `Band6`=9 `Band7`=10 `InvAll`=11 `InvBass`=12 `InvMid`=13 `InvHigh`=14 `InvBand1`=15 `InvBand2`=16 `InvBand3`=17 `InvBand4`=18 `InvBand5`=19 `InvBand6`=20 `InvBand7`=21

`Enums.SoundValues.All`

## SourceType

`show`=0 `library`=1 `PSR`=2

`Enums.SourceType.show`

## SpecialAttribute

`None`=0 `NoFeature`=1 `Dummy`=2 `Dimmer`=3 `PanTilt`=4 `XYZ_Pos`=5 `XYZ_Rot`=6 `XYZ_Scale`=7 `ColorRGB`=8 `HSB`=9 `CIE`=10 `Color`=11 `ColorWheelSpin`=12 `Gobo`=13 `GoboWheelSpin`=14 `GoboSelectShake`=15 `GoboPos`=16 `GoboPosRotate`=17 `GoboPosShake`=18 `Prism`=19 `PrismPos`=20 `PrismPosRotate`=21 `Focus`=22 `Zoom`=23 `Iris`=24 `Frost`=25 `Shutter`=26 `CTO`=27 `CTB`=28 `CTC`=29 `Blade`=30 `Video`=31

`Enums.SpecialAttribute.None`

## SpecialCycle

`None`=0 `Time`=1 `Channel`=2 `If`=3

`Enums.SpecialCycle.None`

## SpecialExecutor

`None`=-1 `XFade1`=0 `XFade2`=1 `XFade1Btn`=2 `XFade2Btn`=3 `GrandKnob`=4 `RateBtn1`=9 `SpeedBtn1`=10 `RateBtn2`=19 `SpeedBtn2`=20 `ExecEncoder`=29 `ExecBtn1`=30 `ExecBtn2`=31 `ExecBtn3`=32 `ProgEncoder`=39 `ProgBtn1`=40 `ProgBtn2`=41 `ProgBtn3`=42

`Enums.SpecialExecutor.None`

## SpecialIndexBlade

`Blade1A`=0 `Blade1B`=1 `Blade1Rot`=2 `Blade2A`=3 `Blade2B`=4 `Blade2Rot`=5 `Blade3A`=6 `Blade3B`=7 `Blade3Rot`=8 `Blade4A`=9 `Blade4B`=10 `Blade4Rot`=11 `ShaperRot`=12

`Enums.SpecialIndexBlade.Blade1A`

## SpecialIndexIris

`Iris`=0 `IrisStrobe`=1 `IrisPulseClose`=2 `IrisPulseOpen`=3 `IrisStrobeRandom`=4 `IrisRandomPulseOpen`=5 `IrisRandomPulseClose`=6

`Enums.SpecialIndexIris.Iris`

## SpecialIndexShutter

`Shutter`=0 `ShutterStrobe`=1 `ShutterStrobePulse`=2 `ShutterStrobePulseClose`=3 `ShutterStrobePulseOpen`=4 `ShutterStrobeRandom`=5 `ShutterStrobeRandomPulse`=6 `ShutterStrobeRandomPulseClose`=7 `ShutterStrobeRandomPulseOpen`=8 `ShutterStrobeEffect`=9

`Enums.SpecialIndexShutter.Shutter`

## SpecialPurposeFT

`None`=0 `MArker`=1 `BitmapController`=2 `Universal`=3 `Generic`=3 `MVR Environmental`=4

`Enums.SpecialPurposeFT.None`

## SpecialValueTypes

`Sound`=0 `Generators`=1 `Specials`=2 `None`=255

`Enums.SpecialValueTypes.Sound`

## SpecialValues

`Release`=0 `Hold`=1

`Enums.SpecialValues.Release`

## SpecialWindowRememberedTab

`Color`=0 `Shapers`=1

`Enums.SpecialWindowRememberedTab.Color`

## SpecialWindowTab

`Color`=0 `Shapers`=1 `None`=2

`Enums.SpecialWindowTab.Color`

## SpeedMaster

`Speed1`=0 `Speed2`=1 `Speed3`=2 `Speed4`=3 `Speed5`=4 `Speed6`=5 `Speed7`=6 `Speed8`=7 `Speed9`=8 `Speed10`=9 `Speed11`=10 `Speed12`=11 `Speed13`=12 `Speed14`=13 `Speed15`=14 `BPM`=15 `None`=255 ``=255

`Enums.SpeedMaster.Speed1`

## SpeedMasterMtxOverride

`Speed1`=0 `Speed2`=1 `Speed3`=2 `Speed4`=3 `Speed5`=4 `Speed6`=5 `Speed7`=6 `Speed8`=7 `Speed9`=8 `Speed10`=9 `Speed11`=10 `Speed12`=11 `Speed13`=12 `Speed14`=13 `Speed15`=14 `BPM`=15 `No Master`=254 `None`=255 ``=255

`Enums.SpeedMasterMtxOverride.Speed1`

## SpeedReadoutMode

`Hertz`=0 `BPM`=1 `Seconds`=2

`Enums.SpeedReadoutMode.Hertz`

## SpeedReadoutModeAuto

`Auto`=-1 `Hertz`=0 `BPM`=1 `Seconds`=2

`Enums.SpeedReadoutModeAuto.Auto`

## SpeedScale

`Div256`=-8 `Div128`=-7 `Div64`=-6 `Div32`=-5 `Div16`=-4 `Div8`=-3 `Div4`=-2 `Div2`=-1 `One`=0 `Mul2`=1 `Mul4`=2 `Mul8`=3 `Mul16`=4 `Mul32`=5 `Mul64`=6 `Mul128`=7 `Mul256`=8

`Enums.SpeedScale.Div256`

## SplineType

`None`=0 ``=0 `Free`=1 `Proportional`=2 `Undefined`=3

`Enums.SplineType.None`

## SplitterH_LeftRight

`Right`=0 `Left`=1

`Enums.SplitterH_LeftRight.Right`

## SplitterV_TopBottom

`Bottom`=0 `Top`=1

`Enums.SplitterV_TopBottom.Bottom`

## StartupBrowserFilter

`Shows`=0 `Demo Shows`=1 `Template Shows`=2

`Enums.StartupBrowserFilter.Shows`

## StoreDisplayNumber

`1`=0 `2`=1 `3`=2 `4`=3 `5`=4 `6`=5 `7`=6

`Enums.StoreDisplayNumber["1"]`

## StoreIndexBase

`Default`=0

`Enums.StoreIndexBase.Default`

## StoreMode

`Ask`=-1 `Abort`=0 `Overwrite`=1 `Merge`=2 `Remove`=3 `Release`=4 `CreateSecondCue`=5

`Enums.StoreMode.Ask`

## StoreSource

`Programmer`=0 `Output`=1 `DMX`=2

`Enums.StoreSource.Programmer`

## StoremodeRadio

`Ask`=-1 `Overwrite`=1 `Merge`=2 `Remove`=3 `Release`=4

`Enums.StoremodeRadio.Ask`

## StrictNormalMode

`Normal`=0 `Strict`=1

`Enums.StrictNormalMode.Normal`

## StructureType

`CenterLineBased`=0 `Detail`=1

`Enums.StructureType.CenterLineBased`

## SubphysicalType

`PlacementOffset`=0 `Amplitude`=1 `AmplitudeMin`=2 `AmplitudeMax`=3 `Duration`=4 `DutyCycle`=5 `TimeOffset`=6 `MinimumOpening`=7 `Value`=8 `RatioHorizontal`=9 `RatioVertical`=10

`Enums.SubphysicalType.PlacementOffset`

## SupportType

`Rope`=0 `GroundSupport`=1

`Enums.SupportType.Rope`

## SyntaxResult

`SyntaxError`=-1 `SyntaxOk`=0 `ExecuteBefore`=1 `ExecuteAfter`=2 `Execute`=3 `AbortBefore`=4 `Ignore`=5 `Erase`=6

`Enums.SyntaxResult.SyntaxError`

## SyntaxState

`SyntaxError`=-1 `None`=0 `DoExecute`=1 `DoFader`=2 `DoChangeDestination`=3 `DoShutdown`=4 `DoLogin`=5 `DoLogout`=6 `DoSetLanguage`=7 `DoSetDMXReadout`=8 `DoLoadShowfile`=9 `DoSaveShowfile`=10 `DoImport`=11 `DoExport`=12 `DoStore`=13 `DoUpdate`=14 `DoOops`=15 `DoEditUpdate`=16 `DoEdit`=17 `DoCut`=18 `DoCopy`=19 `DoPaste`=20 `DoMove`=21 `DoDelete`=22 `DoCall`=23 `DoCrashMe`=24 `DoSelectFixtures`=25 `DoIncrement`=26 `DoIncrementReset`=27 `DoSet`=28 `DoAssign`=29 `DoAlign`=30 `DoAlignTransition`=31 `DoValueReadout`=32 `DoLabel`=33 `DoPatch`=34 `DoPark`=35 `DoLocking`=36 `DoSelect`=37 `DoFix`=38 `DoType`=39 `DoDebug`=40 `DoList`=41 `DoGrid`=42 `DoExchange`=43 `DoNotCare`=44

`Enums.SyntaxState.SyntaxError`

## TCDuration

`To End`=0

`Enums.TCDuration["To End"]`

## TCTextMode

`All`=0 `Tracks`=1 `Selected`=2 `Markers`=3

`Enums.TCTextMode.All`

## TCViewMode

`Text`=0 `Timeline`=1 `Both`=2

`Enums.TCViewMode.Text`

## TTL

`Default(8)`=8

`Enums.TTL["Default(8)"]`

## TagActionToken

`None`=0 `Flash`=1 `Go+`=3 `Off`=8 `Temp`=13 `Toggle`=14 `Top`=15 `Pause`=18 `List Reference`=100 `Pool Default`=417

`Enums.TagActionToken.None`

## TagPoolAction

`Toggle`=2 `Go+`=3 `Flash`=4 `Temp`=5 `Pause`=10 `Off`=11 `Top`=12 `List Reference`=16 `None`=255

`Enums.TagPoolAction.Toggle`

## TagType

`None`=0 `Kill Instant`=4 `Kill Delayed`=5

`Enums.TagType.None`

## TestBlockType

`ui`=0 `root`=1 `rt`=2 `lua`=3

`Enums.TestBlockType.ui`

## TextInputEditor

`Scribble`=0 `Appearance`=1 `Tags`=2 `NameNote`=3 `None`=4

`Enums.TextInputEditor.Scribble`

## TimeCodeSource

`Midi`=0 `Smpte`=1

`Enums.TimeCodeSource.Midi`

## TimeCursorScrollMode

`Page`=0 `Center`=1

`Enums.TimeCursorScrollMode.Page`

## TimeDefault

`Default`=9223372036854775807

`Enums.TimeDefault.Default`

## TimeDisplayClockFormat

`10.11:23:45`=2 `251:23:45`=3 `Default`=255

`Enums.TimeDisplayClockFormat.Default`

## TimeDisplayFormat

`10d11h23m45`=0 `251h23m45`=1 `10.11:23:45`=2 `251:23:45`=3

`Enums.TimeDisplayFormat["10d11h23m45"]`

## TimeDisplayFormatDefault

`10d11h23m45`=0 `251h23m45`=1 `10.11:23:45`=2 `251:23:45`=3 `Default`=255

`Enums.TimeDisplayFormatDefault.Default`

## TimeKeyTarget

`Cue`=0 `Fixture`=1

`Enums.TimeKeyTarget.Cue`

## TimeNone

`None`=9223372036854775807

`Enums.TimeNone.None`

## TimeNoneEmpty

``=9223372036854775807 `None`=9223372036854775807

`Enums.TimeNoneEmpty.None`

## TimeNoneSwap

`Invert`=9223372036854775806 `None`=9223372036854775807

`Enums.TimeNoneSwap.Invert`

## TimeNoneSwapDelay

`No Delay`=9223372036854775805 `Swap Delay`=9223372036854775806 `None`=9223372036854775807

`Enums.TimeNoneSwapDelay.None`

## TimeNoneSwapFade

`No Fade`=9223372036854775805 `Swap Fade`=9223372036854775806 `None`=9223372036854775807

`Enums.TimeNoneSwapFade.None`

## TimeNoneSwapSpeed

`No Speed`=9223372036854775805 `Swap Speed`=9223372036854775806 `None`=9223372036854775807

`Enums.TimeNoneSwapSpeed.None`

## TimeRecipeSpeed

`Half`=9223372036854775803 `Double`=9223372036854775804 `No Speed`=9223372036854775805 `Swap Speed`=9223372036854775806

`Enums.TimeRecipeSpeed.Half`

## TimeSwapDelay

`No Delay`=9223372036854775805 `Swap Delay`=9223372036854775806

`Enums.TimeSwapDelay["No Delay"]`

## TimeSwapFade

`No Fade`=9223372036854775805 `Swap Fade`=9223372036854775806

`Enums.TimeSwapFade["No Fade"]`

## TimecodeEncoderFunction

`Edit`=0

`Enums.TimecodeEncoderFunction.Edit`

## TimecodePoolAction

`Select`=1 `Toggle`=2 `Go+`=3 `Pause`=10 `Off`=11 `Top`=12 `None`=255

`Enums.TimecodePoolAction.Select`

## TimecodeSelectLastEventMode

`Off`=0 `Track`=1 `All`=2

`Enums.TimecodeSelectLastEventMode.Off`

## TimecodeSelectionTarget

`Events`=0 `TimeRanges`=1

`Enums.TimecodeSelectionTarget.Events`

## TimecodeSingleUserRecord

`All Users`=0 `Single User`=1

`Enums.TimecodeSingleUserRecord["All Users"]`

## TimecodeSlot

`TCSlot 1`=0 `TCSlot 2`=1 `TCSlot 3`=2 `TCSlot 4`=3 `TCSlot 5`=4 `TCSlot 6`=5 `TCSlot 7`=6 `TCSlot 8`=7 `TCSlot 9`=8 `TCSlot 10`=9 `TCSlot 11`=10 `TCSlot 12`=11 `TCSlot 13`=12 `TCSlot 14`=13 `TCSlot 15`=14 `TCSlot 16`=15 `<Selected>`=255

`Enums.TimecodeSlot["TCSlot 1"]`

## TimecodeSlotPoolAction

`Select`=1 `Toggle`=2 `Go+`=3 `Pause`=10 `Off`=11 `None`=255

`Enums.TimecodeSlotPoolAction.Select`

## TimecodeSlotShort

`TCSlot 1`=0 `TCSlot 2`=1 `TCSlot 3`=2 `TCSlot 4`=3 `TCSlot 5`=4 `TCSlot 6`=5 `TCSlot 7`=6 `TCSlot 8`=7 `TCSlot 9`=8 `TCSlot 10`=9 `TCSlot 11`=10 `TCSlot 12`=11 `TCSlot 13`=12 `TCSlot 14`=13 `TCSlot 15`=14 `TCSlot 16`=15

`Enums.TimecodeSlotShort["TCSlot 1"]`

## TimecodeTool

`Operate`=0 `Select`=1 `Add`=2 `Delete`=3 `Move`=4 `Resize`=5

`Enums.TimecodeTool.Operate`

## TimerAction

`Select`=1 `Toggle`=2 `None`=255

`Enums.TimerAction.Select`

## TimerMode

`Countdown`=0 `Stopwatch`=1

`Enums.TimerMode.Countdown`

## TimerTriggerToken

`Go+`=0 `Toggle`=1 `Flash`=2 `Temp`=3

`Enums.TimerTriggerToken.Toggle`

## TimingMaster

`Timing50`=-51 `Timing49`=-50 `Timing48`=-49 `Timing47`=-48 `Timing46`=-47 `Timing45`=-46 `Timing44`=-45 `Timing43`=-44 `Timing42`=-43 `Timing41`=-42 `Timing40`=-41 `Timing39`=-40 `Timing38`=-39 `Timing37`=-38 `Timing36`=-37 `Timing35`=-36 `Timing34`=-35 `Timing33`=-34 `Timing32`=-33 `Timing31`=-32 `Timing30`=-31 `Timing29`=-30 `Timing28`=-29 `Timing27`=-28 `Timing26`=-27 `Timing25`=-26 `Timing24`=-25 `Timing23`=-24 `Timing22`=-23 `Timing21`=-22 `Timing20`=-21 `Timing19`=-20 `Timing18`=-19 `Timing17`=-18 `Timing16`=-17 `Timing15`=-16 `Timing14`=-15 `Timing13`=-14 `Timing12`=-13 `Timing11`=-12 `Timing10`=-11 `Timing9`=-10 `Timing8`=-9 `Timing7`=-8 `Timing6`=-7 `Timing5`=-6 `Timing4`=-5 `Timing3`=-4 `Timing2`=-3 `Timing1`=-2

`Enums.TimingMaster.Timing50`

## TimingMasterWithDefault

`Timing50`=-51 `Timing49`=-50 `Timing48`=-49 `Timing47`=-48 `Timing46`=-47 `Timing45`=-46 `Timing44`=-45 `Timing43`=-44 `Timing42`=-43 `Timing41`=-42 `Timing40`=-41 `Timing39`=-40 `Timing38`=-39 `Timing37`=-38 `Timing36`=-37 `Timing35`=-36 `Timing34`=-35 `Timing33`=-34 `Timing32`=-33 `Timing31`=-32 `Timing30`=-31 `Timing29`=-30 `Timing28`=-29 `Timing27`=-28 `Timing26`=-27 `Timing25`=-26 `Timing24`=-25 `Timing23`=-24 `Timing22`=-23 `Timing21`=-22 `Timing20`=-21 `Timing19`=-20 `Timing18`=-19 `Timing17`=-18 `Timing16`=-17 `Timing15`=-16 `Timing14`=-15 `Timing13`=-14 `Timing12`=-13 `Timing11`=-12 `Timing10`=-11 `Timing9`=-10 `Timing8`=-9 `Timing7`=-8 `Timing6`=-7 `Timing5`=-6 `Timing4`=-5 `Timing3`=-4 `Timing2`=-3 `Timing1`=-2 `CueTiming`=-1

`Enums.TimingMasterWithDefault.Timing50`

## TimingMasterWithXAssert

`CueTiming`=-52 `Timing50`=-51 `Timing49`=-50 `Timing48`=-49 `Timing47`=-48 `Timing46`=-47 `Timing45`=-46 `Timing44`=-45 `Timing43`=-44 `Timing42`=-43 `Timing41`=-42 `Timing40`=-41 `Timing39`=-40 `Timing38`=-39 `Timing37`=-38 `Timing36`=-37 `Timing35`=-36 `Timing34`=-35 `Timing33`=-34 `Timing32`=-33 `Timing31`=-32 `Timing30`=-31 `Timing29`=-30 `Timing28`=-29 `Timing27`=-28 `Timing26`=-27 `Timing25`=-26 `Timing24`=-25 `Timing23`=-24 `Timing22`=-23 `Timing21`=-22 `Timing20`=-21 `Timing19`=-20 `Timing18`=-19 `Timing17`=-18 `Timing16`=-17 `Timing15`=-16 `Timing14`=-15 `Timing13`=-14 `Timing12`=-13 `Timing11`=-12 `Timing10`=-11 `Timing9`=-10 `Timing8`=-9 `Timing7`=-8 `Timing6`=-7 `Timing5`=-6 `Timing4`=-5 `Timing3`=-4 `Timing2`=-3 `Timing1`=-2

`Enums.TimingMasterWithXAssert.CueTiming`

## ToolbarScrollType

`Vertical`=0 `Horizontal`=1

`Enums.ToolbarScrollType.Vertical`

## TotalReferenceUpdateStatus

`Idle`=0 `CollectPresets`=1 `CollectCues`=2 `SortHandles`=3 `UpdatePresets`=4 `TrackingConversion`=5 `GeneratorCleanup`=6 `UpdateProgrammer`=7 `RecursionTest`=8 `TagCleanup`=9 `UserCleanup`=10 `UserConversion`=11

`Enums.TotalReferenceUpdateStatus.Idle`

## TotalUpdateType

`None`=0 `UserCleanup`=1 `TagCleanup`=2 `OnlyNames`=3 `References`=4 `Content`=5

`Enums.TotalUpdateType.None`

## TouchMode

`None`=0 `Off`=1 `Select`=2

`Enums.TouchMode.None`

## TrackEditApplyFor

`Selected Part(s)`=0 `All Parts in sel. Cue(s)`=1 `All Cues/Parts`=2

`Enums.TrackEditApplyFor["Selected Part(s)"]`

## TrackEditGrouping

`Selection`=0 `Feature`=1 `Activation Group`=2 `All Fixtures`=3

`Enums.TrackEditGrouping.Selection`

## TrackLayerAuto

`Auto`=-1 `Fade`=2 `Delay`=3 `Speed`=4 `SpeedMaster`=5 `Phase`=6 `GridPos`=7 `Measure`=8 `NShot`=9 `Absolute`=11 `Relative`=12 `Accel`=13 `Decel`=14 `Transition`=15 `Width`=16

`Enums.TrackLayerAuto.Auto`

## TrackingShield

`Off`=0 `^0`=1 `DRZ`=1 `DimmerRisingFromZero`=1 `DimmerAboveZero`=2 `DAZ`=2 `>0`=2

`Enums.TrackingShield.Off`

## TrackingShieldPopup

`Off`=0 `^0`=1 `>0`=2

`Enums.TrackingShieldPopup.Off`

## TrackpadMode

`Mouse`=0 `Pan/Tilt`=1

`Enums.TrackpadMode.Mouse`

## TrackpadPTInvertMode

`Off`=0 `Pan Invert`=1 `Tilt Invert`=2 `Both`=3

`Enums.TrackpadPTInvertMode.Off`

## TrackpadPTMode

`Pan Only`=0 `Tilt Only`=1 `Both`=2

`Enums.TrackpadPTMode.Both`

## TransitionMode

`Linear`=0 `Sinus`=1 `Slow`=2 `Fast`=3

`Enums.TransitionMode.Linear`

## TransitionType

`Linear`=0 `Slow`=1 `Slow+`=2 `Fast`=3 `Fast+`=4 `SCurve`=5 `Swing-`=6 `Swing`=7 `Swing+`=8

`Enums.TransitionType.Linear`

## TrueFalse

`False`=0 `True`=1

`Enums.TrueFalse.False`

## UndefinedAnchors

`Undefined`=-1

`Enums.UndefinedAnchors.Undefined`

## UndefinedMax

`-`=32767

`Enums.UndefinedMax["-"]`

## UndefinedMin

`-`=-32768

`Enums.UndefinedMin["-"]`

## Update

`Original Content Only`=0 `Add New Content`=1

`Enums.Update["Original Content Only"]`

## UsbProductID

`grandMA3 VR wing`=16962 `grandMA3 MA-Key (Blank)`=46352 `grandMA3 MA-Key (Viz-Key)`=46353 `grandMA3 DMX Module`=46528 `MA NPU 3 DMX Module`=46529 `grandMA3 Control Module`=46530 `grandMA3 Master Module (MM)`=46531 `grandMA3 Fader Module Crossfader (MFX)`=46532 `grandMA3 Fader Module Encoder (MFE)`=46533 `grandMA3 Compact`=46534 `grandMA3 Compact XT`=46535 `grandMA3 CommandWing`=46536 `grandMA3 xPort node`=46537 `grandMA3 DIN-Rail node`=46538 `grandMA3 IO Node`=46539 `grandMA3 IO Node DIN Rail`=46540 `grandMA3 Fader Wing`=46541 `grandMA3 onPC DMX-key`=46543 `grandMA3 onPC DMX-key starter`=46544

`Enums.UsbProductID["grandMA3 VR wing"]`

## UserProfileChildIndex

`Environments`=0 `EncoderBarPool`=1 `CameraPool`=2 `ViewPool`=3 `StorePreferences`=4 `ExecFixation`=5 `SpecialExecPageCollect`=6 `TemporaryWindowSettings`=7 `SmartViewPool`=8 `Variables`=9 `ScreenConfig`=10 `LayoutElementDefaults`=11 `KeyboardShortcutsConfig`=12 `AttributePreferences`=13 `RenderQuality`=14 `GridRegistry`=15 `StatusCenter`=16 `PreviewObjects`=17

`Enums.UserProfileChildIndex.Environments`

## UserRights

`Admin`=0 `Setup`=1 `Program`=2 `Presets`=3 `Playback`=4 `View`=5 `None`=6

`Enums.UserRights.Admin`

## UserRightsWithoutNone

`Admin`=0 `Setup`=1 `Program`=2 `Presets`=3 `Playback`=4 `View`=5

`Enums.UserRightsWithoutNone.Admin`

## ValueLayer

`Fade`=2 `Delay`=3 `Absolute`=11 `Relative`=12

`Enums.ValueLayer.Fade`

## ValueNone

`None`=2147483647

`Enums.ValueNone.None`

## ValueNoneEmpty

`Release`=1107296256 `Hold`=1107296257 `None`=2147483647 ``=2147483647

`Enums.ValueNoneEmpty.Release`

## ValueReadoutMode

`Percent`=0 `PercentFine`=1 `Physical`=2 `Decimal8`=3 `Decimal16`=4 `Decimal24`=5 `Hex8`=6 `Hex16`=7 `Hex24`=8

`Enums.ValueReadoutMode.Percent`

## ValueReadoutModeAuto

`Auto`=-1 `Percent`=0 `PercentFine`=1 `Physical`=2 `Decimal8`=3 `Decimal16`=4 `Decimal24`=5 `Hex8`=6 `Hex16`=7 `Hex24`=8 `Natural`=9

`Enums.ValueReadoutModeAuto.Auto`

## ValueReadoutModeDefault

`Default`=-1 `Percent`=0 `PercentFine`=1 `Physical`=2 `Decimal8`=3 `Decimal16`=4 `Decimal24`=5 `Hex8`=6 `Hex16`=7 `Hex24`=8

`Enums.ValueReadoutModeDefault.Default`

## ValueReadoutModeNatural

`Percent`=0 `PercentFine`=1 `Physical`=2 `Decimal8`=3 `Decimal16`=4 `Decimal24`=5 `Hex8`=6 `Hex16`=7 `Hex24`=8 `Natural`=9

`Enums.ValueReadoutModeNatural.Percent`

## ValueRole

`Default`=0 `Display`=1 `DisplayShort`=2

`Enums.ValueRole.Default`

## VerifyResult

`NotVerified`=0 `Valid`=1 `Expired`=2

`Enums.VerifyResult.NotVerified`

## VideoFileSource

`File`=0 `NDI`=1

`Enums.VideoFileSource.File`

## VideoPoolAction

`Toggle`=2 `Go+`=3 `Pause`=10 `Off`=11 `None`=255

`Enums.VideoPoolAction.Toggle`

## VirtualKeyCode

``=0 `UNKNOWN`=0 `MA1`=1 `MA2`=2 `PREV`=3 `NEXT`=4 `SET`=5 `UP`=6 `SELFIX`=7 `DOWN`=8 `MENU`=9 `HIGHLIGHT`=10 `SOLO`=11 `FREEZE`=12 `PREVIEW`=13 `BLIND`=14 `XKEYS`=15 `PAGE_UP`=16 `PAGE_DOWN`=17 `LIST`=18 `X1`=19 `X2`=20 `X3`=21 `X4`=22 `X5`=23 `X6`=24 `X7`=25 `X8`=26 `X9`=27 `X10`=28 `X11`=29 `X12`=30 `X13`=31 `X14`=32 `X15`=33 `X16`=34 `EXEC`=35 `FADER`=36 `DEF_GO`=37 `DEF_PAUSE`=38 `DEF_GOBACK`=39 `PAUSE`=40 `GOBACK`=41 `GO`=42 `LEARN`=43 `GOBACKFAST`=44 `GOFAST`=45 `ON`=46 `OFF`=47 `MOVE`=48 `COPY`=49 `DELETE`=50 `ALIGN`=51 `STOMP`=52 `HELP`=53 `SELECT`=54 `GOTO`=55 `FIXTURE`=56 `CHANNEL`=57 `GROUP`=58 `SEQUENCE`=59 `CUE`=60 `PRESET`=61 `EDIT`=62 `ASSIGN`=63 `TIME`=64 `UPDATE`=65 `STORE`=66 `NUM0`=67 `NUM1`=68 `NUM2`=69 `NUM3`=70 `NUM4`=71 `NUM5`=72 `NUM6`=73 `NUM7`=74 `NUM8`=75 `NUM9`=76 `PLUS`=77 `THRU`=78 `MINUS`=79 `DOT`=80 `IF`=81 `AT`=82 `SLASH`=83 `PLEASE`=84 `FULL`=85 `UNDO`=86 `OOPS`=86 `CLEAR`=87 `ESC`=88 `ENCODER_INSIDE1`=89 `ENCODER_OUTSIDE1`=90 `ENCODER_INSIDE2`=91 `ENCODER_OUTSIDE2`=92 `ENCODER_INSIDE3`=93 `ENCODER_OUTSIDE3`=94 `ENCODER_INSIDE4`=95 `ENCODER_OUTSIDE4`=96 `ENCODER_INSIDE5`=97 `ENCODER_OUTSIDE5`=98 `USER1`=99 `USER2`=100 `FLASH`=101 `BLACK`=102 `KILL`=103 `RATE1`=104 `TEMP`=105 `TOGGLE`=106 `TOP`=107 `LOAD`=108 `LOWLIGHT`=109 `GOSTEP`=110 `SWAP`=111 `HALF_SPEED`=112 `DOUBLE_SPEED`=113 `RECORD`=114 `PREV_X`=115 `PREV_Y`=116 `PREV_Z`=117 `PREV_STEP`=118 `NEXT_X`=119 `NEXT_Y`=120 `NEXT_Z`=121 `NEXT_STEP`=122 `STEP`=123 `TOGGLE_STEP`=124 `TOGGLE_MATRICKS`=125 `RESET_MATRICKS`=126 `ONPC_SCREEN2`=127 `ONPC_SCREEN3`=128 `ONPC_SCREEN4`=129 `ONPC_SCREEN5`=130 `ONPC_SCREEN6`=131 `ONPC_SCREEN7`=132 `ASTERISK`=133 `FIX`=134 `CLONE`=135 `GRID`=136 `LAYOUT`=137 `TIMECODE`=138 `VIEW`=139 `DMX`=140 `PHASER`=141 `MACRO`=142 `PAGE`=143 `EXECUTOR`=144 `FLIP`=145 `LOCATE`=146

`Enums.VirtualKeyCode.UNKNOWN`

## VirtualKeyExecutionType

`Normal`=0 `Immediate`=1 `ClearImmediate`=2 `Background`=3 `Release`=4

`Enums.VirtualKeyExecutionType.Normal`

## WeekDay

`Monday`=0 `Tuesday`=1 `Wednesday`=2 `Thursday`=3 `Friday`=4 `Saturday`=5 `Sunday`=6

`Enums.WeekDay.Monday`

## WeekDayShort

`Mon`=0 `Tue`=1 `Wed`=2 `Thu`=3 `Fri`=4 `Sat`=5 `Sun`=6

`Enums.WeekDayShort.Mon`

## WeekOfMonth

`First Week`=0 `Second Week`=1 `Third Week`=2 `Fourth Week`=3 `Fifth Week`=4 `Sixth Week`=5

`Enums.WeekOfMonth["First Week"]`

## WheelMode

`Additive`=0 `Incremental`=1 `Prop.+`=2 `Prop.-`=3

`Enums.WheelMode.Additive`

## WhiteListPacketIDs

`grandMA3_fixtures`=1158 `onpc_mac`=1158 `demoshows`=1158 `updater_mac`=1158 `grandMA3_manuals`=1158 `updater_windows`=1158 `gdtf_mvr_addon`=1158 `grandMA2_manuals`=1158 `grandMA2_compat`=1158 `onpc_windows`=1158 `worldserver`=1158 `grandMA3_console`=1158 `web_daemon`=1158 `force_x64`=1166 `grandMA2_npu_compat`=1166 `updater_x64`=1166 `disttestmaster`=1166 `grandMA3_unittest`=1166 `third_party`=1166 `utils`=1166 `ndi_addon`=1166 `bootloader_x64`=1166 `luatest`=1166 `grandMA3_pu`=1166 `grandMA2_ffmpeg`=1166 `grandMA2_resource`=1166 `system_x64`=1166 `grandMA3_net_duct_windows`=1174 `grandMA3_viz_key_mac`=1174 `grandMA3_net_duct_mac`=1174 `grandMA3_viz_key_windows`=1174 `grandMA3_updater_linux`=1174 `grandMA3_res_usb`=1174 `grandMA3_net_duct_linux`=1174 `updater_arm`=1974 `force_arm`=1974 `grandMA3_xport`=1974 `grandMA2_xport_compat`=1974 `system_arm`=1974 `grandMA3_wing`=1974 `grandMA3_resource`=1982 `force_all`=1982

`Enums.WhiteListPacketIDs.grandMA3_fixtures`

## WhiteListPacketNames

`web_daemon`=1158 `gdtf_mvr_addon`=1158 `onpc_mac`=1158 `onpc_windows`=1158 `gma2_manuals`=1158 `console`=1158 `demoshows`=1158 `gma2_compat`=1158 `manuals`=1158 `fixtures`=1158 `worldserver`=1158 `updater_x64`=1166 `utils`=1166 `third_party`=1166 `luatest`=1166 `force_x64`=1166 `unittest`=1166 `bootloader_x64`=1166 `pu`=1166 `system_x64`=1166 `gma2_ffmpeg`=1166 `ndi_addon`=1166 `gma2_resource`=1166 `npu_compat`=1166 `resource_usb`=1174 `viz_key`=1174 `wing`=1974 `xport`=1974 `force_arm`=1974 `updater_arm`=1974 `system_arm`=1974 `xport_compat`=1974 `force_all`=1982 `resource`=1982

`Enums.WhiteListPacketNames.web_daemon`

## WhiteListPacketNamesBefore_1_7

`luatest`=1166 `npu_compat`=1166 `updater_x64`=1166 `worldserver`=1166 `third_party`=1166 `manuals`=1166 `system_x64`=1166 `unittest`=1166 `onpc_windows`=1166 `gdtf_mvr_addon`=1166 `ndi_addon`=1166 `console`=1166 `gma2_manuals`=1166 `gma2_ffmpeg`=1166 `bootloader_x64`=1166 `gma2_resource`=1166 `web_daemon`=1166 `demoshows`=1166 `gma2_compat`=1166 `utils`=1166 `fixtures`=1166 `pu`=1166 `onpc_mac`=1166 `resource_usb`=1182 `viz_key`=1182 `xport_compat`=1982 `updater_arm`=1982 `wing`=1982 `system_arm`=1982 `xport`=1982 `resource`=1982

`Enums.WhiteListPacketNamesBefore_1_7.luatest`

## WindowCategories

`Show Data`=0 `Media`=1 `User Profile`=2 `Data Pool`=3 `Dynamic`=4 `Feature Group`=5 `All`=6 `Sheets`=7 `Programmer Tools`=8 `Viewers and Editors`=9 `Bars`=10 `Playback`=11 `Info and System`=12

`Enums.WindowCategories.Media`

## WindowInfoTab

`Referenced by`=0 `Depends on`=1 `Note`=2

`Enums.WindowInfoTab.Note`

## WindowTypes

`Sheets`=0 `Pools`=1 `Presets`=2 `Others`=3

`Enums.WindowTypes.Sheets`

## WingID

`Wing1`=1 `Wing2`=2 `Wing3`=3 `Wing4`=4 `Wing5`=5 `Wing6`=6

`Enums.WingID.Wing1`

## WingType

`grandMA3 Master Module (MM)`=0 `grandMA3 Fader Module Crossfader (MFX)`=1 `grandMA3 Fader Module Encoder (MFE)`=2 `grandMA3 TEST`=3 `grandMA3 Compact`=4

`Enums.WingType["grandMA3 Master Module (MM)"]`

## WorldAction

`Select`=1 `SelFix`=15 `None`=255

`Enums.WorldAction.Select`

## XFadeMode

`AB`=0 `Split`=1

`Enums.XFadeMode.AB`

## XYZMapping

`X`=0 `Y`=1 `Z`=2

`Enums.XYZMapping.X`

## Yes

``=0 `<Blank>`=0 `Yes`=1

`Enums.Yes.Yes`

## YesNo

`No`=0 `Yes`=1

`Enums.YesNo.No`

## ZoomFactor

`10%`=-5 `20%`=-4 `30%`=-3 `40%`=-2 `50%`=-1 `60%`=0 `70%`=1 `80%`=2 `90%`=3 `100%`=4 `110%`=5 `120%`=6 `130%`=7 `140%`=8 `150%`=9 `160%`=10 `170%`=11 `180%`=12 `190%`=13 `200%`=14 `210%`=15 `220%`=16 `230%`=17 `240%`=18 `250%`=19 `260%`=20 `270%`=21 `280%`=22 `290%`=23 `300%`=24

`Enums.ZoomFactor["10%"]`

