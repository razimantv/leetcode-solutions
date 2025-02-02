# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution:
    def check(self, nums: list[int]) -> bool:
        n, bad = len(nums), -1
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                if bad != -1:
                    return False
                bad = i
        return bad == -1 or nums[-1] <= nums[0]
