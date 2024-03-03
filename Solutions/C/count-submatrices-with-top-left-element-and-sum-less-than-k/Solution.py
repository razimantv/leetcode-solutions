# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ret = 0
        for i in range(m):
            for j in range(n):
                grid[i][j] += (
                    (grid[i-1][j] if i else 0) +
                    (grid[i][j-1] if j else 0) -
                    (grid[i-1][j-1] if i and j else 0)
                )
                ret += (grid[i][j] <= k)

        return ret
