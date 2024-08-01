# Count visited nodes in a directed graph

[Problem link](https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        seen = [-1] * n
        ret = [-1] * n
        for i in range(n):
            if seen[i] != -1:
                continue
            cur = []
            u = i
            while seen[u] == -1:
                cur.append(u)
                seen[u] = i
                u = edges[u]

            if seen[u] == i:
                cycle = [u]
                while True:
                    u = cur.pop()
                    if u == cycle[0]:
                        break
                    cycle.append(u)
                L = len(cycle)
                for u in cycle:
                    ret[u] = L
            else:
                L = ret[u]

            while cur:
                L += 1
                u = cur.pop()
                ret[u] = L

        return ret
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Single outdegree graphs](/Collections/graph-theory.md#single-outdegree-graphs)
