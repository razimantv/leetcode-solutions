# https://leetcode.com/problems/walking-robot-simulation/

class Solution:
    def robotSim(
        self, commands: List[int], obstacles: List[List[int]]
    ) -> int:
        dr = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x, y, d, ret = 0, 0, 0, 0
        obstacles = set(map(tuple, obstacles))

        for c in commands:
            if c == -1:
                d = (d + 1) & 3
            elif c == -2:
                d = (d + 3) & 3
            else:
                dx, dy = dr[d]
                for i in range(c):
                    xx, yy = x + dx, y + dy
                    if (xx, yy) in obstacles:
                        break
                    x, y = xx, yy
                    ret = max(ret, x ** 2 + y ** 2)
        return ret
