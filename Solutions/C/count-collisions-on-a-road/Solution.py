# https://leetcode.com/problems/count-collisions-on-a-road/

class Solution:
    def countCollisions(self, directions: str) -> int:
        r, s, ret = 0, 0, 0
        for x in directions:
            if x == 'R':
                r += 1
            elif x == 'S':
                ret += r
                r, s = 0, 1
            elif r + s:
                ret += r + 1
                r, s = 0, 1
        return ret
