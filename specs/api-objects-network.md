# API Objects: Network / Session

## MAnetSocket

An object with path: Root()["MAnetSocket"]
has a property STATUS which tells the network status of the current station:
Values: 'IdleMaster' | 'GlobalMaster' | 'Connected' | 'Standalone'

## HostTypes

These 2 objects have children which are of type NetworkStation:
Root/MAnetSocket/HostTypes/onPC
Root/MAnetSocket/HostTypes/Console

A NetworkStation hase properties:

- IP
- SESSION - Session name
- STATUS
