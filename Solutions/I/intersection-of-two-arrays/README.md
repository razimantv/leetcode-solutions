# Intersection of two arrays

[Problem link](https://leetcode.com/problems/intersection-of-two-arrays/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
