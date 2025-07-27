# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        prev, ret = [nums[0]] * 2, 0
        for x in nums:
            if x != prev[1]:
                if (x - prev[1]) * (prev[1] - prev[0]) < 0:
                    ret += 1
                prev = [prev[-1], x]
        return ret
