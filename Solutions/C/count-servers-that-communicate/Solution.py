# https://leetcode.com/problems/count-servers-that-communicate

class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c = [0] * m, [0] * n
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x:
                    r[i] += 1
                    c[j] += 1
        return sum(
            1 for i in range(m) for j in range(n)
            if grid[i][j] * (r[i] + c[j]) > 2
        )
