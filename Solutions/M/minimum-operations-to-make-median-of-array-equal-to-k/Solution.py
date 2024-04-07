# https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums, n = sorted(nums), len(nums)
        ret = 0
        for i, x in enumerate(nums):
            if 2 * i < n - 1 and x > k:
                ret += x - k
                nums[i] = k
            elif 2 * i > n - 1 and x < k:
                ret += k - x
                nums[i] = k
            elif 2 * i == n - 1:
                ret += abs(k - x)
                nums[i] = k
        if n % 2 == 0:
            ret += abs(nums[n // 2] - k)
        return ret
