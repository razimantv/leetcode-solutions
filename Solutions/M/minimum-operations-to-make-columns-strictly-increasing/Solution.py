# https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n, ret = len(grid), len(grid[0]), 0
        for j in range(n):
            for i in range(1, m):
                cur = max(grid[i][j], grid[i - 1][j] + 1)
                ret += cur - grid[i][j]
                grid[i][j] = cur
        return ret
