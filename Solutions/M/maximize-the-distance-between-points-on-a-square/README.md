# Maximize the distance between points on a square

[Problem link](https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

class Solution:
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        def key(xy):
            if xy[1] == 0:
                return xy[0]
            elif xy[0] == side:
                return side + xy[1]
            elif xy[1] == side:
                return 3 * side - xy[0]
            else:
                return 4 * side - xy[1]

        n, pos = len(points), sorted([key(p) for p in points])

        def work(x):
            for i in range(n):
                if pos[i] - pos[0] >= x:
                    break
                cur = i
                for j in range(1, k):
                    cur = bisect_left(pos, pos[cur] + x)
                    if cur == n or 4 * side + pos[i] - pos[cur] < x:
                        break
                else:
                    return True
            return False

        start, end = 1, side + 1
        while end - start > 1:
            mid = (start + end) // 2
            if work(mid):
                start = mid
            else:
                end = mid
        return start
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Geometry](/Collections/mathematics.md#geometry)
