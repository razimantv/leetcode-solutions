# Number of ways to split array

[Problem link](https://leetcode.com/problems/number-of-ways-to-split-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/number-of-ways-to-split-array/

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        psum = list(accumulate(nums))
        return sum(1 for x in psum[:-1] if 2 * x >= psum[-1])
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
