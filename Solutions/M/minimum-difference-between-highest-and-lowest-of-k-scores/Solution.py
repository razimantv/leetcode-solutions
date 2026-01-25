# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums = sorted(nums)
        return min(y - x for x, y in zip(nums, nums[k - 1:]))
