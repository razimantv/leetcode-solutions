# Widest vertical area between two points containing no points

[Problem link](https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        return max(x2-x1 for (x1, y1), (x2, y2) in pairwise(sorted(points)))
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
