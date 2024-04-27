# https://leetcode.com/problems/freedom-trail/

zlass Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        dp = [0] + [math.inf] * (n-1)
        for i, c in enumerate(key):
            dp = [
                math.inf if d != c else min(
                    dp[k] + min(abs(k - j), n - abs(k - j)) for k in range(n)
                )
                for j, d in enumerate(ring)
            ]
        return min(dp) + len(key)
