# https://leetcode.com/problems/check-if-grid-satisfies-conditions/

class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i and grid[i][j] != grid[i-1][j]:
                    return False
                if j and grid[i][j] == grid[i][j-1]:
                    return False
        return True
