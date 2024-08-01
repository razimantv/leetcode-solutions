# Check if bitwise or has trailing zeros

[Problem link](https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        cnt = len([x for x in nums if x % 2 == 0])
        return cnt > 1
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
