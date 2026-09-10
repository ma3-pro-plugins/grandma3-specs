# Remote command

- A station can run a command on a remote station by IP.
- A station can use `RemoteCommand` to call a Plugin on a remote station, along with a single string argument.
- The command string relayed by `RemoteCommand` is subject to the same **~16K total length limit** as local `Cmd()` / `Call Plugin` — see [Command string length limit (~16K)](plugins.md#command-string-length-limit-16k) in [`plugins.md`](plugins.md).

For general `Call Plugin` string-arg quoting rules (double vs single quotes, receiver decode rules), see [String argument quoting (JSON and escaped content)](plugins.md#string-argument-quoting-json-and-escaped-content) in [`plugins.md`](plugins.md).

## JSON payloads over RemoteCommand

Empirical testing with playground plugins **JSON Sender** / **JSON Receiver** (MA 2.3.2) confirms that **`RemoteCommand` relays single-quote-wrapped JSON the same way as local `Cmd()`**.

| Path                | Wrapper around plugin arg | JSON in arg | Result                                       |
| ------------------- | ------------------------- | ----------- | -------------------------------------------- |
| Local `Cmd()`       | Double quotes `"..."`     | Yes         | **Fails at command parse** — `Illegal name:` |
| Local `Cmd()`       | Single quotes `'...'`     | Yes         | **Works** — full `json.decode` on arg 2      |
| **`RemoteCommand`** | Single quotes `'...'`     | Yes         | **Works** — full `json.decode` on arg 2      |

**Test setup:** sender on **10.0.0.1** calls `RemoteCommand('10.0.0.2', command)`; receiver plugin runs on **10.0.0.2**. Command shape:

```text
Call Plugin "JSON Receiver" '{"caseId":"quotes","payload":{"msg":"He said \"hello\""},...}'
```

**Confirmed roundtrips over `RemoteCommand` (all 8 test cases, arg on arg 2):**

- embedded double quotes in string values (`\"` in JSON)
- backslashes in string values (`\\` in JSON, e.g. `C:\Users\test`)
- nested objects, arrays, spaces, empty strings, and mixed payloads

Backslashes in JSON escape sequences are **preserved** across the relay when the receiver decodes the **raw** arg (do not strip `\` before `json.decode`).

**Apostrophe edge case (same as local):** single-quote wrapping breaks when a JSON string value contains a literal `'`, because it terminates the outer command argument:

```text
RemoteCommand(ip, 'Call Plugin "JSON Receiver" \'{"msg":"it\'s fine"}\'')
```

For payloads that may contain apostrophes, escape `'` in the command-layer wrapper or use a non-JSON wire format (e.g. pipe-delimited prefix such as `__cprpc__|...`).

**Practical rule:** for JSON-over-`Call Plugin` on both local and remote paths, use **`json.encode`** on the sender, wrap the result in **single quotes** in the command string, and **`json.decode` the raw arg** on the receiver.
