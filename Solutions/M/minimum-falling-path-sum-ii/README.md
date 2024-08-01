# Minimum falling path sum ii

[Problem link](https://leetcode.com/problems/minimum-falling-path-sum-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-falling-path-sum-ii/

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        for r1, r2 in pairwise(grid):
            a, b = min(r1[0], r1[1]), max(r1[0], r1[1])
            for x in r1[2:]:
                if x < a:
                    a, b = x, a
                elif x < b:
                    b = x
            for i in range(n):
                r2[i] += b if r1[i] == a else a
        return min(grid[-1])
```
## Tags

* [Matrix](/Collections/matrix.md#matrix) > [Path](/Collections/matrix.md#path)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
