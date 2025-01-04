# Longest subsequence with decreasing adjacent difference

[Problem link](https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # f(i, j) = max length ending at value i
        #           such that lady difference is at least j
        M = max(nums)
        dp = [[0] * (M + 1) for _ in range(M + 1)]
        for x in nums:
            newdp = [0] * (M + 1)
            for j in range(M - 1, -1, -1):
                newdp[j] = max(1, dp[x][j], newdp[j + 1])
                for k in [x - j, x + j]:
                    if 0 <= k <= M:
                        newdp[j] = max(newdp[j], 1 + dp[k][j])
            dp[x] = newdp
        return max(row[0] for row in dp)
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
