# Check if the rectangle corner is reachable

[Problem link](https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/

class Solution:
    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
        n = len(circles) + 4
        par = list(range(n))

        def parent(u):
            if par[u] != u:
                par[u] = parent(par[u])
            return par[u]

        par[:2] = [3, 1]
        for i, (x, y, r) in enumerate(circles):
            for j, cond in enumerate([x <= r, y <= r, x + r >= X, y + r >= Y]):
                if cond:
                    par[parent(i + 4)] = parent(j)
            for j in range(i):
                xp, yp, rp = circles[j]
                if (x - xp) ** 2 + (y - yp) ** 2 <= (r + rp) ** 2:
                    par[parent(i + 4)] = parent(j + 4)

        return parent(0) != parent(1)
```
## Tags

* [Disjoint set union](/Collections/disjoint-set-union.md#disjoint-set-union)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Geometry](/Collections/mathematics.md#geometry)
