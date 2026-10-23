# https://leetcode.com/problems/maximum-k-to-sort-a-permutation/


class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        ret = (1 << 20) - 1
        for i, x in enumerate(nums):
            if i != x:
                ret &= i
        return 0 if ret > len(nums) else ret
