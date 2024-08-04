# Shortest distance after road addition queries ii

[Problem link](https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        next = list(range(1, n))
        removed = [0] * n
        dist = n - 1
        for q, (u, v) in enumerate(queries):
            if removed[u] or removed[v]:
                queries[q] = dist
                continue

            while next[u] != v:
                dist -= 1
                removed[next[u]] = 1
                next[u] = next[next[u]]
            queries[q] = dist

        return queries
```
## Tags

* [Dynamic update of left and right neighbours](/Collections/dynamic-update-of-left-and-right-neighbours.md#dynamic-update-of-left-and-right-neighbours)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Directed acyclic graph](/Collections/graph-theory.md#directed-acyclic-graph)
