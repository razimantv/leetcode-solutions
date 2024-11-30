# Valid arrangement of pairs

[Problem link](https://leetcode.com/problems/valid-arrangement-of-pairs/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/valid-arrangement-of-pairs/

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        indeg, outdeg = [Counter() for _ in (0, 1)]
        for u, v in pairs:
            adj[u].append(v)
            indeg[v] += 1
            outdeg[u] += 1

        start = pairs[0][0]
        for u in outdeg:
            if outdeg[u] > indeg[u]:
                start = u
                break
        tour = []
        cur = [start]
        while cur:
            while adj[cur[-1]]:
                cur.append(adj[cur[-1]].pop())
            tour.append(cur.pop())
        return list(pairwise(tour[::-1]))
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Degree counting](/Collections/graph-theory.md#degree-counting)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Euler tour](/Collections/graph-theory.md#euler-tour)
