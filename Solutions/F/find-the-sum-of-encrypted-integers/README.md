# Find the sum of encrypted integers

[Problem link](https://leetcode.com/problems/find-the-sum-of-encrypted-integers/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(x):
            return int(max(str(x)) * len(str(x)))
        return sum(encrypt(x) for x in nums)
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
