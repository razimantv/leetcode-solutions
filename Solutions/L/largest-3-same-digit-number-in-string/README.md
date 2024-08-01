# Largest 3 same digit number in string

[Problem link](https://leetcode.com/problems/largest-3-same-digit-number-in-string/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/largest-3-same-digit-number-in-string/

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for c in "9876543210":
            if c * 3 in num:
                return c * 3
        return ""
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
