# https://leetcode.com/problems/smallest-stable-index-i/

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        left = list(accumulate(nums, max))
        right = list(accumulate(nums[::-1], min))[::-1]
        return next(
            (i for i, (x, y) in enumerate(zip(left, right)) if x - y <= k),
            -1
        )
