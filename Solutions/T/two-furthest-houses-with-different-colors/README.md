# Two furthest houses with different colors

[Problem link](https://leetcode.com/problems/two-furthest-houses-with-different-colors/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)
        for i, x in enumerate(colors):
            if x != colors[-1]:
                ret = n - 1 - i
                break
        for i, x in enumerate(colors[::-1]):
            if x != colors[0]:
                ret = max(ret, n - 1 - i)
                break
        return ret
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [From both ends of array](/Collections/array-scanning.md#from-both-ends-of-array)
