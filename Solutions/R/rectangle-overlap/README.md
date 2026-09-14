# Rectangle overlap

[Problem link](https://leetcode.com/problems/rectangle-overlap/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/rectangle-overlap/

class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        return all(
            min(rec1[i + 2], rec2[i + 2]) > max(rec1[i], rec2[i])
            for i in (0, 1)
        )
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Geometry](/Collections/mathematics.md#geometry)
