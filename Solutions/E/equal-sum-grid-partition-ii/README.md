# Equal sum grid partition ii

[Problem link](https://leetcode.com/problems/equal-sum-grid-partition-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/equal-sum-grid-partition-ii/

import numpy as np


class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        def work(grid):
            ctr1, ctr2, s1, s2 = Counter(), Counter(grid.flat), 0, grid.sum()
            m, n = grid.shape
            for i in range(m - 1):
                for x in grid[i]:
                    ctr1[x] += 1
                    ctr2[x] -= 1
                    s1 += x
                    s2 -= x

                diff = s1 - s2
                if not diff:
                    return True

                if n == 1:
                    if (
                        diff in [grid[0][0], grid[i][0]]
                        or -diff in [grid[i + 1][0], grid[-1][0]]
                    ):
                        return True
                else:
                    if i == 0:
                        if diff in [grid[0][0], grid[0][-1]]:
                            return True
                    else:
                        if ctr1[diff]:
                            return True
                    if i == m - 2:
                        if -diff in [grid[-1][0], grid[-1][-1]]:
                            return True
                    else:
                        if ctr2[-diff]:
                            return True

            return False

        return work(np.array(grid)) or work(np.array(grid).T)
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Matrix](/Collections/matrix.md#matrix) > [Subdivision](/Collections/matrix.md#subdivision)
