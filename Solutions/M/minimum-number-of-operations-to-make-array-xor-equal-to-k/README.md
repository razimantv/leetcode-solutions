# Minimum number of operations to make array xor equal to k

[Problem link](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for x in nums:
            k ^= x
        return k.bit_count()
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Self-inverse property of xor](/Collections/bitwise-operation.md#self-inverse-property-of-xor)
