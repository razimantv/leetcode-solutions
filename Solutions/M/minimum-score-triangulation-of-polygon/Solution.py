# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        @cache
        def dp(i, j):
            if j - i == 2:
                return values[i] * values[i + 1] * values[j]
            ret = inf
            for k in range(i + 1, j):
                cur = values[i] * values[j] * values[k]
                if k > i + 1:
                    cur += dp(i, k)
                if k < j - 1:
                    cur += dp(k, j)
                ret = min(ret, cur)
            return ret

        return dp(0, len(values) - 1)
