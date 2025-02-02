# Check if array is sorted and rotated

[Problem link](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution:
    def check(self, nums: list[int]) -> bool:
        n, bad = len(nums), -1
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                if bad != -1:
                    return False
                bad = i
        return bad == -1 or nums[-1] <= nums[0]
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Cyclic array](/Collections/array-scanning.md#cyclic-array)
