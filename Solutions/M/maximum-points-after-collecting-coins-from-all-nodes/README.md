# Maximum points after collecting coins from all nodes

[Problem link](https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        Q = 14
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u]. append(v)
            adj[v]. append(u)

        def dp(u, par):
            ret = [0] * Q
            children = [0] * (Q + 1)
            for v in adj[u]:
                if v != par:
                    child = dp(v, u)
                    for i in range(Q):
                        if not child[i]:
                            break
                        children[i] += child[i]
            x = coins[u]
            for i in range(Q):
                ret[i] = max(x-k+children[i], x//2 + children[i+1])
                if not ret[i]:
                    break
                x //= 2
            return ret

        return dp(0, -1)[0]
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Trees](/Collections/dynamic-programming.md#trees)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
