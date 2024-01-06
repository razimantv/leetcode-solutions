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

* [Bitwise operation](/README.md#Bitwise_operation) > [Self-inverse property of xor](/README.md#Bitwise_operation-Self_inverse_property_of_xor)
