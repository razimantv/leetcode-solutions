# https://leetcode.com/problems/find-if-digit-game-can-be-won/

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        return sum(x for x in nums if x < 10) != sum(x for x in nums if x > 9)
