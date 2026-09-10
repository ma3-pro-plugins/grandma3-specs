---
keyword: "UpdateContent"
kind: general
shortcuts: ["UC", "Updatec"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_updatecontent.html"
---

## Official

To enter the UpdateContent keyword in the command line, use one of the options:

  * Type **UpdateContent**
  * Type the shortcut **UC** or **Updatec**

### Description

The UpdateContent keyword is used to scan a media pool, for example images, and create XML files for media files.

### Syntax

**UpdateContent [Object] ["Object_Name" or Object_Number]**

### Example

The following example is explained using images. 

**Requirement:**

  1. A media file, for example an image, was added to the corresponding media folder, for example in grandMA3_lib/media/images, without an XML file.
  2. Enter the media pool folder and then the image folder.   
For more information see [ChangeDestination keyword](https://help.malighting.com/grandMA3/2.5/HTML/release_notes.html). 

  * To create the XML files that are missing in the image folder of the media pool, type:

|  User name@ShowData/MediaPools/Images>UpdateContent Image   
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
