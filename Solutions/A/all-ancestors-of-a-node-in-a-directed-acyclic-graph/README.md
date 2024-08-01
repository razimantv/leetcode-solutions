# All ancestors of a node in a directed acyclic graph

[Problem link](https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = [set() for _ in range(n)]
        for u, v in edges:
            ancestors[v].add(u)

        processed = [False] * n

        def get(u):
            if processed[u]:
                return ancestors[u]
            todo = list(ancestors[u])
            for v in todo:
                ancestors[u] |= get(v)
            processed[u] = True
            return ancestors[u]

        return [sorted(list(get(u))) for u in range(n)]
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Directed acyclic graph](/Collections/graph-theory.md#directed-acyclic-graph)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
