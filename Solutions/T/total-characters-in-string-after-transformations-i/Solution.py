# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        ctr = Counter(s)
        dp = [ctr[chr(ord('a') + i)] for i in range(26)]
        mod = 10 ** 9 + 7
        for i in range(t):
            dp = dp[-1:] + dp[:-1]
            dp[1] = (dp[0] + dp[1]) % mod
        return sum(dp) % mod
