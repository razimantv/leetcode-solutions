# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flip, ret = 0, 0
        for x in nums:
            if flip == x:
                ret += 1
                flip ^= 1
        return ret
