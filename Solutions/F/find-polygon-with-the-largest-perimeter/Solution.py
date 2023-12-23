# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        ret = -1
        n, nums = len(nums), sorted(nums)
        tot = nums[0]
        for i in range(1, n-1):
            tot += nums[i]
            if tot > nums[i+1]:
                ret = tot + nums[i+1]
        return ret
