# Maximize area of square hole in grid

[Problem link](https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def hole(ar):
            best, cur, prev = 1, 1, -2
            for x in ar:
                if x == prev + 1:
                    cur += 1
                else:
                    cur = 2
                best = max(best, cur)
                prev = x
            return best

        return min(hole(sorted(hBars)), hole(sorted(vBars))) ** 2
```
## Tags

* [Sorting](/README.md#Sorting)
* [Array scanning](/README.md#Array_scanning) > [Contiguous region](/README.md#Array_scanning-Contiguous_region)
