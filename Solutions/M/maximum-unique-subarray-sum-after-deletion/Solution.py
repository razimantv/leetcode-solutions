# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if (m := max(nums)) <= 0:
            return m
        return sum(set(x for x in nums if x > 0))
