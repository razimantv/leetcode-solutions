# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # Dimensions of the grid
        m, n = len(grid), len(grid[0])

        # Minimum distance from source to each vertex
        dist = [[m * n] * n for _ in grid]
        dist[0][0] = 0

        # Current queue - will contain vertices at distance level from source
        bfsq = [(0, 0)]
        level = 0

        # neigbour array according to order in the question
        neigh = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while bfsq:
            # Process a level
            # Queue of vertices at next level
            next = []

            # Process all vertices at next level
            while bfsq:
                # Not really a queue but fine because of the level-wise split
                i, j = bfsq.pop()

                # If we have already processed at the previous level, ignore
                if dist[i][j] < level:
                    continue

                # Loop over neighbours
                for x, (di, dj) in enumerate(neigh):
                    # Neighbouring vertex and its distance
                    ii, jj = i + di, j + dj
                    newdist = level + (0 if grid[i][j] == x + 1 else 1)

                    # Validation
                    if 0 <= ii < m and 0 <= jj < n and newdist < dist[ii][jj]:
                        # Update distance and add it to the right queue
                        dist[ii][jj] = newdist
                        if newdist == dist[i][j]:
                            bfsq.append((ii, jj))
                        else:
                            next.append((ii, jj))

            # We have exhausted the current level, so process the next
            bfsq = next
            level += 1

        return dist[-1][-1]
