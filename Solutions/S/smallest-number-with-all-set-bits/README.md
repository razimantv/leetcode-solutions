# Smallest number with all set bits

[Problem link](https://leetcode.com/problems/smallest-number-with-all-set-bits/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/smallest-number-with-all-set-bits/

class Solution:
    def smallestNumber(self, n: int) -> int:
        ret = 0
        while ret < n:
            ret = 2 * ret + 1
        return ret
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
