# Find if array can be sorted

[Problem link](https://leetcode.com/problems/find-if-array-can-be-sorted/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-if-array-can-be-sorted/

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        l, r = 0, 0
        while r < n:
            while r < n and nums[l].bit_count() == nums[r].bit_count():
                r += 1
            nums[l:r] = sorted(nums[l:r])
            if l and nums[l] < nums[l-1]:
                return False
            l = r
        return True
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
