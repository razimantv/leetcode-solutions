# https://leetcode.com/problems/magic-squares-in-grid/

import numpy as np


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def good(M):
            if not np. all((M.sum(0) == 15) & (M.sum(1) == 15)):
                return False
            return M.diagonal().sum() == M[::-1].diagonal().sum() == 15 and\
                len(Counter(M.flat)) == 9 and 0 not in M.flat

        grid = np.array(grid)
        m, n = grid.shape
        return sum(
            good(grid[i:i+3, j:j+3]) for i in range(m-2) for j in range(n-2)
        )
