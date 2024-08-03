# Make two arrays equal by reversing subarrays

[Problem link](https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
