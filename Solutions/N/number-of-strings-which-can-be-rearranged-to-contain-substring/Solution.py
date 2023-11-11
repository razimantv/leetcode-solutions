# https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/

import numpy as np


class Solution:
    def stringCount(self, n: int) -> int:
        dp = np.zeros([2, 2, 3], dtype=int)
        dp[0, 0, 0] = 1
        cnt = [1, 1, 1, 23]
        MOD = 10**9 + 7
        for i in range(n):
            newdp = dp * 0
            for index in np.ndindex(dp.shape):
                for j, x in enumerate(cnt):
                    idx = list(index)
                    nidx = idx.copy()
                    if j < 3:
                        nidx[j] = min(dp.shape[j]-1, nidx[j]+1)
                    newdp[tuple(nidx)] = (
                        newdp[tuple(nidx)] + dp[tuple(idx)] * x
                    ) % MOD
            dp = newdp
        return dp[-1, -1, -1]
