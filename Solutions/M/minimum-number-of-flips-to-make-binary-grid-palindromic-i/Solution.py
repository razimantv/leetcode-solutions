# https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        rowfix = 0
        for row in grid:
            i, j = 0, n - 1
            while i < j:
                if row[i] != row[j]:
                    rowfix += 1
                i, j = i + 1, j - 1

        colfix = 0
        for k in range(n):
            i, j = 0, m - 1
            while i < j:
                if grid[i][k] != grid[j][k]:
                    colfix += 1
                i, j = i + 1, j - 1

        return min(rowfix, colfix)
