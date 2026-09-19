# Circle and rectangle overlapping

[Problem link](https://leetcode.com/problems/circle-and-rectangle-overlapping/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/circle-and-rectangle-overlapping/

class Solution:
    def checkOverlap(
        self, r: int, x: int, y: int, x1: int, y1: int, x2: int, y2: int
    ) -> bool:
        if x1 <= x <= x2 and y1 <= y <= y2:
            return True

        def distsq(x1, y1, x2, y2):
            return (x1 - x2) ** 2 + (y1 - y2) ** 2

        # overlap between (x0, y=a to b) and (x, y, r)
        def overlap(x0, a, b, x, y, r):
            coords = [a, b]
            if (a - y) * (b - y) < 0:
                coords.append(y)
            return any(distsq(x0, c, x, y) <= r ** 2 for c in coords)

        return (
            overlap(x1, y1, y2, x, y, r) or overlap(x2, y1, y2, x, y, r) or
            overlap(y1, x1, x2, y, x, r) or overlap(y2, x1, x2, y, x, r)
        )
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Geometry](/Collections/mathematics.md#geometry)
