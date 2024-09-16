# Minimum time difference

[Problem link](https://leetcode.com/problems/minimum-time-difference/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, time: List[str]) -> int:
        time = sorted(list(map(lambda x: int(x[:2]) * 60 + int(x[3:]), time)))
        return min(y-x for x, y in pairwise(time + [time[0] + 1440]))
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Cyclic array](/Collections/array-scanning.md#cyclic-array)
