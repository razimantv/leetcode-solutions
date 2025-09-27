# Largest triangle area

[Problem link](https://leetcode.com/problems/largest-triangle-area/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/largest-triangle-area/

def area(pts):
    drs = [[pts[i][j] - pts[0][j] for j in [0, 1]] for i in [1, 2]]
    return abs(drs[0][1] * drs[1][0] - drs[0][0] * drs[1][1]) / 2


class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        return max(area(pts) for pts in combinations(points, 3))
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Geometry](/Collections/mathematics.md#geometry)
