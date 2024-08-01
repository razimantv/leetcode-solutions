# Minimum cost to make array equalindromic

[Problem link](https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n, nums = len(nums), sorted(nums)
        if n & 1:
            median = nums[n // 2]
        else:
            median = (nums[n // 2] + nums[n // 2 - 1]) // 2

        def ispali(x):
            s = str(x)
            return s == s[::-1]

        def next(x):
            while not ispali(x):
                x += 1
            return x

        def prev(x):
            while not ispali(x):
                x -= 1
            return x

        ret = sum(nums) - n
        for x in [next(median), prev(median)]:
            ret = min(ret, sum(abs(y-x) for y in nums))
        return ret
```
## Tags

* [Palindrome](/Collections/palindrome.md#palindrome)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Median](/Collections/mathematics.md#median)
