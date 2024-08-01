# Minimum number of operations to make array continuous

[Problem link](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(list(set(nums)))
        ret = n
        l = 0
        for r in range(len(nums)):
            while nums[r]-nums[l] >= n:
                l += 1
            ret = min(ret, n+l-r-1)
        return ret
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
* [Sliding window](/Collections/sliding-window.md#sliding-window)
