# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n, nums = len(nums), sorted(nums)
        if nums[0] >= n:
            return n
        for i, (x, y) in enumerate(pairwise(nums)):
            if x < n - i - 1 <= y:
                return n - 1 - i
        return 0 if nums[-1] < 0 else -1
