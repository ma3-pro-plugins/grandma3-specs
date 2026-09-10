# DMXRemote / Agenda Startup Event

When a DMXRemote (or Agenda startup event) is set up to run a startup macro, it will run in the following cases:

<!-- prettier-ignore -->
|Scenario|Behavior|
|---|---|
|Master Station Shutdown|Runs Macro on Non-Master (which becomes Idle Master after 4 seconds of failing to re-connect to Master: "Peer has performed an orderly shutdown")|
|Master Station Takes Over (same show file)|Runs Macro on Master ONLY|
|Master Station Quick Restart|Runs Macro on Master ONLY|
|Non-Master Station Restart|Runs Macro on Slave ONLY|
|Non-Master Station Joins a session|DOES NOT RUN|
|Show loaded|Runs on the station that loaded the show file.|
