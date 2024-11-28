# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[math.inf] * n for _ in range(m)]
        dist[0][0] = 0
        cur, next = [(0, 0)], []

        while cur:
            while cur:
                i, j = cur.pop()
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ii, jj = i + di, j + dj
                    if (
                        0 <= ii < m and 0 <= jj < n and
                        (dnew := dist[i][j] + grid[ii][jj]) < dist[ii][jj]
                    ):
                        dist[ii][jj] = dnew
                        [cur, next][grid[ii][jj]].append((ii, jj))
            cur, next = next, []
        return dist[-1][-1]
