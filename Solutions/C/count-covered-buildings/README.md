# Count covered buildings

[Problem link](https://leetcode.com/problems/count-covered-buildings/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/count-covered-buildings/

class Solution:
    def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
        xmin, xmax, ymin, ymax = {}, {}, {}, {}
        for x, y in buildings:
            if x not in ymin:
                ymin[x] = ymax[x] = y
            else:
                ymin[x] = min(y, ymin[x])
                ymax[x] = max(y, ymax[x])
            if y not in xmin:
                xmin[y] = xmax[y] = x
            else:
                xmin[y] = min(x, xmin[y])
                xmax[y] = max(x, xmax[y])

        return sum(
            1 for x, y in buildings
            if ymin[x] < y < ymax[x] and xmin[y] < x < xmax[y]
        )
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
