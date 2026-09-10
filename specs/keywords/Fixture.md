---
keyword: "Fixture"
kind: general
shortcuts: ["F", "Fi"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_fixture.html"
---

## Official

To enter the Fixture keyword in the command line, use one of the options:

  * Press `Fixture`
  * Type **Fixture**
  * Type the shortcut **F** or **Fi**

### Description

The Fixture keyword is used as an object keyword to access fixtures that have a fixture ID.

### Syntax

Fixture ["Fixture_Name" or Fixture_Number]

Fixture ["Fixture_Name" or Fixture_Number].["SubFixture_Name" or SubFixture_Number]

### Option Keywords

The Fixture keyword uses the following option keywords:

  * [/OddEven](https://help.malighting.com/grandMA3/2.5/HTML/ok_oddeven.html)

### Examples

  * To select fixture 2, type:

```
Fixture 2
```

  * To select the fifth subfixture of fixture 10, type:

```
Fixture 10.5
```

  * To call values of fixture 1 of the next cue in the selected sequence to programmer, type:

```
Fixture 1 At Cue Next
```

  * To call values of fixture 5 of the previous cue in the selected sequence to programmer, type:

```
Fixture 5 At Cue Previous
```

For information on the key and its location see [Fixture key](https://help.malighting.com/grandMA3/2.5/HTML/key_fixture.html).

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
