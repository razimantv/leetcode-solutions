# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i] in [nums[i - 1], nums[i - 2]]:
                return nums[i]
        return -1
