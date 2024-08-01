# Maximum product of two elements in an array

[Problem link](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a, b = 0, 0
        for x in nums:
            if x > a:
                a, b = x, a
            elif x > b:
                b = x
        return (a - 1) * (b - 1)
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
