# https://leetcode.com/problems/cyclically-rotating-a-grid/

import numpy as np


class Solution:
    def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        grid = np. array(grid)
        m, n = grid.shape

        def work(d):
            cur = np. concatenate((
                grid[d:m-d-1, d], grid[m-d-1, d:n-d-1],
                grid[m-d-1:d:-1, n-d-1], grid[d, n-d-1:d:-1]
            ))
            s = len(cur) - k % len(cur)
            cur = np.concatenate((cur[s:], cur[:s]))
            grid[d:m-d-1, d] = cur[:m-2*d-1]
            grid[m-d-1, d:n-d-1] = cur[m-2*d-1:m+n-4*d-2]
            grid[m-d-1:d:-1, n-d-1] = cur[m+n-4*d-2:2*m+n-6*d-3]
            grid[d, n-d-1:d:-1] = cur[2*m+n-6*d-3:]

        for d in range(min(m, n) // 2):
            work(d)

        return grid
