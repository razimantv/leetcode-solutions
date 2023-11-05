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

* [Graph theory](/README.md#Graph_theory) > [Degree counting](/README.md#Graph_theory-Degree_counting)
* [Graph theory](/README.md#Graph_theory) > [Directed acyclic graph](/README.md#Graph_theory-Directed_acyclic_graph)
