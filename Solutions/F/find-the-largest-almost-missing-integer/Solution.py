# https://leetcode.com/problems/find-the-largest-almost-missing-integer/

class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n, ctr = len(nums), Counter(nums)
        if n == k:
            return max(nums)
        elif k == 1:
            return max([x for x in nums if ctr[x] == 1], default=-1)
        return max([x for x in [nums[0], nums[-1]] if ctr[x] == 1], default=-1)
