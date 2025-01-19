# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(abs(y - x) for x, y in pairwise(nums + [nums[0]]))
