---
source: lab
---

# Hardware Layout

Concept map (executors / playback handles): [`concepts/executors.md`](concepts/executors.md).

## Executors

Executors are laid out in 4 rows on the physical console (bottom to top):

| Range   | Row (from bottom) | Controls      |
| ------- | ----------------- | ------------- |
| 101–190 | 1st               | Key only      |
| 201–290 | 2nd               | Fader + key   |
| 301–390 | 3rd               | Encoder + key |
| 401–490 | 4th               | Encoder + key |

Within each row, executors are physically grouped in sets of 5 (e.g., 101–105, 106–110, 111–115). There is a physical gap between each group of 5. This grouping applies to all four rows.

This file is the **canonical** lab layout. The same table is shown on [`concepts/executors.md`](concepts/executors.md) so agents reading the manual TOC map see it without an extra hop — if the numbers change, update **this** Spec first, then sync the concept table.
