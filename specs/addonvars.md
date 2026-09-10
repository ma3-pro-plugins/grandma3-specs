# AddonVars

AddonVariables are stored in the showfile (persistent storage), and are accesible from any station.

- Containers: We create a Container accessor using the function:
  `AddonVars(containerId: string): VariablesContainer`

## Performance and Limits

- I created 10,000 containers in 1 second
- I can create a single conteiner and:
    - Create 10,000 variables (name/value) in 18ms
    - Read these 10,000 variables in 10ms

## Accessors

- GetVar(variablesContainer, varName): string
- SetVar(variablesContainer, varName, value): void
- DeleteVar(variablesContainer, varName): void

## Limitations

- There is no way to iterate through the variables in the container.
- variable content string max length is 65535

## Containers

The Containers reside in the ShowData:

ShowData/ShowSettings/AddonVariables

In the object graph, the AddonVariables pool is the same node as:

- By numeric indices: `Root()[14][1][7]`
- By names from `Root()`: `Root().ShowData.ShowSettings/AddonVariables`
- By convenience from show data: `ShowData().ShowSettings/AddonVariables`

We can list them, or iterate through them.

## Hooks

You can register `HookObjectChange` on an AddonVars container handle (the value returned by `AddonVars(containerId)`). That hook fires when variables are **added** or **removed** from the container (for example via `SetVar` on a new key or `DeleteVar` / equivalent removal).

Hooks fired for **insertion** of variables do **not** receive the name of the added variable; you only get notified that the container’s variable set changed structurally, not which key was introduced.

You **cannot** hook a single variable by name to get notified only when **that variable’s value** changes. Updates to an existing key’s value through `SetVar` do not surface as a per-variable object change you can subscribe to; use container-level hooks for structural changes, or another strategy (for example a sentinel MA object) if you need to react to value updates.
