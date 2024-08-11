# https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j, seen):
            grid[i][j] = seen
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ii, jj = i + di, j + dj
                if 0 <= ii < m and 0 <= jj < n and 0 < grid[ii][jj] < seen:
                    dfs(ii, jj, seen)

        def bad(seen):
            one = False
            for i in range(m):
                for j in range(n):
                    if 0 < grid[i][j] < seen:
                        if one:
                            return True
                        dfs(i, j, seen)
                        one = True
            return not one

        if bad(2):
            return 0

        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                grid[i][j] = cur = i * n + j + 3
                if bad(cur):
                    return 1
        return 2
