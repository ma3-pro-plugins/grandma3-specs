---
keyword: "User"
kind: general
shortcuts: ["Us"]
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/keyword_user.html"
---

## Official

To enter the User keyword in the command line, use one of the options:

  * Type **User**
  * Type the shortcut **Us**

### Description

The User keyword is used to log in or to change the user settings.

For more information on users and different settings see [User Setting](https://help.malighting.com/grandMA3/2.5/HTML/users_and_profiles_configuration.html).

### Syntax

User ["User_Name" or User_Number]

[Function] User ["User_Name or User_Number] ([Setting] [Setting_Value])

### Settings

The User keyword uses a number of settings. Change the settings using the [Set Keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_set.html). If a setting has to have a pool object, use the [Assign keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_assign.html) to assign an object to the setting.

Here are the settings:

Setting | Object/Option/Value | Description  
---|---|---  
Name | Text | The name of the user. This can be used as user ID.  
Scribble | Scribble pool object | The Scribble assigned to the User object.  
Appearance | Appearance pool object | The Appearance assigned to the User object.  
Password | Text | The password is not shown in clear text.  
Profile | UserProfile object | The assigned User Profile.  
ScreenConfig | Screen configuration object | The active screen configuration.  
Rights | "Admin", "Setup", "Program", "Preset", "Playback", "View", or "None" | The access right assigned to the user.  
Language | "de", "en", "ru", or "dk" | The language assigned to the user.  
Keyboard | "German", "English", "Russian", or "Danish" | The keyboard layout assigned to the user's onscreen keyboard.  
  
### Example  
  

  * To list the details of all users, type: 

```
List User
```
---|---  
  
  * To log in as "Admin", type:

```
User Admin
```
---|---  
  
Alternatively see the [Login Keyword](https://help.malighting.com/grandMA3/2.5/HTML/keyword_login.html).

  * To assign appearance number 1 to User 2

```
Assign Appearance 1 At User 2
```
---|---  
  
  * To change the rights to Playback for user Remote, type:

```
Set User "Remote" "Rights" "Playback"
```
---|---

## Extra

<!-- Contributor notes. Crawler must not overwrite this section. -->
