# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        sl = SortedList()
        ret, l = 0, 0
        for r, x in enumerate(nums):
            sl.add(x)
            while sl[-1] - sl[0] > limit:
                sl. discard(nums[l])
                l += 1
            ret = max(ret, r - l + 1)
        return ret
