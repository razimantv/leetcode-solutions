# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[0] * n for _ in range(m)]
        for i, j in guards + walls:
            grid[i][j] = 2
        for i, j in guards:
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ii, jj = i + di, j + dj
                while 0 <= ii < m and 0 <= jj < n and grid[ii][jj] != 2:
                    grid[ii][jj] = 1
                    ii, jj = ii + di, jj + dj
        return sum(x == 0 for row in grid for x in row)
