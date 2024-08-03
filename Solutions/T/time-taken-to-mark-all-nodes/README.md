# Time taken to mark all nodes

[Problem link](https://leetcode.com/problems/time-taken-to-mark-all-nodes/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/time-taken-to-mark-all-nodes/

class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        subtreetime = [0] * n

        def dfs(u, par):
            subtreetime[u] = 0
            for v in adj[u]:
                if v == par:
                    continue
                subtreetime[u] = max(subtreetime[u], dfs(v, u) + 2 - (v & 1))
            return subtreetime[u]
        dfs(0, -1)

        ret = [0] * n

        def dfs2(u, par, partime):
            ret[u] = max(subtreetime[u],  partime)
            children = [v for v in adj[u] if v != par]
            childtime = [subtreetime[child] + 2 -
                         (child & 1) for child in children]
            prefmax = [0] + list(accumulate(childtime, max))
            sufmax = list(accumulate(childtime[::-1], max))[::-1] + [0]
            for i, v in enumerate(children):
                newpartime = 2 - (u & 1) + max(
                    partime, prefmax[i], sufmax[i + 1]
                )
                dfs2(v, u, newpartime)
        dfs2(0, -1, 0)

        return ret
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Trees](/Collections/dynamic-programming.md#trees) > [DP over children](/Collections/dynamic-programming.md#dp-over-children)
* [Prefix](/Collections/prefix.md#prefix) > [Extremum](/Collections/prefix.md#extremum)
