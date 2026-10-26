# https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/


class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            ret, grid[i][j] = grid[i][j], 0
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ii, jj = i + di, j + dj
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj]:
                    ret += dfs(ii, jj)
            return ret

        return sum(
            1 for i in range(m) for j in range(n)
            if grid[i][j] and (dfs(i, j) % k == 0)
        )
