# Maximum value of an ordered triplet i

[Problem link](https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        large, small = max(nums[0], nums[1]), min(nums[0], nums[1])
        largediff, smalldiff = nums[0]-nums[1], nums[0]-nums[1]
        best = 0
        for x in nums[2:]:
            best = max([best, x*largediff, x*smalldiff])
            largediff = max(largediff, large-x)
            smalldiff = min(smalldiff, small-x)
            large = max(large, x)
            small = min(small, x)
        return best
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning)
