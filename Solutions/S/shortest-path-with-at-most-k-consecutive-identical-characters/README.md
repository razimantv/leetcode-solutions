# Shortest path with at most k consecutive identical characters

[Problem link](https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/


class Solution:
    def shortestPath(
        self, n: int, edges: list[list[int]], labels: str, k: int
    ) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        dist = {(0, 1): 0}
        todo = SortedList([(0, 0, 1)])

        ret = inf
        while len(todo):
            d, u, c = todo.pop(0)
            if u == n - 1:
                ret = min(ret, d)
            for v, w in adj[u]:
                dv = d + w
                cv = 1 if labels[u] != labels[v] else (c + 1)
                if cv > k:
                    continue
                if (v, cv) in dist:
                    if (dvold := dist[(v, cv)]) <= dv:
                        continue
                    todo.remove((dvold, v, cv))
                dist[(v, cv)] = dv
                todo.add((dv, v, cv))
        return -1 if ret == inf else ret
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Dijkstra's algorithm](/Collections/graph-theory.md#dijkstra-s-algorithm)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Key update using insert and remove](/Collections/priority-queue.md#key-update-using-insert-and-remove)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Python SortedList](/Collections/priority-queue.md#python-sortedlist)
