# Maximum profit from trading stocks with discounts

[Problem link](https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/

class Solution:
    def maxProfit(
        self, n: int, present: list[int], future: list[int],
        hierarchy: list[list[int]], budget: int
    ) -> int:
        adj = [[] for _ in range(n)]
        for u, v in hierarchy:
            adj[u - 1].append(v - 1)

        topo, i = [0], 0
        while i < len(topo):
            topo += adj[topo[i]]
            i += 1

        dp = [[[0] * (budget + 1) for _ in range(n)] for __ in (0, 1)]

        for u in topo[::-1]:
            notake, take = [0] * (budget + 1), [0] * (budget + 1)
            for v in adj[u]:
                for i in range(budget, -1, -1):
                    for j in range(i + 1):
                        notake[i] = max(notake[i], notake[i - j] + dp[0][v][j])
                        take[i] = max(take[i], take[i - j] + dp[1][v][j])
            for par in (0, 1):
                cur = present[u] // (2 if par else 1)
                for i in range(budget + 1):
                    dp[par][u][i] = notake[i]
                    if i >= cur:
                        dp[par][u][i] = max(
                            dp[par][u][i], take[i - cur] + future[u] - cur)
        return max(dp[0][0])
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Graph-like state transitions](/Collections/dynamic-programming.md#graph-like-state-transitions)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Topological sort](/Collections/graph-theory.md#topological-sort) > [Dynamic Programming](/Collections/graph-theory.md#dynamic-programming)
