# Maximum distance in arrays

[Problem link](https://leetcode.com/problems/maximum-distance-in-arrays/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        small = sorted([(a[0], i) for i, a in enumerate(arrays)])[:2]
        big = sorted([(a[-1], i) for i, a in enumerate(arrays)])[-2:]
        return max(y-x for y, i in big for x, j in small if i != j)
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Suboptimal solution](/Collections/suboptimal-solution.md#suboptimal-solution)
