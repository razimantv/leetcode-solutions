# https://leetcode.com/problems/maximum-difference-score-in-a-grid/

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n, ret = len(grid), len(grid[0]), -math.inf
        for i in range(m):
            for j in range(n):
                cur = min(grid[i-1][j] if i else math.inf,
                          grid[i][j-1] if j else math.inf)
                ret = max(ret, grid[i][j] - cur)
                grid[i][j] = min(grid[i][j], cur)
        return ret
