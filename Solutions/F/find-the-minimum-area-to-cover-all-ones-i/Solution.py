# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        i1, i2, j1, j2 = m-1, 0, n-1, 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x:
                    i1, j1 = min(i1, i), min(j1, j)
                    i2, j2 = max(i2, i), max(j2, j)
        return (i2 - i1 + 1) * (j2 - j1 + 1)
