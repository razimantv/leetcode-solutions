# Minimum cost path with edge reversals

[Problem link](https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u]. append((v, w))
            adj[v]. append((u, 2 * w))

        dist, djset = {0: 0}, SortedList([(0, 0)])
        while djset:
            d, u = djset.pop(0)
            for v, w in adj[u]:
                if v in dist and dist[v] > d + w:
                    djset.remove((dist[v], v))
                    dist.pop(v)
                if v not in dist:
                    dist[v] = d + w
                    djset.add((d + w, v))

        return dist.get(n - 1, -1)
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Dijkstra's algorithm](/Collections/graph-theory.md#dijkstra-s-algorithm)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Python SortedList](/Collections/priority-queue.md#python-sortedlist)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Key update using insert and remove](/Collections/priority-queue.md#key-update-using-insert-and-remove)
