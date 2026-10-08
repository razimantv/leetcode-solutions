# Minimum cost to reach city with discounts

[Problem link](https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/


class Solution:
    def minimumCost(
        self, n: int, highways: list[list[int]], discounts: int
    ) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in highways:
            adj[u].append((v, w))
            adj[v].append((u, w))

        def work(dist):
            todo = SortedList([(x, i) for i, x in enumerate(dist) if x < inf])
            while todo:
                x, u = todo.pop(0)
                for v, w in adj[u]:
                    if x + w < dist[v]:
                        if dist[v] < inf:
                            todo.remove((dist[v], v))
                        dist[v] = x + w
                        todo.add((dist[v], v))

        dist = [0] + [inf] * (n - 1)
        work(dist)
        for i in range(discounts):
            temp = copy.deepcopy(dist)
            for u in range(n):
                for v, w in adj[u]:
                    dist[v] = min(dist[v], temp[u] + w // 2)
            work(dist)
        return -1 if dist[-1] == inf else dist[-1]
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Dijkstra's algorithm](/Collections/graph-theory.md#dijkstra-s-algorithm)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Dijkstra's algorithm](/Collections/priority-queue.md#dijkstra-s-algorithm)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Python SortedList](/Collections/priority-queue.md#python-sortedlist)
