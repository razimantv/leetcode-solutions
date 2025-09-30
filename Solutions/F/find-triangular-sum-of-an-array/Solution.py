# https://leetcode.com/problems/find-triangular-sum-of-an-array/

class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n - 1, 0, -1):
            for j in range(i):
                nums[j] = (nums[j] + nums[j + 1]) % 10
        return nums[0]
