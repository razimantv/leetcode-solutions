# Maximum path score in a grid

[Problem link](https://leetcode.com/problems/maximum-path-score-in-a-grid/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-path-score-in-a-grid/

class Solution:
    def maxPathScore(self, grid: list[list[int]], k: int) -> int:
        n = len(grid[0])
        dp = [[-inf] * (k + 2) for _ in range(n + 1)]
        dp[0][0] = 0

        for row in grid:
            for i, x in enumerate(row):
                d, olddp = (x > 0), deepcopy(dp[i])
                for j in range(k + 1):
                    dp[i][j] = max(
                        dp[i][j - 1], dp[i - 1][j - d] + x, olddp[j - d] + x
                    )

        return -1 if dp[n - 1][k] < 0 else dp[n - 1][k]
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Matrix](/Collections/matrix.md#matrix) > [Path](/Collections/matrix.md#path)
