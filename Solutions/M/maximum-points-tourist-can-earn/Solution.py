# https://leetcode.com/problems/maximum-points-tourist-can-earn/

class Solution:
    def maxScore(
        self, n: int, k: int, stayScore: List[List[int]],
        travelScore: List[List[int]]
    ) -> int:
        dp = [0] * n
        for d in range(k):
            dp = [
                max(
                    dp[i] + stayScore[d][i],
                    max(dp[j] + travelScore[j][i] for j in range(n))
                )
                for i in range(n)
            ]
        return max(dp)
