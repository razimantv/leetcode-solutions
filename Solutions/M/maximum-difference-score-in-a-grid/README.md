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

* [Dynamic programming](/README.md#Dynamic_programming) > [Array reuse](/README.md#Dynamic_programming-Array_reuse)
* [Dynamic programming](/README.md#Dynamic_programming) > [Grid](/README.md#Dynamic_programming-Grid)
* [Matrix](/README.md#Matrix) > [Prefix](/README.md#Matrix-Prefix)
* [Prefix](/README.md#Prefix) > [Extremum](/README.md#Prefix-Extremum) > [2D](/README.md#Prefix-Extremum-2D)
