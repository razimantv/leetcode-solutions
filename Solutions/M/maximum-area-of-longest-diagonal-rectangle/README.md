# Maximum area of longest diagonal rectangle

[Problem link](https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        return max((x ** 2 + y ** 2, x * y) for x, y in dimensions)[1]
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Geometry](/Collections/mathematics.md#geometry)
