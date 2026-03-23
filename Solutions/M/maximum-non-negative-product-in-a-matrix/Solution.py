# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/

class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        @cache
        def dp(i, j):
            if not grid[i][j]:
                return [0, 0]
            prev = [] if (i + j) else [1]
            if i:
                prev += dp(i - 1, j)
            if j:
                prev += dp(i, j - 1)
            ret = sorted([x * grid[i][j] for x in prev])
            return [ret[0], ret[-1]]

        best = dp(len(grid) - 1, len(grid[0]) - 1)[1]
        return - 1 if best < 0 else (best % (10 ** 9 + 7))
