# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n, ret = len(nums), 0
        for i in range(1, n - 1):
            if 2 * (nums[i - 1] + nums[i + 1]) == nums[i]:
                ret += 1
        return ret
