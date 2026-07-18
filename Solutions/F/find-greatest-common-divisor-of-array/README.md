# Find greatest common divisor of array

[Problem link](https://leetcode.com/problems/find-greatest-common-divisor-of-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: list[int]) -> int:
        return gcd(min(nums), max(nums))
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
