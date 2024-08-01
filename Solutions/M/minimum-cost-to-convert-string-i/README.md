# Minimum cost to convert string i

[Problem link](https://leetcode.com/problems/minimum-cost-to-convert-string-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-cost-to-convert-string-i/

class Solution:
    def minimumCost(
        self, source: str, target: str,
        original: List[str], changed: List[str], cost: List[int]
    ) -> int:
        dp = [[-1] * 26 for _ in range(26)]
        for i in range(26):
            dp[i][i] = 0
        for u, v, w in zip(original, changed, cost):
            u, v = ord(u) - ord('a'), ord(v) - ord('a')
            if dp[u][v] == -1 or dp[u][v] > w:
                dp[u][v] = w

        for i in range(26):
            for j in range(26):
                for k in range(26):
                    if dp[j][i] == -1 or dp[i][k] == -1:
                        continue
                    if dp[j][k] == -1 or dp[j][k] > dp[j][i] + dp[i][k]:
                        dp[j][k] = dp[j][i] + dp[i][k]

        tot = 0
        for u, v in zip(source, target):
            u, v = ord(u) - ord('a'), ord(v) - ord('a')
            if dp[u][v] == -1:
                return -1
            tot += dp[u][v]
        return tot
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Floyd-Warshall algorithm](/Collections/graph-theory.md#floyd-warshall-algorithm)
