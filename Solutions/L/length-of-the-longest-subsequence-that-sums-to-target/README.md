# Length of the longest subsequence that sums to target

[Problem link](https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [-10000] * (target + 1)
        dp[0] = 0
        for x in nums:
            for i in range(target, x-1, -1):
                dp[i] = max(dp[i-x] + 1, dp[i])
        return max(dp[-1], -1)
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Knapsack](/Collections/dynamic-programming.md#knapsack)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
