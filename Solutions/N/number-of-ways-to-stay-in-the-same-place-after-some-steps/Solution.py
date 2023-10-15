# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        n = min(steps+1, arrLen)
        dp = [0] * (n + 2)
        dp[1] = 1

        MOD = 10**9 + 7
        for i in range(steps):
            dpc = dp.copy()
            for j in range(1, n+1):
                dp[j] = (dpc[j-1] + dpc[j] + dpc[j+1]) % MOD
        return dp[1]
