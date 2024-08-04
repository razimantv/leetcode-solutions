# Shortest distance after road addition queries i

[Problem link](https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        dist = list(range(n))
        parents = [[]] + [[i] for i in range(n - 1)]
        for q, (u, v) in enumerate(queries):
            dist[v] = min(dist[v], dist[u] + 1)
            parents[v].append(u)
            for i in range(v + 1, n):
                for j in parents[i]:
                    dist[i] = min(dist[i], dist[j] + 1)
            queries[q] = dist[-1]
        return queries
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Directed acyclic graph](/Collections/graph-theory.md#directed-acyclic-graph)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Graph-like state transitions](/Collections/dynamic-programming.md#graph-like-state-transitions)
