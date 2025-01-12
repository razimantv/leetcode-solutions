# Maximum amount of money robot can earn

[Problem link](https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn

class Solution:
    def maximumAmount(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[-math.inf] * 3 for j in range(n)] for i in range(m)]
        dp[0][0] = [grid[0][0], 0, 0]
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    for di, dj, dk in [
                            (-1, 0, 0), (0, -1, 0), (0, 0, -1),
                            (-1, 0, -1), (0, -1, -1)
                    ]:
                        ii, jj, kk, add = (
                            i + di, j + dj, k + dk, (1 + dk) * grid[i][j]
                        )
                        if min(ii, jj, kk) >= 0:
                            dp[i][j][k] = max(
                                dp[i][j][k], dp[ii][jj][kk] + add
                            )
        return dp[-1][-1][-1]
```
## Tags

* [Matrix](/Collections/matrix.md#matrix) > [Path](/Collections/matrix.md#path)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Grid](/Collections/dynamic-programming.md#grid)
