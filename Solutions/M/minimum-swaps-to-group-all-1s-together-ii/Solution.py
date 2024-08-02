# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n, psum = len(nums), [0] + list(accumulate(nums + nums))
        ones = psum[-1] // 2
        return ones - max(psum[i + ones] - psum[i] for i in range(n))
