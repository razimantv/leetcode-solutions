# https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        ret = ""
        for perm in permutations(nums):
            ret = max(ret, ''.join(f"{x:b}" for x in perm))

        return int(ret, 2)
