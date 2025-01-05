# Maximum subarray with equal products

[Problem link](https://leetcode.com/problems/maximum-subarray-with-equal-products)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-subarray-with-equal-products

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ret, n = 1, len(nums) 
        for i in range(n):
            p, l, g = [nums[i]] * 3
            for j, x in enumerate(nums[i + 1:]):
                p *= x
                g = gcd(g, x)
                l = l * x // gcd(l, x)
                if g * l == p:
                    ret = max(ret, j + 2)
        return ret
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [GCD/LCM](/Collections/mathematics.md#gcd-lcm)
