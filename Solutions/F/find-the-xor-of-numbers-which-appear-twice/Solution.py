# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ret = 0
        for x in nums:
            ret ^= x
        for x in set(nums):
            ret ^= x
        return ret
