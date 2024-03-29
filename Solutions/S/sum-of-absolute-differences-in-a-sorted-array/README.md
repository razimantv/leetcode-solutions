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

* [Prefix](/README.md#Prefix) > [Sum](/README.md#Prefix-Sum)
* [Array scanning](/README.md#Array_scanning)
* [Mathematics](/README.md#Mathematics) > [Basic](/README.md#Mathematics-Basic)
