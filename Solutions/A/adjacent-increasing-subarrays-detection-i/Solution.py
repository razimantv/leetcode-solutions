# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        left = [1]
        for x, y in pairwise(nums):
            left.append((left[-1] + 1) if x < y else 1)

        right = [1]
        for x, y in pairwise(nums[::-1]):
            right.append((right[-1] + 1) if x > y else 1)
        right = right[::-1]

        ret = 0
        for i in range(1, len(nums)):
            ret = max(ret, min(right[i], left[i - 1]))
        return ret >= k
