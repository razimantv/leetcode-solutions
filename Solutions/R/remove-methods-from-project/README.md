# Remove methods from project

[Problem link](https://leetcode.com/problems/remove-methods-from-project/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/remove-methods-from-project/

class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
        seen = [0] * n

        def dfs(u):
            seen[u] = 1
            for v in adj[u]:
                if not seen[v]:
                    dfs(v)

        dfs(k)
        ret = []
        for u in range(n):
            if seen[u]:
                continue
            ret.append(u)
            for v in adj[u]:
                if seen[v]:
                    return list(range(n))
        return ret
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
