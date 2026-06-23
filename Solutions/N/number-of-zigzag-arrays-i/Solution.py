# https://leetcode.com/problems/number-of-zigzag-arrays-i/

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        x, mod = r - l + 1, 10 ** 9 + 7
        dp = [1] * x
        for i in range(1, n):
            newdp, cur = [0] * x, 0
            for j in range(x):
                newdp[j] = cur
                cur += dp[x - 1 - j]
                if cur >= mod:
                    cur -= mod
            dp = newdp
        return (sum(dp) * 2) % mod
