# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        seen = [[0] * n for _ in range(m)]
        dist = [[m * n + 1] * n for _ in range(m)]

        seen[0][0] = 0
        dist[0][0] = grid[0][0]
        todo = [(0, 0)]

        while todo:
            next = []
            while todo:
                x, y = todo.pop()
                if seen[x][y]:
                    continue
                seen[x][y] = 1

                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    xx, yy = x + dx, y + dy
                    if (
                        0 <= xx < m and 0 <= yy < n and
                        dist[x][y] + grid[xx][yy] < dist[xx][yy]
                    ):
                        dist[xx][yy] = dist[x][y] + grid[xx][yy]
                        [todo, next][grid[xx][yy]].append((xx, yy))
            todo = next

        return dist[-1][-1] < health
