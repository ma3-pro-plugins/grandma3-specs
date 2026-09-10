---
keyword: "UserProfile"
kind: general
shortcuts: ["UPR"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_userprofile.html"
---

## Official

To enter the UserProfile keyword in the command line, use one of the options:

  * Type **UserProfile**
  * Type **Userp**
  * Type the shortcut **UPR**

### Description

The UserProfile keyword is an object keyword. It can be used to adjust settings in the UserProfile.

For more information on user profiles see [Create User](https://help.malighting.com/grandMA3/2.5/HTML/user_create.html). For information on different settings see [User Settings](https://help.malighting.com/grandMA3/2.5/HTML/users_and_profiles_configuration.html).

### Syntax

[Function] UserProfile ["UserProfile_Name" or UserProfile_Number] (Property ["Property_Name"] [Property_Value])

### Examples  
  

  * To list all available user profiles, type:

```
List UserProfile
```
---|---  
  
  * To turn off the screen encoder in the default user profile, type:

```
Set UserProfile "Default" "ScreenEncoder" "No"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
