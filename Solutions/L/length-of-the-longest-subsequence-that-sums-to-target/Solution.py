# https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [-10000] * (target + 1)
        dp[0] = 0
        for x in nums:
            for i in range(target, x-1, -1):
                dp[i] = max(dp[i-x] + 1, dp[i])
        return max(dp[-1], -1)
