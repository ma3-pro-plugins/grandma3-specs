---
source: mixed
manual_url: "https://help.malighting.com/grandMA3/2.5/HTML/user.html"
---

# Users (Topic Spec)

Concept map (thin): [`concepts/users.md`](concepts/users.md). Keywords: [`User`](keywords/User.md), [`UserProfile`](keywords/Userprofile.md), [`LogIn`](keywords/Login.md), [`Logout`](keywords/Logout.md), [`List`](keywords/List.md), [`Set`](keywords/Set.md), [`Assign`](keywords/Assign.md), [`Store`](keywords/Store.md), [`ScreenConfiguration`](keywords/Screenconfiguration.md), [`ListOwnership`](keywords/Listownership.md), [`DropOwnership`](keywords/Dropownership.md), [`Menu`](keywords/Menu.md).

Manual hub + subtopics (one object): [Create User](https://help.malighting.com/grandMA3/2.5/HTML/user_create.html), [Users and Profiles Configuration](https://help.malighting.com/grandMA3/2.5/HTML/users_and_profiles_configuration.html), [Object Ownership](https://help.malighting.com/grandMA3/2.5/HTML/user_ownership.html), [Screen Configuration](https://help.malighting.com/grandMA3/2.5/HTML/user_screen_config.html). User Settings HTML is reachable; treated as the same settings surface as Users and Profiles Configuration (no separate Spec).

Single-user vs multi-user session behavior (shared programmer vs not) is already on the concept page — **do not** duplicate [`multi-station.md`](multi-station.md) matrices; one-line link: [`multi-station.md`](multi-station.md).

Users live in the **User** pool. Each user needs a **User Profile** (programmer, selection, pages, cameras, views, …). Same profile → shared programmer state; different profiles → independent programmers (multi-user). Default show users share one profile. **Admin** password resets empty on show load; **Guest** password cannot change (empty).

## Login / list / rights (CLI)

Lists all users:

```
List User
```

Logs in as **Admin** (pool tap / User call):

```
User Admin
```

Logs in as **Jimmy Page** with password **mac** ([`LogIn`](keywords/Login.md); password is case-sensitive):

```
LogIn "Jimmy Page" "mac"
```

Sets rights of user **Remote** to **Playback** (Official rights: Admin, Setup, Program, Preset, Playback, View, None):

```
Set User "Remote" "Rights" "Playback"
```

Assigns appearance **1** to user **2**:

```
Assign Appearance 1 At User 2
```

Official `Set User` / Assign settings ([`User`](keywords/User.md)):

| Setting | Object/Option/Value |
| --- | --- |
| Name | Text |
| Scribble | Scribble pool object (via Assign) |
| Appearance | Appearance pool object (via Assign) |
| Password | Text |
| Profile | UserProfile object |
| ScreenConfig | Screen configuration object |
| Rights | `Admin` \| `Setup` \| `Program` \| `Preset` \| `Playback` \| `View` \| `None` |
| Language | `de` \| `en` \| `ru` \| `dk` |
| Keyboard | `German` \| `English` \| `Russian` \| `Danish` |

Creating a user by editing an empty pool object is **GUI**. There is no `Store User` form on the User Keyword Spec.

Opens the User Configuration menu:

```
Menu "UserConfiguration"
```

## Screen configurations

Screen configs belong to the **user profile** (not a global pool). Each user selects one; calling it on login. Call/store/assign via [`ScreenConfiguration`](keywords/Screenconfiguration.md):

Stores screen configuration **3** named **Average Joe**:

```
Store ScreenConfiguration 3 "Average Joe"
```

Calls screen configuration **2**:

```
ScreenConfiguration 2
```

Typical pattern: same User Profile, different Users with different ScreenConfig — shared programmer, different views (main vs backup / 3D onPC).

## Object ownership (multi-user)

While a user edits an object, others see a lock (full red / partial yellow). Same user on another station: yellow frame. Conflict pop-up (~10 s). List locks:

```
ListOwnership
```

Lists ownership related to macro **1**:

```
ListOwnership Macro 1
```

Requests the current owner to drop ownership of group **1**:

```
DropOwnership Group 1
```

Owner gets Drop / Keep (~10 s; timeout drops). Some automatic processes (e.g. Total Reference Update) hold ownership until finished — retry DropOwnership if needed.

## Related

- Session single vs multi / where commands run: [`multi-station.md`](multi-station.md), [`concepts/users.md`](concepts/users.md)
- Programmer: [`concepts/programmer.md`](concepts/programmer.md)
- Layout element locks mention ownership: [`layouts.md`](layouts.md)
