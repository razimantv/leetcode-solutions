# https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/

class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        n, nums = len(nums), sorted(nums)
        psum = [0] * (n + 1)
        for i, x in enumerate(nums):
            psum[i+1] = psum[i] + x

        def tot(l, r):
            m = (l + r) // 2
            x = nums[m]
            return (
                (m - l) * x - (psum[m] - psum[l]) +
                (psum[r+1] - psum[m + 1]) - (r - m) * x
            )

        r, best = 0, 1
        for l in range(n):
            while r < n and tot(l, r) <= k:
                r += 1
            best = max(best, r - l)
        return best
