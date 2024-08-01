# Minimum operations to maximize last elements in arrays

[Problem link](https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        a1, a2 = max(nums1), max(nums2)
        a = max(a1, a2)
        b = nums2[-1] if nums1[-1] == a else nums1[-1]
        if a != nums1[-1] and a != nums2[-1]:
            return -1
        elif a == b:
            return 0

        b1, b2 = 0, 0
        for x, y in zip(nums1[:-1], nums2[:-1]):
            if min(x, y) > b:
                return -1
            elif max(x, y) <= b:
                continue
            elif x > b:
                b1 += 1
            else:
                b2 += 1

        if a == nums1[-1]:
            return min(b2, b1+1)
        else:
            return min(b1, b2+1)
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning)
