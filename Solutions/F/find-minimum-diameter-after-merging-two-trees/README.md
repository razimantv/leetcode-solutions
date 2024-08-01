# Find minimum diameter after merging two trees

[Problem link](https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/

class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        def adj(edges):
            n = len(edges) + 1
            ret = [[] for _ in range(n)]
            for u, v in edges:
                ret[u].append(v)
                ret[v].append(u)
            return ret

        adj1, adj2 = adj(edges1), adj(edges2)

        def longest(u, par, adj):
            ret = [0, u]
            for v in adj[u]:
                if v != par:
                    lc = longest(v, u, adj)
                    if lc[0] >= ret[0]:
                        ret = [lc[0] + 1, lc[1]]
            return ret

        d1 = longest(longest(0, -1, adj1)[1], -1, adj1)[0]
        d2 = longest(longest(0, -1, adj2)[1], -1, adj2)[0]
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search) > [Tree diameter](/Collections/graph-theory.md#tree-diameter)
* [Greedy](/Collections/greedy.md#greedy)
