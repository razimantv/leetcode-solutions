# https://leetcode.com/problems/maximum-multiplication-score/

class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        dp = [0] + [-math.inf] * 4
        for x in b:
            for i in range(4, 0, -1):
                dp[i] = max(dp[i], dp[i - 1] + x * a[i - 1])
        return dp[-1]
