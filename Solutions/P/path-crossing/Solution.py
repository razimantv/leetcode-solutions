# https://leetcode.com/problems/path-crossing/

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        neigh = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
        return max(
            Counter(
                [(x := 0, y := 0)] +
                [
                    (x := x + neigh[c][0], y := y + neigh[c][1])
                    for c in path
                ]
            ).values()
        ) > 1
