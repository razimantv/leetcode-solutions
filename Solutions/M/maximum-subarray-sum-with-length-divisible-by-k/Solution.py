# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n, ret = len(nums), -math.inf
        psum = [0] + list(accumulate(nums))
        for i in range(k):
            low = psum[i]
            for j in range(i + k, n + 1, k):
                ret = max(ret, psum[j] - low)
                low = min(psum[j], low)
        return ret
