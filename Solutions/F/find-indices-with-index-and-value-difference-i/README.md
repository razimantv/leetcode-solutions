# Find indices with index and value difference i

[Problem link](https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

class Solution:
    def findIndices(self, nums: List[int], index: int, value: int) -> List[int]:
        n = len(nums)
        small, big = 0, 0
        for i in range(index, n):
            if nums[i-index] < nums[small]:
                small = i-index
            elif nums[i-index] > nums[big]:
                big = i-index

            if nums[i] - nums[small] >= value:
                return [small, i]
            elif nums[big] - nums[i] >= value:
                return [big, i]
        return [-1, -1]
```
## Tags

* [Two pointers](/Collections/two-pointers.md#two-pointers)
