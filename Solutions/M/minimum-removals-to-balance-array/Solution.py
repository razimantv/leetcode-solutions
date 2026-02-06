# https://leetcode.com/problems/minimum-removals-to-balance-array/

class Solution:
    def minRemoval(self, nums: list[int], k: int) -> int:
        nums, n, j, ret = sorted(nums), len(nums), 0, 1
        for i in range(n):
            while j < n and nums[j] <= nums[i] * k:
                j += 1
            ret = max(ret, j - i)
        return n - ret
