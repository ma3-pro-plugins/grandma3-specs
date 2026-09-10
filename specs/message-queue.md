# Message queue (Lua)

Notes from a **multi-station playground** (`MQ Test`, plugin note `erez@mq_test@v1_0_0`) using grandMA3’s Lua message-queue API.

**Important:** despite the API name, this is **not** a durable message queue. Lab behavior matches a **named channel with at-most-one active waiter** — see [Delivery semantics](#delivery-semantics-not-a-real-queue).

## APIs involved

- **`OpenMessageQueue(name)`** — register interest in a named queue on this station. Call once per queue you plan to listen on in this plugin/listener setup.
- **`coroutine.yield({ queues = name })`** — block until the runtime delivers something on that queue (no wall-clock timeout in the usual pattern).
- **`coroutine.yield({ queues = { name1, name2, ... } })`** — same, but wait on **multiple** queues in one yield. Each name must already be opened with **`OpenMessageQueue`**. On resume, the yield result is a table keyed by queue name (e.g. `result[name1]`, `result[name2]`); only queues that received messages are populated.
- **`SendLuaMessage(targetIp, name, payloadTable)`** — send a message to another station’s queue **by MANet IP**. Returns **`true` on successful send**, including when **no coroutine is currently waiting** on that name (see delivery semantics below). **`true` does not mean the message was received or buffered.**
- **`CloseMessageQueue(name)`** — tear down when the listener ends.

**Naming inconsistency in MA typings:** `OpenMessageQueue` / `CloseMessageQueue` use “queue”, but `SendLuaMessage`’s second parameter is documented as **`channel name`** (`grandMA3_lua_functions 2.3.2.0.txt`). That mismatch aligns with observed behavior: a **signal channel**, not a persisted queue.

**Registration rules:**

- **Open before yield:** a plugin **cannot** `yield` on a queue name unless it has already called **`OpenMessageQueue`** for that name (same listener setup). Yielding on an unopened name does not register a waiter.
- **Shared queue names:** queue channels are keyed by **name**, not by plugin. **Multiple plugins** on the same station may each call **`OpenMessageQueue`** and **`yield`** on the **same** queue name; a message to that name can wake any registered listener.

Payloads are plain Lua tables suitable for MA’s routing; follow MA’s constraints on serializable content.

**Payload table keys must be strings.** If a payload table includes numeric keys (e.g. `{ 1 = "a", seq = 1 }`), grandMA3 logs a warning and **skips** those entries:

```text
Lua queue message: Warning! Only keys of type 'string' are supported. Provided key of type 'number'; Skipped
```

Use string keys only (e.g. `{ seq = 1, text = "hello" }`). Array-style `{ "a", "b" }` tables use numeric indices internally and are not valid payload shape for this API.

## Delivery semantics (not a real queue)

Messages are **not stored**. Delivery requires a coroutine to be **parked on `coroutine.yield({ queues = ... })`** at the moment the message arrives on the target station.

### No listener → message lost

If `SendLuaMessage` targets a name where **no coroutine is currently yielding**, the message is **discarded**. A listener that **`OpenMessageQueue`s and starts yielding later does not receive** messages sent while it was absent.

`SendLuaMessage` still returns **`true`** (send accepted / routed). grandMA3 also logs:

```text
SecureProtocolRemoteCall : Got lua message for MQ_TEST_A. But no one is waiting for it
```

The name in the log is the channel that was addressed. **Test use:** after shutting down a listener, send a probe message; this log line confirms the listening coroutine is no longer registered.

### Gap between yields → message lost

Even when a listener **is** running, each `yield` handles **at most one** wakeup. After a message resumes the coroutine, there is a window **until the coroutine yields again** (typically at the bottom of a loop, after handling the payload) where **no one is waiting**. Messages sent in that window are **lost** the same way as with no listener.

Typical listener shape:

```lua
OpenMessageQueue("MQ_TEST")
while running do
    local result = coroutine.yield({ queues = "MQ_TEST" })
    -- handle result["MQ_TEST"] here — NOT safe to send more until yield below
end
```

Any traffic to `MQ_TEST` while the coroutine is executing handler code (between resume and the next `yield`) has no active waiter.

### Implication for reliable messaging

Because delivery is **best-effort** and **unbuffered**, product code cannot treat this API as a queue. For **reliable** inter-station messaging, build an **ack + retry** layer on top:

- Assign **monotonic sequential message IDs** (`seq`) in the payload.
- Receiver sends an **ack** (same channel or a paired reply channel) after handling each `seq`.
- Sender **retries** unacked messages until acked or a timeout/policy limit.

Without that, silent loss is expected — including when `SendLuaMessage` returns `true`.

## What we proved (lab)

- **Two-seat onPC session** (e.g. `10.0.0.1` master, `10.0.0.2` non-master): **bidirectional** traffic on a shared channel name (e.g. `MQ_TEST`) with logs on both sides showing **`SendLuaMessage` returned true** and **receive** with expected fields (`from`, `seq`, `text`) when a listener was actively yielding.
- **Multi-queue listener (same coroutine):** `OpenMessageQueue` for each channel, then **`coroutine.yield({ queues = { "MQ_TEST_A", "MQ_TEST_B" } })`** wakes when either queue has traffic; the resume value names which queue(s) delivered messages (lab: `MQ Test Receiver`, plugin note `erez@mq_test_receiver@v1_0_0`).
- **Multi-station Lua source**: `ComponentLua` **`Installed="No"`** so component Lua is **embedded in the show** after import. **`Installed="Yes"`** loads `.lua` from each machine’s `gma3_library`; a station without that file opens no queue → **“But no one is waiting for it”** and the message is lost (see [Delivery semantics](#delivery-semantics-not-a-real-queue)).
- **Automation**: drive **OSC only to the master**; run commands on another seat with **`RemoteCommand IP <ip> "<cmd>"`**. Direct OSC to a non-master station is unreliable. After actions, `DumpLog` on the station whose log you need. Import pattern: `Import Plugin Library "FileName.xml" At Plugin "" /o` (see [`osc.md`](osc.md)).
- **Deferring the listener**: starting **`OpenMessageQueue` + the `yield` loop inside `Timer(..., 0, 1)`** (or a small positive delay) runs the blocking logic on a **timer coroutine**, not on the **`Call Plugin` / component entry** stack. This avoids tying the long wait to the same thread as the immediate plugin invocation.

## Plugin object UX (why we avoid blocking MQ in product)

When the message-queue **`yield` runs on the same context as the plugin’s “active” invocation** (e.g. blocking directly inside `Call Plugin` without deferral), grandMA3 shows the **plugin object active-bar** (“busy” / working indication) for as long as the coroutine is parked on the queue.

That behavior is poor UX for a shipping plugin: the bar reads as “the plugin is doing work,” **masks** other legitimate busy states, and makes the active-bar harder to trust.

Until there is a pattern that preserves acceptable UX (or MA changes how the bar is driven), avoid blocking message-queue listeners on the `Call Plugin` stack in product plugins.

## References

- Help Dump: [`lua-functions/grandMA3_lua_functions 2.5.0.3.txt`](lua-functions/grandMA3_lua_functions%202.5.0.3.txt) (`OpenMessageQueue`, `CloseMessageQueue`, `SendLuaMessage` — note queue vs channel naming).
- [`remote-command.md`](remote-command.md) and [`osc.md`](osc.md).
