# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        p, pmin, pmax, ret = 0, 0, 0, 0
        for x in nums:
            p += x
            ret = max(ret, pmax - p, p - pmin)
            pmin = min(pmin, p)
            pmax = max(pmax, p)
        return ret
