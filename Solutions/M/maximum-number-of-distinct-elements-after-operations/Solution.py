# https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        last, ret = -math.inf, 0
        for x in sorted(nums):
            y = max(last + 1, x - k)
            if y <= x + k:
                ret += 1
                last = y
        return ret
