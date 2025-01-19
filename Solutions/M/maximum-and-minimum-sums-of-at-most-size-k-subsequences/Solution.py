# https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

class Solution:
    def minMaxSums(self, nums: list[int], k: int) -> int:
        n, nums, ret, mod = len(nums), sorted(nums), 0, 10 ** 9 + 7
        dp, tot = [1] + [0] * (k - 1), [1] * n
        for i in range(1, n):
            for r in range(k - 1, 0, -1):
                dp[r] += dp[r - 1]
                if dp[r] >= mod:
                    dp[r] -= mod
                tot[i] += dp[r]
                if tot[i] >= mod:
                    tot[i] -= mod

        for i, x in enumerate(nums):
            ret = (ret + x * (tot[i] + tot[n - 1 - i])) % mod
        return ret
