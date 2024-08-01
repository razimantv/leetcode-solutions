# Parallel courses iii

[Problem link](https://leetcode.com/problems/parallel-courses-iii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/parallel-courses-iii/

from sortedcontainers import SortedList


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        degree = [0] * n
        adj = [[] for _ in range(n)]
        for u, v in relations:
            degree[v-1] += 1
            adj[u-1]. append(v-1)

        start = [0] * n
        todo = SortedList()
        for i, d in enumerate(degree):
            if not d:
                todo.add((0, i))

        ret = 0
        while todo:
            t, u = todo.pop()
            t += time[u]
            ret = max(ret, t)
            for v in adj[u]:
                start[v] = max(start[v], t)
                degree[v] -= 1
                if not degree[v]:
                    todo.add((start[v], v))
        return ret
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Topological sort](/Collections/graph-theory.md#topological-sort) > [Dynamic Programming](/Collections/graph-theory.md#dynamic-programming)
* [Priority queue](/Collections/priority-queue.md#priority-queue)
