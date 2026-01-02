# N repeated element in size 2n array

[Problem link](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i] in [nums[i - 1], nums[i - 2]]:
                return nums[i]
        return -1
```
## Tags

* [Unique/duplicate element finding with bizarro algorithms](/Collections/unique-duplicate-element-finding-with-bizarro-algorithms.md#unique-duplicate-element-finding-with-bizarro-algorithms)
