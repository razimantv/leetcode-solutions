# Minimum time visiting all points

[Problem link](https://leetcode.com/problems/minimum-time-visiting-all-points/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(
            max(abs(x2 - x1), abs(y2 - y1))
            for (x1, y1), (x2, y2) in pairwise(points)
        )
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
