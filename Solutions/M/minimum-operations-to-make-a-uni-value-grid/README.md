# Minimum operations to make a uni value grid

[Problem link](https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        grid = sorted([v for row in grid for v in row])
        if any((b - a) % x for a, b in pairwise(grid)):
            return -1
        target = grid[len(grid) // 2]
        return sum(abs(v - target) for v in grid) // x
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Median](/Collections/mathematics.md#median)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
* [Sorting](/Collections/sorting.md#sorting)
