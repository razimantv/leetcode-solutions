# https://leetcode.com/problems/number-of-ways-to-split-array/

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        psum = list(accumulate(nums))
        return sum(1 for x in psum[:-1] if 2 * x >= psum[-1])
