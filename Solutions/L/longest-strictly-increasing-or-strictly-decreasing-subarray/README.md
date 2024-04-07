# Longest strictly increasing or strictly decreasing subarray

[Problem link](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n, ret = len(nums), 1
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] > nums[j - 1]:
                    ret = max(ret, j - i + 1)
                else: 
                    break
            for j in range(i + 1, n):
                if nums[j] < nums[j - 1]:
                    ret = max(ret, j - i + 1)
                else: 
                    break
        return ret
```
## Tags

* [Simple implementation](/README.md#Simple_implementation)
* [Suboptimal solution](/README.md#Suboptimal_solution)
