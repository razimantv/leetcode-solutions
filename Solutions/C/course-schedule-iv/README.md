# Course schedule iv

[Problem link](https://leetcode.com/problems/course-schedule-iv/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/course-schedule-iv/

class Solution:
    def checkIfPrerequisite(
        self, n: int, prerequisites: list[list[int]], queries: list[list[int]]
    ) -> list[bool]:
        adj = [set() for _ in range(n)]
        for u, v in prerequisites:
            adj[u].add(v)

        @cache
        def query(u, v):
            return (v in adj[u]) or any(query(w, v) for w in adj[u])

        return [query(u, v) for u, v in queries]
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Directed acyclic graph](/Collections/graph-theory.md#directed-acyclic-graph)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
