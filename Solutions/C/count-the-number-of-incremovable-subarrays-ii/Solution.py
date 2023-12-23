# https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-ii/

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n-1):
            if nums[i] >= nums[i+1]:
                left = i
                break
        else:
            return n * (n + 1) // 2

        for i in range(n-1, 0, -1):
            if nums[i] <= nums[i-1]:
                right = i
                break

        r, tot = right, n - right + left + 2
        for l in range(left + 1):
            while r < n and nums[r] <= nums[l]:
                r += 1
            tot += n - r
        return tot
