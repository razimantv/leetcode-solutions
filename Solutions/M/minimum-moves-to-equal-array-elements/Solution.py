# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        m = min(nums)
        return sum(x - m for x in nums)
