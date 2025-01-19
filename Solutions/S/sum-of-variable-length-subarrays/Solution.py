# https://leetcode.com/problems/sum-of-variable-length-subarrays/

class Solution:
    def subarraySum(self, nums: list[int]) -> int:
        return sum(sum(nums[max(0, i - x):i + 1]) for i, x in enumerate(nums))
