# Maximum difference score in a grid

[Problem link](https://leetcode.com/problems/maximum-difference-score-in-a-grid/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-difference-score-in-a-grid/

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n, ret = len(grid), len(grid[0]), -math.inf
        for i in range(m):
            for j in range(n):
                cur = min(grid[i-1][j] if i else math.inf,
                          grid[i][j-1] if j else math.inf)
                ret = max(ret, grid[i][j] - cur)
                grid[i][j] = min(grid[i][j], cur)
        return ret
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Grid](/Collections/dynamic-programming.md#grid)
* [Matrix](/Collections/matrix.md#matrix) > [Prefix](/Collections/matrix.md#prefix)
* [Prefix](/Collections/prefix.md#prefix) > [Extremum](/Collections/prefix.md#extremum) > [2D](/Collections/prefix.md#2d)
