# Minimum average of smallest and largest elements

[Problem link](https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        return min((x + y) / 2 for x, y in zip(nums, nums[::-1]))
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
