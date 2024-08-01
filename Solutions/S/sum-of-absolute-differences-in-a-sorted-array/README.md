# Sum of absolute differences in a sorted array

[Problem link](https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n, nums, tot = len(nums), sorted(nums), sum(nums)
        pref, ret = 0, [0] * n
        for i in range(n):
            ret[i] = (2*i-n) * nums[i] + tot - 2*pref
            pref += nums[i]
        return ret
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Array scanning](/Collections/array-scanning.md#array-scanning)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Basic](/Collections/mathematics.md#basic)
