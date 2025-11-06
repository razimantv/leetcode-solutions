# Power grid maintenance

[Problem link](https://leetcode.com/problems/power-grid-maintenance/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/power-grid-maintenance/

class Solution:
    def processQueries(
        self, c: int, connections: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        par = list(range(c + 1))

        def parent(u):
            if u == par[u]:
                return u
            par[u] = parent(par[u])
            return par[u]

        for u, v in connections:
            pu, pv = parent(u), parent(v)
            if pu != pv:
                par[pu] = pv

        left = defaultdict(SortedList)
        for u in range(1, c + 1):
            left[parent(u)].add(u)

        ret = []
        for q, u in queries:
            pu = parent(u)
            if q == 1:
                if u in left[pu]:
                    ret.append(u)
                elif left[pu]:
                    ret.append(left[pu][0])
                else:
                    ret.append(-1)
            elif u in left[pu]:
                left[pu].remove(u)
        return ret
```
## Tags

* [Disjoint set union](/Collections/disjoint-set-union.md#disjoint-set-union)
