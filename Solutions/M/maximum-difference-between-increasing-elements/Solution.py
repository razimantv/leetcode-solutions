# https://leetcode.com/problems/maximum-difference-between-increasing-elements/

class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        ret, m = -1, nums[0]
        for x in nums:
            if x > m:
                ret = max(ret, x - m)
            m = min(m, x)
        return ret
