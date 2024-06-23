# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        return min((x + y) / 2 for x, y in zip(nums, nums[::-1]))
