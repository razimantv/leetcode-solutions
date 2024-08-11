# https://leetcode.com/problems/snake-in-matrix/

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        diff = {'RIGHT': 1, 'LEFT': -1, 'DOWN': n, 'UP': -n}
        return sum(diff[c] for c in commands)
