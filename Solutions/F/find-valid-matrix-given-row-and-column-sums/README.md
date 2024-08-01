# Find valid matrix given row and column sums

[Problem link](https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

from sortedcontainers import SortedList


class Solution:
    def restoreMatrix(
        self, row: List[int], column: List[int]
    ) -> List[List[int]]:
        row = SortedList([[x, i] for i, x in enumerate(row)])
        column = SortedList([[x, i] for i, x in enumerate(column)])
        grid = [[0] * len(column) for _ in row]
        while row and row[-1][0]:
            v1, r = row.pop(0)
            v2, c = column.pop(0)
            cur = min(v1, v2)
            grid[r][c] = cur
            if v1 > cur:
                row.add([v1 - cur, r])
            if v2 > cur:
                column.add([v2 - cur, c])
        return grid
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Priority queue](/Collections/priority-queue.md#priority-queue)
