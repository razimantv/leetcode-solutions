# https://leetcode.com/problems/stone-game-v/

class Solution:
    def stoneGameV(self, stones: list[int]) -> int:
        n = len(stones)
        dp, dp1, dp2 = [[[0] * n for _ in range(n)] for d in range(3)]
        psum = list(accumulate(stones, initial=0))
        for i in range(n):
            dp1[i][i] = dp2[i][i] = stones[i]

        for L in range(2, n + 1):
            l, m, r = 0, 0, L - 1
            while r < n:
                while psum[m + 1] - psum[l] <= psum[r + 1] - psum[m + 1]:
                    m += 1
                m1 = m - 1
                m2 = m if psum[r + 1] - psum[m] == psum[m] - psum[l] else m + 1
                dp[l][r] = max(
                    dp1[l][m1] if m1 >= l else 0, dp2[m2][r] if m2 <= r else 0
                )
                dp1[l][r] = max(
                    dp1[l][r - 1], dp[l][r] + psum[r + 1] - psum[l]
                )
                dp2[l][r] = max(
                    dp2[l + 1][r], dp[l][r] + psum[r + 1] - psum[l]
                )

                l, r = l + 1, r + 1

        return dp[0][-1]
