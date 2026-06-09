# https://leetcode.com/problems/maximum-total-subarray-value-i/

class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        return (max(nums) - min (nums)) * k
