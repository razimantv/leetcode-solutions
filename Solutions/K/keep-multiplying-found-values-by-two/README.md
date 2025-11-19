# Keep multiplying found values by two

[Problem link](https://leetcode.com/problems/keep-multiplying-found-values-by-two/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/keep-multiplying-found-values-by-two/

class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        for x in sorted(nums):
            if x == original:
                original *= 2
        return original
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
