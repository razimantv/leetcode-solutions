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

* [Bitwise operation](/README.md#Bitwise_operation) > [Self-inverse property of xor](/README.md#Bitwise_operation-Self_inverse_property_of_xor)
