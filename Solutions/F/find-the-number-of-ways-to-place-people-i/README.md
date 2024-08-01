# Find the number of ways to place people i

[Problem link](https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n, points = len(points), sorted(points, key=lambda x: [x[0], -x[1]])
        ret = 0
        for i in range(n):
            y, worst = points[i][1], 10 ** 10
            for j in range(i - 1, -1, -1):
                yp = points[j][1]
                if y <= yp < worst:
                    ret += 1
                    worst = yp
        return ret
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
* [Points in 2D plane](/Collections/points-in-2d-plane.md#points-in-2d-plane)
