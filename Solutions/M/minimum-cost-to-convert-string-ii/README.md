# Minimum cost to convert string ii

[Problem link](https://leetcode.com/problems/minimum-cost-to-convert-string-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

class Solution:
    def minimumCost(
        self, source: str, target: str,
        original: List[str], changed: List[str], cost: List[int]
    ) -> int:
        stov, perl = {}, defaultdict(list)
        for sl in [original, changed]:
            for s in sl:
                if s not in stov:
                    cur = len(stov)
                    stov[s] = cur
                    perl[len(s)].append(cur)

        n = len(stov)
        dp = [[-1] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        for u, v, w in zip(original, changed, cost):
            u, v = stov[u], stov[v]
            if dp[u][v] == -1 or dp[u][v] > w:
                dp[u][v] = w

        for i in range(n):
            for j in range(n):
                if dp[j][i] == -1:
                    continue
                for k in range(n):
                    if dp[i][k] == -1:
                        continue
                    if dp[j][k] == -1 or dp[j][k] > dp[j][i] + dp[i][k]:
                        dp[j][k] = dp[j][i] + dp[i][k]

        perl = sorted(list(perl))
        m, lm = len(source), max(perl)
        dp2 = [-1] * (m + 1)
        dp2[-1] = 0
        for i in range(m-1, -1, -1):
            curl = min(lm, m-i)
            if source[i] == target[i]:
                dp2[i] = dp2[i+1]
            for l in perl:
                if l > curl:
                    break
                if dp2[i + l] == -1:
                    continue
                h1 = stov.get(source[i:i+l], -1)
                h2 = stov.get(target[i:i+l], -1)
                if h1 == -1 or h2 == -1 or dp[h1][h2] == -1:
                    continue
                newdist = dp2[i+l] + dp[h1][h2]
                if dp2[i] == -1 or dp2[i] > newdist:
                    dp2[i] = newdist

        return dp2[0]
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Floyd-Warshall algorithm](/Collections/graph-theory.md#floyd-warshall-algorithm)
* [Hashmap](/Collections/hashmap.md#hashmap)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
