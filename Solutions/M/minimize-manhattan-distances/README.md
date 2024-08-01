# Minimize manhattan distances

[Problem link](https://leetcode.com/problems/minimize-manhattan-distances/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimize-manhattan-distances/

class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        a = sorted([(x + y, i) for i, (x, y) in enumerate(points)])
        s = sorted([(x - y, i) for i, (x, y) in enumerate(points)])
        ret = inf
        for idx in [a[0][1], a[-1][1], s[0][1], s[-1][1]]:
            cur = 0
            for ar in [a, s]:
                l, r = 0, -1
                if ar[l][1] == idx:
                    l += 1
                if ar[r][1] == idx:
                    r -= 1
                cur = max(cur, ar[r][0] - ar[l][0])
            ret = min(ret, cur)
        return ret
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Geometry](/Collections/mathematics.md#geometry)
