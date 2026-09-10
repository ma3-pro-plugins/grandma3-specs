# Multi-Station & Sessions

## MA Session Management

- A station may join a session with a MAsterPriority.
- If the joining station's MasterPriority is higher then the existing Master's MAsterPriority, then the new joining station will become the master.
- The showfile is shared with all stations, any change in it, is continously synced to other stations by UDP.

grandMA3 can work with multiple stations connected to the same session.
There can always be only one Master station.
