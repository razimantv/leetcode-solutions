# Convert integer to the sum of two no zero integers

[Problem link](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        for a in range(1, n):
            if '0' not in str(a) and '0' not in str(b := n - a):
                return [a, b]
        return [-1, -1]
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
