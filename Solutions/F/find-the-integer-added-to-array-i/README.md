# Find the integer added to array i

[Problem link](https://leetcode.com/problems/find-the-integer-added-to-array-i/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-integer-added-to-array-i/

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return min(nums2) - min(nums1)
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
