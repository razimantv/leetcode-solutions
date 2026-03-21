# https://leetcode.com/problems/flip-square-submatrix-vertically/

import numpy as np


class Solution:
    def reverseSubmatrix(
        self, grid: list[list[int]], x: int, y: int, k: int
    ) -> list[list[int]]:
        grid = np.array(grid)
        grid[x:x+k, y:y+k] = np.flip(grid[x:x+k, y:y+k], axis=0)
        return grid.tolist()
