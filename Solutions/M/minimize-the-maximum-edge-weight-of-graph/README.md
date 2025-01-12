# Minimize the maximum edge weight of graph

[Problem link](https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph

class Solution:
    def minMaxWeight(
        self, n: int, edges: List[List[int]], threshold: int
    ) -> int:
        adj, end = [[] for _ in range(n)], 0
        for u, v, w in edges:
            adj[v].append((u, w))
            end = max(end, w)
        seen = [-1] * n

        def dfs(u, lim):
            if seen[u] == lim:
                return 0
            seen[u], ret = lim, 1
            for v, w in adj[u]:
                if w <= lim:
                    ret += dfs(v, lim)
            return ret

        if dfs(0, end) < n:
            return -1

        start = -1
        while end - start > 1:
            mid = (start + end) // 2
            if dfs(0, mid) == n:
                end = mid
            else:
                start = mid
        return end
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Reuse visited array](/Collections/graph-theory.md#reuse-visited-array)
