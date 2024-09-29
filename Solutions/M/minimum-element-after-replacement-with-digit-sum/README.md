# Minimum element after replacement with digit sum

[Problem link](https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(int(x) for x in str(y)) for y in nums)
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
