# Find the integer added to array ii

[Problem link](https://leetcode.com/problems/find-the-integer-added-to-array-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-integer-added-to-array-ii/

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1, nums2 = sorted(nums1), sorted(nums2)

        def work(diff):
            miss = 0
            for i, x in enumerate(nums2):
                while nums1[i + miss] + diff != x:
                    miss += 1
                    if miss > 2:
                        return False
            return True

        for x in nums1[2::-1]:
            if work(nums2[0] - x):
                return nums2[0] - x

        return -1
```
## Tags

* [Two pointers](/Collections/two-pointers.md#two-pointers)
