# Number of ways to assign edge weights i

[Problem link](https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        n = len(edges) + 1
        seen, adj = [0] * n, [[] for _ in range(n)] 
        for u, v in edges: 
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)
            
        def maxd(u):
            seen[u] = 1
            return max((1 + maxd(v) for v in adj[u] if not seen[v]), default=0)

        return pow(2, maxd(0) - 1, 1000000007)
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
