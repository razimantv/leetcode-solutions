# Element appearing more than 25 in sorted array

[Problem link](https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        n4 = n // 4
        for i in range(n4, n):
            if arr[i] == arr[i-n4]:
                return arr[i]
        return -1
```
## Tags

* [Suboptimal solution](/Collections/suboptimal-solution.md#suboptimal-solution)
