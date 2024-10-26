# Find subtree sizes after changes

[Problem link](https://leetcode.com/problems/find-subtree-sizes-after-changes/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-subtree-sizes-after-changes/

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i, p in enumerate(parent[1:]):
            adj[p].append(i + 1)

        last = defaultdict(list)

        def dfs(u):
            if last[s[u]]:
                parent[u] = last[s[u]][-1]

            last[s[u]].append(u)
            for v in adj[u]:
                dfs(v)
            last[s[u]].pop()
        dfs(0)

        adj = [[] for _ in range(n)]
        for i, p in enumerate(parent[1:]):
            adj[p].append(i + 1)

        ret = [0] * n

        def dfs2(u):
            ret[u] = 1
            for v in adj[u]:
                ret[u] += dfs2(v)
            return ret[u]
        dfs2(0)

        return ret
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
* [Backtracking](/Collections/backtracking.md#backtracking) > [Push and pop for efficient state update](/Collections/backtracking.md#push-and-pop-for-efficient-state-update)
* [Hashmap](/Collections/hashmap.md#hashmap)
