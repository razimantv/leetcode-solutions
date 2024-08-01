# Restore the array from adjacent pairs

[Problem link](https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

class Solution:
    def restoreArray(self, pairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in pairs:
            adj[u].append(v)
            adj[v].append(u)

        for u, var in adj.items():
            if len(var) == 1:
                v = var[0]
                ret = [u, v]
                break

        while len(adj[v]) == 2:
            par, u = u, v
            v1, v2 = adj[u]
            v = v2 if par == v1 else v1
            ret.append(v)

        return ret
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Degree counting](/Collections/graph-theory.md#degree-counting)
