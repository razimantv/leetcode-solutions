# https://leetcode.com/problems/count-partitions-with-even-sum-difference

class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        return (len(nums) - 1) if sum(nums) & 1 == 0 else 0
