# https://leetcode.com/problems/single-number-ii

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        N0, N1, N2 = ~0, 0, 0
        for x in nums:
            N0, N1, N2 = (N0 & ~x) | (N2 & x), (N1 & ~x) | (N0 & x), (N2 & ~x) | (N1 & x)
        return N1
