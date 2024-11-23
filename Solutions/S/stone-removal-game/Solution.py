# https://leetcode.com/problems/stone-removal-game

class Solution:
    def canAliceWin(self, n: int) -> bool:
        for x in range(10, 0, -1):
            if x > n:
                return x % 2 == 1
            n -= x
        return False
