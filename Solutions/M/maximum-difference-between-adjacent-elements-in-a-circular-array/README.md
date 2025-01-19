# Maximum difference between adjacent elements in a circular array

[Problem link](https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(abs(y - x) for x, y in pairwise(nums + [nums[0]]))
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
