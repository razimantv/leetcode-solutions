# Find champion i

[Problem link](https://leetcode.com/problems/find-champion-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-champion-i/

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i, row in enumerate(grid):
            if sum(row) == n-1:
                return i
        return -1
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Degree counting](/Collections/graph-theory.md#degree-counting)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Directed acyclic graph](/Collections/graph-theory.md#directed-acyclic-graph)
