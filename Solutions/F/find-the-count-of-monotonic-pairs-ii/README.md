# Find the count of monotonic pairs ii

[Problem link](https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/

class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        dp = list(range(1, nums[0] + 2))
        for x, y in pairwise(nums):
            newdp = [0] * (y + 1)
            for i in range(max(0, y - x), y + 1):
                newdp[i] = dp[min(i, x, i + x - y)]
            dp = [x % mod for x in accumulate(newdp)]
        return dp[-1]
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Auxiliary array](/Collections/dynamic-programming.md#auxiliary-array) > [Prefix sum](/Collections/dynamic-programming.md#prefix-sum)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
