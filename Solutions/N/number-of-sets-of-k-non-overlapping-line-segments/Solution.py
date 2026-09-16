# https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        dp, dp2 = [[[0] * n for _ in range(k + 1)] for _ in (0, 1)]
        dp[0], dp2[0] = [1] * n, list(range(1, n + 1))
        mod = 10 ** 9 + 7
        for i in range(1, k + 1):
            for j in range(1, n):
                dp[i][j] = dp2[i - 1][j - 1] + dp[i][j - 1]
                if dp[i][j] >= mod:
                    dp[i][j] -= mod
                dp2[i][j] = dp2[i][j - 1] + dp[i][j]
                if dp2[i][j] >= mod:
                    dp2[i][j] -= mod
        return dp[-1][-1]
