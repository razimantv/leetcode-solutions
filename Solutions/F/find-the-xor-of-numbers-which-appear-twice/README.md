# Find the xor of numbers which appear twice

[Problem link](https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ret = 0
        for x in nums:
            ret ^= x
        for x in set(nums):
            ret ^= x
        return ret
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Self-inverse property of xor](/Collections/bitwise-operation.md#self-inverse-property-of-xor)
