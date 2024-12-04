# Maximize the number of target nodes after connecting trees ii

[Problem link](https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> List[int]:
        def graph(edges):
            n = len(edges) + 1
            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u]. append(v)
                adj[v]. append(u)
            return n, adj
        n1, adj1 = graph(edges1)
        n2, adj2 = graph(edges2)

        def colouring(n, adj):
            ret, tot = [0] * n, [0, 0]

            def dfs(u, par, c):
                ret[u] = c
                tot[c] += 1
                for v in adj[u]:
                    if v != par:
                        dfs(v, u, c ^ 1)
            dfs(0, -1, 0)
            return ret, tot

        colours, ctot = colouring(n1, adj1)
        c2max = max(colouring(n2, adj2)[1])
        return [ctot[x] + c2max for x in colours]
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search) > [Colouring](/Collections/graph-theory.md#colouring)
