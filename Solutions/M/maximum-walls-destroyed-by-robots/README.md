# Maximum walls destroyed by robots

[Problem link](https://leetcode.com/problems/maximum-walls-destroyed-by-robots/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

class Solution:
    def maxWalls(
        self, robots: list[int], distance: list[int], walls: list[int]
    ) -> int:
        rd = sorted(list(zip(robots, distance)))
        walls = sorted(walls)

        def work(x, y):
            return bisect_right(walls, y) - bisect_left(walls, x)

        n = len(robots)
        dp1, dp2 = 0, 0
        for i, (r, d) in enumerate(rd):
            left1 = r - d if i == 0 else max(r - d, rd[i - 1][0] + 1)
            left2 = r - d if i == 0 else max(r - d, min(sum(rd[i - 1]) + 1, r))
            right = r + d if i == n - 1 else min(r + d, rd[i + 1][0] - 1)
            newdp1 = max(dp1 + work(left1, r), dp2 + work(left2, r))
            newdp2 = max(dp1, dp2) + work(r, right)
            dp1, dp2 = newdp1, newdp2

        return max(dp1, dp2)
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Binary search](/Collections/binary-search.md#binary-search)
