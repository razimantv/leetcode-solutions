# Minimum absolute difference in sliding submatrix

[Problem link](https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        return [
            [
                min(
                    (
                        y - x for x, y in pairwise(sorted(set(
                            grid[ii][jj] for ii in range(i, i + k)
                            for jj in range(j, j + k)
                        )))
                    ),
                    default=0
                )
                for j in range(n - k + 1)
            ]
            for i in range(m - k + 1)
        ]
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
