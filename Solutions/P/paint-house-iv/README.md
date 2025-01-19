# Paint house iv

[Problem link](https://leetcode.com/problems/paint-house-iv/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/paint-house-iv/

class Solution:
    def minCost(self, n: int, cost: list[list[int]]) -> int:
        good = [(i, j) for i in range(3) for j in range(3) if i != j]
        m = len(good)
        pairs = [
            (i, j) for i in range(m) for j in range(m)
            if good[i][0] != good[j][0] and good[i][1] != good[j][1]
        ]

        dp = [0] * m
        for i in range(n // 2):
            newdp = [math.inf] * m
            for u, v in pairs:
                a, b = good[v]
                newdp[v] = min(
                    newdp[v], dp[u] + cost[i][a] + cost[n - 1 - i][b]
                )
            dp = newdp
        return min(dp)
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Graph-like state transitions](/Collections/dynamic-programming.md#graph-like-state-transitions)
