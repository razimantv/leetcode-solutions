# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        return len(set(nums)) - (min(nums) == k)
