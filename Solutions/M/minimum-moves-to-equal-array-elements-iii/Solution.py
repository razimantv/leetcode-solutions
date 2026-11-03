# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        m = max(nums)
        return sum(m - x for x in nums)
