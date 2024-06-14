# https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n, nums = len(nums), sorted(nums)
        ret = 0
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                ret += nums[i - 1] + 1 - nums[i]
                nums[i] = nums[i - 1] + 1
        return ret
