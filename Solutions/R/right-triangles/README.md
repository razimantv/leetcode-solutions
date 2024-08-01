# Right triangles

[Problem link](https://leetcode.com/problems/right-triangles/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/right-triangles/

import numpy


class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt_x = [Counter(row) for row in grid]
        cnt_y = [Counter(col) for col in numpy.array(grid).T]
        return sum(
            (cnt_x[i][1] - 1) * (cnt_y[j][1] - 1)
            for i in range(m) for j in range(n) if grid[i][j]
        )
```
## Tags

* [Matrix](/Collections/matrix.md#matrix)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
