# Minimum cost path with teleportations

[Problem link](https://leetcode.com/problems/minimum-cost-path-with-teleportations)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-cost-path-with-teleportations

class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp, group = [[inf] * n for _ in grid], defaultdict(list)
        dp[-1][-1] = 0

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                group[x].append((i, j))
        values = sorted(list(group.keys()))

        def update():
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if (i, j) == (m - 1, n - 1):
                        continue
                    if i == m - 1:
                        dp[i][j] = min(dp[i][j], grid[i][j + 1] + dp[i][j + 1])
                    elif j == n - 1:
                        dp[i][j] = min(dp[i][j], grid[i + 1][j] + dp[i + 1][j])
                    else:
                        dp[i][j] = min(
                            dp[i][j], grid[i][j + 1] + dp[i][j + 1],
                            grid[i + 1][j] + dp[i + 1][j]
                        )

        update()
        for x in range(k):
            cur = inf
            for value in values:
                coords = group[value]
                cur = min(cur, min(dp[i][j] for i, j in coords))
                for i, j in coords:
                    dp[i][j] = min(dp[i][j], cur)
            update()

        return dp[0][0]
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Graph-like state transitions](/Collections/dynamic-programming.md#graph-like-state-transitions)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Group items](/Collections/hashmap.md#group-items)
