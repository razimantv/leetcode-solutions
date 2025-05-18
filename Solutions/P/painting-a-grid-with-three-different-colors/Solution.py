# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        poss, mod = [[0], [1], [2]], 10 ** 9 + 7
        for L in range(m - 1):
            poss = [
                old + [i] for old in poss for i in range(3) if i != old[-1]
            ]

        neigh = [
            [
                i for i, P2 in enumerate(poss)
                if all(x != y for x, y in zip(P1, P2))
            ]
            for P1 in poss
        ]

        dp = [1 for P in poss]
        for L in range(n - 1):
            dp = [sum(dp[j] for j in neigh[i]) % mod for i, x in enumerate(dp)]
        return sum(dp) % mod
