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

* [Graph theory](/README.md#Graph_theory) > [Directed acyclic graph](/README.md#Graph_theory-Directed_acyclic_graph)
* [Dynamic programming](/README.md#Dynamic_programming) > [Memoised recursion](/README.md#Dynamic_programming-Memoised_recursion)
